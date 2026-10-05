def analyze_student_marks(marks):
    valid_marks = []
    for mark in marks:
        try:
            mark = float(mark)
            if 0 <= mark <= 100:
                valid_marks.append(mark)
        except ValueError:
            pass

    if not valid_marks:
        return "No valid marks provided."

    average = sum(valid_marks) / len(valid_marks)
    highest = max(valid_marks)
    lowest = min(valid_marks)
    passed = [mark for mark in valid_marks if mark >= 50]
    pass_rate = len(passed) / len(valid_marks) * 100

    return {
        "avg": average,
        "high": highest,
        "low": lowest,
        "pass_rate": pass_rate,
    }


if __name__ == "__main__":
    raw_marks = input("Enter marks separated by commas: ")
    marks = raw_marks.split(",")
    result = analyze_student_marks(marks)
    print(result)

