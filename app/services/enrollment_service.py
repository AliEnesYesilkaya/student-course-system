#  kontenjan kontrolü
def check_capacity(current_students, capacity):

    return current_students < capacity

# alınabilecek maksimum ders saati
def check_course_limit(current_course_count, max_courses=40):

    return current_course_count < max_courses

# ilk alttan dersi al
def check_failed_courses_priority(
        failed_courses,
        selected_courses
):

    for course in failed_courses:

        if course not in selected_courses:
            return False

    return True

# her seçmeli grubundan bir seçmeli al
def check_elective_group(
        selected_groups,
        new_group
):

    return new_group not in selected_groups

# seçmeli ve zorunlu derslerin kontenjanlarını ayır
def get_course_capacity(course_type):

    if course_type == "mandatory":
        return 70

    elif course_type == "elective":
        return 30

    return 0

# dersin daha önce geçilip geçilmediği
def check_previous_completion(letter_grade, gpa):

    passed_grades = [
        "AA",
        "BA",
        "BB",
        "CB",
        "CC"
    ]

    failed_grades = [
        "FF",
        "FD",
        "DD",
        "D"
    ]

    if letter_grade in passed_grades:
        return False

    if letter_grade == "DC":

        if gpa >= 2.0:
            return False

        return True

    if letter_grade in failed_grades:
        return True

    return True

# ön koşullu dersler
def check_prerequisites(
        course_name,
        completed_courses,
        has_completed_internship
):

    prerequisites = {

        "Nesne Yönelimli Programlama": [
            "Programlamaya Giriş ve Algoritmalar",
            "Veri Yapıları"
        ],

        "Yazılım Tasarım Mimarisi": [
            "Nesne Yönelimli Programlama"
        ]
    }

    if course_name == "İş Yeri Eğitimi":

        return has_completed_internship

    required_courses = prerequisites.get(course_name)

    if not required_courses:
        return True

    if course_name == "Nesne Yönelimli Programlama":

        for course in required_courses:

            if course in completed_courses:
                return True

        return False

    for course in required_courses:

        if course not in completed_courses:
            return False

    return True

#kayıt olunabilir mi
def can_student_enroll(
        current_students,
        course_type,
        current_course_count,
        failed_courses,
        selected_courses,
        selected_groups,
        new_group,
        letter_grade,
        gpa,
        course_name,
        completed_courses,
        has_completed_internship
):

    capacity = get_course_capacity(course_type)

    if not check_capacity(current_students, capacity):

        return (
            f"Kayıt başarısız: "
            f"Kontenjan dolu. "
            f"Maksimum kapasite: {capacity}"
        )

    if not check_course_limit(current_course_count):

        return (
            "Kayıt başarısız: "
            "40 ders saati limiti aşıldı."
        )

    if not check_failed_courses_priority(
            failed_courses,
            selected_courses
    ):

        return (
            "Kayıt başarısız: "
            "Önce alttan kalan dersler alınmalıdır."
        )

    if not check_elective_group(
            selected_groups,
            new_group
    ):

        return (
            "Kayıt başarısız: "
            f"{new_group} grubundan zaten ders seçildi."
        )

    if not check_previous_completion(letter_grade, gpa):

        return (
            "Kayıt başarısız: "
            "Bu ders daha önce başarıyla geçildi."
        )

    if not check_prerequisites(
            course_name,
            completed_courses,
            has_completed_internship
    ):

        return (
            "Kayıt başarısız: "
            "Ön koşul şartları sağlanmıyor."
        )

    return "Kayıt başarılı."




