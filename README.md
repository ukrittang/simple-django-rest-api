# Simple Django REST API

Clone the project and run these commands:

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    python src/manage.py migrate

To start server:

    python src/manage.py runserver

## API Routes

| Endpoint             | Method | Usage             |
| -------------------- | ------ | ----------------- |
| `/api/auth/login/`   | POST   | Login             |
| `/api/auth/logout/`  | POST   | Logout            |
| `/api/auth/user/`    | GET    | Get user details  |
| `/api/articles`      | GET    | Get articles      |
| `/api/articles`      | POST   | Create an article |
| `/api/articles/:id/` | GET    | Get an article    |
| `/api/articles/:id/` | PUT    | Update an article |
| `/api/articles/:id/` | DELETE | Delete an article |

### Admin

    username: admin
    password: your_password
