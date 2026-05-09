def calculate_gpa(courses):

    grade_points = {

        "AA": 4.0,
        "BA": 3.5,
        "BB": 3.0,
        "CB": 2.5,
        "CC": 2.0,
        "DC": 1.5,
        "DD": 1.0,
        "FD": 0.5,
        "FF": 0.0
    }

    total_points = 0
    total_ects = 0

    for course in courses:

        letter_grade = course["letter_grade"]
        ects = course["ects"]

        point = grade_points[letter_grade]

        total_points += point * ects
        total_ects += ects

    if total_ects == 0:
        return 0

    gpa = total_points / total_ects

    return round(gpa, 2)

