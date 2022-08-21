from flask import Flask, request, jsonify
import mysql.connector as connection
app = Flask(__name__)
mydb=connection.connect(host='localhost', user='root', passwd='Letsplay@12345678')
cursor=mydb.cursor()
cursor.execute('create database if not exists tasksql')
cursor.execute("create table if not exists tasksql.tasktable(name varchar(30), number int)")

@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute('insert into tasksql.tasktable values (%s, %s)', (name,number))
        mydb.commit()
        return jsonify(str('successfully inserted'))

@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method=='POST':
        get_name = request.json['get_name']
        cursor.execute('update tasksql.tasktable set number = number+500 where name = %s', (get_name,))
        mydb.commit()
        return jsonify(str('successfully updated'))

@app.route('/fetch', methods=['POST', 'GET'])
def fetch_data():
    cursor.execute('select * from tasksql.tasktable')
    l=[]
    for i in cursor.fetchall():
        l.append(i)
        return jsonify(str(l))

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method=='POST':
        name_delete = request.json['name_delete']
        cursor.execute('delete from tasksql.tasktable where name = %s', (name_delete,))
        mydb.commit()
        return jsonify(str('successfully deleted'))

if __name__ == '__main__':
    app.run()

