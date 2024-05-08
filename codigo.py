 
# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

# aqui a cada comando do pyautogui ele faz uma pausa de 0.5 segundos para não atropelar os comandos
pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que ele demore alguns segundos para carregar o site, o time sleep fica parado ate carregar o site.
time.sleep(2)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=651, y=514)
# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")

# aqui o programa esta pedindo pra alterar a palavra passe então pedi pra ele esperar 3 segundos ai apertar confirmar.
time.sleep(2)
pyautogui.press("enter")

# aqui quando ele confirmar o enter vai começar a rodar novamente o programa apos 3 segundos
time.sleep(0.5)

# para trabalhar com base de dados vamos usar a biblioteca pandas, o Pandas fornece ferramentas para trabalhar com dados tabulares, para abreviar o nome da biblioteca usamos (as pd) quando formos usar os comandos do pandas vamos usar pd ao inves de pandas e como um apelido.

# # Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

# aqui estou importando a base de dados que eu quero trabalhar o nome tem que ser exatamente como esta na base de dados que no caso aqui produtos.csv, o comando (.read) mostra todas as bases de dados que o pandas consegue ler, e vamos armazenalas todas em uma variavel chamada tabela.  
tabela = pd.read_csv("produtos.csv")

print(tabela)

# # para cada linha dentro da minha tabela.index (esse .index seginifica que ele vai pegar uma lista com as linhas da minha tabela, se quisesse pegar uma lista com as colunas da minha tabela usaria o comando .columns), as linhas da tabela no pandas são chamadas de indices.
# Teste para cadastrar um por UM produto de forma manual.
# Para cadastrar o codigo de acordo com as linhas da tabela, vamos usar a variavel linha.

for linha in tabela.index:
    # cadastrar produto
    # para localizar um informação dentro de uma tabela, vai usar.loc[] dentro dos colchetes, vamos colocar a linha que ja esta sendo dinamica na variavel linha no for, e a coluna entre "", nesse exemplo, .loc[linha, "codigo"], mais vai ser usado no restante da tabela. E interessante tranformar as informações numericas em texto para que possamos colocar os numeros dentro do .write que precisa e obrigatorio estar entre "", para transformar vamos colocar o str.
    codigo = str(tabela.loc[linha, "codigo"])

    # campo do codigo do produto
    pyautogui.click(x=617, y=369)

    # preencher o codigo
    pyautogui.write(codigo)

    # passar para o proximo campo
    pyautogui.press("tab")

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    # passar para o proximo campo
    pyautogui.press("tab")
    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    # passar para o proximo campo
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    # passar para o proximo campo
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    # passar para o proximo campo
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    # passar para o proximo campo
    pyautogui.press("tab")

    # obs
    # obs vamos fazer uma variavel, ao inves de fazer como estava sendo feito anteriormente, por que so queremos preencher o obs, se for diferente de nan, com isso vamos tratar usando if, para fazermos uma condição, so vai executar se a condição for verdadeira.
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    # passar para o proximo campo
    pyautogui.press("tab")

    # apertar o botão
    pyautogui.press("enter")

    # .scroll e para que a movimente a tela como se fosse o scroll do mouse mesmo, mais nunca vamos saber quantos scrolls vamos dar para voltar ao inicio da tela para cadastrar um novo produto, a dica e colocar um numero muito alto, quando chegar no inicio da tela ele vai parar, se colocar o numero positivo ele vai dar scroll para cima se colocar negativo vai scroll para baixo.
    # pyautogui.scroll(5000)

    # outra forma de fazer tambem seria ao inves de usar o scroll, usar a tecla home que tambem vai funcionar.
    pyautogui.press("home")


