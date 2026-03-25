# MySQL User Manager

Simple Python CLI application for managing users in a MySQL database running in Docker.

---

## 🚀 Features

- List users from database
- Add new users
- Connect Python app to MySQL (Docker)
- Uses environment variables for configuration

---

## 🧱 Technologies

- Python 3
- MySQL
- Docker
- mysql-connector-python

---

## 📁 Project Structure

````
.
├── main.py # CLI application logic
├── db.py # Database connection
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md
````

---

## ⚙️ Requirements

- Python 3
- Docker

---

## 📦 Install dependencies

```bash
pip install -r requirements.txt

```
## 🐳 Run MySQL in Docker
```bash
docker volume create mysql_data

docker run -d \
  --name muj-mysql \
  -e MYSQL_ROOT_PASSWORD=heslo123 \
  -p 3306:3306 \
  -v mysql_data:/var/lib/mysql \
  mysql:8
 ``` 
## 🗄️ Create database and table
Connect to MySQL:

````bash

docker exec -it muj-mysql mysql -u root -p

````

Password:
```bash
heslo123
```
Then run:
```MySQL
CREATE DATABASE testlab;
USE testlab;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);
```
## 🌍 Environment variables

The application supports these environment variables:

|   Variable   |  Default  |
|:------------:|:---------:|
|   DB_HOST    | localhost |
|   DB_PORT    |   3306    |  
|    DB_USE    |   root    |  
| DB_PASSWORD  | 	heslo123 | 
|   DB_NAME    | 	testlab  |  

Example:             

```bash
export DB_HOST=localhost
export DB_PORT=3306
export DB_USER=root
export DB_PASSWORD=heslo123
export DB_NAME=testlab
```

## ▶️ Run the application
```bash
python main.py
```

## 💻 Example usage
````
1 - zobraz uživatele
2 - přidat uživatele
3 - konec
````
## 📚 What I learned
- Running MySQL in Docker
- Using Docker volumes for persistence
- Connecting Python to MySQL
- Executing SQL queries (SELECT, INSERT)
- Basic CLI application design
- Using environment variables in Python apps
## ⚠️ Notes
This is a learning project
Do not use default credentials in production
## 📌 Author
````
Jan Hanzlík