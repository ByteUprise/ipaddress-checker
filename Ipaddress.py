
import os
import time
import sys
import socket


def clr():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

clr()

print('\033[31m∙∙·▫▫ᵒᴼᵒ FETCH IP ADDRESS ᵒᴼᵒ▫▫·∙∙\033[0m')
start = time.time()
print('\n\033[1;31mFORTIFY\033[0m SOLUTIONS\n\033[0;32mVersion:1.01\trelease date:07-12-2019\033[0m')
print(time.asctime(),'\n')

red = '\033[1;31m'
green = '\033[1;32m'
blue = '\033[1;34m'
print(green,'\"This Tool is to fetch the IP address\"')

while True:
    print(f'{blue}Enter website name \n{red}e.g: google/yahoo/bing')
    a = input('> ').strip()

    b = 'www.'
    ccom = '.com'
    dcom = b+a+ccom
    cnet = ".net"
    dnet = b+a+cnet
    cin = ".in"
    din = b+a+cin
    cgov = ".gov"
    dgov = b+a+cgov
    try:
        print('\033[0m','-'*13,'-'*(len(a)+8),'-'*20)
        ip_com = socket.gethostbyname(dcom)
        print(f'{blue}IP address of {red}{dcom}{blue} : {red}{ip_com}\n')
        time.sleep(2)
        print('\033[0m', '-'
