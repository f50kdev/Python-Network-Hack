from flask import Flask, render_template, request, send_file, redirect, url_for, jsonify
import os
import random
import tempfile
import openai
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, static_url_path='/uploads', static_folder='uploads')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def substituicoes_comuns(senha):
    mapa = str.maketrans({'a': '@', 'A': '@', 'o': '0', 'O': '0', 'e': '3', 'E': '3', 'i': '1', 'I': '1', 's': '$', 'S': '$'})
    return senha.translate(mapa)

def gerar_variacoes(senha, n_var, especiais):
    variacoes = set()
    variacoes.add(senha)
    variacoes.add(substituicoes_comuns(senha))
    especiais_lista = ['!', '@', '#', '$', '%', '&', '*']
    for _ in range(n_var):
        nova = senha
        if especiais:
            nova = random.choice(especiais_lista) + nova
            variacoes.add(nova)
            nova = senha + random.choice(especiais_lista)
            variacoes.add(nova)
        variacoes.add(substituicoes_comuns(nova))
    return variacoes

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        senhas = []
        if 'file' in request.files and request.files['file'].filename:
            file = request.files['file']
            for line in file:
                senha = line.decode('utf-8').strip()
                if senha:
                    senhas.append(senha)
        else:
            manual_input = request.form.get('manual_input', '').strip()
            if manual_input:
                senhas = [s.strip() for s in manual_input.split('\n') if s.strip()]
        if not senhas:
            return render_template('index.html', error="Nenhuma senha fornecida.")
        n_var = int(request.form.get('n_var', 1))
        especiais = request.form.get('especiais') == 'on'
        todas_variacoes = set()
        for senha in senhas:
            todas_variacoes.update(gerar_variacoes(senha, n_var, especiais))
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w') as f:
            for v in todas_variacoes:
                f.write(v + '\n')
            temp_path = f.name
        return redirect(url_for('download', filepath=temp_path))
    return render_template('index.html')

@app.route('/download/<path:filepath>')
def download(filepath):
    return send_file(filepath, as_attachment=True, download_name='dicionario_senhas.txt')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'Mensagem vazia'}), 400
            
        # Create chat completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente especializado em segurança de senhas e geração de dicionários para testes de penetração. Forneça respostas úteis e seguras."},
                {"role": "user", "content": message}
            ],
            max_tokens=150
        )
        
        return jsonify({'response': response.choices[0].message.content})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 