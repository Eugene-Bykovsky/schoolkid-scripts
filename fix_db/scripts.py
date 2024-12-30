from random import choice
from datacenter.models import (Schoolkid, Mark, Chastisement, Commendation,
                               Lesson)


COMMENDATIONS = [
    "Молодец!",
    "Отлично!",
    "Прекрасно!",
    "Ты меня приятно удивил!",
    "Хвалю за старания!",
    "Очень хороший ответ!",
    "Ты сегодня прыгнул выше головы!",
    "Замечательно!",
    "Так держать!",
    "Талантливо!",
]


def get_schoolkid_by_name(schoolkid_name):
    try:
        return Schoolkid.objects.get(full_name__icontains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print("Ученик не найден. Проверьте имя.")
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников. Уточните имя.")


def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid_by_name(schoolkid_name)
    if not schoolkid:
        return

    schoolkid_bad_points = Mark.objects.filter(schoolkid=schoolkid,
                                               points__in=[2, 3])
    bad_points_count = schoolkid_bad_points.count()
    schoolkid_bad_points.update(points=5)
    print(f"Исправлено оценок: {bad_points_count}")


def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid_by_name(schoolkid_name)
    if not schoolkid:
        return
    schoolkid_chastisements = Chastisement.objects.filter(
        schoolkid=schoolkid)
    chastisements_count = schoolkid_chastisements.count()
    schoolkid_chastisements.delete()
    print(f"Удалено замечаний: {chastisements_count}")


def create_commendation(schoolkid_name, subject):
    schoolkid = get_schoolkid_by_name(schoolkid_name)
    if not schoolkid:
        return
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject
    ).order_by('?').first()
    if not lesson:
        print("Уроки по предмету не найдены.")
        return
    commendation = Commendation.objects.create(
        text=choice(COMMENDATIONS),
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher
    )
    print(f"Похвала создана: {commendation.text}")
