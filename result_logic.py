def check_result(attendance, marks):
    if attendance < 75:
        return "Fail"

    if marks < 40:
        return "Fail"

    return "Pass"
