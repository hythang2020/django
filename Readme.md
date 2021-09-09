Add new code in:

1. main/settings.py

   - Import library django_heroku
   - Add page app to INSTALLED_APPS
   - Add django_heroku.settings(locals()) at the end of file

2. main/urls.py

   - Connect with file urls in app pages

3. page/urls.py

   - Create link so that client can call to it

4. page/views.py

   - Create function will return data when client call to a specific url.

5. Run those command:

   - pip install -r requirements.txt
   - python manage.py showmigrations
   - python manage.py migrate
   - python manage.py runserver
