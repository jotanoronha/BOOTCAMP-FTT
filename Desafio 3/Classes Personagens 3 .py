

### IMPORT FLASK É RESPONSÁVEL POR IMPORTAR A BIBLIOTECA FLASK, O BÁSICO NESSESÁRIO PARA CRIAÇÃO DAS API'S 


from flask import Flask, jsonify, request

app = Flask(__name__)
        
## CRIA UM DICIONÁRIO PARA ALOCAR AS INFORMAÇÕES DOS PERSONAGENS EM QUESTÃO

lista = [
	{
	'id': 1,
	'nome': 'Moana', 
	'descricao': 'Uma jovem havaiana',
	'link_imagem': 'https://static.wikia.nocookie.net/disney/images/f/fc/Moana_promo_2.jpg/revision/latest/scale-to-width-down/258?cb=20160914022940&path-prefix=pt-br',
	'programa': 'Moana (filme)',
	'animador': 'Joshua Beveridge',
	},
	{
	'id': 2,
	'nome': 'Mickey Mouse', 
	'descricao': 'Um rato bondoso, romantico e prestativo',
	'link_imagem': 'https://upload.wikimedia.org/wikipedia/pt/thumb/d/d4/Mickey_Mouse.png/250px-Mickey_Mouse.png',
	'programa': 'O mundo maravilhoso de Mickey Mouse',
	'animador': 'Walt Dinsey',
	},
	{
	'id': 3,
	'nome': 'Perna Longa', 
	'descricao': 'Um coelho astuto',
	'link_imagem': 'https://static.wikia.nocookie.net/liga-da-zueira-oficial/images/9/98/Pernalonga_png_e_gifs_1.png/revision/latest?cb=20220728194852&path-prefix=pt-br',
	'programa': 'Looney Tunes',
	'animador': 'Chuck Jones, Tex Avery, Bob Clampett, Robert McKimson, Bob Givens',
	},
	{
	'id': 4,
	'nome': 'Shrek', 
	'descricao': 'Um ogro que vive em um pântano',
	'link_imagem': 'https://upload.wikimedia.org/wikipedia/pt/e/ed/Shrek%28personagem%29.jpg',
	'programa': 'Shrek',
	'animador': 'Dreamworks'
	},
	]


## @APP.ROUTE CRIA UMA ROTA/ENDPOINT PARA A ABA '/CHARACTERS/' EM QUESTÃO. É POR ONDE AS INFORMAÇÕES DE PERSONAGENS PODEM SER ACESSADAS.
## "def obter_lista" É RESPONSÁVEL POR CRIAR UMA FUNÇÃO QUE EXIBE AS INFORMAÇÕES DOS PERSONAGENS DISPONÍVEIS.

@app.route('/characters/',methods=['GET'])
def obter_lista():
	return jsonify(lista)



## O ENDPOINT @APP.ROUTE PARA /CHARACTERS/ID É RESPONSÁVEL PELA FUNÇÃO DE BUSCA POR 'ID' NO CASO, CRIAMOS OUTRA @APP.ROUTE. PORÉM COM OUTRA ENDPOINT '/PERSONAGENS/ID/'
## FOI CRIADO TAMBÈM UMA FUNÇÃO RESPONSÁVEL POR CONSULTAR OS PERSONAGENS POR 'ID' NO CASO: "def obter_lista_id(id)"
## PARA ENCONTRAR OS LIVROS USANDO ESTA FUNÇÃO É NECESSÁRIO INCLUIR O NÚMERO(ID) DO PERSONAGEM DEPOIS DO ENDPOINT 'CHARACTERS'.
## EXEMPLO : http://localhost:5000/characters/2


@app.route('/characters/<int:id>',methods=['GET'])
def obter_lista_id(id):
	for listar in lista:
		if listar['id'] == id:
			return jsonify(listar)
	return jsonify({'message': 'Personagem não encontrado'}),


## A FUNÇÃO "incluir_personagem" É RESPONSÁVEL PELA CRIAÇÃO DE PERSONAGENS, INCLUINDO NOVAMENTE O ENDPOINT: @APP.ROUTE('/CHARACTERS/') PARA INCLUIR OS NOVOS PERSONAGENS
## PARA INCLUSÃO DE UM NOVO PERSONAGEM, ALTERAMOS OS MÉTODO DE REQUEST PARA 'POST' 
## (Por se tratar de um servidor local, é necessário utilizar um programa de edição depuração e teste de API'S no caso foi utilizado o POSTMAN)
## PARA O FUNCIONAMENTO CORRETO DO POSTMAN, O PROGRAMA PRECISA ESTAR INSTALADO NA MÁQUINA.
## A ADIÇÃO DE PERSONAGEM PRECISA SER FEITA EM FORATO .JSON SEGUE O EXEMPLO ABAIXO:
## EX:
# 
#   {
#    "animador": "joao",
#    "descricao": "Um jovem de 23 anos",
#    "id": 10,
#    "link_imagem": "https://imagens.com.br/joao",
#    "nome": "joao vitor",
#    "programa": "FTT"
#   }


@app.route('/characters/',methods=['POST'])
def incluir_personagem():
	novo_personagem = request.get_json()
	lista.append(novo_personagem)
	return jsonify(lista),
	
### EXECUTA A APLICAÇÃO FLASK, COM INDICAÇÃO DO LOCAL EM FORMA DE LINK HTTP

if __name__ == '__main__':
	app.run()
