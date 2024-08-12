# payment-email-system
 
 Estrutura de arquivo : 
 ```
payment-email-system/
│
├── payment_api/              # Diretório para a API de Pagamento
│   ├── Dockerfile
│   ├── app.py                # Código principal da API de Pagamento
│   └── requirements.txt
│
├── email_api/                # Diretório para a API de Envios de Email
│   ├── Dockerfile
│   ├── app.py                # Código principal da API de Envios de Email
│   └── requirements.txt
│
├── docker-compose.yml        # Arquivo Docker Compose para rodar RabbitMQ e as APIs
└── README.md                 # Documentação do projeto
```
# Passo a Passo do Projeto

1. Processamento de Pagamento: O cliente envia uma requisição para a API de Pagamento (/process_payment) com detalhes do pagamento.

2. Envio para RabbitMQ: A API de Pagamento, após processar o pagamento, envia uma mensagem para a fila do RabbitMQ (payment_queue) com as informações do pagamento.

3. Consumo e Envio de Email: A API de Envios de Email escuta a fila payment_queue. Quando uma nova mensagem é recebida, a API processa essa mensagem e envia um email de confirmação para o cliente.

# Execução do Projeto

1. Execute o comando abaixo para iniciar todos os serviços definidos no docker-compose.yml:
```
docker-compose up --build
```

2. Testando a API de Pagamento: Você pode enviar uma requisição POST para http://localhost:5000/process_payment com um JSON contendo os detalhes do pagamento. 

```
{
    "order_id": "12345",
    "amount": "100.00",
    "currency": "USD",
    "email": "customer@example.com"
}
```
2. Verificando o Envio de Email: O consumidor na API de Envios de Email processará a mensagem e simulará o envio de um email de confirmação, que será exibido no terminal.