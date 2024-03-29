# Weather-Forecast-Backend

Previsão do Tempo por CEP  
Este é um aplicativo web que permite ao usuário obter a previsão do tempo para uma determinada região usando o CEP como referência. O aplicativo consome a API do viacep https://viacep.com.br para consultar o local e a API http://servicos.cptec.inpe.br/XML/ para a consulta da previsão do tempo e exibe a previsão dos próximos 4 dias para a cidade solicitada

Como usar  
Para usar o aplicativo, basta acessar a página inicial realizar um cadastro ou login e inserir um CEP válido na caixa de pesquisa. Então aplicativo exibirá a previsão atual para a região correspondente ao CEP fornecido.

Tecnologias  
Este aplicativo foi desenvolvido usando as seguintes tecnologias:

- Python
- Docker
- JWT
- MongoDB
- ElasticSearch
- API do viacep
- API do cptec

Instalação  
Para instalar e executar o aplicativo em sua própria máquina, siga as etapas abaixo:

Clone o repositório para sua máquina local  
Navegue até o diretório do projeto  
Execulte o comando 'docker-compose up'  
Abra o navegador e acesse https://127.0.0.1:5000

## Endpoints

```
openapi: 3.0.0
info:
  title: Weather-Forecast
  description: Previsão do Tempo por CEP.
  version: 1.0.0
servers:
  - url: https://127.0.0.1:5000
paths:
  /api/user/signup:
    post:
      summary: Registrar um novo usuário
      description: Registra um novo usuário no sistema.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                password:
                  type: string
      responses:
        '200':
          description: Login bem-sucedido
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
        '409':
          description: Usuário já existe
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
        '422':
          description: Dados de entrada inválidos
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    detail:
                      type: object                        
                    title:
                      type: string

  /api/user/login:
    post:
      summary: Login de usuário
      description: Autentica um usuário no sistema.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                password:
                  type: string
      responses:
        '200':
          description: Login bem-sucedido
          headers:
            token:
              description: Cookie contendo o token JWT
              schema:
                type: string
            username:
              description: Cookie contendo o nome de usuario
              schema:
                type: string
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
        '401':
          description: Falha na autenticação
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
        '422':
          description: Dados de entrada inválidos
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    detail:
                      type: object                        
                    title:
                      type: string

  /api/user/logout:
    get:
      summary: Logout de usuário
      description: Encerra a sessão de um usuário no sistema.
      parameters:
        - name: token
          in: cookie
          description: Token JWT necessário para autenticação
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Logout bem-sucedido
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
        '401':
          description: Não autorizado
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string

  /api/forecast/get-weather:
    post:
      summary: Obter previsão do tempo
      description: Retorna a previsão do tempo para uma determinada localização com base no CEP fornecido.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                cep:
                  type: string
      parameters:
        - name: token
          in: cookie
          description: Token JWT necessário para autenticação
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Previsão do tempo obtida com sucesso
          content:
            application/json:
              schema:
                type: object
                properties:
                  address:
                    type: object
                    properties:
                      bairro:
                        type: string
                      cep:
                        type: string
                      complemento:
                        type: string
                      ddd:
                        type: string
                      gia:
                        type: string
                      ibge:
                        type: string
                      id:
                        type: string
                      localidade:
                        type: string
                      logradouro:
                        type: string
                      siafi:
                        type: string
                      uf:
                        type: string
                  forecast:
                    type: object
                    properties:
                      cidade:
                        type: object
                        properties:
                          atualizacao:
                            type: string
                            format: date
                          nome:
                            type: string
                          previsao:
                            type: array
                            items:
                              type: object
                              properties:
                                dia:
                                  type: string
                                  format: date
                                iuv:
                                  type: string
                                maxima:
                                  type: string
                                minima:
                                  type: string
                                tempo:
                                  type: string
                          uf:
                            type: string
        '401':
          description: Não autorizado
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string

  /api/logs:
    get:
      summary: Obter registros de logs
      description: Retorna registros de logs com base na solicitação enviada.
      parameters:
        - name: token
          in: cookie
          description: Token JWT necessário para autenticação
          required: true
          schema:
            type: string
        - name: username
          in: cookie
          description: Cookie necessário para busca de usuario no Banco de Dados
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Registros de logs obtidos com sucesso
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    _id:
                      type: string
                    _index:
                      type: string
                    _score:
                      type: number
                    _source:
                      type: object
                      properties:
                        method:
                          type: string
                        path:
                          type: string
                        timestamp:
                          type: string
                          format: date-time
                        username:
                          type: string
        '401':
          description: Não autorizado
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
```