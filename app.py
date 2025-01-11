from flask import Flask, render_template, redirect, request #até aqui, já tinhamos visto tudo, menos o redirect
import os #Biblioteca para ler arquivos como se fosse um "Sistema Operacional"
from dotenv import load_dotenv #Biblioteca para trabalhar com arquivos env
from flask_sqlalchemy import SQLAlchemy #Biblioteca necessária para mapear classes Python para tabelas do banco de dados relacional
from models.atividade import *
from util import *

app = Flask(__name__) #Criando o app Flask

load_dotenv()

dbusuario = os.getenv("DB_USERNAME") #Importando informação de usuário do arquivo env
dbsenha = os.getenv("DB_PASSWORD") #Importando informação de senha do arquivo env
host = os.getenv("DB_HOST") #Importando informação de host do arquivo env
meubanco = os.getenv("DB_DATABASE") #Importando informação de banco de dados do arquivo env
porta = os.getenv("DB_PORT") #importando a informação da porta da conexão do arquivo env
conexao = f"mysql+pymysql://{dbusuario}:{dbsenha}@{host}:{porta}/{meubanco}" #Formatando a linha de conexão com o banco
app.config["SQLALCHEMY_DATABASE_URI"] = conexao #Criando uma "rota" de comunicação
db.init_app(app) #Sinaliza que o banco será gerenciado pelo app

@app.route('/', methods = ["get", "post"])
def todo_list():
    atividades = Atividades.query.all()
    return render_template('lista.html', atividade = atividades)

@app.route('/new_task')
def new_task():
    return render_template('new_task.html')


'''
nome = request.form.get('nome')
    prioridade = request.form.get('prioridade')
    data = request.form.get('data')
    
    nome = "aaaa"
    idatividade = 1
    prioridade = "alta"
    data = "11/01/2025"
    nova_tarefa = Atividades(idatividade = idatividade, nome = nome, prioridade = prioridade, data=data)
    db.session.add(nova_tarefa)
    db.session.commit()

'''