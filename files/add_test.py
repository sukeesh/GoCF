import io
from subprocess import call
from colorama import init
from colorama import Fore, Back, Style


print ""
print (Fore.RED + " :: GoCF ") + (Fore.GREEN + "Custom test ") + (Fore.WHITE + "Editor ")
print ""
problem_code = raw_input(" >> QUESTION CODE? : ")

with open('sukeesh.txt', 'r') as file:
	data = file.readlines()

x = ord(problem_code) - 64
y = int(data[x][2]) + 1
stri = data[x]
stri = stri[0:2]
stri = stri + str(y)
data[x] = stri
print data[x]

with open('sukeesh.txt', 'w') as file:
    file.writelines(data)

file_name = problem_code + str(data[x][2]) + ".in"
print file_name
call(["touch", file_name])
with open(file_name, 'w') as file:
	file.write("/*Enter Input here*/")
call(["subl", file_name])

file_name = problem_code + str(data[x][2]) + ".out"
print file_name
call(["touch", file_name])
with open(file_name, 'w') as file:
	file.write("/*Enter Output here*/")
call(["subl", file_name])

file_name = problem_code + str(data[x][2]) + ".rc"
call(["touch", file_name])

print (Fore.GREEN + " Don't Forget to save those files! ")