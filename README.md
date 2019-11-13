# Simple Django REST API

Clone the project and run these commands:

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate

To start server:

    python manage.py runserver

## API Routes

| Endpoint                            | Method | Usage                  |
| ----------------------------------- | ------ | ---------------------- |
| `/api/auth/login/`                  | POST   | Login                  |
| `/api/auth/logout/`                 | POST   | Logout                 |
| `/api/auth/register/`               | POST   | Register new account   |
| `/api/auth/user/`                   | GET    | Get user details       |
| `/api/auth/google/`                 | POST   | Login with Google      |
| `/api/auth/facebook/`               | POST   | Login with Facebook    |
| `/api/auth/password/change/`        | POST   | Change password        |
| `/api/auth/password/reset/`         | POST   | Reset password         |
| `/api/auth/password/reset/confirm/` | POST   | Confirm reset password |
| `/api/articles`                     | GET    | Get articles           |
| `/api/articles`                     | POST   | Create an article      |
| `/api/articles/:id/`                | GET    | Get an article         |
| `/api/articles/:id/`                | PUT    | Update an article      |
| `/api/articles/:id/`                | DELETE | Delete an article      |

### Admin

    username: admin
    password: your_password
