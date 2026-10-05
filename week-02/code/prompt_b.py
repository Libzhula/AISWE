def analyze_marks(marks, pass_mark=50):
    if not marks:
        raise ValueError("marks list cannot be empty")

    valid_marks = []
    for mark in marks:
        if not isinstance(mark, (int, float)):
            raise ValueError("all marks must be numeric")
        if mark < 0 or mark > 100:
            raise ValueError("marks must be between 0 and 100")
        valid_marks.append(mark)

    average = sum(valid_marks) / len(valid_marks)
    highest = max(valid_marks)
    lowest = min(valid_marks)
    passing_count = sum(1 for mark in valid_marks if mark >= pass_mark)
    pass_rate = (passing_count / len(valid_marks)) * 100

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "pass_rate": pass_rate,
    }

