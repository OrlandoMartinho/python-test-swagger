
### 📄 `README.md` – Book API Project (Flask + PostgreSQL + Swagger + Pydantic)

# 📚 Book API – Flask + PostgreSQL + Swagger + Pydantic

This is a RESTful API project built with **Flask**, integrated with:
- **PostgreSQL** (relational database)
- **Flask-SQLAlchemy** (ORM)
- **Flask-RESTX** (Swagger-style documentation)
- **Pydantic** (data validation like Zod in JavaScript)



## 🚀 Features

- ✅ Create a book
- ✅ List all books
- ✅ Update a book
- ✅ Delete a book
- ✅ Request body validation using Pydantic
- ✅ Swagger UI for easy API testing



## ⚙️ Tech Stack

| Technology         | Description                           |
|--------------------|----------------------------------------|
| Python 3.11+       | Programming language                   |
| Flask              | Lightweight web framework              |
| Flask-RESTX        | REST routing + Swagger UI              |
| Flask-SQLAlchemy   | ORM for database interaction           |
| Pydantic           | Data validation (Zod-like)             |
| PostgreSQL         | Relational database                    |

---

## 🧪 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/book-api.git
cd book-api
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

> Create a `requirements.txt` file with:
>
> ```
> flask
> flask-restx
> flask-sqlalchemy
> psycopg2-binary
> pydantic
> ```

---

## 🔧 Configuration

In `config.py`, set your database credentials:

```python
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/bookdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

Replace:

* `username` = your PostgreSQL username
* `password` = your PostgreSQL password
* `bookdb` = your PostgreSQL database name

---

## ▶️ Running the Application

```bash
python app.py
```

Access the API via:

* Swagger UI: [http://localhost:5000/](http://localhost:5000/)
* API Endpoints: `/livros`, `/livros/<id>`

---

## 📬 Example Requests

### Create a Book (POST `/livros`)

```json
{
  "titulo": "Don Quixote",
  "autor": "Miguel de Cervantes",
  "publicado_em": "1605-01-16"
}
```

### Update a Book (PUT `/livros/1`)

```json
{
  "titulo": "Updated Don Quixote"
}
```



## 📌 Notes

* Database used: **PostgreSQL**
* Request data is validated using **Pydantic**
* Automatic API documentation provided by **Swagger (via Flask-RESTX)**

---

## 👨‍💻 Author

**Orlando Martinho**
📧 [srsaiombo@gmail.com](mailto:srsaiombo@gmail.com)
🌍 Angola

