import random

def jogar_adivinhacao():
    # 1. Gerar número aleatório de 1 a 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10
    acertou = False

    print("--- Bem-vindo ao Jogo de Adivinhação! ---")
    print(f"Tente adivinhar o número entre 1 e 100. Você tem {max_tentativas} tentativas.")

    # 2. Laço de repetição para as tentativas
    while tentativas < max_tentativas:
        try:
            # 3. Obter palpite do usuário
            palpite = int(input(f"\nTentativa {tentativas + 1}/{max_tentativas}: Digite seu palpite: "))
            tentativas += 1

            # 4. Verificar se o palpite está correto, maior ou menor
            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                acertou = True
                break
            elif palpite < numero_secreto:
                print("Muito baixo! Tente um número maior.")
            else:
                print("Muito alto! Tente um número menor.")

        except ValueError:
            print("Por favor, digite um número válido.")

    # 5. Fim do jogo
    if not acertou:
        print(f"\nQue pena! Acabaram suas tentativas. O número era {numero_secreto}.")

# Iniciar o jogo
if __name__ == "__main__":
    jogar_adivinhacao()
99
