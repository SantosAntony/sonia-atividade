from django.shortcuts import render
from django.http import HttpResponse
def pagina_inicial(request) :
  return HttpResponse('''
<!DOCTYPE html>
<html>
  <head>
    <title>Sistema</title>
  </head>
  <body>
    <h1>tonysistemas</h1>
    <p>descrição dos projetos....</p>
  </body>
  <a href="http://127.0.0.1:8000/pagina2/"> pagina sobre <a>
                      <br>
  <a href="http://127.0.0.1:8000/pagina3/"> pagina projetos <a>
                      <br>
  <a href="http://127.0.0.1:8000/pagina4/"> pagina contato <a>

</html>
                      ''')

def pagina_sobre(request) :
  return HttpResponse('''
<!DOCTYPE html>
<html>
  <head>
    <title>Sistemas</title>
  </head>
  <body>
    <h1>explicação do sistema</h1>
    <p>.........................</p>
    <p>nome da equipe<p>
    <a href="http://127.0.0.1:8000/pagina1/"> VOLTAR <a>
</html>
    
  </body>
</html>
                      ''')

def pagina_projetos(request) :
  return HttpResponse('''
<!DOCTYPE html>
<html>
  <head>
    <title>Sistemas</title>
  </head>
  <body>
    <h1>listas de projetos</h1>
    <table boder="1">
                      <thead>
                      </tr>
                      <th>projeto</th>
                      <th>descrição</th>
                      </tr>
                      <tbody>
                      <tr>
                      <td>lava rapido</td>
                      <td>    /    lavar as ruas de paulista</td>
                      </tr>
                      <tr>
                      <td>ajudar</td>
                      <td>    /    sei la qualquer coisa</td>
                      </tr>
                      </tbody>
                      </table>
    <a href="http://127.0.0.1:8000/pagina1/"> VOLTAR <a>
</html>
    
  </body>
</html>
                      ''')

def pagina_contato(request) :
  return HttpResponse('''
<!DOCTYPE html>
<html>
  <head>
    <title>Sistemas</title>
  </head>
  <body>
    <h1>contatos</h1>
    <ul>
    <li>seila@gmail.com</li>
    <li>81 9 8765-6374</li>
    <li>instituição mais pika do mundo</li>
    <li>antony</li>
    <li>yuri</li>
    <li>raphael</li>
    </ul>
    <a href="http://127.0.0.1:8000/pagina1/"> VOLTAR <a>
</html>
    
  </body>
</html>
                      ''')


