# Trilha de Python 26.1 -  Desafio 2: 
Desafio da 2ª semana da trilha de Python da for_code, no qual aprendemos sobre condicionais, loops e funções.

## Funcionamento do programa
O programa simula um jogo de cartas por turnos, no qual dois monstros duelam entre si até que um deles fique com 0 de vida. Inicialmente, o programa exige que o usuário forneça nome, pontos de vida e pontos de ataque de cada monstro. Depois da entrada de dados, são definidas duas funções: a função atacar, com os parâmetros nome_atacante, ataque, nome_defensor e hp_defensor; e a função exibir_placar, com os parâmetros nome1, hp1, nome2 e hp2. A primeira função imprime a ação do ataque e o dano sofrido pelo defensor, além de calcular e retornar o novo valor do hp, enquanto a segunda imprime o placar. Implementou-se um laço while para fazer o sistema de turnos, utilizando as funções para exibir os ataques e o placar a cada rodada. O laço termina quando o hp de um dos monstros é igual ou menor que 0. Por fim, utilizou-se as condicionais if/elif para definir o vencedor da batalha.

## Instruções para o usuário
1) O usuário deve inserir todos os dados pedidos pelo programa: nomes, pontos de vida e pontos de ataque de cada monstro. É importante que todos os números inseridos sejam maiores que 0, caso contrário, o programa para de executar.
2) Após a inserção dos dados, 

## Respostas às perguntas teóricas

1) Qual a principal diferença prática entre usar um laço for e um laço while em Python? Por que o while foi a melhor escolha para esse duelo?
R: O laço for executa uma determinada ação um número definido de vezes, já o laço while executa uma ação enquanto uma condição for verdadeira. O laço while foi o mais adequado nesse caso porque a quantidade de turnos vai depender dos dados de entrada, portanto não há um número definido de repetições.

2) Para que serve a palavra chave return dentro de uma função? O que acontece se uma função fizer um cálculo matemático mas não possuir o return?
R: 

3) O que é um "loop infinito" e como podemos evitá-lo ao construir uma estrutura while?
R: 

