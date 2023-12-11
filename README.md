# tree-like-menu

Stack
-----------------------------------
asgiref==3.7.2
***
Django==4.2.7
***
django-debug-toolbar==4.2.0
***
psycopg2==2.9.9
***
sqlparse==0.4.4
***
tzdata==2023.3

Установка postgresql с помощью docker
-----------------------------------

docker run --name menu -e POSTGRES_PASSWORD=postgres -p 1964:5432 -d postgres

добавление моделей 
-----------------------------------
модели добавляются черед admin. 

Debag_foobar
-----------------------------------
в проекте настроен toolbar для просмотра количества запросов к бд
