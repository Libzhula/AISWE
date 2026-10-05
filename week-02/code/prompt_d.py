def analyze_marks(marks, pass_mark=50):
    """
    Analyze a non-empty list of numeric student marks.

    Returns a dictionary with exactly these keys:
    average, highest, lowest, pass_rate.
    """
    if len(marks) == 0:
        raise ValueError("marks must not be empty")

    checked_marks = []
    for mark in marks:
        if type(mark) not in (int, float):
            raise ValueError("each mark must be numeric")
        if mark < 0 or mark > 100:
            raise ValueError("marks must be from 0 to 100 inclusive")
        checked_marks.append(mark)

    pass_count = sum(1 for mark in checked_marks if mark >= pass_mark)

    return {
        "average": sum(checked_marks) / len(checked_marks),
        "highest": max(checked_marks),
        "lowest": min(checked_marks),
        "pass_rate": round((pass_count / len(checked_marks)) * 100, 2),
    }

