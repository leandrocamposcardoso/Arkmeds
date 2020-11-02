﻿
# Arkmeds



##Teste técnico Lenadro de Campos Cardoso




**Tecnologias envolvidas:**

Projeto desenvolvido em _Python 3.8.5_ utilizando o framework _Django 3.1_ + DRF(Django Rest Framework) e banco de dados Postgres



# Banco (Docker)

### Postgres Docker
Uma forma fácil de configurar o banco é através de docker, o componente utilizado e maiores informações podem ser encontrados neste link do [DockerHub](https://hub.docker.com/_/postgres) .

Levando em conta que já tenha o docker instalado em sua maquina, basta rodar o comando.

```shell
docker pull postgres
docker run -d --name <NOME_DO_CONTAINER> -e POSTGRES_PASSWORD=<SENHA_DO_BANCO> -p 5431:5432 postgres
```



# API Django

### Variáveis de ambiênte

**SECRET_KEY** Secret key do Django

**DB_NAME** Nome do banco

**DB_USER** usuário do banco

**DB_PASSWORD** Senha do banco

**HOST** Servidor

**PORT** Porta



**ARKMEDS_USER** Usario arkmeds
**ARKMEDS_PASSWORD** Senha arkmeds



  ## Instalação

Para configurar o ambiente corretamente os comandos abaixo devem ser executados dentro da pasta **arkmeds-api** onde se encontra a API do django.
### Instalar dependências
```shell
pip install -r requirements.txt
```

### Rodar os migrations

```shell
python manage.py migrate
```

**Pronto! Agora o backend esta pronto para rodar!**


## Execução do projeto
Para executar o script do desafio basta executar o comando:

```shell
python manage.py arkmeds_script
```

Este comando irá executar as **partes 1 e 2** do desafio, capturando os dados, abrindo os chamados e populando o banco  com os dados coletados. As etapas do processo podem ser acompanhadas pelo log do terminal.

### Rodar os migrations

```shell
python manage.py migrate
```

**Ah, não podemos esquecer dos testes!**

Para executar os testes do projeto basta rodar o comando:

```shell
python manage.py test
```

### Rodar dar o servidor

```shell
python manage.py runserver
```

**Back-end rodando com sucesso!!!**

## Endpoints
As APIs seguem os padrões de URL do *DRF(Django Resf Framework)* :
**eg:**
1. endpoint/view - Listar (GET)
2. endpoint/view/[id] - Receber (GET)
3. endpoint/view - Criar (POST)
4. endpoint/view/[id]  - Remover (DELETE)
5. endpoint/view/[id] - Modificar (Put)


**HOST(localhost:8000)/equipamentos**

1. /empresa - [get post put delete]
2. /equipamento - [get post put delete]
3. /proprietario - [get post put delete]
4. /tipo_equipamento - [get post put delete]
5. /responsavel_tecnico - [get post put delete]
6. /chamado_equipamentoget - [post put delete]
7. /equipamento/num_tickets - [get ]
8. /proprietario/num_equipments - [get ]


# Frontend React
**Primeiramente me desculpe pelo layout! Mas imagino que esse não seja o foco do teste.**
O Front-end foi feito em React, consumindo as APIs do Django

## Url da API
A url da api pode ser definida com a variável de ambiente **REACT_APP_API_HOST** mas já possui o valor padrão em **localhost** na porta **8080**.

## Configurando o Front-end
Para configurar o ambiente corretamente os comandos abaixo devem ser executados dentro da pasta **arkmeds-ui**.

### Instalando
Para instalar os pacotes de dependências do React basta executar o comando:

```shell
npm install
```

### Rodar o servidor
Apos ter certeza que o servidor de backend esta rodando, para iniciar a aplicação react basta executar o comando:

```shell
npm start
```


**Pronto! Agora tempos tudo rodando!**

# Obrigado a todos pela oportunidade!
