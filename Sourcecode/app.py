"""
Arquivo: app.py
Descrição: Arquivo destinado para a implementação flask no código do trabalho.
Trabalho Final de Ecossistema Web, Móvel e Nuvem
Alunos:
- Afonso Esteves - 55047
- Duarte Azenhas - 55281
- Felipe Dourado - 53394
"""

#! -----------------------------------------------------------------------------------------------------------------------------

from flask import Flask, render_template, request

app = Flask(__name__)
#TODO: Para remover o debug, lembrar para colocar em False!
app.debug = True

#! -----------------------------------------------------------------------------------------------------------------------------

#* Rota Principal
@app.route("/")
def index():
        return render_template("index.html")

#! -----------------------------------------------------------------------------------------------------------------------------

#* Rota para Tabela de Gray
@app.route("/gray", methods=["GET", "POST"])
def gray():
    tabela = []
    n = None
    if request.method == "POST":
        try:
            n = int(request.form.get("bits", 0))
            tabela = gerar_tabela_gray(n)
        except ValueError:
            tabela = []
    return render_template("gray.html", tabela=tabela, n=n)


#* Função para gerar a tabela de gray para n bits
def codigo_binario(n):
    return [format(i, f"0{n}b") for i in range(2**n)]

def gerar_tabela_gray(n):
    if n <= 0:
        return []

    codigos = codigo_gray(n)
    binarios = codigo_binario(n)
    
    tabela = []
    for i in range(len(codigos)):
        tabela.append((i, binarios[i], codigos[i]))  # (decimal, binário, gray)
    
    return tabela

def codigo_gray(n):
    if n <= 0:
        return []
    
    if n == 1:
        return ["0", "1"]
    
    gray_menor = codigo_gray(n-1)
    resultado = []
    
    for codigo in gray_menor:
        resultado.append("0" + codigo)
    
    for codigo in reversed(gray_menor):
        resultado.append("1" + codigo)
    
    return resultado   
     
#! -----------------------------------------------------------------------------------------------------------------------------

#* Rota para Conversão de Bases
@app.route("/conversao", methods=["GET", "POST"])

#* Função para converter entre bases numéricas
def conversao():
    resultado = None
    de = para = valor = ""
    
    if request.method == "POST":
        de = request.form.get("de")
        para = request.form.get("para")
        valor = request.form.get("valor", "").strip()
        
        #! Validar a entrada
        if not valor:
            resultado = "Por favor, insira um valor."
            return render_template("conversao.html", resultado=resultado, de=de, para=para, valor=valor)
        
        try:
            if de == "binario" and para == "decimal":
                if not all(c in '01' for c in valor):
                    raise ValueError("Valor binário inválido")
                resultado = int(valor, 2)
                
            elif de == "decimal" and para == "binario":
                resultado = bin(int(valor))[2:] 
                
            elif de == "decimal" and para == "hexadecimal":
                resultado = hex(int(valor))[2:].upper() 
                
            elif de == "hexadecimal" and para == "decimal":
                try:
                    resultado = int(valor, 16)
                except ValueError:
                    raise ValueError("Valor hexadecimal inválido")
                    
            elif de == "binario" and para == "hexadecimal":
                if not all(c in '01' for c in valor):
                    raise ValueError("Valor binário inválido")
                decimal = int(valor, 2)
                resultado = hex(decimal)[2:].upper()
                
            elif de == "hexadecimal" and para == "binario":
                decimal = int(valor, 16)
                resultado = bin(decimal)[2:]
                
            elif de == para:
                resultado = valor
            else:
                resultado = "Conversão não suportada."
                
        except ValueError as e:
            resultado = f"Erro: {str(e)}"
        except Exception as e:
            resultado = "Erro na conversão. Verifique o valor inserido."
            
    return render_template("conversao.html", resultado=resultado, de=de, para=para, valor=valor)

#! -----------------------------------------------------------------------------------------------------------------------------
#* Rota para Operações Aritméticas
@app.route("/operacoes", methods=["GET", "POST"])

#* Função para operações entre números
def operacoes():
    resultado = None
    sistema = operacao = valor1 = valor2 = ""
    
    if request.method == "POST":
        sistema = request.form.get("sistema")
        operacao = request.form.get("operacao")
        valor1 = request.form.get("valor1", "").strip().upper()
        valor2 = request.form.get("valor2", "").strip().upper()
        
        try:
            # Validar se o sistema foi selecionado
            if not sistema:
                raise ValueError("Por favor, selecione um sistema numérico")
            
            # Converter valores para decimal baseado no sistema selecionado
            if sistema == "Binario":
                # Validar se são valores binários válidos
                if not all(c in '01' for c in valor1) or not all(c in '01' for c in valor2):
                    raise ValueError("Valores binários inválidos. Use apenas 0 e 1")
                decimal1 = int(valor1, 2)
                decimal2 = int(valor2, 2)
                
            elif sistema == "Hexadecimal":
                # Validar e converter hexadecimal
                try:
                    decimal1 = int(valor1, 16)
                    decimal2 = int(valor2, 16)
                except ValueError:
                    raise ValueError("Valores hexadecimais inválidos")
            else:
                raise ValueError("Sistema numérico não suportado")
            
            # Realizar operação
            if operacao == "+":
                resultado_decimal = decimal1 + decimal2
            elif operacao == "-":
                resultado_decimal = decimal1 - decimal2
            else:
                raise ValueError("Operação não suportada")
            
            # Converter resultado apenas para o sistema selecionado
            if sistema == "Binario":
                resultado = {
                    'valor': bin(abs(resultado_decimal))[2:],
                    'sistema': 'Binário',
                    'negativo': resultado_decimal < 0
                }
            elif sistema == "Hexadecimal":
                resultado = {
                    'valor': hex(abs(resultado_decimal))[2:].upper(),
                    'sistema': 'Hexadecimal',
                    'negativo': resultado_decimal < 0
                }
            
        except ValueError as e:
            resultado = {'erro': str(e)}
        except Exception:
            resultado = {'erro': 'Erro na operação. Verifique os valores inseridos.'}
    
    return render_template("operacoes.html", resultado=resultado, sistema=sistema, operacao=operacao, valor1=valor1, valor2=valor2)     

#! -----------------------------------------------------------------------------------------------------------------------------
