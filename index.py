from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tabela-gray', methods=['GET', 'POST'])
def tabela_gray():
    resultado = None
    if request.method == 'POST':
        try:
            n = int(request.form['bits'])
            if n <= 0:
                return render_template('tabela_gray.html', erro="O número de bits deve ser maior que zero.")
            
            codigos = codigo_gray(n)
            binarios = codigo_binario(n)
            
            tabela = []
            for i, (codigo_gray, codigo_bin) in enumerate(zip(codigos, binarios)):
                tabela.append({
                    'decimal': i,
                    'binario': codigo_bin,
                    'gray': codigo_gray
                })
            
            return render_template('tabela_gray.html', tabela=tabela, n_bits=n)
        except ValueError:
            return render_template('tabela_gray.html', erro="Entrada inválida. Digite um número inteiro positivo.")
    
    return render_template('tabela_gray.html')

@app.route('/conversao', methods=['GET', 'POST'])
def conversao():
    resultado = None
    erro = None
    
    if request.method == 'POST':
        tipo_conversao = request.form['tipo_conversao']
        
        try:
            if tipo_conversao == 'binario_decimal':
                binario = request.form['input']
                if not all(digito in '01' for digito in binario):
                    raise ValueError("Número binário inválido")
                resultado = binario_decimal(binario)
                tipo_resultado = 'Decimal'
                tipo_entrada = 'Binário'
            
            elif tipo_conversao == 'decimal_binario':
                decimal = int(request.form['input'])
                resultado = decimal_binario(decimal)
                tipo_resultado = 'Binário'
                tipo_entrada = 'Decimal'
            
            elif tipo_conversao == 'decimal_hexadecimal':
                decimal = int(request.form['input'])
                resultado = decimal_para_hexadecimal(decimal)
                tipo_resultado = 'Hexadecimal'
                tipo_entrada = 'Decimal'
            
            elif tipo_conversao == 'hexadecimal_decimal':
                hexadecimal = request.form['input'].upper()
                if not all(digito in '0123456789ABCDEF' for digito in hexadecimal):
                    raise ValueError("Número hexadecimal inválido")
                resultado = hexadecimal_decimal(hexadecimal)
                tipo_resultado = 'Decimal'
                tipo_entrada = 'Hexadecimal'
            
            elif tipo_conversao == 'binario_hexadecimal':
                binario = request.form['input']
                if not all(digito in '01' for digito in binario):
                    raise ValueError("Número binário inválido")
                resultado = binario_hexadecimal_intermediario(binario)
                tipo_resultado = 'Hexadecimal'
                tipo_entrada = 'Binário'
            
            elif tipo_conversao == 'hexadecimal_binario':
                hexadecimal = request.form['input'].upper()
                if not all(digito in '0123456789ABCDEF' for digito in hexadecimal):
                    raise ValueError("Número hexadecimal inválido")
                resultado = hexadecimal_binario_intermediario(hexadecimal)
                tipo_resultado = 'Binário'
                tipo_entrada = 'Hexadecimal'
            
            else:
                raise ValueError("Tipo de conversão inválido")
        
        except ValueError as e:
            erro = str(e)
    
    return render_template('conversao.html', 
                           resultado=resultado, 
                           erro=erro, 
                           tipo_resultado=tipo_resultado if 'tipo_resultado' in locals() else None,
                           tipo_entrada=tipo_entrada if 'tipo_entrada' in locals() else None)

@app.route('/operacoes', methods=['GET', 'POST'])
def operacoes():
    resultado = None
    erro = None
    
    if request.method == 'POST':
        tipo_operacao = request.form['tipo_operacao']
        
        try:
            input1 = request.form['input1']
            input2 = request.form['input2']
            
            if tipo_operacao == 'adicao_binario':
                if not all(digito in '01' for digito in input1 + input2):
                    raise ValueError("Números binários inválidos")
                resultado = adicao_binario(input1, input2)
                tipo_resultado = 'Binário'
                operacao = 'Adição'
            
            elif tipo_operacao == 'subtracao_binario':
                if not all(digito in '01' for digito in input1 + input2):
                    raise ValueError("Números binários inválidos")
                resultado = subtracao_binario(input1, input2)
                tipo_resultado = 'Binário'
                operacao = 'Subtração'
            
            elif tipo_operacao == 'adicao_hexadecimal':
                input1 = input1.upper()
                input2 = input2.upper()
                if not all(digito in '0123456789ABCDEF' for digito in input1 + input2):
                    raise ValueError("Números hexadecimais inválidos")
                resultado = adicao_hexadecimal(input1, input2)
                tipo_resultado = 'Hexadecimal'
                operacao = 'Adição'
            
            elif tipo_operacao == 'subtracao_hexadecimal':
                input1 = input1.upper()
                input2 = input2.upper()
                if not all(digito in '0123456789ABCDEF' for digito in input1 + input2):
                    raise ValueError("Números hexadecimais inválidos")
                resultado = subtracao_hexadecimal(input1, input2)
                tipo_resultado = 'Hexadecimal'
                operacao = 'Subtração'
            
            else:
                raise ValueError("Tipo de operação inválido")
        
        except ValueError as e:
            erro = str(e)
    
    return render_template('operacoes.html', 
                           resultado=resultado, 
                           erro=erro, 
                           tipo_resultado=tipo_resultado if 'tipo_resultado' in locals() else None,
                           operacao=operacao if 'operacao' in locals() else None)

if __name__ == '__main__':
    app.run(debug=True)