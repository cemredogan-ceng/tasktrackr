#  TaskTrackr

**TaskTrackr** is a full-featured task management backend built with Flask. It provides secure authentication, task tracking per user, and a scalable structure for future frontend or mobile integrations.

---

##  Features

- User registration and login with JWT authentication  
- Create, retrieve, update, and delete tasks  
- Tasks are user-specific and private  
- Secure password hashing  
- Modular and scalable project structure  
- Postman-tested API endpoints

---

##  Built With

- Python 3.12  
- Flask  
- Flask-JWT-Extended  
- Flask-SQLAlchemy  
- SQLite (can be switched to PostgreSQL or others)

---

##  Folder Structure
backend/ ├── app.py ├── config.py ├── db.py ├── models/ │ ├── user.py │ └── task.py ├── routes/ │ ├── auth_routes.py │ └── task_routes.py └── instance/ └── tasktrackr.sqlite (auto-generated)


---

##  API Endpoints

| Method | Endpoint              | Description                |
|--------|------------------------|----------------------------|
| POST   | `/api/auth/register`   | Register a new user        |
| POST   | `/api/auth/login`      | Login and get JWT token    |
| GET    | `/api/auth/profile`    | View user profile (auth)   |
| POST   | `/api/tasks/`          | Create a task (auth)       |
| GET    | `/api/tasks/`          | List all tasks (auth)      |
| PUT    | `/api/tasks/<id>`      | Update a task (auth)       |
| DELETE | `/api/tasks/<id>`      | Delete a task (auth)       |

>  All `/api/tasks/` routes require Authorization: Bearer `<JWT Token>` in headers.

---

##  Setup Instructions

1. Clone the repository  
   ```bash
   git clone https://github.com/cemredogan-ceng/tasktrackr.git
   cd tasktrackr/backend
   
2.Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate

3.Install dependencies
pip install -r requirements.txt

4.Run the Flask server
python app.py

**Test with Postman**
Make sure to:

Register a user

Login to get your access token

Add the token as a Bearer Token in the Authorization header for all protected endpoints
