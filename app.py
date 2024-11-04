from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://GabrielFarias:SenhaTeste@localhost:3306/desafio03'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    assunto = db.Column(db.String(255))
    descricao = db.Column(db.Text)
    data_envio = db.Column(db.DateTime, default=db.func.current_timestamp())

@app.route('/')
def contato():
    return render_template('contato.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    assunto = request.form['assunto']
    descricao = request.form['descricao']
    
    novo_contato = Contato(email=email, assunto=assunto, descricao=descricao)
    db.session.add(novo_contato)
    db.session.commit()
    
    return redirect(url_for('contato'))

@app.route('/lista')
def lista():
    contatos = Contato.query.all() 
    return render_template('lista.html', contatos=contatos)
    # http://127.0.0.1:5000/lista
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
