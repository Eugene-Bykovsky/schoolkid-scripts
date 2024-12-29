# Скрипты для исправления данных в Django

Этот репозиторий содержит набор скриптов для работы с базой данных школьного сайта.

## Установка
1. Склонируйте репозиторий:
   ```
   git clone git@github.com:Eugene-Bykovsky/schoolkid-scripts.git

2. Поместите папку fix_db рядом с файлом manage.py в вашем Django-проекте.

## Использование

1. Откройте Django Shell:
    ```
   python manage.py shell

2. Импортируйте нужные функции:
    ```
   from fix_db.scripts import fix_marks, remove_chastisements, create_commendation

## Примеры:


1. Исправить оценки ученика:

   ```
   fix_marks('Фролов Иван Григорьевич')
   ```
   
2. Удалить замечания ученика:

   ```
   remove_chastisements('Фролов Иван Григорьевич')
   ```

3. Создать похвалу:

   ```
   create_commendation('Фролов Иван Григорьевич', 'Физкультура')
   ```
