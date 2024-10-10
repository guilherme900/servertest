from flask import Flask, request, jsonify,render_template
from waitress import serve
from flask_cors import CORS
import hashlib
import mysql.connector
app = Flask(__name__)
CORS(app)


mydb = mysql.connector.connect(
  host="localhost",
  user="MySQL80",
  password="1234"
)

print(mydb)
# Simulando um banco de dados com um dicionário
users_db = {}

# Função para hash da senha
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/',methods=['GET'])
def page():
    return render_template('teste.html',data =users_db)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email in users_db:
        return jsonify({'message': 'Usuário já existe!'}), 400

    users_db[email] = hash_password(email+password)
    return jsonify({'message': 'Usuário registrado com sucesso!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email not in users_db or users_db[email] != hash_password(email+password):
        return jsonify({'message': 'E-mail ou senha inválidos!'}), 401

    return jsonify({'message': 'Login bem-sucedido!'}), 200

if __name__ == '__main__':
    #app.run(debug=True) 
    serve(app, host="0.0.0.0", port=5000)
