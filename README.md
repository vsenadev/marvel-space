# Projeto Marvel Flask REST API

Bem-vindo ao repositório do projeto Marvel Flask REST API! Este projeto é uma REST API desenvolvida em Python utilizando o framework Flask e um banco de dados MongoDB. A API fornece funcionalidades para gerenciamento de dados relacionados ao universo da Marvel, incluindo personagens, quadrinhos, quizzes e batalhas entre personagens.

## Requisitos

Certifique-se de ter o Python e o MongoDB instalados em seu ambiente de desenvolvimento antes de começar.

- Python 3.x
- Flask
- Flask-RESTful
- PyMongo
- MongoDB

## Configuração

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/marvel-flask-api.git
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure as variáveis de ambiente em um arquivo `.env` na raiz do projeto. Você pode utilizar o arquivo `.env.example` como referência.

    ```env
    FLASK_APP=app.py
    FLASK_ENV=development
    MONGO_URI=sua_url_do_mongo
    SECRET_KEY=sua_chave_secreta
    ```

4. Inicie o servidor Flask:

    ```bash
    flask run
    ```

A aplicação estará disponível em [http://localhost:5000/](http://localhost:5000/).

## Endpoints

A API possui os seguintes endpoints:

- `/api/login` - Realiza o login do usuário.
- `/api/characters` - Lista todos os personagens da Marvel.
- `/api/comics` - Lista todos os quadrinhos da Marvel.
- `/api/quiz` - Inicia um quiz sobre a Marvel.
- `/api/battle` - Inicia uma batalha entre dois personagens, informados pelo usuário.

Para mais detalhes sobre os parâmetros e respostas de cada endpoint, consulte a documentação da API.

## Documentação

A documentação detalhada da API pode ser encontrada no arquivo [API_DOC.md](API_DOC.md).

## Contribuição

Se deseja contribuir para este projeto, sinta-se à vontade para abrir issues ou enviar pull requests. Toda contribuição é bem-vinda!

## Licença

Este projeto está sob a licença [MIT](LICENSE).
