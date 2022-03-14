"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
print(f'{"JOGO DA ADIVINHAÇÃO":=^40}')
computador = randint(0, 10)
print('Sou seu computador \n'
      'Acabei de pensar em um número entre 0 e 10\n'
      'Será que você consegue adivinhar qual foi?')
jogador = int(input('Qual é o seu palpite? '))
palpite = 1
while jogador != computador:
    if jogador > computador:
        jogador = int(input('Menos...tente outra vez'))
    if jogador < computador:
        jogador = int(input('Mais...tente outra vez'))
    if jogador == computador:
        print('Você acertou!')
    palpite += 1
print(f'Você acertou! Você levou {palpite} tentativas para acertar')
