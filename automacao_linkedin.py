import pyautogui as pa
import time
pa.PAUSE=1

#definição de variaveis e descrição
link='https://www.linkedin.com/feed/'
with open('descricao.txt' ,'r') as arquivo: 
    text= arquivo.readlines()

#abrir o navegador
pa.press("win")
pa.write('google')
pa.press('enter')
time.sleep(1)
pa.click(x=855, y=461)
time.sleep(1)

#navegar ate o linkedin
pa.click(x=674, y=79)
pa.write(link)
pa.press('enter')
time.sleep(2)

#criar a bublicação
pa.click(x=864, y=314)#nova publicação
time.sleep(2)
pa.write(str(text).replace('\n',' '))#escreve a publicação
time.sleep(2)

#buscar a imagem para a publicação
pa.click(x=506, y=873)#imagem da publicação
time.sleep(1)
pa.write("Captura.png")
time.sleep(1)
pa.press('enter')
time.sleep(1)

#publicar e salvar publicação
pa.click(x=1631, y=903)
time.sleep(1)
pa.click(x=1340, y=956)