from flask import Flask, render_template, request, url_for
import uuid
from io import BytesIO
from question_ex import question_extracter
from randomized_ques import random_ques
from stud_quiz_view import stud_view

app = Flask(__name__)

dic_quiz_id = {}

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_quiz', methods=['POST'])
def create_quiz():
    quiz_data = request.form.to_dict()
    quiz_id = str(uuid.uuid4())  # Generate a unique ID for the quiz

    title = quiz_data.get('title', '')
    subject = quiz_data.get('subject', '')
    start_reg_number = quiz_data.get('start_reg_number', '')
    end_reg_number = quiz_data.get('end_reg_number', '')
    num_questions_per_stud = quiz_data.get('num_questions', '')
    file = request.files.get('file_upload')


    quiz_input = {'Quiz Title' : title, 'Subject' : subject, 'Start Reg no' : start_reg_number,
           'End Reg no' : end_reg_number, 'Number of Questions' : num_questions_per_stud}

    print(quiz_input)

    if file and allowed_file(file.filename):
        file_content = file.read() 
        file_stream = BytesIO(file_content)  # Create an in-memory stream
        lst_of_questions = question_extracter(file_stream)
        file_stream.close()  

        shuffeled_question = random_ques(quiz_input, lst_of_questions)

        dic_quiz_id[quiz_id] = shuffeled_question


        quiz_link = url_for('view_quiz', quiz_id=quiz_id, _external=True)
        
        return render_template('quiz_table.html', shuffled_questions=shuffeled_question, quizs_link=quiz_link)


@app.route('/quiz/<quiz_id>', methods=['GET', 'POST'])
def view_quiz(quiz_id):
    if request.method == 'POST':
        data = request.form.to_dict()
        reg_no = data.get('Reg_No', '')
        print(reg_no)

        res = stud_view(quiz_id, dic_quiz_id, reg_no)
        # print(res)
        
        return render_template('quiz.html', res=res)
    
    return render_template('quiz.html', res=None)



if __name__ == '__main__':
    app.run(debug=True, port=7000)