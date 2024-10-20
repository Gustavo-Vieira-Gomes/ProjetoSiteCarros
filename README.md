# Projeto Carros

Este é o Projeto Carros, um projeto desenvolvido em Django e HTML5 para apresentar carros em estoque em uma concessonária, o qual acompanhei o desenvolvimento durante o Curso Django Master. Este README fornece informações essenciais sobre como configurar e executar o projeto em seu ambiente local.

## Requisitos
Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Python (versão recomendada: 3.7 ou superior)
- Django (instalado automaticamente ao seguir as instruções abaixo)
- Outras dependências listadas no arquivo requirements.txt

## Instalação das Dependências
Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:

```
pip install -r requirements.txt

```

## Criação do Token do Gemini
- Crie uma conta no site https://ai.google.dev/gemini-api?hl=pt-br
- Obtenha seu token de acesso, guarde-o no seu lugar de preferência dentro do computador
- Adicione o caminho até o token em uma variável de ambiente chamada GEMINI_API_KEY

## Rodar o projeto
Após instalar as dependências, aplique as migrations no banco de dados com o comando:

```
python manage.py migrate
```

Agora o projeto jã pode ser inicializado com o comando:

```
python manage.py runserver
```
Após isso, o sistema estará pronto para ser acessado em: http://localhost:8000


### 🤝 Suporte/Contato
[![Whatsapp Badge](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/5511947747178)
[![Instagram Badge](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/pyhelpbr/)