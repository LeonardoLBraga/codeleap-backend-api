# 📘 CodeLeap Backend API

This is a RESTful API built with **Django** and **Django REST Framework** as part of the backend technical challenge for **CodeLeap**.

## 🧰 Tech Stack

- Python 3.11+
- Django 5.0+
- Django REST Framework
- SQLite (used for development; easily replaceable)

## 🚀 Features

- ✅ Create posts
- ✅ List all posts
- ✅ Update posts
- ✅ Delete posts

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/LeonardoLBraga/codeleap-backend-api
   cd codeleap-backend-api
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

Visit: [http://localhost:8000/careers/](http://localhost:8000/careers/)

## 📬 API Endpoints

### Base Model Structure
```json
{
  "id": number,
  "username": "string",
  "created_datetime": "datetime",
  "title": "string",
  "content": "string"
}
```

### Available Endpoints

| Method | Route               | Description                  |
|--------|---------------------|------------------------------|
| GET    | `/careers/`         | List all posts               |
| POST   | `/careers/`         | Create a new post            |
| PATCH  | `/careers/<id>/`    | Update a post                |
| DELETE | `/careers/<id>/`    | Delete a post                |

### Request Examples

#### ➕ Create Post (POST `/careers/`)
```json
{
  "username": "string",
  "title": "string",
  "content": "string"
}
```
#### ➕ Get Post (GET `/careers/`)
```No body required.```

#### ✏️ Update Post (PATCH `/careers/<id>/`)
```json
{
  "title": "string",
  "content": "string"
}
```

#### 🗑️ Delete Post (DELETE `/careers/<id>/`)
```No body required.```

## 🌐 Deployment (Render)

The API is live at:

🔗 https://codeleap-backend-api-oxdh.onrender.com/careers/

## 📎 Notes

- All endpoints end with a trailing slash (`/`), as required by Django REST Framework.
- The SQLite database is used only for local/testing purposes.
- This API is fully ready to be integrated with any frontend framework (e.g., React).
