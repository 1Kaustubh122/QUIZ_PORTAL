import random

def random_ques(quiz_input_data, lst_of_questions):

    start_reg_number = quiz_input_data['Start Reg no']
    end_reg_number = quiz_input_data['End Reg no']
    number_of_ques_per_stud = int(quiz_input_data['Number of Questions'])

    RegNo_Frame = start_reg_number[:-3]

    start = int(start_reg_number[-4:])
    end = int(end_reg_number[-4:])
    total_stud = (end - start)+1

    distributed_questions = []
    
    for _ in range(total_stud):
        student_questions = random.sample(lst_of_questions, number_of_ques_per_stud)
        distributed_questions.append(student_questions)


    # for i in range(len(distributed_questions)):
    #     print(distributed_questions[i])

    # print(distributed_questions, len(distributed_questions), total_stud)

    datalist = {}

    for i in range(total_stud):
        x = distributed_questions[i]

        # print(len(RegNo_Frame), len(str(start)))

        if (len(RegNo_Frame) + len(str(start)) < 15):
            zeroes = 15 - (len(RegNo_Frame) + len(str(start)))
            datalist[(f'{RegNo_Frame}{'0'*zeroes}{start}')] = x
        else:
            datalist[(f'{RegNo_Frame}{start}')] = x

        start += 1

    # for key, val in datalist:
    #     print(key, val)
    
    return datalist


        

    # string_data = ""

    # for i in datalist:
    #     string_data += i
    #     string_data += '\n'
    # print(string_data)

    # return string_data
    
