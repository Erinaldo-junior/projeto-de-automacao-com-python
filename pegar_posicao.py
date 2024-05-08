import time
import pyautogui

# aqui o codigo vai esperar 5 segundos para que eu possa posicionar o
time.sleep(5)

# para descobrir a posição o pyautogui.position() printa a posição do meu mouse, usando print vai me mostrar onde esta
print(pyautogui.position())

# .scroll e para que a movimente a tela como se fosse o scroll do mouse mesmo, mais nunca vamos saber quantos scrolls vamos dar para voltar ao inicio da tela para cadastrar um novo produto, a dica e colocar um numero muito alto, quando chegar no inicio da tela ele vai parar, se colocar o numero positivo ele vai dar scroll para cima se colocar negativo vai scroll para baixo.
# pyautogui.scroll(5000)


# OBS: OPCIONAL----------------------------------------------------------------------------------------------------------------------
# para saber o nome das teclas, caso queira adicionar no codigo principal
# print(pyautogui.KEYBOARD_KEYS)


# -----------------------------------------------------------------------------------------------------------------------------------
# Aqui eu mostro a tabela
#          codigo       marca        tipo  categoria  preco_unitario  custo               obs
# 0    MOLO000251    Logitech       Mouse          1           25.95    6.5               NaN
# 1    MOLO000192    Logitech       Mouse          2           19.95    5.0               NaN
# 2    CAHA000251     Hashtag      Camisa          1           25.00   11.0               NaN
# 3    CAHA000252     Hashtag      Camisa          2           25.00   11.0  Conferir estoque
# 4    MOMU000111  Multilaser       Mouse          1           11.99    3.4               NaN
# ..          ...         ...         ...        ...             ...    ...               ...
# 288  ACAP000192       Apple  Acessorios          2           19.00    3.8               NaN
# 289  ACSA0009.3     Samsung  Acessorios          3            9.55    2.1               NaN
# 290  CEMO000271    Motorola     Celular          1          279.00   72.5               NaN
# 291  FOMO000152    Motorola        Fone          2          150.00   33.0               NaN
# 292  CEMO000223    Motorola     Celular          3          229.00   55.0               NaN