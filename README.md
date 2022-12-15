<h1 align="center"> NutriLab </h1>

<p style='text-align: justify;'> 
Um sistema completo de gestão para nutricionistas com cadastro e login, listagem e perfil de cada paciente, plano alimentar e diversas funcionalidades de interesse para esse nicho.
</p>


<img align="center" alt="Proj-gif"  src="templates\static\readme\Projeto Nutrilab.gif">



</div>


<br>

&nbsp;
![license](https://img.shields.io/badge/license-MIT-green)

# :hammer: Funcionalidades do projeto

- `Cadastro e Login de nutricionistas`: Autenticação de nutricionistas com email, nome de usuário e senha.
&nbsp;
- `Confirmação de email no cadatro`: Ativação de conta por meio de um link enviado para o email cadastrado com um token único criado para cada usuário com o sha256.
&nbsp;
- `Listagem e cadastro de pacientes de cada nutricionista`: Página de acesso com todos os pacientes cadastrados e opção de cadastrar novos clientes.
&nbsp;

- `Perfil do paciente`: Histórico de evolução das medidas do paciente com gráficos relacionados
&nbsp;

- `Ambiente de planejamento alimentar`: Cadastro e listagem de refeições de cada de pacientes com upload de imagem
&nbsp;


# ✔️ Técnicas e tecnologias utilizadas

- ``Framework Django``
- ``Python, Js, html, css, Bootstrap``
- ``Geração de token com sha256``
- ``Importação de imagens``
- ``Expressões regulares``
- ``ORM compatível com MySQL, PostgreSQL, SQLite e Oracle``
- ``Arquitetura MVT``
- ``Paradigma de orientação a objetos``



# 📁 Acesso ao projeto


https://github.com/joaoreider/nutri-lab


# 🛠️ Abrir e rodar o projeto

Primeiramente, você precisa ter o python instalado na sua máquina.
Após baixar o projeto, você pode abrir a IDE e instalar as dependências com o comando: 
```
pip install -r requirements.txt  
```
Depois é só rodar o servidor local com o comando:
```
python manage.py runserver
```
Esse comando funciona no Windows.

Após isso você pode copiar o IP fornecido e colar no seu navegador adicionando a url o nome auth (ex: http://127.0.0.1:8000/auth) realizar o cadastro de usuário e logar na sua conta para acessar todas as funcionalidades!


:point_down: Acesse meu perfil no Linkedin 
<div> 
 <a href="https://www.linkedin.com/in/jo%C3%A3o-paulo-2345b3170/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>

</div>