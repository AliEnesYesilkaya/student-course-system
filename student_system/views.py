from django.http import HttpResponse

from student_system.services.gpa_service import calculate_gpa

# İleride eklenecek model importları
# from student_system.models import Student, Enrollment


def home(request):

    return HttpResponse("Ana Sayfa")


def courses(request):

    return HttpResponse("Dersler Sayfası")


def enrollment(request):

    return HttpResponse("Ders Kayıt Sayfası")


def transcript(request):

    """
    Şu an demo veriler kullanılmaktadır.
    İleride Enrollment modeli üzerinden
    gerçek veriler database'den çekilecektir.
    """

    # Gelecekteki yapı örneği:
    # student = Student.objects.get(id=1)
    # courses = Enrollment.objects.filter(student=student)

    # Demo amaçlı örnek ders verileri
    courses = [

        {
            "course_name": "Programlamaya Giriş",
            "ects": 6,
            "letter_grade": "BA"
        },

        {
            "course_name": "Veri Yapıları",
            "ects": 5,
            "letter_grade": "CB"
        },

        {
            "course_name": "Matematik 1",
            "ects": 5,
            "letter_grade": "CC"
        }
    ]

    gpa = calculate_gpa(courses)

    return HttpResponse(
        f"Öğrenci GANO: {gpa}"
    )