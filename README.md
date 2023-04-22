[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-9f69c29eadd1a2efcce9672406de9a39573de1bdf5953fef360cfc2c3f7d7205.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=9174823)
# Atividade: Consenso e API (`06-consensus`)

Esta atividade tem como objetivo implementar uma API de acesso ao nosso blockchain. Isso permitirá a interação entre múltiplos nós que implementem nosso protocolo. Outro objetivo desta atividade é definir o modelo de consenso.

## Metodologia e Avaliação

Essa atividade encerra o projeto de desenvolvimento de nosso blockchain privado. A entrega será realizada no Github Classroom mas a avaliação será feita no formato de apresentação ao professor, no dia **09/11/2022, das 16:50 as 18:30**. O trabalho deve ser desenvolvido **individualmente ou em dupla** (O GitHub Classroom gerencia as duplas). Plágios não serão tolerados, resultando em nota zero para todos os envolvidos.

## Instruções de submissão

Submissão deve ser feita a partir do GitHub Classroom até às 23:59 do dia 09/11/2022 (mesmo dia da apresentação). Basta realizar o *commit* do seu arquivo `blockchain.py` no repositório privado criado para você a partir do link disponibilizado. Qualquer dúvida nesta etapa consulte o professor no Discord.

## Instalação

Baixe o arquivo `./blockchain.py` para obter o *boilerplate* para esta atividade. Caso seja necessário, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os módulos necessários. Todos os *boilerplates* são compatíveis com o Python 3+.

## Descrição

Sua API precisará implementar 5 *end-points*:

- **[POST]** `/transactions/create` para criar uma nova transação a ser incluída no próximo bloco. No corpo da requisicão HTTP, usando POST, inclua as informações necessárias para criação de uma nova transação.
- **[GET]** `/transactions/mempool` para retornar a *memory pool* do nó.
- **[GET]** `/mine` para informar o nó para criar e minerar um novo bloco. Ou seja, um nó que for requisitado a partir desse end-point deve pegar todas as transações incluídas em seu memory pool, montar um bloco e minera-lo.
- **[GET]** `/chain` para retornar o blockchain completo daquele nó.
- **[POST]** `/nodes/register` para aceitar uma lista de novos nós no formato de URLs. Note que já existe uma variável do tipo conjunto (*set*) chamado `nodes` para armazenar os nós registrados.
- **[GET]** `/nodes/resolve` para executar o modelo de consenso, resolvendo conflitos e garantindo que contém a cadeia de blocos correta. Basicamente o que deve ser feito pelo nó é solicitar a todos os seus nós registrados os seus respectivos blockchains. Então deve-se conferir se o blockchain é válido, e, se for maior (mais longo) que o atual, deve substitui-lo.

Para auxiliar no desenvolvimento do consenso, implemente os métodos `isValidChain()` e `resolveConflicts()`. As assinaturas e a descrição já estão no código exemplo.

Utilize qualquer *framework* que desejar para implementar a API. Uma sugestão é o *framework* [Flask](https://palletsprojects.com/p/flask/), bastante leve e de fácil utilização. Instale usando o `pip`. Veja como é simples criar um _end-point_:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=5000)
```

Se eu executar esse código, temos um serviço web em execução. Caso entre em `http://127.0.0.1:5000/hello`, o método `hello()` será executado!

Caso precise fazer requisições HTTP no Python, você pode utilizar o módulo `requests`. Também é bem simples, por exemplo, para requisitar o blockchain completo do nó `127.0.0.1:5001`:

```python
import requests

response = requests.get('http://127.0.0.1:5001/chain')
obj = response.json()
```

Para testar, será necessário executar no mínimo dois nós simultaneamente, e no caso de ser na mesma máquina, as instâncias em execução devem usar portas diferentes (por exemplo, porta 5000 e 5001). Você pode testar no seu navegador, usando _curl_, ou então usando o [Postman](https://www.postman.com/) ou [Insomnia](https://insomnia.rest/).

## Roteiro da apresentação

Para a apresentação, já se organize para realizar os seguintes passos:

```
[  ] Sobe um primeiro nó (ex: porta 5001)
[  ] Sobe um segundo nó (ex: porta 5002)
[  ] Cria uma nova transação (tx) no nó #1
[  ] Confere o mempool do nó #1
[  ] Cria e minera um novo bloco no nó #1
[  ] Cria e minera outro bloco (sem transações) no nó #1
[  ] Confere a atual chain do nó #1
[  ] Registra o nó #2 no nó #1
[  ] Resolve (consenso) o nó #1 (o blockchain não deve mudar)
[  ] Cria e minera um único bloco (sem transações) no nó #2
[  ] Confere a atual chain do nó #2
[  ] Registra o nó #1 no nó #2
[  ] Resolve (consenso) o nó #2 (o blockchain deve mudar para a chain do nó #1)
[  ] Confere a atual chain do nó #2
```


## Licença
[MIT](https://choosealicense.com/licenses/mit/)
