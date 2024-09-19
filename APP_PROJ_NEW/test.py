# # start_reg_number = 'RA2311026010001'
# # end_reg_number = 'RA2311026010062'
# # start = int(start_reg_number[-4:])
# # end = int(end_reg_number[-4:])
# # print(end - start)



# quizzes[quiz_id] = {
#             'quiz_input': quiz_input,
#             'questions': shuffeled_question
#         }


# @app.route('/quiz/<quiz_id>')
# def view_quiz(quiz_id):
#     quiz_data = quizzes.get(quiz_id)
    
#     if quiz_data:
#         return render_template('quiz.html', quiz=quiz_data)
#     else:
#         return "Quiz not found!", 404
    
# <!-- quiz.html -->
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>{{ quiz.quiz_input['Quiz Title'] }}</title>
# </head>
# <body>
#     <h1>{{ quiz.quiz_input['Quiz Title'] }}</h1>
#     <h2>Subject: {{ quiz.quiz_input['Subject'] }}</h2>
#     <ol>
#     {% for question in quiz.questions %}
#         <li>{{ question }}</li>
#     {% endfor %}
#     </ol>
# </body>
# </html>





