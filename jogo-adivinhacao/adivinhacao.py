from random import randint

class Jogo_da_adivinhacao:
    
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_corretas = list()
        self.letras_erradas = list()
    
    def adivinhar_letra(self, letra):
        if letra in self.palavra and letra not in self.letras_corretas:
            self.letras_corretas.append(letra)

        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)

        else:
            return False

        return True   

    def fim_de_jogo(self):
        return self.vitoria_jogador() or (len(self.letras_erradas) == 6)

    def vitoria_jogador(self):
        if '_' not in self.esconder_palavra():
            return True
        
        return False

    def esconder_palavra(self):
        esconder_palavra = str()

        for letra in self.palavra:
            if letra not in self.letras_corretas:
                esconder_palavra += '_'
            
            else:
                esconder_palavra += letra
        
        return esconder_palavra

    def mostrar_estado_jogo(self):
        print('\nA palavra aleatória é: {}'.format(self.esconder_palavra()))
        print('\nLetras erradas: ')
        for letra in self.letras_erradas:
            print(letra)
        
        print('\nLetras corretas: ')
        for letra in self.letras_corretas:
            print(letra)


def palavra_aleatoria():
        with open("palavras.txt", "rt") as file:
            banco_palavras = file.readlines()

        return banco_palavras[randint(0, len(banco_palavras))].strip()

def main():

    game = Jogo_da_adivinhacao(palavra_aleatoria())

    while not game.fim_de_jogo():
        game.mostrar_estado_jogo()
        user_input = input('\nEscolha uma letra: ').lower()
        game.adivinhar_letra(user_input)
    
    if game.vitoria_jogador():
        print ('\nParabéns! Você venceu!! A palavra era: {}'.format(game.palavra))
    
    else:
        print ('\nGame over! Você perdeu!! A palavra era: {}. Foi bom jogar com você!'.format(game.palavra))


if __name__ == "__main__":
    main()