from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'  # Banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desabilita rastreamento de modificações
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
    tickets = Ticket.query.all()
    return render_template('index.html', tickets=tickets)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        tarefa = request.form.get('tarefa')
        turno = request.form.get('turno')
        operador = request.form.get('operador')

        novo_ticket = Ticket(tarefa=tarefa, turno=turno, operador=operador)
        db.session.add(novo_ticket)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('adicionar.html')

if __name__ == '__main__':
    app.run(debug=True)
