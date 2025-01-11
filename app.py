from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tarefa = db.Column(db.String(100), nullable=False)
    turno = db.Column(db.String(50), nullable=False)
    operador = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Ticket {self.tarefa} - {self.turno} - {self.operador}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    tickets = Ticket.query.all()
    return render_template('index.html', tickets=tickets)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if 'logged_in' not in session:
        return redirect(url_for('login')) 
    
    if request.method == 'POST':
        tarefa = request.form.get('tarefa')
        turno = request.form.get('turno')
        operador = request.form.get('operador')

        novo_ticket = Ticket(tarefa=tarefa, turno=turno, operador=operador)
        db.session.add(novo_ticket)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('adicionar.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        if nome == 'admin' and senha == 'admin':  
            session['logged_in'] = True 
            return redirect(url_for('index'))  
        else:
            flash('Credenciais inválidas. Tente novamente.')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        genero = request.form.get('genero')
        data_nascimento = request.form.get('data_nascimento')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        endereco = request.form.get('endereco')

        flash('Conta criada com sucesso! Faça login para continuar.')
        return redirect(url_for('login'))

    return render_template('registrar.html')

if __name__ == '__main__':
    app.run(debug=True)
