# 📝 Django Blog Application

## 🚀 Introduction
Welcome to the **Django Blog Application** – a simple yet effective blogging platform built with Django. This application allows users to explore blogs, save them for later reading, and engage through comments.

## 🎯 Features
- 📝 **Blog Listing** – View all available blog posts
- 📖 **Detailed Blog View** – Read complete blog content
- 📌 **Read Later** – Save blogs to read later
- 📂 **Read Later List** – Access saved blogs anytime
- 🗨️ **Comment System** – Engage with posts through comments

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default) / PostgreSQL (optional)
- **Deployment:** Docker, AWS (optional)

## 🏗️ Installation & Setup
Follow these steps to get the Django Blog Application up and running on your local machine.

### 1️⃣ Clone the Repository
```sh
https://github.com/iam-harshsoni/Python_Projects.git
cd Projects/my_site/
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Apply Migrations & Create a Superuser
```sh
python manage.py migrate
python manage.py createsuperuser
```

### 4️⃣ Run the Development Server
```sh
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`

## 🔧 Environment Variables
Create a `.env` file and add the following environment variables:
```
APP_HOST=""
SECRET_KEY=""
IS_DEVELOPMENT=""
DB_NAME=""
DB_USER=""
DB_PASSWORD=""
DB_HOST=""
DB_PORT=""

AWS_STORAGE_BUCKET_NAME=""
AWS_S3_REGION_NAME=""
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
AWS_S3_ENDPOINT_URL=""
AWS_CUSTOM_DOMAIN=""
```

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/11344d9f-76f6-4d31-8997-749d480b6cfe)

## 🤝 Contributing
We welcome contributions! Feel free to fork, create a feature branch, and submit a pull request.

## 📬 Contact
For any queries or suggestions, reach out at **soni.harshs777@example.com** or connect on [LinkedIn](https://www.linkedin.com/in/harsh-soni-007hs).

Happy Blogging! 🎉
