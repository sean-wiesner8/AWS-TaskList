import pymysql
pymysql.install_as_MySQLdb()
import json
from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'database-1.cyhwuaohcrrn.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Penguini8!'
app.config['MYSQL_DB'] = 'tasklist'

mysql = MySQL(app)

def success_response(body, status_code=200):
    return json.dumps(body), status_code

def failure_response(message, status_code=404):
    return json.dumps({"error" : message}), status_code

@app.route('/')
def firstroute():
    return success_response({"Hello" : "World"})

@app.route('/users/')
def get_users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = []
    for row in cursor:
        users.append({"id" : row[0], "name" : row[1], "username" : row[2]})
    return success_response(users)

@app.route('/users/<int:id>/')
def get_user(id):
    cursor = mysql.connection.cursor()
    checkuser = cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    if not checkuser:
        return failure_response("user does not exist")
    for row in cursor:
        return success_response({"id" : row[0], "username" : row[1], "password" : row[2]})
    return None

@app.route('/users/', methods=['POST'])
def create_user():
    body = json.loads(request.data)
    username = body.get('username')
    password = body.get('password')
    if username is None or password is None:
        return failure_response("username or password fields empty", 400)
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    mysql.connection.commit()
    return success_response(cursor.lastrowid, 201)

@app.route('/users/<int:id>/', methods=['DELETE'])
def delete_user(id):
    cursor = mysql.connection.cursor()
    checkuser = cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    if not checkuser:
        return failure_response("user does not exist")
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    mysql.connection.commit()
    return success_response({"result" : "success"})

@app.route('/tasks/<int:users_id>/')
def get_user_tasks(users_id):
    cursor = mysql.connection.cursor()
    checkuser = cursor.execute("SELECT * FROM users WHERE id = %s", (users_id,))
    if not checkuser:
        return failure_response("user does not exist")
    cursor.execute("SELECT * FROM tasks WHERE users_id = %s", (users_id,))
    tasks = []
    for row in cursor:
        tasks.append({"id" : row[0], "task_name" : row[1], "description" : row[2], "users_id" : row[3]})
    return success_response(tasks)

@app.route('/tasks/<int:users_id>/', methods=['POST'])
def create_task(users_id):
    cursor = mysql.connection.cursor()
    checkuser = cursor.execute("SELECT * FROM users WHERE id = %s", (users_id,))
    if not checkuser:
        return failure_response("user does not exist")
    body = json.loads(request.data)
    task_name = body.get("task_name")
    description = body.get("description")
    if task_name is None or description is None:
        return failure_response("task_name or description fields are missing", 400)
    cursor.execute("INSERT INTO tasks (task_name, description, users_id) VALUES (%s, %s, %s)", (task_name, description, users_id))
    mysql.connection.commit()
    return success_response(cursor.lastrowid)

@app.route('/tasks/<int:id>/', methods=['DELETE'])
def delete_task(id):
    cursor = mysql.connection.cursor()
    checkuser = cursor.execute("SELECT * FROM tasks WHERE id = %s", (id,))
    if not checkuser:
        return failure_response("task does not exist")
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    mysql.connection.commit()
    return success_response({"result" : "success"})

if __name__ == "__main__":
    app.run()
