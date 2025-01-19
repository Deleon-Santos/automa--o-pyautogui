import pyautogui as pa
import time
pa.PAUSE=1

#abrir o navegador
pa.press("win")
pa.write('google')
pa.press('enter')
time.sleep(1)
pa.press('tab')
pa.press('tab')
pa.press('tab')
pa.press('tab')
pa.press('enter')

#navegar ate o linkedin
time.sleep(1)
pa.click(x=674, y=79)
link='https://www.linkedin.com/feed/'
pa.write(link)
pa.press('enter')
time.sleep(2)

#criar a bublicação
pa.click(x=864, y=314)#nova publicação
time.sleep(2)


with open('descricao.txt' ,'r') as arquivo: 
    text= arquivo.readlines()
pa.write(str(text).replace('\n',' '))#escreve a publicação
time.sleep(2)

pa.click(x=506, y=873)#imagem da publicação
time.sleep(1)
pa.write("Captura.png")
time.sleep(1)

pa.press('enter')
time.sleep(1)
pa.click(x=1631, y=903)
time.sleep(1)
pa.click(x=1340, y=956)
#pegar a imagem pelo endereço

#pegar o txt lendo o doc 

#publicar