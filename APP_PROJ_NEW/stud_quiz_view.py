def stud_view(quiz_id, dic_quiz_id, reg_no):
    # print(quiz_id, dic_quiz_id, reg_no)
    for key, val, in dic_quiz_id.items():
        # print(quiz_id, dic_quiz_id, reg_no, key, val)
        if key == quiz_id:
            for key_, val_ in val.items():
                # print(key_, val_, reg_no)
                if key_ == reg_no:
                    return val_
