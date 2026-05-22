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


# Adicionando a função ataque

def atacar(nome_atacante,ataque,nome_defensor,hp_defensor):
  hp_defensor = hp_defensor - ataque
  print(f"{nome_atacante} usou ataque rápido! {nome_defensor} sofreu {ataque} de dano!")
  return hp_defensor, ataque
  
def exibir_placar(nome1,hp1,nome2,hp2):
  print(f"{nome1}: {hp1} hp. {nome2}: {hp2} hp.")
  

# Implementação do loop principal

while hp2 > 0 and hp1 > 0:
  atacar(nome1,atk1,nome2,hp2)
  hp2 = hp2 - atk1
  if hp2 > 0 and hp1 > 0:
    atacar(nome2,atk2,nome1,hp1)
    hp1 = hp1 - atk2
  else:
    break

if hp1 <= 0:
  exibir_placar(nome1,0,nome2,hp2)
  print(f"{nome2} venceu o duelo!")
elif hp2 <= 0:
  exibir_placar(nome1,hp1,nome2,0)
  print(f"{nome1} venceu o duelo!")