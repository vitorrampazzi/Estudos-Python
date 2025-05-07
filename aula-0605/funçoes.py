#a = '2 + 3 * 5'
#resultado = eval(a)

#print(resultado)

# Definindo algumas variáveis
#x = 10
#y = 5
# Definindo uma expressão que usa essas variáveis
#expressao = "x * y + 2"
# Usando eval para avaliar a expressão
#resultado = eval(expressao)
# Exibindo o resultado
#print(resultado) # Saída: 52

#x = 2
#expressao = ('print(x + 3 * 5)')
#eval(expressao, {}, {'x': x})

# Definindo uma string com um laço for e uma condição if
code_str = """
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)
print(result)   
"""
# Usando eval para executar a string como código Python
exec(code_str)