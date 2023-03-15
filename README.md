# Site Cadastro Django
  Repositório destinado ao projeto de aprendizado para a criação de um site com a utilização do Django.

## Primeiros passos:
1. Intalar o `Python`, pode realizar o download [aqui.](https://www.python.org/downloads/)
2. Ter a biblioteca do Django instalada, caso não tenha deverá no terminal digitar o seguinte código:
  ````console
  pip install django
  ````
3. Criei uma pasta para o seu projeto (no windows, git, linux, etc)
4. Como sugestão utilize o Visual Code, se não tiver o mesmo instalado, pode realizar o download [aqui](https://code.visualstudio.com/download)
5. Dentro da pasta do seu projeto no terminal do Visual Code `Ctrl + J` digite o seguinte comando:
````console
python -m django startproject nome_do_seu_projeto
````
6. Depois entre na pasta do projeto criada através do comando:
````console
cd nome_do_seu_projeto
````
7. Garanta que você está na pasta correta, execute o comando ls:
````console
ls
````
Para verificar se a pasta que você está tem o arquivo manage.py
8. Estando na pasta correta execute o comando abaixo para criar o app do seu projeto:
````console
python -m django startapp app_do_seu_projeto
````

---

## Iniciando o seu projeto:
Para iniciar o seu projeto execute no terminal o comando:
````console
python .\manage.py runserver
````

---

## Comandos Importantes
1. Criar Migrations
````console
python .\manage.py makemigrations
````
2. Executar Migrations
````console
python .\manage.py migrate
````