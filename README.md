# emprestimo_pessoal
Sistema de Gestão de Propostas de Empréstimo Pessoal

# Executar projeto

Pra executar o projeto, é necessário ter o docker instalado. Na pasta com o arquivo 'docker-compose.yml' execute o comando 'docker-compose up --build'

#Admin

Super user para acesso ao admin:
- Username: admin
- Passsword: admin

#Rota para solicitar emprestime:

POST em 'http://localhost:8000/api/personal_loan/loan_proposal/'

Dados a serem enviados: 

- name: string
- document_number: string (cpf pode começar com 0)
- address: string
- loan_value: double

# Verificar status de um emprestimo

GET 'http://localhost:8000/api/personal_loan/loan_proposal/{id}/'

