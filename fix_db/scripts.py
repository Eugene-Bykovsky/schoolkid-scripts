import random
from datacenter.models import (Schoolkid, Mark, Chastisement, Commendation,
                               Lesson)


def fix_marks(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__icontains=schoolkid_name)
        schoolkid_bad_points = Mark.objects.filter(schoolkid=schoolkid,
                                                   points__in=[2, 3])
        schoolkid_bad_points.update(points=5)
        print(f"Исправлено оценок: {schoolkid_bad_points.count()}")
    except Schoolkid.DoesNotExist:
        print("Ученик не найден. Проверьте имя.")
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников. Уточните имя.")


def remove_chastisements(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__icontains=schoolkid_name)
        schoolkid_chastisements = Chastisement.objects.filter(
            schoolkid=schoolkid)
        chastisements_count = schoolkid_chastisements.count()
        schoolkid_chastisements.delete()
        print(f"Удалено замечаний: {chastisements_count}")
    except Schoolkid.DoesNotExist:
        print("Ученик не найден. Проверьте имя.")
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников. Уточните имя.")


def create_commendation(schoolkid_name, subject):
    try:
        schoolkid = Schoolkid.objects.get(full_name__icontains=schoolkid_name)
        lessons = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject
        ).order_by('date')
        if not lessons.exists():
            print("Уроки по предмету не найдены.")
            return
        lesson = random.choice(list(lessons))
        commendation = Commendation.objects.create(
            text='Хвалю удальца!',
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher
        )
        print(f"Похвала создана: {commendation.text}")
    except Schoolkid.DoesNotExist:
        print("Ученик не найден. Проверьте имя.")
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников. Уточните имя.")
