def calcular_imc(peso, altura):
  """
  Calcula o Índice de Massa Corporal (IMC).
  :param peso: Peso em kg
  :param altura: Altura em metros
  :return: Valor do IMC
  """
  return peso / (altura ** 2)

def classificar_imc(imc):
  """
  Classifica o IMC de acordo com a tabela da OMS.
  :param imc: Valor do IMC
  :return: Classificação em string
  """
  if imc < 18.5:
    return "Abaixo do peso"
  elif imc < 25:
    return "Peso normal"
  elif imc < 30:
    return "Sobrepeso"
  elif imc < 35:
    return "Obesidade grau I"
  elif imc < 40:
    return "Obesidade grau II"
  else:
    return "Obesidade grau III"

if __name__ == "__main__":
  try:
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificar_imc(imc)}")
  except ValueError:
    print("Por favor, insira valores numéricos válidos.")