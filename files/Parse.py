#parse.py 'sukeesh'
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import urllib3
import subprocess
import os
import sys
from os.path import expanduser
from colorama import init
from colorama import Fore, Back, Style

home = expanduser("~")

url1 = "https://www.codeforces.com/contest/"
print (Fore.RED + "\n      GoCF" + Fore.GREEN + "" + Fore.WHITE)
code = int(input("Contest code : "))

http = urllib3.PoolManager()


url = url1+str(code)
http.request('Get', url)
page = http.request('Get', url)
# print(page.data)
soup = BeautifulSoup(page.data, features="lxml")
sz = soup.findAll(title="Submit")

url2 = "/problem/"
ch = []
chtest = []
for p in soup.findAll('td', attrs={'class':"id"}): 
    for s in p.find('a').stripped_strings:
        ch.append(s)
        chtest.append(0) 

jj = 0
print ("   Connected!\n")
while jj<len(sz):
	url = url1+str(code)+url2+str(ch[jj])
	page = http.request('Get', url)
	soup = BeautifulSoup(page.data, features="lxml")
	PRE=soup.findAll('pre')
	L=len(PRE)
	inde = 1
	for i in range(L):
		if PRE[i].parent['class']=='note':
			break
		elif(i%2==0):
			In=str(PRE[i])
			In=In.replace('<pre>','').replace('</pre>','')
			In=In.replace('&gt;','>')
			In=In.replace('&lt;','<')
			In=In.replace('&quot;','"')
			In=In.replace('&amp;','&')
			In=In.replace('<br />','\n')
			In=In.replace('<br/>','\n')
			In=In.replace('</ br>','\n')
			In=In.replace('</br>','\n')
			In=In.replace('<br>','\n')
			In=In.replace('< br>','\n')
			In=In.split('\n')
			if(i==0):
				pathe = '/GoCF/'+str(ch[jj])+str(inde)+'.in'
				f=open(home+pathe,'w')
			else:
				pathe = '/GoCF/'+str(ch[jj])+str(inde)+'.in'
				f=open(home+pathe,'w')
			for j in In:
				y=j.replace('\n','')
				if(y!='' and y!=' '):
					f.write(y+'\n')
			f.close()
		else:
			Out=str(PRE[i])
			Out=Out.replace('<pre>','').replace('</pre>','')
			Out=Out.replace('&gt;','>')
			Out=Out.replace('&lt;','<')
			Out=Out.replace('&quot;','"')
			Out=Out.replace('&amp;','&')
			Out=Out.replace('<br />','\n')
			Out=Out.replace('<br/>','\n')
			Out=Out.replace('</ br>','\n')
			Out=Out.replace('<br>','\n')
			Out=Out.split('\n')
			if(i==1):
				pathe = '/GoCF/'+str(ch[jj])+str(inde)+'.out'
				f=open(home+pathe,'w')
			else:
				pathe = '/GoCF/'+str(ch[jj])+str(inde)+'.out'
				f=open(home+pathe,'w')
			for j in Out:
				y=j.replace('\n','')
				if(y!='' and y!=' '):
					f.write(y+'\n')
			f.close()
			inde = inde + 1
			chtest[jj] = chtest[jj] + 1
	print ((Fore.WHITE + "parsing " + str(ch[jj])) + (Fore.GREEN + "  [Success]  ") + (Fore.WHITE + ""))
	jj= jj + 1
pathe = '/GoCF/sukeesh.txt'
f = open(home+pathe,'w')
f.write(str(code)+'\n')
jj = 0
while jj < len(sz):
	f.write(str(ch[jj]) + " " + str(chtest[jj])+'\n')
	jj = jj + 1
f.close()
