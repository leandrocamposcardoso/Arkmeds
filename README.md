# Arkmeds

##Teste técnico Lenadro de Campos Cardoso


**Tecnologias envolvidas:**
Projeto desenvolvido em _Python 3.8.5_ utilizando o framework _Django 3.1_ + DRF(Django Rest Framework) e banco de dados Postgres

## Instalação
### Postgres Docker
Levando em conta que já tenha o docker instalado, basta rodar o comando.
```shell
docker pull postgres
docker run -d --name <NOME_DO_CONTAINER> -e POSTGRES_PASSWORD=<SENHA_DO_BANCO> -p 5431:5432 postgres
```
### Variaveis de ambiênte
**SECRET_KEY** Secret key do Django
**DB_NAME** Nome do banco
**DB_USER** usuário do banco
**DB_PASSWORD** Senha do banco
**HOST** Servidor
**PORT** Porta
