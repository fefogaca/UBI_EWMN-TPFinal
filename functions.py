# Trabalho Prático Intermédio da Disciplina de Ecossistemas Web, Móvel e na Nuvem da Universidade da Beira Interior
# Autores: Felipe Dourado - 53394, Afonso Esteves - 55047, Duarte Azenhas - 55281

#! Gera a sequência de códigos Gray de n bits
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

#! Gera a sequência de código binário em sequencia
def codigo_binario(n):
    if n <= 0:
        return []
    
    if n == 1:
        return ["0", "1"]
    
    binario_menor = codigo_binario(n-1)
    resultado = []
    
    for codigo in binario_menor:
        resultado.append("0" + codigo)
    
    for codigo in binario_menor:
        resultado.append("1" + codigo)
    
    return resultado

#! Converte binário para decimal
def binario_decimal(binary):
    decimal = 0
    troca = 0
    
    for digito in reversed(binary):
        if digito == '1':
            decimal += 2 ** troca
        troca += 1
    
    return decimal

#! Converte decimal para binário
def decimal_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    
    return binario

#! Converte decimal para hexadecimal
def decimal_para_hexadecimal(decimal):
    if decimal == 0:
        return "0"
    
    digito_hex = "0123456789ABCDEF"
    hexadecimal = ""
    
    while decimal > 0:
        restante = decimal % 16
        hexadecimal = digito_hex[restante] + hexadecimal
        decimal //= 16
    
    return hexadecimal

#! Converte hexadecimal para decimal
def hexadecimal_decimal(hexadecimal):
    digito_hex = "0123456789ABCDEF"
    decimal = 0
    
    for digito in hexadecimal.upper():
        decimal = decimal * 16 + digito_hex.index(digito)
    
    return decimal

#! Converte binário para hexadecimal usando conversão para decimal como intermediário
def binario_hexadecimal_intermediario(binario):
    decimal = binario_decimal(binario)
    return decimal_para_hexadecimal(decimal)

#! Converte hexadecimal para binário usando conversão para decimal como intermediário
def hexadecimal_binario_intermediario(hexadecimal):
    decimal = hexadecimal_decimal(hexadecimal)
    return decimal_binario(decimal)

#! Adição em binário
def adicao_binario(binario1, binario2):
    decimal1 = binario_decimal(binario1)
    decimal2 = binario_decimal(binario2)
    resultado_decimal = decimal1 + decimal2
    return decimal_binario(resultado_decimal)

#! Subtração em binário
def subtracao_binario(binario1, binario2):
    decimal1 = binario_decimal(binario1)
    decimal2 = binario_decimal(binario2)
    
    if decimal1 < decimal2:
        return "-" + decimal_binario(decimal2 - decimal1)
    
    resultado_decimal = decimal1 - decimal2
    return decimal_binario(resultado_decimal)

#! Adição em hexadecimal
def adicao_hexadecimal(hexa1, hexa2):
    decimal1 = hexadecimal_decimal(hexa1)
    decimal2 = hexadecimal_decimal(hexa2)
    resultado_decimal = decimal1 + decimal2
    return decimal_para_hexadecimal(resultado_decimal)

#! Subtração em hexadecimal
def subtracao_hexadecimal(hexa1, hexa2):
    decimal1 = hexadecimal_decimal(hexa1)
    decimal2 = hexadecimal_decimal(hexa2)
    
    if decimal1 < decimal2:
        return "-" + decimal_para_hexadecimal(decimal2 - decimal1)
    
    resultado_decimal = decimal1 - decimal2
    return decimal_para_hexadecimal(resultado_decimal)