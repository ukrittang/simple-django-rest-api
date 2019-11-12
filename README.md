# Simple Django REST API

Clone the project and run these commands:

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    python src/manage.py migrate

To start server:

    python src/manage.py runserver

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

    username: admin
    password: your_password
