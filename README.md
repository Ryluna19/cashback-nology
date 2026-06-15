# Calculadora de Cashback - Desafio Nology

Projeto desenvolvido para o desafio de Estagiário de Dev da Nology.

A aplicação calcula o cashback de uma compra com base nas regras de negócio informadas no desafio. O usuário pode informar o tipo de cliente, o valor da compra e o percentual de desconto. Cada consulta realizada é salva em banco de dados e exibida no histórico apenas para o IP que realizou a consulta.

## Tecnologias utilizadas

* Python
* Flask
* MySQL
* HTML
* CSS
* JavaScript
* phpMyAdmin
* XAMPP

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

- Cálculo de cashback
- Validação dos dados enviados pelo usuário
- API em Python com Flask
- Registro das consultas em banco MySQL
- Histórico de consultas separado por IP
- Exclusão de itens individuais do histórico
- Frontend estático em HTML, CSS e JavaScript

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
│
├── .gitignore
└── README.md
```

## Como executar o projeto localmente

### 1. Clonar o repositório

```bash
git clone link-do-repositorio
cd cashback-nology
```

### 2. Criar o banco de dados

Abra o phpMyAdmin e execute o script localizado em:

```text
database/01_create_database.sql
```

Esse script cria o banco `db_cashback_nology` e a tabela `tbl_cashback_queries`.

### 3. Configurar variáveis de ambiente

Dentro da pasta `backend`, crie um arquivo chamado `.env` com base no arquivo `.env.example`.

Exemplo:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=db_cashback_nology
```

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

### Calcular cashback

```http
POST /calculate
```

### Deletar item do histórico

```http
DELETE /history/:id
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

## Observações

O projeto foi desenvolvido com foco em clareza, simplicidade e aderência às regras de negócio do desafio. As funções e variáveis foram mantidas em inglês por padrão de desenvolvimento, enquanto os comentários, mensagens para o usuário e documentação foram escritos em português.
