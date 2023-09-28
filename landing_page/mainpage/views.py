from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Curators, Enrollment, EnrollmentType, GraduateProjects


def index(request: HttpRequest) -> HttpResponse:
    enrollment = Enrollment.get_enrollment_with_active_registration(enrollment_type=EnrollmentType.BASE)
    context = {
        'enrollment': enrollment,
        'projects': GraduateProjects.objects.all(),
        'registration_closes_date_formatted': (
            enrollment.end_registration_date.strftime('%b %d, %Y %H:%M:%S')
            if enrollment else ""
        ),
        'student_videos': [
            {
                'title': 'Путь джуна — из геодезиста в Support Engineer',
                'youtube_id': 'YySKSlNHDXo',
            },
            {
                'title': 'Как становятся джунами в британской компании на удалёнке',
                'youtube_id': 'TsqEigK2WQk',
            },
            {
                'title': 'Python-стрим - вход джуниора в АйТи',
                'youtube_id': 'wvijeR-eINA',
            },
            {
                'title': 'Как войти в разработку за считанные месяцы',
                'youtube_id': 'DkHWpgctTuA',
            },
            {
                'title': 'Личный опыт джуниора: удачи, фейлы, рецепты',
                'youtube_id': 'vKKqsJ8IvAg',
            },
            {
                'title': 'Python для врача и медицина для программиста.',
                'youtube_id': 's_ZNqjIW3ZA',
            }
        ],
        'curators_list': Curators.objects.filter(is_visible=True),
        'today': date.today(),
    }
    return render(request, 'mainpage/index.html', context)


def advanced_handle(request: HttpRequest) -> HttpResponse:
    enrollment = Enrollment.get_enrollment_with_active_registration(enrollment_type=EnrollmentType.ADVANCED)
    return render(
        request,
        'mainpage/advanced.html',
        context={
            'today': date.today(),
            'enrollment': enrollment,
            'registration_closes_date_formatted': (
                enrollment.end_registration_date.strftime('%b %d, %Y %H:%M:%S')
                if enrollment else ""
            ),
        },
    )


def success_handle(request: HttpRequest) -> HttpResponse:
    enrollment = Enrollment.get_enrollment_with_active_registration(enrollment_type=EnrollmentType.BASE)
    return render(
        request,
        'mainpage/success.html',
        context={
            'enrollment': enrollment,
        },
    )


def success_handle_advanced(request: HttpRequest) -> HttpResponse:
    enrollment = Enrollment.get_enrollment_with_active_registration(enrollment_type=EnrollmentType.ADVANCED)
    return render(
        request,
        'mainpage/success.html',
        context={
            'enrollment': enrollment,
        },
    )
