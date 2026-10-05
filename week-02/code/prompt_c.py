# Assumptions:
# - marks must be a non-empty list of int or float values.
# - valid marks are in the inclusive range 0 to 100.
# - a mark passes when it is greater than or equal to pass_mark.
# - pass_rate is rounded to two decimal places.


def analyze_marks(marks, pass_mark=50):
    if not marks:
        raise ValueError("marks cannot be empty")

    for mark in marks:
        if not isinstance(mark, (int, float)):
            raise ValueError("all marks must be numeric")
        if mark < 0 or mark > 100:
            raise ValueError("marks must be between 0 and 100")

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    passed = sum(1 for mark in marks if mark >= pass_mark)
    pass_rate = round((passed / len(marks)) * 100, 2)

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "pass_rate": pass_rate,
    }


def test_one_mark():
    assert analyze_marks([100]) == {
        "average": 100,
        "highest": 100,
        "lowest": 100,
        "pass_rate": 100.0,
    }


def test_decimals():
    assert analyze_marks([49.5, 50]) == {
        "average": 49.75,
        "highest": 50,
        "lowest": 49.5,
        "pass_rate": 50.0,
    }


def test_custom_pass_mark():
    assert analyze_marks([40, 60, 80], 70) == {
        "average": 60.0,
        "highest": 80,
        "lowest": 40,
        "pass_rate": 33.33,
    }


def test_empty_list():
    try:
        analyze_marks([])
    except ValueError:
        return
    raise AssertionError("Expected ValueError for empty list")


def test_text_value():
    try:
        analyze_marks([40, "60"])
    except ValueError:
        return
    raise AssertionError("Expected ValueError for text value")


def test_out_of_range_values():
    try:
        analyze_marks([-1, 50, 101])
    except ValueError:
        return
    raise AssertionError("Expected ValueError for out-of-range marks")


if __name__ == "__main__":
    test_one_mark()
    test_decimals()
    test_custom_pass_mark()
    test_empty_list()
    test_text_value()
    test_out_of_range_values()
    print("All tests passed.")

