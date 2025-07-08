# Fazer uma calculadora simples
def calcular(operacao, num1, num2):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"
# Exemplo de uso
if __name__ == "__main__":
    operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = calcular(operacao, num1, num2)
    print(f"Resultado: {resultado}")
# Testes
def test_calcular():
    assert calcular('soma', 2, 3) == 5
    assert calcular('subtracao', 5, 3) == 2
    assert calcular('multiplicacao', 2, 3) == 6
    assert calcular('divisao', 6, 3) == 2.0
    assert calcular('divisao', 6, 0) == "Erro: Divisão por zero"
    assert calcular('modulo', 6, 3) == "Operação inválida"
    print("Todos os testes passaram!")