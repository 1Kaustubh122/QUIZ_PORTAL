from pypdf import PdfReader
def question_extracter(path):  
    page = PdfReader(path)
    text = ""
    q_cnt = 0
    for i in range(len(page.pages)):
        text += page.pages[i].extract_text()

    len_page = len(text)


    question_st_idx = []

    for i in range(len_page-4):
        if ((text[i] == 'Q' or text[i] == 'q') and 
            (text[i].isdigit() or text[i+1].isdigit() or text[i+2].isdigit()) and 
            (text[i+1] == ":" or text[i+2] == ":" or text[i+3] == ":" or text[i+1] == "." or text[i+2] == "." or text[i+3] == ".")):
            q_cnt += 1
            question_st_idx.append(i)
        


    questions = []
    for i in range(len(question_st_idx)-1):
        questions.append(text[question_st_idx[i] : question_st_idx[i+1]])

    questions.append(text[question_st_idx[-1]:])

    return questions



