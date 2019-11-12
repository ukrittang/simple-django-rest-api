# Simple Django REST API

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    cd src
    python manage.py migrate
    python manage.py runserver

## API Routes

    /api/auth/login/
    /api/auth/logout/
    /api/auth/password/reset/confirm/
    /api/auth/user/
    /api/auth/password/change/

    /api/articles/create/
    /api/articles/update/
    /api/articles/delete/
    /api/articles/

### Admin

    admin/your_password
