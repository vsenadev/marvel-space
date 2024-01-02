# Projeto Marvel Space

Bem-vindo ao repositório do projeto Marvel Flask REST API! Este projeto é uma REST API desenvolvida em Python utilizando o framework Flask e um banco de dados MongoDB. A API fornece funcionalidades para gerenciamento de dados relacionados ao universo da Marvel, incluindo personagens, quadrinhos, quizzes e batalhas entre personagens.

## Requisitos

Certifique-se de ter o Python e o MongoDB instalados em seu ambiente de desenvolvimento antes de começar.

[![My Skills](https://skillicons.dev/icons?i=py,flask,mongodb)](https://skillicons.dev)

## Configuração

1. Clone o repositório:

    ```bash
    git clone https://github.com/vsenadev/marvel-space.git
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure as variáveis de ambiente em um arquivo `.env` na raiz do projeto. Você pode utilizar o arquivo `.env.example` como referência.

    ```env
    DATAUSER=usuário do banco de dados
    PASSWORD=senha do banco de dados
    DATABASE_URL=url do banco de dados .mongodb.net
    SENDER_MAIL=usuário do email de disparo 
    MAIL_PASSWORD=senha do email de disparo
    SENDGRID_API_KEY=key do send grid
    IMG_BB_KEY=key do image bb
    ```

4. Inicie o servidor Flask:

    ```bash
    flask run
    ```

A aplicação estará disponível em http://192.168.100.71:3050/.

## Endpoints

Download Collection Insomnia:

https://drive.google.com/file/d/1ejn54IQYsFFJ09Vy0zHQN0MNCCXp1bZ7/view?usp=sharing

Para mais detalhes sobre os parâmetros e respostas de cada endpoint, consulte a documentação da API.

## Documentação

A documentação detalhada da API pode ser encontrada na página /documentation.

## Contribuição

Se deseja contribuir para este projeto, sinta-se à vontade para abrir issues ou enviar pull requests. Toda contribuição é bem-vinda!

## Licença

Este projeto está sob a licença [MIT](LICENSE).
