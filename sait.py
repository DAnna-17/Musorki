from flask import Flask, url_for, app, request, redirect
from main import func1
import sqlite3

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/map', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        with open('form.html', encoding="utf-8") as f:
            return f.read()
    if request.method == 'POST':
        print(request.form['legal'])
        print(request.form['type'])
        func1( request.form['type'], request.form['legal'])
        with open('form.html', encoding="utf-8") as f:
            return f.read()

@app.route('/caba', methods=['POST', 'GET'])
def caba():
    if request.method == 'GET':
        s = ''
        con = sqlite3.connect("static//base//admin.db")
        cur = con.cursor()
        t = cur.execute("SELECT * FROM orders").fetchall()
        con.close()
        con = sqlite3.connect("static//base//dump.db")
        cur = con.cursor()
        t1 = cur.execute("SELECT * FROM dump").fetchall()
        con.close()
        for i in t:
            s += " ".join([str(k) for k in i]) + '<br>'
        s += '<br><br>'
        for i in t1:
            s += " ".join([str(k) for k in i]) + '<br>'
        with open('cab_adm.html') as f:
            return f.read().format(s)
    if request.method == 'POST':
        con = sqlite3.connect("static//base//dump.db")
        cur = con.cursor()
        n = len(cur.execute("SELECT ID_Dump FROM dump").fetchall()) + 1
        con.commit()
        con.close()
        con = sqlite3.connect("static//base//dump.db")
        cur = con.cursor()
        cur.execute("INSERT INTO dump VALUES (?, ?, ?, ?, ?, ?, ?)", (n, request.form["coord"], request.form["op_mod"],
                                                                      request.form["resp_org"], request.form["tel"],
                                                                      request.form["leg"], request.form["area"])).fetchall()
        con.commit()
        con.close()
        if (request.form['type']) == 'y':
            con = sqlite3.connect("static//base//dump.db")
            cur = con.cursor()
            n = len(cur.execute('DELETE FROM orders WHERE id = ?;', (request.form['id'])).fetchall()) + 1
            con.commit()
            con.close()

        with open('cab_adm.html', encoding="utf-8") as f:
            return f.read()

@app.route('/cabu', methods=['POST', 'GET'])
def cabu():
    if request.method == 'GET':
        with open('cab_us.html', encoding="utf-8") as f:
            return f.read()
    if request.method == 'POST':
        con = sqlite3.connect("static//base//admin.db")
        cur = con.cursor()
        n = len(cur.execute("SELECT id FROM orders").fetchall()) + 1
        con.commit()

        con = sqlite3.connect("static//base//admin.db")
        cur = con.cursor()
        cur.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?)", (n, request.form["coord"], request.form["resp_org"],
                                                                     request.form["area"], request.form["tel"], request.form["log"])).fetchall()
        con.commit()
        con.close()
        print(11111111111111)
        with open('cab_us.html', encoding="utf-8") as f:
            return f.read()

@app.route('/reg', methods=['POST', 'GET'])
def reg():
    if request.method == 'GET':
        with open('form1.html', encoding="utf-8") as f:
            return f.read()
    if request.method == 'POST':
        con = sqlite3.connect("static//base//admin.db")
        cur = con.cursor()

        s2 = "SELECT login FROM users"

        result = cur.execute(s2).fetchall()
        con.close()

        result1 = []

        for i in result:
            result1.append(i[0])

        result = result1
        print(result)

        if request.form['email'] in result:
            con = sqlite3.connect("static//base//admin.db")
            cur = con.cursor()
            pas = cur.execute('SELECT password, admin FROM users WHERE login=?', (request.form["email"], )).fetchall()[0]
            con.close()
            if pas[0] == request.form['password'] and pas[1] == 1:
                return redirect(url_for('caba'))
            elif pas[0] == request.form['password'] and pas[1] == 0:
                return redirect(url_for('cabu'))
        else:
            con = sqlite3.connect("static//base//admin.db")
            cur = con.cursor()
            print(request.form["email"], request.form["password"])
            cur.execute("INSERT INTO users VALUES (?, ?, 0)", (request.form["email"], str(request.form["password"]))).fetchall()
            con.commit()
            con.close()
            with open('form1.html', encoding="utf-8") as f:
                return f.read()




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')