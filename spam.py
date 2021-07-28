import requests,json,datetime
from random import choice
from colorama import init,Style,Fore

banner="""\033[91m
------------------------------------------------------------
Instagram Spam Bot | Theós Hack Team | www.theosforum.org
------------------------------------------------------------

Coder     : Apathe
Instagram : Ap4the

------------------------------------------------------------
"""

class Main:
	
	def __init__(self,username,passwd,spamUser,spamUserId):
		self.username = username
		self.passwd = passwd
		self.spamUser = spamUser
		self.spamUserId = spamUserId
		self.csrf = "csrftokenZmidz&#PWD_INSTAGRAM_BROWSER:0:1589682409:{}z{}Zfalse)ÚusernameZenc_passwordZqueryParamsZ optIntoOneTap)ÚheadersÚdataZuserIdzX-CSRFTokenZ csrftokenz login Truez#https://www.instagram.com/{}/"
		self.log = False
		
		
		self.useragent_list=[
			"Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0",
			"Mozilla/5.0 (Android 4.4; Tablet; rv:41.0) Gecko/41.0 Firefox/41.0",
			"Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0",
			"Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
			"Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0",
			"Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0"
		]
		self.user_agent=choice(self.useragent_list)
		
		#Login fuction parametres
		self.link = 'https://www.instagram.com/accounts/login/' 
		self.login_url = 'https://www.instagram.com/accounts/login/ajax/'  
		self.time = int(datetime.datetime.now().timestamp())
		
		self.ses=requests.Session()
		
	
	def login(self):
		
		response = requests.get(self.link)

		payload = {
			'username': self.username,     
			'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{self.time}:{self.passwd}',
			'queryParams': {},     
			'optIntoOneTap': 'false'
		 }  
		login_header = {     
			"User-Agent": self.user_agent,     
			"X-Requested-With": "XMLHttpRequest",     
			"Referer": "https://www.instagram.com/accounts/login/",     
			"x-csrftoken": self.csrf 
		}  
		login_response = requests.post(self.login_url, data=payload, headers=login_header) 
		json_data = json.loads(login_response.text)  
		if json_data["authenticated"]:      
			print(f"Giriş Başarılı ! [ {self.username} ]")                   #cookies = login_response.cookies
#			cookie_jar = cookies.get_dict()     
#			csrf_token = cookie_jar['csrftoken']     
#			print("csrf_token: ", csrf_token)     
#			session_id = cookie_jar['sessionid']     
#			print("session_id: ", session_id)
			self.log = True
		else:
			print(f"""Giriş Başarısız !({self.username}) \n 
Sizden kaynaklı bir sorun tespit edildi , bize ulaşabilirsiniz.""")
	
	
	
	def spam(self):
		if self.log == True:
			link = "https://www.instagram.com/" + self.spamUserId + "/"
			profileGetResponse = self.ses.get(link)
			self.ses.cookies.update(profileGetResponse.cookies)
		    
			spamHeaders = {
	            "Accept":"*/*",
	            "Accept-Encoding":"gzip,deflate,br",
	            "Accept-Language":"en-US,en;q=0.5",
	            "Connection":"keep-alive",
	            "Content-Type":"application/x-www-form-urlencoded",
	            "DNT":"1",
	            "Host":"www.instagram.com",
	            "X-Instagram-AJAX":"2",
	            "X-Requested-With":"XMLHttpRequest",
	            "Referer":link,
	            "User-Agent":self.user_agent,
	            "X-CSRFToken":self.csrf
	            }
	            
			spamData = {
	            "reason_id":"1",
	            "source_name":"profile"
	            }
	            
			self.ses.headers.update(spamHeaders)
			
			spamPostResponse= self.ses.post("https://www.instagram.com/users/"+ self.spamUserId +"/report/",data=spamData)
			
			if spamPostResponse.status_code == 200:self.ses.close();return 1
			else:return 0
		else:
			self.login()
	    
	def start(self):
		self.login()
		if self.log==True:
			self.spam()
		else:
			self.login()


if __name__ == "__main__":
	userFile = open("userlist.txt","r")
	USERS = []
	for user in userFile.readlines():
		if user.replace("\n","").replace("\r","\n") != "":
			USERS.append(user.replace("\n","").replace("\r","\n"))
	print(Fore.RED + banner + Style.RESET_ALL)
	print(str(len(USERS)) + " Adet Kullanıcı Yüklendi !\n")
	spamUser = input(Fore.GREEN + "Spam Atılacak Hesabın Kullanıcı Adı ; " + Style.RESET_ALL)
	spamUserId = input(Fore.GREEN + "Spam Atılacak Hesabın User ID'si    ; " + Style.RESET_ALL)
	print("")
	print("Spam Saldırısı Başlatılıyor !\n")
	for user in USERS:
		spam= Main(user.split(" ")[0],user.split(" ")[1],spamUser,spamUserId)
		spam.start()
		if spam.log== True and spam.spam() == 1:
			print("Başarıyla Spam Atıldı !")

#  : D lol






