from util import *

class Atividades(db.Model): #Criando classe Python herdando as informações do SQLAlchemy
    __tablename__ = "atividades" #Indicando o nome da tabela que será utilizada
    idatividade = db.Column(db.Integer(), primary_key=True, nullable=False)  #Definindo CPF como chave primária e não permitindo valor nulo
    nome = db.Column(db.String(45), nullable=False)  #Não permitindo valor nulo
    prioridade = db.Column(db.String(45), nullable=False)
    data =db.Column(db.String(10), nullable=False)