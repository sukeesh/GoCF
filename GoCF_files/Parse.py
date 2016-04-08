#parse.py 'sukeesh'
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import urllib2
import subprocess
import os
import sys
from os.path import expanduser
from colorama import init
from colorama import Fore, Back, Style

home = expanduser("~")

url1 = "http://www.codeforces.com/contest/"
print (Fore.RED + "\n      GoCF" + Fore.GREEN + "" + Fore.WHITE)
code = int(raw_input("Contest code : "))

url = url1+str(code)
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
sz = soup.findAll(title="Submit")

url2 = "/problem/"
ch = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
chtest = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
jj = 0
print "   Connected!\n"
while jj<len(sz):
	url = url1+str(code)+url2+str(ch[jj])
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	PRE=soup.findAll('pre')
	L=len(PRE)
	inde = 1
	for i in xrange(L):
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
	print (Fore.WHITE + "parsing " + str(ch[jj])) + (Fore.GREEN + "  [Success]  ") + (Fore.WHITE + "")
	jj= jj + 1
pathe = '/GoCF/sukeesh.txt'
f = open(home+pathe,'w')
f.write(str(code)+'\n')
jj = 0
while jj < len(sz):
	f.write(str(ch[jj]) + " " + str(chtest[jj])+'\n')
	jj = jj + 1
f.close()
