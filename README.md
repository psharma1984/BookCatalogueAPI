# BookCatalogueAPI
API that displays collection of books and their authors
Quick Setup:
1. Git clone the repo
2. create a virtual environment
3. (Install the dependencies) pip install -r requirements.txt
4. Make Migrations : python manage.py makemigrations
5. python manage.py migrate
6. Run the server : python manage.py runserver

The different endpoints of the API are that can be accessed in POSTMAN or the browser:
1. http://127.0.0.1:8000/catalogue/books/              (Books List)
2. http://127.0.0.1:8000/catalogue/books/2              (Book detail view)
3. same goes for genres and authors
