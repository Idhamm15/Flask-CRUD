# Merender Template
from flask import Flask, render_template, request, redirect, url_for

# Import Database
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)
app.static_folder = 'static'

# Koneksi Database
app.secret_key = 'latihan'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1'
app.config['MYSQL_DB'] = 'mahasiswa'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)



@app.route('/')
def home():
    # GET DATA
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute('SELECT * FROM mahasiswa')
    mahasiswa = curl.fetchall()
    curl.close()

    # Mengembalikan nilai
    return render_template('index.html',mahasiswa=mahasiswa)


# CREATE DATA
@app.route('/store', methods=['POST'])
def store():  
    nim = request.form['nim']
    nama = request.form['nama']
    jurusan = request.form['jurusan']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO mahasiswa (nim, nama, jurusan)  VALUES (%s, %s, %s)', (nim, nama, jurusan))
    mysql.connection.commit()
    return redirect(url_for('home'))


# UPDATE DATA nim disable
@app.route('/update/<string:id>', methods=['POST'])
def update(id):
    # nim = request.form['nim']
    nama = request.form['nama']
    jurusan = request.form['jurusan']
    cur = mysql.connection.cursor()
    cur.execute('UPDATE mahasiswa SET nama=%s, jurusan=%s WHERE id=%s', (nama, jurusan,id,))
    mysql.connection.commit()
    return redirect(url_for('home'))

# UPDATE DATA Dengan nim
# @app.route('/update/<string:id>', methods=['POST'])
# def update(id):
#     nim = request.form['nim']
#     nama = request.form['nama']
#     jurusan = request.form['jurusan']
#     cur = mysql.connection.cursor()
#     cur.execute('UPDATE mahasiswa SET nim=%s, nama=%s, jurusan=%s WHERE id=%s', (nama, jurusan,id,))
#     mysql.connection.commit()
#     return redirect(url_for('home'))


# DELETE DATA
@app.route('/delete/<string:id>', methods=['GET'])
def DELETE(id):
    nim = request.form['nim']
    nama = request.form['nama']
    jurusan = request.form['jurusan']
    cur = mysql.connection.cursor()
    cur.execute('DELETE mahasiswa where id=%s', (id,))
    mysql.connection.commit()
    return redirect(url_for('home'))



# if __name__ == '__main__':
#     app.run(debug=True, port=8001)