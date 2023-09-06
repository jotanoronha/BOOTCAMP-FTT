print("Esse programa cria personagens e atribui métodos e atributos a eles.")

### Cria a classe personagem:

class Personagem:
    def __init__(self, nome, descricao, link_imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.link_imagem = link_imagem
        self.programa = programa
        self.animador = animador

### Cria a função de exibição 
    def exibir_info(self):
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Link para a imagem: {self.link_imagem}")
        print(f"Programa: {self.programa}")
        print(f"Animador: {self.animador}")

### Lista para armazenar as informações dos personagens

personagens = []


while True:
   
    nome = str(input("Digite o nome do personagem (ex: Um personagem da Disney):: "))
    descricao = str(input("Digite a descrição do personagem (ex: Alto, baixo, jovem, 31 anos etc..): "))
    link_imagem = str(input("Digite o link para a imagem do personagem (Deixe em branco caso necessário): "))
    programa = str(input("Digite o programa do personagem (ex: Looney Tunes, Fineas e Ferb, Hora da Aventura etc..): "))
    animador = str(input("Digite o nome do animador do personagem (ex: Nome do responsável por criar a animação): "))

    personagem1 = Personagem(nome,descricao,link_imagem,programa,animador)

  # Adicionar o personagem à lista de personagens
    personagens.append(personagem1)

    continuar = input("\nDeseja criar outro personagem? (Digite 'sim' ou 'não'): ").lower()
    if continuar != 'sim':
        break

# Função de exibição que exibe informações de todos os personagens já criados.
print("\nInformações dos personagens:")
for index, personagem in enumerate(personagens, start=1):
    print(f"\nPersonagem {index}:")
    personagem.exibir_info()


