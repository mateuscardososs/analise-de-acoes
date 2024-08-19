import matplotlib
import yfinance


ticker = input("Digite o código da ação desejada: ")
dados = yfinance.Ticker(ticker).history(start = "2024-01-01", end = "2024-08-18")
fechamento = dados.Close
fechamento.plot()

#AO RODAR O CODIGO ELE PEDE O COD. DA BOLSA DESEJADA# 



maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

print(maxima)
print(minima)
print(valor_medio)


 
import pyautogui 
import pyperclip
import webbrowser 
import time 

destinatário = "mateus7.cardoso@hotmail.com" #DIGITE O EMAIL PARA QUEM DESEJA ENVIAR
assunto = "analise do projeto 2024"

mensagem = f"""
Prezado gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!

"""

# abrir o navegador e ir para o gmail#
webbrowser.open("www.gmail.com")
time.sleep(6)

#configurando uma pausa de 3 segundos 
pyautogui.PAUSE = 5

#clicar no botão escrever 
pyautogui.click(x=152, y=241)

#Digitar o email do destinatário e teclar TAB
pyperclip.copy(destinatário)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#Digitar o assunto e teclar TAB
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#Digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=1229, y=1040)