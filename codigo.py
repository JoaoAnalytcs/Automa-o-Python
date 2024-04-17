import pyautogui
import time
import pandas

#click clicar em algum lugar
#press pressionar una  tecla do teclado
#write escrever 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


#entrar no site
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

#passo 2
pyautogui.click(x=702, y=386)

pyautogui.write("joaotec.ti@hotmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha aqui")
pyautogui.click(x=823, y=551)
time.sleep(3)
tabela =pandas.read_csv("produtos.csv")
print (tabela)

for linha in tabela.index:

 pyautogui.click(x=752, y=275)
 codigo =tabela.loc[linha, "codigo"]
 pyautogui.write(codigo)
 pyautogui.press("tab")

 pyautogui.write(str(tabela.loc[linha, "marca"]))
 pyautogui.press("tab")

 pyautogui.write(str(tabela.loc[linha, "tipo"]))
 pyautogui.press("tab")

 pyautogui.write(str(tabela.loc[linha, "categoria"]))
 pyautogui.press("tab")

 pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
 pyautogui.press("tab")

 pyautogui.write(str(tabela.loc[linha, "custo"]))
 pyautogui.press("tab")

 obs = tabela.loc[linha, "obs"]
 if not pandas.isna(obs):
    pyautogui.write(obs)
 pyautogui.press("tab")


 pyautogui.press("enter")
 pyautogui.scroll(5000)





