# Calculadora de Cashback - Desafio Nology

Projeto desenvolvido para o desafio de Estagiário de Dev da Nology.

A aplicação calcula o cashback de uma compra com base nas regras de negócio informadas no desafio. O usuário pode informar o tipo de cliente, o valor da compra e o percentual de desconto. Cada consulta realizada é salva em banco de dados e exibida no histórico apenas para o IP que realizou a consulta.

## Tecnologias utilizadas

* Python
* Flask
* PostgreSQL
* Neon
* HTML
* CSS
* JavaScript
* GitHub
* Render
* GitHub Pages

## Regras de negócio

O cálculo do cashback segue as seguintes regras:

* O cashback é calculado sobre o valor final da compra, após descontos.
* O cashback base é de 5%.
* Compras acima de R$ 500,00 recebem cashback em dobro.
* Clientes VIP recebem 10% de bônus sobre o cashback calculado.
* O bônus VIP é aplicado após o cálculo do cashback base e da promoção.

## Exemplo de cálculo

Cliente VIP compra um produto de R$ 600,00 com cupom de 20% de desconto.

* Valor da compra: R$ 600,00
* Desconto: 20%
* Valor final: R$ 480,00
* Cashback base: 5% de R$ 480,00 = R$ 24,00
* Bônus VIP: 10% de R$ 24,00 = R$ 2,40
* Cashback final: R$ 26,40

## Funcionalidades

* Cálculo de cashback
* Validação dos dados enviados pelo usuário
* API em Python com Flask
* Registro das consultas em banco PostgreSQL
* Histórico de consultas separado por IP
* Exclusão de itens individuais do histórico
* Frontend estático em HTML, CSS e JavaScript
* Configuração por variável de ambiente usando `DATABASE_URL`

## Estrutura do projeto

```text
cashback-nology/
│
├── backend/
│   ├── app.py
│   ├── cashback.py
│   ├── database.py
│   ├── requirements.txt
│   ├── test_cashback.py
│   ├── test_database.py
│   ├── .env.example
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── database/
│   └── 01_create_database.sql
│
├── docs/
│   └── respostas_desafio_nology.docx
│
├── .gitignore
├── Procfile
└── README.md
```

## Como executar o projeto localmente

### 1. Clonar o repositório

```bash
git clone link-do-repositorio
cd cashback-nology
```

### 2. Criar o banco de dados

O projeto utiliza PostgreSQL. Para executar localmente, é possível usar um banco local pelo pgAdmin ou uma instância online no Neon.

Crie um banco chamado:

```text
db_cashback_nology
```

Depois execute o script localizado em:

```text
database/01_create_database.sql
```

Esse script cria a tabela `tbl_cashback_queries`, responsável por armazenar o histórico de consultas.

### 3. Configurar variáveis de ambiente

Dentro da pasta `backend`, crie um arquivo chamado `.env` com base no arquivo `.env.example`.

Exemplo usando PostgreSQL local:

```env
DATABASE_URL=postgresql://postgres:sua_senha@localhost:5432/db_cashback_nology
```

Exemplo usando Neon:

```env
DATABASE_URL=postgresql://usuario:senha@host-do-neon/neondb?sslmode=require
```

O arquivo `.env` não deve ser enviado para o GitHub.

### 4. Instalar dependências do backend

Entre na pasta `backend`:

```bash
cd backend
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### 5. Rodar a API

```bash
python app.py
```

A API ficará disponível em:

```text
http://127.0.0.1:5000
```

### 6. Abrir o frontend

Abra o arquivo abaixo no navegador:

```text
frontend/index.html
```

Também é possível abrir usando a extensão Live Server do VS Code.

## Rotas da API

### Verificar se a API está funcionando

```http
GET /health
```

Exemplo de resposta:

```json
{
  "message": "API em execução"
}
```

### Calcular cashback

```http
POST /calculate
```

Exemplo de corpo da requisição:

```json
{
  "customer_type": "vip",
  "purchase_value": 600,
  "discount_percentage": 20
}
```

Exemplo de resposta:

```json
{
  "customer_type": "vip",
  "purchase_value": 600.0,
  "discount_percentage": 20.0,
  "cashback": 26.4
}
```

### Buscar histórico por IP

```http
GET /history
```

Essa rota retorna apenas as consultas feitas pelo IP atual.

Exemplo de resposta:

```json
{
  "user_ip": "127.0.0.1",
  "history": [
    {
      "id": 1,
      "customer_type": "vip",
      "purchase_value": 600.0,
      "discount_percentage": 20.0,
      "cashback": 26.4,
      "created_at": "2026-06-15 18:50:40"
    }
  ]
}
```

### Deletar item do histórico

```http
DELETE /history/:id
```

Essa rota remove um item específico do histórico, desde que ele pertença ao mesmo IP do usuário que está fazendo a requisição.

Exemplo:

```http
DELETE /history/1
```

Exemplo de resposta:

```json
{
  "message": "Registro deletado com sucesso."
}
```

## Banco de dados

Tabela utilizada no projeto:

```sql
CREATE TABLE IF NOT EXISTS tbl_cashback_queries (
    id SERIAL PRIMARY KEY,
    user_ip VARCHAR(45) NOT NULL,
    customer_type VARCHAR(20) NOT NULL,
    purchase_value NUMERIC(10,2) NOT NULL,
    discount_percentage NUMERIC(5,2) NOT NULL,
    cashback NUMERIC(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Links do projeto

* App publicado: https://cashback-nology.netlify.app/
* API publicada: https://cashback-nology-532z.onrender.com

## Deploy

O projeto foi publicado utilizando serviços gratuitos:

* Frontend estático hospedado no Netlify
* Backend Flask hospedado no Render
* Banco PostgreSQL hospedado no Neon

O frontend consome a API publicada no Render, e a API registra as consultas no banco PostgreSQL hospedado no Neon.

Observação: por utilizar planos gratuitos, o backend no Render e o banco no Neon podem ficar inativos após um período sem uso. Caso isso aconteça, o primeiro acesso pode demorar alguns segundos enquanto os serviços são reativados automaticamente.

Para produção, a variável `API_URL` no arquivo `frontend/script.js` aponta para a API publicada no Render:

```javascript
const API_URL = "https://cashback-nology-532z.onrender.com";
```


## Observações

O projeto foi desenvolvido com foco em clareza, simplicidade e aderência às regras de negócio do desafio.

As funções e variáveis foram mantidas em inglês por padrão de desenvolvimento, enquanto os comentários, mensagens para o usuário e documentação foram escritos em português, considerando o contexto da vaga e do avaliador.

O arquivo `.env` não deve ser enviado para o repositório, pois pode conter credenciais de acesso ao banco de dados.
