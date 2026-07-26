# Entrada de dados

## Utilizando a função input para que o usuário possa inserir nome, ataque e defesa dos monstros
## Utilizando condicional if com a função raise para que o programa pare de executar se for inserido um valor < 0 (ValueError)

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

## Definindo a função atacar com os argumentos nome_atacante, ataque, nome_defensor, hp_defensor para retornar o hp novo do defensor toda vez que houver um ataque

def atacar(nome_atacante,ataque,nome_defensor,hp_defensor):
  hp_novo = hp_defensor - ataque
  print(f"{nome_atacante} usou ataque rápido! {nome_defensor} sofreu {ataque} de dano!")
  return hp_novo
  
## Definindo a função exibir_placar com os argumentos nome1, hp1, nome2 e hp2 para printar o placar com o hp de cada monstro

def exibir_placar(nome1,hp1,nome2,hp2):
  print(f"{nome1}: {hp1} hp. {nome2}: {hp2} hp.")
  

# Implementação do loop principal

## Implementando um loop while para que o código se repita somente enquanto os dois monstros tiverem hp > 0

while hp2 > 0 and hp1 > 0:
  
  ## Definindo hp2 = atacar para retornar o hp novo do segundo monstro depois de um ataque, começando a batalha

  hp2 = atacar(nome1,atk1,nome2,hp2)

  ## Implementando if/else com a função exibir_placar para exibir o placar depois de cada turno, de forma que o hp2 sempre deve ser exibido como um número maior que ou igual a 0, nunca um valor negativo

  if hp2 < 0:
    exibir_placar(nome1,hp1,nome2,0)
  else:
    exibir_placar(nome1,hp1,nome2,hp2)
  
## Implementando um loop if/else para que a batalha continue somente enquanto os dois monstros tiverem hp maior que 0

  if hp2 > 0 and hp1 > 0:
    
    ## Definindo hp1 = atacar para retornar o hp novo do primeiro monstro depois de um ataque

    hp1 = atacar(nome2,atk2,nome1,hp1)
    
    ## Implementando if/else com a função exibir_placar para exibir o placar depois de cada turno, sendo que o hp1 sempre deve ser exibido como um número maior que ou igual a 0, nunca um valor negativo

    if hp1 < 0:
      exibir_placar(nome1,0,nome2,hp2)
    else:
      exibir_placar(nome1,hp1,nome2,hp2)
  else:
    break

# Condição de vitória

## Utilizando if/else para exibir o vencedor do duelo, baseando-se em qual dos monstros teve seu hp zerado  

if hp1 <= 0:
  print(f"{nome2} venceu o duelo!")
elif hp2 <= 0:
  print(f"{nome1} venceu o duelo!")