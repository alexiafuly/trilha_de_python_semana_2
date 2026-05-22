# Entrada de dados

nome1 = input("Digite um nome para o primeiro monstro: ")

hp1 = int(input("Digite um valor para a vida do primeiro monstro: "))
if hp1 <= 0:
  raise ValueError("Ops, parece que você digitou um valor inválido! Digite um número maior que 0.")

atk1 = int(input("Digite um valor para o ataque do primeiro monstro: "))
if atk1 <= 0:
  raise ValueError("Ops, parece que você digitou um valor inválido! Digite um número maior que 0.")


nome2 = input("Digite um nome para o segundo monstro: ")

hp2 = int(input("Digite um valor para a vida do segundo monstro: "))
if hp2 <= 0:
  raise ValueError("Ops, parece que você digitou um valor inválido! Digite um número maior que 0.")

atk2 = int(input("Digite um valor para o ataque do segundo monstro: "))
if atk2 <= 0:
  raise ValueError("Ops, parece que você digitou um valor inválido! Digite um número maior que 0.")

