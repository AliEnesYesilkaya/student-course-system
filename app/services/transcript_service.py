from app.services.gpa_service import calculate_gpa


def generate_transcript(student_name, courses):

    print("\n========== TRANSKRIPT ==========")
    print(f"Öğrenci: {student_name}")
    print("--------------------------------")

    for course in courses:

        print(
            f"Ders: {course['course_name']} | "
            f"AKTS: {course['ects']} | "
            f"Harf Notu: {course['letter_grade']}"
        )

    gpa = calculate_gpa(courses)

    print("--------------------------------")
    print(f"GANO: {gpa}")

    if gpa >= 2.0:
        print("Durum: Başarılı")

    else:
        print("Durum: Başarısız")

    print("================================")

