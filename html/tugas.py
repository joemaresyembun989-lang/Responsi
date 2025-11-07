from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'secret123'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'responsi'

UPLOAD_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, bio, photo FROM users WHERE username='joseph123'")
    user = cur.fetchone()

    cur.execute("SELECT name, level FROM skills")
    skills = cur.fetchall()

    cur.execute("SELECT title, description FROM projects")
    projects = cur.fetchall()
    cur.close()
    return render_template('index.html', user=user, skills=skills, projects=projects)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cur.fetchone()
        cur.close()

        if user:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash("Username atau password salah!", "danger")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Anda telah logout.", "info")
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash("Silakan login terlebih dahulu!", "warning")
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT name, bio, photo FROM users WHERE username=%s", (session['user'],))
    user = cur.fetchone()

    cur.execute("SELECT id, name, level FROM skills")
    skills = cur.fetchall()

    cur.execute("SELECT id, title, description FROM projects")
    projects = cur.fetchall()
    cur.close()
    return render_template('dashboard.html', user=user, skills=skills, projects=projects)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if 'user' not in session:
        flash("Silakan login terlebih dahulu!", "warning")
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()

    if request.method == 'POST':
        name = request.form['name']
        bio = request.form['bio']
        photo = request.files['photo']

        if photo and photo.filename != '':
            filename = photo.filename
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            cur.execute(
                "UPDATE users SET name=%s, bio=%s, photo=%s WHERE username=%s",
                (name, bio, filename, session['user'])
            )
        else:
            cur.execute(
                "UPDATE users SET name=%s, bio=%s WHERE username=%s",
                (name, bio, session['user'])
            )

        mysql.connection.commit()
        cur.close()
        flash("Profil berhasil diperbarui!", "success")
        return redirect(url_for('index'))

    cur.execute("SELECT name, bio, photo FROM users WHERE username=%s", (session['user'],))
    user = cur.fetchone()
    cur.close()
    return render_template('edit_profile.html', user=user)

@app.route('/add_skill', methods=['GET','POST'])
def add_skill():
    if 'user' not in session:
        flash("Silakan login terlebih dahulu!", "warning")
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        level = request.form['level']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO skills(name, level) VALUES(%s,%s)", (name, level))
        mysql.connection.commit()
        cur.close()
        flash("Skill berhasil ditambahkan!", "success")
        return redirect(url_for('dashboard'))
    return render_template('add_skill.html')

@app.route('/edit_skill/<int:id>', methods=['GET','POST'])
def edit_skill(id):
    if 'user' not in session:
        flash("Silakan login terlebih dahulu!", "warning")
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        level = request.form['level']
        cur.execute("UPDATE skills SET name=%s, level=%s WHERE id=%s", (name, level, id))
        mysql.connection.commit()
        cur.close()
        flash("Skill berhasil diperbarui!", "success")
        return redirect(url_for('dashboard'))

    cur.execute("SELECT id, name, level FROM skills WHERE id=%s", (id,))
    skill = cur.fetchone()
    cur.close()
    return render_template('edit_skill.html', skill=skill)

@app.route('/delete_skill/<int:id>')
def delete_skill(id):
    if 'user' not in session:
        flash("Silakan login terlebih dahulu!", "warning")
        return redirect(url_for('login'))
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM skills WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash("Skill berhasil dihapus!", "success")
    return redirect(url_for('dashboard'))

@app.route('/add_project', methods=['GET','POST'])
def add_project():
    if 'user' not in session:
        flash("Silakan login terlebih dahulu!", "warning")
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO projects(title, description) VALUES(%s,%s)", (title, description))
        mysql.connection.commit()
        cur.close()
        flash("Project berhasil ditambahkan!", "success")
        return redirect(url_for('dashboard'))
    return render_template('add_project.html')

@app.route('/edit_project/<int:id>', methods=['GET','POST'])
def edit_project(id):
    if 'user' not in session:
        flash("Silakan login terlebih dahulu!", "warning")
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        cur.execute("UPDATE projects SET title=%s, description=%s WHERE id=%s", (title, description, id))
        mysql.connection.commit()
        cur.close()
        flash("Project berhasil diperbarui!", "success")
        return redirect(url_for('dashboard'))

    cur.execute("SELECT id, title, description FROM projects WHERE id=%s", (id,))
    project = cur.fetchone()
    cur.close()
    return render_template('edit_project.html', project=project)

@app.route('/delete_project/<int:id>')
def delete_project(id):
    if 'user' not in session:
        flash("Silakan login terlebih dahulu!", "warning")
        return redirect(url_for('login'))
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM projects WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash("Project berhasil dihapus!", "success")
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
