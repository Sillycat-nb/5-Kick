# แก้โดย SELFBOT-BY:MAX ติดต่อได้ที่เบอร์ 191
# -*- coding: utf-8 -*-
import linepy
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
#==============================================================================#
ptatan1983 = LineClient()
#ptatan1983 = LineClient(authToken=' TOKEN MU CINTA')
ptatan1983.log("Auth Token : " + str(ptatan1983.authToken))
channel = LineChannel(ptatan1983)
ptatan1983.log("Channel Access Token : " + str(channel.channelAccessToken))
#==============================================================================#
k1 = LineClient()
#k1 = LineClient(authToken=' TOKEN MU CINTA')
k1.log("Auth Token : " + str(k1.authToken))
channel1 = LineChannel(k1)
k1.log("Channel Access Token : " + str(channel1.channelAccessToken))
#==============================================================================#
k2 = LineClient()
#k2 = LineClient(authToken=' TOKEN MU CINTA')
k2.log("Auth Token : " + str(k2.authToken))
channel2 = LineChannel(k2)
k2.log("Channel Access Token : " + str(channel2.channelAccessToken))
#==============================================================================#
k3 = LineClient()
#k3 = LineClient(authToken=' TOKEN MU CINTA')
k3.log("Auth Token : " + str(k3.authToken))
channel3 = LineChannel(k3)
k3.log("Channel Access Token : " + str(channel3.channelAccessToken))
#==============================================================================#
k4 = LineClient()
#k4 = LineClient(authToken=' TOKEN MU CINTA')
k4.log("Auth Token : " + str(k4.authToken))
channel4 = LineChannel(k4)
k4.log("Channel Access Token : " + str(channel4.channelAccessToken))
#==============================================================================#
k5 = LineClient()
#k5 = LineClient(authToken=' TOKEN MU CINTA')
k5.log("Auth Token : " + str(k5.authToken))
channel5 = LineChannel(k5)
k5.log("Channel Access Token : " + str(channel5.channelAccessToken))
#==============================================================================#
k6 = LineClient()
#k6 = LineClient(authToken=' TOKEN MU CINTA')
k6.log("Auth Token : " + str(k6.authToken))
channel6 = LineChannel(k6)
k6.log("Channel Access Token : " + str(channel6.channelAccessToken))
#==============================================================================#
k7 = LineClient()
#k7 = LineClient(authToken=' TOKEN MU CINTA')
k7.log("Auth Token : " + str(k7.authToken))
channel7 = LineChannel(k7)
k7.log("Channel Access Token : " + str(channel7.channelAccessToken))
#==============================================================================#
k8 = LineClient()
#k8 = LineClient(authToken=' TOKEN MU CINTA')
k8.log("Auth Token : " + str(k8.authToken))
channel8 = LineChannel(k8)
k8.log("Channel Access Token : " + str(channel8.channelAccessToken))
#==============================================================================#
k9 = LineClient()
#k9 = LineClient(authToken=' TOKEN MU CINTA')
k9.log("Auth Token : " + str(k9.authToken))
channel9 = LineChannel(k9)
k9.log("Channel Access Token : " + str(channel9.channelAccessToken))
#==============================================================================#
k10 = LineClient()
#k10 = LineClient(authToken=' TOKEN MU CINTA')
k10.log("Auth Token : " + str(k10.authToken))
channel10 = LineChannel(k10)
k10.log("Channel Access Token : " + str(channel10.channelAccessToken))
#==============================================================================#
sw = LineClient()
#sw = LineClient(authToken=' TOKEN MU CINTA')
sw.log("Auth Token : " + str(sw.authToken))
channel = LineChannel(sw)
sw.log("Channel Access Token : " + str(channel.channelAccessToken))
#==============================================================================#
poll = LinePoll(ptatan1983)
poll = LinePoll(k1)
poll = LinePoll(k2)
poll = LinePoll(k3)
poll = LinePoll(k4)
poll = LinePoll(k5)
poll = LinePoll(k6)
poll = LinePoll(k7)
poll = LinePoll(k8)
poll = LinePoll(k9)
poll = LinePoll(k10)
call = ptatan1983
creator = ["u14f64e139a3817afaabe27d237afb36b"]
owner = ["u14f64e139a3817afaabe27d237afb36b"]
admin = ["u14f64e139a3817afaabe27d237afb36b"]
staff = ["u14f64e139a3817afaabe27d237afb36b"]
mid = ptatan1983.getProfile().mid
Amid = k1.getProfile().mid
Bmid = k2.getProfile().mid
Cmid = k3.getProfile().mid
Dmid = k4.getProfile().mid
Emid = k5.getProfile().mid
Fmid = k6.getProfile().mid
Gmid = k7.getProfile().mid
Hmid = k8.getProfile().mid
Imid = k9.getProfile().mid
Jmid = k10.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [ptatan1983,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,sw]
ABC = [ptatan1983,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,sw]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Zmid]
nadya = admin + staff + creator

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []

welcome = []
simisimi = []
translateen = []
translateid = []
translateth = []
translatetw = []
translatear = []

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

ptatan1983Profile = ptatan1983.getProfile()
myProfile["displayName"] = ptatan1983Profile.displayName
myProfile["statusMessage"] = ptatan1983Profile.statusMessage
myProfile["pictureStatus"] = ptatan1983Profile.pictureStatus

responsename1 = k1.getProfile().displayName
responsename2 = k2.getProfile().displayName
responsename3 = k3.getProfile().displayName
responsename4 = k4.getProfile().displayName
responsename5 = k5.getProfile().displayName
responsename6 = k6.getProfile().displayName
responsename7 = k7.getProfile().displayName
responsename8 = k8.getProfile().displayName
responsename9 = k9.getProfile().displayName
responsename10 = k10.getProfile().displayName
responsename = sw.getProfile().displayName

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(nadya.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        ptatan1983.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ptatan1983.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(nadya.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        ptatan1983.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ptatan1983.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = ptatan1983.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nDi group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(nadya.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        ptatan1983.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ptatan1983.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Keluar「{}」\nByee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = ptatan1983.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nDari group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(nadya.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        ptatan1983.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ptatan1983.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = ptatan1983.getAllContactIds()
        gid = ptatan1983.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n🐚 Group : "+str(len(gid))+"\n🐚 Teman : "+str(len(teman))+"\n🐚 Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n🐚 Runtime : \n • "+bot
        ptatan1983.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ptatan1983.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╔═════════════════╗" + "\n" + \
                  "╠  🤖 SELFBOT-BY:MAX 🤖" + "\n" + \
                  "╚═════════════════╝" + "\n" + \
                  "╔═════════════════╗" + "\n" + \
                  "╠       🤖 MENU SELF 🤖" + "\n" + \
                  "╠═════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Help 1\n" + \
                  "╠❂͜͡☬➣ " + key + "Help 2\n" + \
                  "╠❂͜͡☬➣ " + key + "Help 3\n" + \
                  "╠❂͜͡☬➣ " + key + "Help 4\n" + \
                  "╠❂͜͡☬➣ " + key + "Me\n" + \
                  "╠❂͜͡☬➣ " + key + "Mid\n" + \
                  "╠❂͜͡☬➣ " + key + "Mid「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Info「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Nk「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Kick「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Mybot\n" + \
                  "╠❂͜͡☬➣ " + key + "Status\n" + \
                  "╠❂͜͡☬➣ " + key + "Status translate\n" + \
                  "╠❂͜͡☬➣ " + key + "About\n" + \
                  "╠❂͜͡☬➣ " + key + "Restart\n" + \
                  "╠❂͜͡☬➣ " + key + "Runtime\n" + \
                  "╠❂͜͡☬➣ " + key + "Creator\n" + \
                  "╠❂͜͡☬➣ " + key + "Respon\n" + \
                  "╠❂͜͡☬➣ " + key + "Sp\n" + \
                  "╠❂͜͡☬➣ " + key + "Spb\n" + \
                  "╠❂͜͡☬➣ " + key + "Sprespon\n" + \
                  "╠❂͜͡☬➣ " + key + "Mentionall\n" + \
                  "╠❂͜͡☬➣ " + key + "Tagall\n" + \
                  "╠❂͜͡☬➣ " + key + "Mjoin\n" + \
                  "╠❂͜͡☬➣ " + key + "Mbye\n" + \
                  "╠❂͜͡☬➣ " + key + "Pulang\n" + \
                  "╠❂͜͡☬➣ " + key + "Assist join\n" + \
                  "╠❂͜͡☬➣ " + key + "Ginfo\n" + \
                  "╠❂͜͡☬➣ " + key + "Open\n" + \
                  "╠❂͜͡☬➣ " + key + "Close\n" + \
                  "╠❂͜͡☬➣ " + key + "Url grup\n" + \
                  "╠❂͜͡☬➣ " + key + "Reject\n" + \
                  "╠❂͜͡☬➣ " + key + "Gruplist\n" + \
                  "╠❂͜͡☬➣ " + key + "Infogrup「angka」\n" + \
                  "╠❂͜͡☬➣ " + key + "Infomem「angka」\n" + \
                  "╠❂͜͡☬➣ " + key + "Lurking「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Lurkers\n" + \
                  "╠❂͜͡☬➣ " + key + "Sider「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Uppro\n" + \
                  "╠❂͜͡☬➣ " + key + "Updategrup\n" + \
                  "╠❂͜͡☬➣ " + key + "Upbot\n" + \
                  "╠❂͜͡☬➣ " + key + "Broadcast:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Setkey「New Key」\n" + \
                  "╠❂͜͡☬➣ " + key + "Mykey\n" + \
                  "╠❂͜͡☬➣ " + key + "Resetkey\n" + \
                  "╠══════════════════╗" + "\n" + \
                  "╠    BY: SELFBOT-BY:MAX" + "\n" + \
                  "╚══════════════════╝" 
    return helpMessage

def help1():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╔══════════════════╗" + "\n" + \
                  "╠          🤖 Hiburan 🤖" + "\n" + \
                  "╠══════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Musik:「Judul Lagu」\n" + \
                  "╠❂͜͡☬➣ " + key + "Musik2:「Judul Lagu」\n" + \
                  "╠❂͜͡☬➣ " + key + "Playlist「Nama Penyanyi」\n" + \
                  "╠❂͜͡☬➣ " + key + "Ytmp3:「Judul Lagu」\n" + \
                  "╠❂͜͡☬➣ " + key + "Ytmp4:「Judul Video\n" + \
                  "╠❂͜͡☬➣ " + key + "Meme@Nama@Teks1@Teks2\n" + \
                  "╠❂͜͡☬➣ " + key + "1cak\n" + \
                  "╠❂͜͡☬➣ " + key + "Profilesmule:「ID Smule」\n" + \
                  "╠❂͜͡☬➣ " + key + "Randomnumber:「Nmor-Nmor」\n" + \
                  "╠❂͜͡☬➣ " + key + "Gimage:「Keyword」\n" + \
                  "╠❂͜͡☬➣ " + key + "Img food:「Nama Makanan」\n" + \
                  "╠❂͜͡☬➣ " + key + "Cekig:「ID IG」\n" + \
                  "╠❂͜͡☬➣ " + key + "Profileig:「Nama IG」\n" + \
                  "╠❂͜͡☬➣ " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spamtag:「jumlahnya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spamtag「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spamcall:「jumlahnya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spamcall\n" + \
                  "╠══════════════════╗" + "\n" + \
                  "╠    BY: SELFBOT-BY:MAX " + "\n" + \
                  "╚══════════════════╝" 
    return helpMessage1

def help2():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╔══════════════════╗" + "\n" + \
                  "╠          🤖 Protect 🤖" + "\n" + \
                  "╠══════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Pro「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Notag「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Allpro「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Protecturl「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Protectjoin「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Protectkick「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Protectcancel「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Protectinvite「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Blockjs「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Js\n" + \
                  "╠══════════════════╗" + "\n" + \
                  "╠          🤖 Settings 🤖" + "\n" + \
                  "╠══════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Unsend「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Jointicket「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Sticker「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Respon「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Respongift「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Contact「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Autojoin「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Autoadd「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Welcome「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Simi「on/off」\n" + \
                  "╠❂͜͡☬➣ " + key + "Autoleave「on/off」\n" + \
                  "╠══════════════════╗" + "\n" + \
                  "╠           🤖 Admin 🤖" + "\n" + \
                  "╠══════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Admin:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Admin:delete\n" + \
                  "╠❂͜͡☬➣ " + key + "Staff:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Staff:delete\n" + \
                  "╠❂͜͡☬➣ " + key + "Bot:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Bot:delete\n" + \
                  "╠❂͜͡☬➣ " + key + "Adminadd「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Admindell「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Staffadd「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Staffdell「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Botadd「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Botdell「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Refresh\n" + \
                  "╠❂͜͡☬➣ " + key + "Listbot\n" + \
                  "╠❂͜͡☬➣ " + key + "Listadmin\n" + \
                  "╠❂͜͡☬➣ " + key + "Listprotect\n" + \
                  "╠❂͜͡☬➣ Ketik「 Refresh 」Jika Sudah\n╠❂͜͡☬➣ Menggunakan Command Diatas...\n" + \
                  "╠══════════════════╗" + "\n" + \
                  "╠    BY: SELFBOT-BY:MAX" + "\n" + \
                  "╚══════════════════╝" 
    return helpMessage2
    
  
def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "╔══════════════════╗" + "\n" + \
                  "╠  🤖 SELFBOT-BY:MAX 🤖" + "\n" + \
                  "╚══════════════════╝" + "\n" + \
                  "╔══════════════════╗" + "\n" + \
                  "╠             🤖 BOT 🤖" + "\n" + \
                  "╠══════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Mytoken\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek sider\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek spam\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek pesan\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek respon\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek welcome\n" + \
                  "╠❂͜͡☬➣ " + key + "Cek leave\n" + \
                  "╠❂͜͡☬➣ " + key + "Set sider:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set spam:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set pesan:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set respon:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set welcome:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Set leave:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Myname:「Nama」\n" + \
                  "╠❂͜͡☬➣ " + key + "Bot1name:「Nama」\n" + \
                  "╠❂͜͡☬➣ " + key + "Bot2name:「Nama」\n" + \
                  "╠❂͜͡☬➣ " + key + "Bot1up「Kirim fotonya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Bot2up「Kirim fotonya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spam:「Mid korban」「Jumlah」\n" + \
				  "╠❂͜͡☬➣ " + key + "Spamtag:「jumlahnya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spamtag「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spamcall:「jumlahnya」\n" + \
                  "╠❂͜͡☬➣ " + key + "Spamcall\n" + \
				  "╠❂͜͡☬➣ " + key + "Uppro\n" + \
                  "╠❂͜͡☬➣ " + key + "Updategrup\n" + \
                  "╠❂͜͡☬➣ " + key + "Upbot\n" + \
                  "╠❂͜͡☬➣ " + key + "Broadcast:「Text」\n" + \
                  "╠❂͜͡☬➣ " + key + "Setkey「New Key」\n" + \
                  "╠❂͜͡☬➣ " + key + "Mykey\n" + \
                  "╠❂͜͡☬➣ " + key + "Resetkey\n" + \
				  "╠❂͜͡☬➣ " + key + "Self「on/off」\n" + \
				  "╠❂͜͡☬➣ " + key + "Hapus chat\n" + \
                  "╠❂͜͡☬➣ " + key + "Remove chat\n" + \
				  "╠❂͜͡☬➣ " + key + "Leave:「Namagrup」\n" + \
                  "╠══════════════════╗" + "\n" + \
                  "╠          🤖 Blacklist 🤖" + "\n" + \
                  "╠══════════════════╝" + "\n" + \
                  "╠❂͜͡☬➣ " + key + "Blc\n" + \
                  "╠❂͜͡☬➣ " + key + "Ban:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Unban:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Ban「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Unban「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Talkban「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Untalkban「@」\n" + \
                  "╠❂͜͡☬➣ " + key + "Talkban:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Untalkban:on\n" + \
                  "╠❂͜͡☬➣ " + key + "Banlist\n" + \
                  "╠❂͜͡☬➣ " + key + "Talkbanlist\n" + \
                  "╠❂͜͡☬➣ " + key + "Clearban\n" + \
                  "╠❂͜͡☬➣ " + key + "Refresh\n" + \
                  "╠══════════════════╗" + "\n" + \
                  "╠    BY: SELFBOT-BY:MAX" + "\n" + \
                  "╚══════════════════╝"
    return helpMessage3
    
def infomeme():
    helpMessage4 = """
╔══════════════════╗
╠  🤖 SELFBOT-BY:MAX 🤖
╚══════════════════╝
╔══════════════════╗
╠    ◄]·✪·List Meme·✪·[►
╠══════════════════╝
╠❂͜͡☬➣ Buzz
╠❂͜͡☬➣ Spongebob
╠❂͜͡☬➣ Patrick
╠❂͜͡☬➣ Doge
╠❂͜͡☬➣ Joker
╠❂͜͡☬➣ Xzibit
╠❂͜͡☬➣ You_tried
╠❂͜͡☬➣ cb
╠❂͜͡☬➣ blb
╠❂͜͡☬➣ wonka
╠❂͜͡☬➣ keanu
╠❂͜͡☬➣ cryingfloor
╠❂͜͡☬➣ disastergirl
╠❂͜͡☬➣ facepalm
╠❂͜͡☬➣ fwp
╠❂͜͡☬➣ grumpycat
╠❂͜͡☬➣ captain
╠❂͜͡☬➣ mmm
╠❂͜͡☬➣ rollsafe
╠❂͜͡☬➣ sad-obama
╠❂͜͡☬➣ sad-clinton
╠❂͜͡☬➣ aag
╠❂͜͡☬➣ sarcasticbear
╠❂͜͡☬➣ sk
╠❂͜͡☬➣ sparta
╠❂͜͡☬➣ sad
╠❂͜͡☬➣ contoh:
╠❂͜͡☬➣ Meme@buzz@lu tau?@gatau
╠══════════════════╗
╠    BY: SELFBOT-BY:MAX
╚══════════════════╝
"""
    return helpMessage4

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return

        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait['leaveRoom'] == True:
                ptatan1983.leaveRoom(op.param1)
                k1.leaveRoom(op.param1)
                k2.leaveRoom(op.param1)
                k3.leaveRoom(op.param1)
                k4.leaveRoom(op.param1)  
                k5.leaveRoom(op.param1)
                k6.leaveRoom(op.param1)
                k7.leaveRoom(op.param1)
                k8.leaveRoom(op.param1)
                k9.leaveRoom(op.param1)
                k10.leaveRoom(op.param1)   
        if op.type == 24:
            if wait['leaveRoom'] == True:
                ptatan1983.leaveRoom(op.param1)
                k1.leaveRoom(op.param1)
                k2.leaveRoom(op.param1)
                k3.leaveRoom(op.param1)
                k4.leaveRoom(op.param1)  
                k5.leaveRoom(op.param1)
                k6.leaveRoom(op.param1)
                k7.leaveRoom(op.param1)
                k8.leaveRoom(op.param1)
                k9.leaveRoom(op.param1)
                k10.leaveRoom(op.param1)        
                
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if boy.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            ptatan1983.reissueGroupTicket(op.param1)
                            X = ptatan1983.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            ptatan1983.updateGroup(X)
                            ptatan1983.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if k1.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                k1.reissueGroupTicket(op.param1)
                                X = k1.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                k1.updateGroup(X)
                                k1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if k2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    k2.reissueGroupTicket(op.param1)
                                    X = k2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    k2.updateGroup(X)
                                    k2.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if k3.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        k3.reissueGroupTicket(op.param1)
                                        X = k3.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        k3.updateGroup(X)
                                        k3.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if k4.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            k4.reissueGroupTicket(op.param1)
                                            X = k4.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            k4.updateGroup(X)
                                            k4.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if k5.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                k5.reissueGroupTicket(op.param1)
                                                X = k5.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                k5.updateGroup(X)
                                                k5.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if k6.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            k6.reissueGroupTicket(op.param1)
                            X = k6.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            k6.updateGroup(X)
                            k6.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if k7.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                k7.reissueGroupTicket(op.param1)
                                X = k7.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                k7.updateGroup(X)
                                k7.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if k8.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    k8.reissueGroupTicket(op.param1)
                                    X = k8.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    k8.updateGroup(X)
                                    k8.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if k9.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        k9.reissueGroupTicket(op.param1)
                                        X = k9.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        k9.updateGroup(X)
                                        k9.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if k10.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            k10.reissueGroupTicket(op.param1)
                                            X = k10.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            k10.updateGroup(X)
                                            k10.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if sw.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                sw.reissueGroupTicket(op.param1)
                                                X = sw.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                sw.updateGroup(X)
                                                sw.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                         pass
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        ptatan1983.sendText(op.param1, wait["message"])
                        ptatan1983.blockContact(op.param1)
                          
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ptatan1983.acceptGroupInvitation(op.param1)
                        ginfo = ptatan1983.getGroup(op.param1)
                        ptatan1983.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ptatan1983.leaveGroup(op.param1)
                    else:
                        ptatan1983.acceptGroupInvitation(op.param1)
                        ginfo = ptatan1983.getGroup(op.param1)
                        ptatan1983.sendMessage(op.param1,"Hai " + str(ginfo.name))
                        
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ptatan1983.acceptGroupInvitation(op.param1)                     
                        ginfo = ptatan1983.getGroup(op.param1)
                        ptatan1983.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        ptatan1983.acceptGroupInvitation(op.param1)
                        ginfo = ptatan1983.getGroup(op.param1)
                        ptatan1983.sendMessage(op.param1,"Haii " + str(ginfo.name))
        if op.type == 13:
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k1.acceptGroupInvitation(op.param1)
                        ginfo = k1.getGroup(op.param1)
                        k1.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        k1.leaveGroup(op.param1)
                    else:
                        k1.acceptGroupInvitation(op.param1)
                        ginfo = k1.getGroup(op.param1)
                        k1.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k2.acceptGroupInvitation(op.param1)
                        ginfo = k2.getGroup(op.param1)
                        k2.sendMessage(op.param1,"Selamat Tinggal\nGroup " +str(ginfo.name))
                        k2.leaveGroup(op.param1)
                    else:
                        k2.acceptGroupInvitation(op.param1)
                        ginfo = k2.getGroup(op.param1)
                        k2.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k3.acceptGroupInvitation(op.param1)
                        ginfo = k3.getGroup(op.param1)
                        k3.sendMessage(op.param1,"Selamat Tinggal\nGroup " +str(ginfo.name))
                        k3.leaveGroup(op.param1)
                    else:
                        k3.acceptGroupInvitation(op.param1)
                        ginfo = k3.getGroup(op.param1)
                        k3.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k4.acceptGroupInvitation(op.param1)
                        ginfo = k4.getGroup(op.param1)
                        k4.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        k4.acceptGroupInvitation(op.param1)
                        ginfo = k4.getGroup(op.param1)
                        k4.sendMessage(op.param1,"Haii " + str(ginfo.name))
        if op.type == 13:
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k5.acceptGroupInvitation(op.param1)
                        ginfo = k5.getGroup(op.param1)
                        k5.sendMessage(op.param1,"Selamat Tinggal\nGroup " +str(ginfo.name))
                        k5.leaveGroup(op.param1)
                    else:
                        k5.acceptGroupInvitation(op.param1)
                        ginfo = k5.getGroup(op.param1)
                        k5.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k6.acceptGroupInvitation(op.param1)
                        ginfo = k6.getGroup(op.param1)
                        k6.sendMessage(op.param1,"Selamat Tinggal\nGroup " +str(ginfo.name))
                        k6.leaveGroup(op.param1)
                    else:
                        k6.acceptGroupInvitation(op.param1)
                        ginfo = k6.getGroup(op.param1)
                        k6.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k7.acceptGroupInvitation(op.param1)
                        ginfo = k7.getGroup(op.param1)
                        k7.sendMessage(op.param1,"Selamat Tinggal\nGroup " +str(ginfo.name))
                        k7.leaveGroup(op.param1)
                    else:
                        k7.acceptGroupInvitation(op.param1)
                        ginfo = k7.getGroup(op.param1)
                        k7.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k8.acceptGroupInvitation(op.param1)
                        ginfo = k8.getGroup(op.param1)
                        k8.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        k8.acceptGroupInvitation(op.param1)
                        ginfo = k8.getGroup(op.param1)
                        k8.sendMessage(op.param1,"Haii " + str(ginfo.name))
        if op.type == 13:
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k9.acceptGroupInvitation(op.param1)
                        ginfo = k9.getGroup(op.param1)
                        k9.sendMessage(op.param1,"Selamat Tinggal\nGroup " +str(ginfo.name))
                        k9.leaveGroup(op.param1)
                    else:
                        k9.acceptGroupInvitation(op.param1)
                        ginfo = k9.getGroup(op.param1)
                        k9.sendMessage(op.param1,"Hai " + str(ginfo.name))
        if op.type == 13:
            if Jmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k10.acceptGroupInvitation(op.param1)
                        ginfo = k10.getGroup(op.param1)
                        k10.sendMessage(op.param1,"Selamat Tinggal\nGroup " +str(ginfo.name))
                        k10.leaveGroup(op.param1)
                    else:
                        k10.acceptGroupInvitation(op.param1)
                        ginfo = k10.getGroup(op.param1)
                        k10.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = ptatan1983.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            boy.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = k1.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                k1.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = k2.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    k2.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = k3.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        k3.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = k4.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            k4.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = k5.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                k5.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = k6.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    k6.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = k7.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        k7.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = k8.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            k8.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = k9.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                k9.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = k10.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    k10.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = k1.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        k1.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    k1.findAndAddContactsByMid(op.param3)
                    k1.inviteIntoGroup(op.param1,[op.param3])
                    ptatan1983.acceptGroupInvitation(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k1.findAndAddContactsByMid(op.param3)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        ptatan1983.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if Amid in op.param3:
                if op.param2 in Bots:
                    k2.findAndAddContactsByMid(op.param3)
                    k2.inviteIntoGroup(op.param1,[op.param3])
                    k1.acceptGroupInvitation(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k2.findAndAddContactsByMid(op.param3)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if Bmid in op.param3:
                if op.param2 in Bots:
                    k3.findAndAddContactsByMid(op.param3)
                    k3.inviteIntoGroup(op.param1,[op.param3])
                    k2.acceptGroupInvitation(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k3.findAndAddContactsByMid(op.param3)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k3.inviteIntoGroup(op.param1,[op.param3])
                        k2.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if Cmid in op.param3:
                if op.param2 in Bots:
                    k4.findAndAddContactsByMid(op.param3)
                    k4.inviteIntoGroup(op.param1,[op.param3])
                    k3.acceptGroupInvitation(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k4.findAndAddContactsByMid(op.param3)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k4.inviteIntoGroup(op.param1,[op.param3])
                        k3.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if Dmid in op.param3:
                if op.param2 in Bots:
                    k5.findAndAddContactsByMid(op.param3)
                    k5.inviteIntoGroup(op.param1,[op.param3])
                    k4.acceptGroupInvitation(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k5.findAndAddContactsByMid(op.param3)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k5.inviteIntoGroup(op.param1,[op.param3])
                        k4.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if Emid in op.param3:
                if op.param2 in Bots:
                    k6.findAndAddContactsByMid(op.param3)
                    k6.inviteIntoGroup(op.param1,[op.param3])
                    k5.acceptGroupInvitation(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k6.findAndAddContactsByMid(op.param3)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k6.inviteIntoGroup(op.param1,[op.param3])
                        k5.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if Fmid in op.param3:
                if op.param2 in Bots:
                    k7.findAndAddContactsByMid(op.param3)
                    k7.inviteIntoGroup(op.param1,[op.param3])
                    k1.acceptGroupInvitation(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k7.findAndAddContactsByMid(op.param3)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k7.inviteIntoGroup(op.param1,[op.param3])
                        k6.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if Gmid in op.param3:
                if op.param2 in Bots:
                    k10.findAndAddContactsByMid(op.param3)
                    k10.inviteIntoGroup(op.param1,[op.param3])
                    k7.acceptGroupInvitation(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k10.findAndAddContactsByMid(op.param3)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k10.inviteIntoGroup(op.param1,[op.param3])
                        k7.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if Hmid in op.param3:
                if op.param2 in Bots:
                    k7.findAndAddContactsByMid(op.param3)
                    k7.inviteIntoGroup(op.param1,[op.param3])
                    k8.acceptGroupInvitation(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k7.findAndAddContactsByMid(op.param3)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k7.inviteIntoGroup(op.param1,[op.param3])
                        k8.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if Imid in op.param3:
                if op.param2 in Bots:
                    k8.findAndAddContactsByMid(op.param3)
                    k8.inviteIntoGroup(op.param1,[op.param3])
                    k9.acceptGroupInvitation(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k8.findAndAddContactsByMid(op.param3)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k8.inviteIntoGroup(op.param1,[op.param3])
                        k9.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if Jmid in op.param3:
                if op.param2 in Bots:
                    k9.findAndAddContactsByMid(op.param3)
                    k9.inviteIntoGroup(op.param1,[op.param3])
                    k10.acceptGroupInvitation(op.param1)
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k9.findAndAddContactsByMid(op.param3)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k9.inviteIntoGroup(op.param1,[op.param3])
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        pass
        if op.type == 19:
            if op.param2 in Bots:
            	pass
            else:
              try:
                 if op.param1 in protectkick:
                     wait["blacklist"][op.param2] = True
                     G = random.choice(ABC).getGroup(op.param1)
                     random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                     k1.findAndAddContactsByMid(op.param3)
                     k1.inviteIntoGroup(op.param1,[op.param3])
                 else:
                   pass
              except:
                try:
                    G = random.choice(ABC).getGroup(op.param1)
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    k2.findAndAddContactsByMid(op.param3)
                    k2.inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
                except:
                    pass

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = ptatan1983.getGroup(op.param1)
                contact = ptatan1983.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                ptatan1983.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = ptatan1983.getGroup(op.param1)
                contact = ptatan1983.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                ptatan1983.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	k5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	k10.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k9.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	k6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k5.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        ptatan1983.sendText(op.param1, wait["message"])
                        ptatan1983.blockContact(op.param1)
#===========KICK============#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 11:
            if op.param1 in protectqr:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
#===========Accepet===========#
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Bots:
                    ptatan1983.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Bots:
                    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Bots:
                    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Bots:
                    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Bots:
                    k4.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Bots:
                    k5.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Bots:
                    k6.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Bots:
                    k7.acceptGroupInvitation(op.param1)                    
            if op.param3 in Hmid:
                if op.param2 in Bots:
                    k8.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Bots:
                    k9.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
                if op.param2 in Bots:
                    k10.acceptGroupInvitation(op.param1)

#--------------------------------------------------------
            if op.param3 in mid:
                            if op.param2 in Amid:
                                ptatan1983.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Bmid:
		                ptatan1983.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Cmid:
		                ptatan1983.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Dmid:
		                ptatan1983.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Emid:
		                ptatan1983.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Fmid:
		                ptatan1983.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Gmid:
		                ptatan1983.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Hmid:
		                ptatan1983.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Imid:
		                ptatan1983.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		            if op.param2 in Jmid:
		                ptatan1983.acceptGroupInvitation(op.param1)

#--------------------------------------------------------
            if op.param3 in Amid:
                            if op.param2 in Dmid:
                                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Bmid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Cmid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Dmid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Emid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Fmid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Gmid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Hmid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Imid:
		                k1.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		            if op.param2 in Jmid:
		                k1.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Bmid:
                            if op.param2 in Fmid:
                                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Emid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Cmid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Dmid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Emid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Fmid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Gmid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Hmid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Imid:
		                k2.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		            if op.param2 in Jmid:
		                k2.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Cmid:
                            if op.param2 in Dmid:
                                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Bmid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Amid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Dmid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Emid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Fmid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Gmid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Hmid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Imid:
		                k3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		            if op.param2 in Jmid:
		                k3.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Dmid:
                            if op.param2 in Fmid:
                                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Bmid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Cmid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Amid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Emid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Fmid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Gmid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Hmid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Imid:
		                k4.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		            if op.param2 in Jmid:
		                k4.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Emid:
                            if op.param2 in Bmid:
                                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Bmid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Cmid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Dmid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Amid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Fmid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Gmid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Hmid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Imid:
		                k5.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
		            if op.param2 in Jmid:
		                k5.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Fmid:
                            if op.param2 in Fmid:
                                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Bmid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Cmid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Dmid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Emid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Jmid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Gmid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Hmid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Imid:
		                k6.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
		            if op.param2 in Jmid:
		                k6.acceptGroupInvitation(op.param1)
#-------------------------------------------------------- 
            if op.param3 in Gmid:
                            if op.param2 in Fmid:
                                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Bmid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Cmid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Dmid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Emid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Jmid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Jmid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Hmid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Imid:
		                k7.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
		            if op.param2 in Jmid:
		                k7.acceptGroupInvitation(op.param1)               
#--------------------------------------------------------
            if op.param3 in Hmid:
                            if op.param2 in Fmid:
                                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Bmid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Cmid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Dmid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Emid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Fmid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Gmid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Bmid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Imid:
		                k8.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
		            if op.param2 in Jmid:
		                k8.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Imid:
                            if op.param2 in Gmid:
                                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Bmid:
		                kI.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Cmid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Dmid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Emid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Fmid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Gmid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Hmid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Dmid:
		                k9.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
		            if op.param2 in Jmid:
		                k9.acceptGroupInvitation(op.param1)
#___________batas ____________
            if op.param3 in Jmid:
                            if op.param2 in Imid:
                                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Bmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Cmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Dmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Emid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Fmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Gmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Hmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Dmid:
		                k10.acceptGroupInvitation(op.param1)
            if op.param3 in Jmid:
		            if op.param2 in Amid:
		                k10.acceptGroupInvitation(op.param1)

#===========Cancel============#
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "「 Detail Postingan 」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = boy.getContact(sender)
                                auth = "\n• Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n• Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n• Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n• Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n• Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            boy.sendMessage(to, str(ret_))
                            channel.like(url[25:58], url[66:], likeType=1006)
                            channel.comment(url[25:58], url[66:], wait["message"])

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = random.choice(ABC).getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        random.choice(ABC).updateGroup(G)
                        invsend = 0
                        Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        X = random.choice(ABC).getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        random.choice(ABC).updateGroup(X)
            except:
                pass
       
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.prevenJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        boy.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.prevenJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        boy.inviteIntoGroup(op.param1,[Zmid])
                        boy.inviteIntoGroup(op.param1,[admin])
                    else:
                       pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param3)
                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                        random.choice(ABC).sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param3)
                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                        random.choice(ABC).sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).findAndAddContactsByMid(op.param3)
                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                            random.choice(ABC).sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass

#___________________________________________________
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = boy.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = boy.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            boy.sendMessage(msg.to, "「Awas kikil boss... hpus daftar bl dulu baru invite lagi boss」")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                            try:
                                boy.findAndAddContactsByMid(target)
                                boy.inviteIntoGroup(msg.to,[target])
                                fira = boy.getContact(target)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Sukses Invite 」\nNama "
                                ret_ = "「Ketik Invite off jika sudah done」"
                                fa = str(fira.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':fira.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boy.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                wait["invite"] = False
                                break
                            except:
                                boy.sendText(msg.to,"Limit boss")
                                wait["invite"] = False
                                break

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["invite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = boy.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            boy.sendText(msg.to, _name + "sᴜᴅᴀʜ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                boy.findAndAddContactsByMid(target)
                                boy.inviteIntoGroup(msg.to,[target])
                                boy.sendText(msg.to,"Invite " + _name)
                                wait["invite"] = False
                                break                              
                            except:             
                                    boy.sendText(msg.to,"ᴇʀʀᴏʀ")
                                    wait["invite"] = False
                                    break
#_______________________________________ __________
        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.inviteIntoGroup(op.param1,[Zmid])
                            sw.acceptGroupInvitation(op.param1)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.inviteIntoGroup(op.param1,[Zmid])
                                sw.acceptGroupInvitation(op.param1)
                                sw.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    k3.inviteIntoGroup(op.param1,[Zmid])
                                    sw.acceptGroupInvitation(op.param1)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[Zmid])
                                        sw.acceptGroupInvitation(op.param1)
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                            k6.inviteIntoGroup(op.param1,[Zmid])
                                            sw.acceptGroupInvitation(op.param1)
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                boy.kickoutFromGroup(op.param1,[op.param2])
                                                boy.inviteIntoGroup(op.param1,[Zmid])
                                                sw.acceptGroupInvitation(op.param1)
                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            k1.findAndAddContactsByMid(op.param1,[Zmid])
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.inviteIntoGroup(op.param1,[Zmid])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k2.findAndAddContactsByMid(op.param1,[Zmid])
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.inviteIntoGroup(op.param1,[Zmid])
                        except:
                            pass
                return

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            k5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                boy.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            k5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k6.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k7.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        boy.acceptGroupInvitation(op.param1)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            G = random.choice(ABC).getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            random.choice(ABC).updateGroup(G)
                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                            boy.acceptGroupInvitationByTicket(op.param1,Ticket)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            G = random.choice(ABC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).updateGroup(G)
                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                        except:
                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        boy.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                        boy.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            G = random.choice(ABC).getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            random.choice(ABC).updateGroup(G)
                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            G = random.choice(ABC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).updateGroup(G)
                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                        except:
                            pass
                return


        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        boy.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            boy.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.inviteIntoGroup(op.param1,[op.param3])
                                boy.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                    boy.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                        k1.inviteIntoGroup(op.param1,[op.param3])
                                        boy.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k2.inviteIntoGroup(op.param1,[op.param3])
                                            boy.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
        if op.type == 19:
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.inviteIntoGroup(op.param1,[op.param3])
                                k1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k2.inviteIntoGroup(op.param1,[op.param3])
                                        k1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                            k1.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
        if op.type == 19:
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        k3.inviteIntoGroup(op.param1,[op.param3])
                        k2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k4.kickoutFromGroup(op.param1,[op.param2])
                            k4.inviteIntoGroup(op.param1,[op.param3])
                            k2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.inviteIntoGroup(op.param1,[op.param3])
                                k2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                        k2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                            k2.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
        if op.type == 19:
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k4.kickoutFromGroup(op.param1,[op.param2])
                        k4.inviteIntoGroup(op.param1,[op.param3])
                        k3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k5.kickoutFromGroup(op.param1,[op.param2])
                            k5.inviteIntoGroup(op.param1,[op.param3])
                            k3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k6.kickoutFromGroup(op.param1,[op.param2])
                                k6.inviteIntoGroup(op.param1,[op.param3])
                                k3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[op.param3])
                                        k3.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.inviteIntoGroup(op.param1,[op.param3])
                                            k3.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
        if op.type == 19: 
           if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k6.kickoutFromGroup(op.param1,[op.param2])
                        k6.inviteIntoGroup(op.param1,[op.param3])
                        k4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.inviteIntoGroup(op.param1,[op.param3])
                            k4.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                                k8.inviteIntoGroup(op.param1,[op.param3])
                                k4.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                        k5.inviteIntoGroup(op.param1,[op.param3])
                                        k4.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                            k6.inviteIntoGroup(op.param1,[op.param3])
                                            k4.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
        if op.type == 19:
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k6.kickoutFromGroup(op.param1,[op.param2])
                        k6.inviteIntoGroup(op.param1,[op.param3])
                        k5.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.inviteIntoGroup(op.param1,[op.param3])
                            k5.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                                k8.inviteIntoGroup(op.param1,[op.param3])
                                k5.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k6.kickoutFromGroup(op.param1,[op.param2])
                                        k6.inviteIntoGroup(op.param1,[op.param3])
                                        k5.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k7.kickoutFromGroup(op.param1,[op.param2])
                                            k7.inviteIntoGroup(op.param1,[op.param3])
                                            k5.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
        if op.type == 19:
            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k7.kickoutFromGroup(op.param1,[op.param2])
                        k7.inviteIntoGroup(op.param1,[op.param3])
                        k6.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k8.kickoutFromGroup(op.param1,[op.param2])
                            k8.inviteIntoGroup(op.param1,[op.param3])
                            k6.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k9.kickoutFromGroup(op.param1,[op.param2])
                                k9.inviteIntoGroup(op.param1,[op.param3])
                                k6.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                        k6.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.inviteIntoGroup(op.param1,[op.param3])
                                            k6.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
        if op.type == 19:
            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.inviteIntoGroup(op.param1,[op.param3])
                        k7.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            k9.inviteIntoGroup(op.param1,[op.param3])
                            k7.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                                k8.inviteIntoGroup(op.param1,[op.param3])
                                k7.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k10.kickoutFromGroup(op.param1,[op.param2])
                                        k10.inviteIntoGroup(op.param1,[op.param3])
                                        k7.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                            k9.inviteIntoGroup(op.param1,[op.param3])
                                            k7.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
        if op.type == 19:
            if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        k8.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            k8.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.inviteIntoGroup(op.param1,[op.param3])
                                k8.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                        k1.inviteIntoGroup(op.param1,[op.param3])
                                        k8.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k2.inviteIntoGroup(op.param1,[op.param3])
                                            k8.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
        if op.type == 19:
            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k9.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k9.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.inviteIntoGroup(op.param1,[op.param3])
                                k9.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k2.inviteIntoGroup(op.param1,[op.param3])
                                        k9.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                            k9.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
        if op.type == 19:
            if Jmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.inviteIntoGroup(op.param1,[op.param3])
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                    boy.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k2.inviteIntoGroup(op.param1,[op.param3])
                                        k10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                            k10.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
        if op.type == 19:
            if Zmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        sw.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            sw.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.inviteIntoGroup(op.param1,[op.param3])
                                sw.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                    boy.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = random.choice(ABC).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(ABC).updateGroup(G)
                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k2.inviteIntoGroup(op.param1,[op.param3])
                                        sw.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                            sw.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if op.param3 in admin: #Kalo Admin ke Kick
              if op.param2 in Bots:
                pass
              if op.param2 in admin:
                pass
              else:
                  random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                  boy.inviteIntoGroup(op.param1,[op.param3])                
            if op.param3 in Zmid: #Akun Utama Ke Kick
                G = random.choice(ABC).getGroup(op.param1)
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(ABC).updateGroup(G)
                Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                boy.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                random.choice(ABC).updateGroup(G)
                random.choice(ABC).updateGroup(G)
                wait["blacklist"][op.param2] = True

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        boy.findAndAddContactsByMid(op.param1,admin)
                        boy.inviteIntoGroup(op.param1,admin)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k1.findAndAddContactsByMid(op.param1,admin)
                            k1.inviteIntoGroup(op.param1,admin)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                k2.findAndAddContactsByMid(op.param1,admin)
                                k2.inviteIntoGroup(op.param1,admin)
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return
            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k4.findAndAddContactsByMid(op.param1,admin)
                        k4.inviteIntoGroup(op.param1,admin)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k5.findAndAddContactsByMid(op.param1,admin)
                            k5.inviteIntoGroup(op.param1,admin)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                k6.findAndAddContactsByMid(op.param1,admin)
                                k6.inviteIntoGroup(op.param1,admin)
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return
            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k7.findAndAddContactsByMid(op.param1,admin)
                        k7.inviteIntoGroup(op.param1,admin)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k8.findAndAddContactsByMid(op.param1,admin)
                            k8.inviteIntoGroup(op.param1,admin)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                k9.findAndAddContactsByMid(op.param1,admin)
                                k9.inviteIntoGroup(op.param1,admin)
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k4.findAndAddContactsByMid(op.param1,staff)
                        k4.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            k3.findAndAddContactsByMid(op.param1,staff)
                            k3.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                k2.findAndAddContactsByMid(op.param1,staff)
                                k2.inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return
            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k6.findAndAddContactsByMid(op.param1,staff)
                        k6.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            k5.findAndAddContactsByMid(op.param1,staff)
                            k5.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                k1.findAndAddContactsByMid(op.param1,staff)
                                k1.inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return
            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        k10.findAndAddContactsByMid(op.param1,staff)
                        k10.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            k9.findAndAddContactsByMid(op.param1,staff)
                            k9.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                k8.findAndAddContactsByMid(op.param1,staff)
                                k8.inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["AFreadPoint"]:
                   if op.param2 in Setmain["AFreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["AFreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = boy.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = boy.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        boy.sendImageWithURL(op.param1, image)                        
                        
                    
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = boy.getGroup(at)
                                Boy = boy.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 UNSEND MESSAGE 」\n❂➣ Pengirim : "
                                ret_ = "❂➣ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n❂➣ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n❂➣ BY: SELFBOT-BY:MAX"
                                ry = str(Boy.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Boy.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boy.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                boy.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = boy.getGroup(at)
                                Boy = boy.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 UNSEND MESSAGE 」\n"
                                ret_ += "❂➣ Pengirim : {}".format(str(Boy.displayName))
                                ret_ += "\n❂➣ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n❂➣ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n❂➣Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n❂➣ BY: SELFBOT-BY:MAX"
                                boy.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = boy.getGroup(at)
                                Boy = boy.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "❂➣ Pengirim : {}".format(str(Boy.displayName))
                                ret_ += "\n❂➣ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n❂➣ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n❂➣ BY: SELFBOT-BY:MAX"
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                boy.sendMessage(at, str(ret_))
                                boy.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message                    
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://corrykalam.pw/api/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               boy.sendMessage(msg.to, str(data["answer"])) 
                   except Exception as error:
                       pass
                   
               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                           
                           
               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translateth:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='th')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass
                   
               if msg.to in translatetw:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='zh-tw')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translatear:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='ar')
                           A = hasil.text
                           boy.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                    


        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   contact = boy.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           boy.sendMessage(msg.to, wait["Respontag"])
                           boy.sendImageWithURL(msg.to,image)
                           boy.sendMessage(msg.to, None, contentMetadata={"STKID":"51626504","STKPKGID":"11538","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           boy.sendMessage(msg.to, "Yang suka ngetag minta di gift yaa!?\nCek di chat, udah aku gift tuh...")
                           boy.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           boy.sendMessage(msg.to, "Jangan tag saya....")
                           boy.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,"「Cek ID Sticker」\n🐚 STKID : " + msg.contentMetadata["STKID"] + "\n⏩ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n⏩ STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = boy.getContact(msg.contentMetadata["mid"])
                        path = boy.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        boy.sendMessage(msg.to,"🤖 Nama : " + msg.contentMetadata["displayName"] + "\n🤖 MID : " + msg.contentMetadata["mid"] + "\n🤖 Status : " + contact.statusMessage + "\n🤖 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        boy.sendImageWithURL(msg.to, image)


        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = boy.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n❂➣ Sticker ID : {}".format(stk_id)
                   ret_ += "\n❂➣ Sticker Version : {}".format(stk_ver)
                   ret_ += "\n❂➣ Sticker Package : {}".format(pkg_id)
                   ret_ += "\n❂➣ Sticker Url : line://shop/detail/{}".format(pkg_id)
                   ret_ += "\n❂➣ By @Boy-FirA™️"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = boy.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                                                      
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    boy.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = boy.getContact(msg.contentMetadata["mid"])
                        path = boy.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        boy.sendMessage(msg.to,"❂➣ Nama : " + msg.contentMetadata["displayName"] + "\n❂➣ MID : " + msg.contentMetadata["mid"] + "\n❂➣ Status : " + contact.statusMessage + "\n❂➣ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        boy.sendImageWithURL(msg.to, image)
#===========ADD BOT============#
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        boy.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        boy.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        boy.sendMessage(msg.to,"Contact itu bukan anggota Boy-FirA™️ BOT")
#===========ADD STAFF============#
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        boy.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        boy.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        boy.sendMessage(msg.to,"Contact itu bukan staff")
#===========ADD ADMIN============#
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        boy.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        boy.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        boy.sendMessage(msg.to,"Contact itu bukan admin")
#===========ADD BLACKLIST============#
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        boy.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        boy.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        boy.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#===========TALKBAN============#
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        boy.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        boy.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        boy.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        boy.sendMessage(msg.to,"Contact itu tidak ada di Talkban")


#===========UPDATE FOTO============#
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = boy.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            boy.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = boy.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     boy.updateGroupPicture(msg.to, path)
                     boy.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["AFfoto"]:
                            path = boy.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][mid]
                            boy.updateProfilePicture(path)
                            boy.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["AFfoto"]:
                            path = k1.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Amid]
                            k1.updateProfilePicture(path)
                            k1.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["AFfoto"]:
                            path = k2.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Bmid]
                            k2.updateProfilePicture(path)
                            k2.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["AFfoto"]:
                            path = k3.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Cmid]
                            k3.updateProfilePicture(path)
                            k3.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["AFfoto"]:
                            path = k4.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Dmid]
                            k4.updateProfilePicture(path)
                            k4.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["AFfoto"]:
                            path = k5.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Emid]
                            k5.updateProfilePicture(path)
                            k5.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Fmid in Setmain["AFfoto"]:
                            path = k6.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Fmid]
                            k6.updateProfilePicture(path)
                            k6.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Gmid in Setmain["AFfoto"]:
                            path = k7.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Gmid]
                            k7.updateProfilePicture(path)
                            k7.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Hmid in Setmain["AFfoto"]:
                            path = k8.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Hmid]
                            k8.updateProfilePicture(path)
                            k8.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Imid in Setmain["AFfoto"]:
                            path = k9.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Imid]
                            k9.updateProfilePicture(path)
                            k9.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Jmid in Setmain["AFfoto"]:
                            path = k10.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Jmid]
                            k10.updateProfilePicture(path)
                            k10.sendMessage(msg.to,"Foto berhasil dirubah")                            
                        elif Zmid in Setmain["AFfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["AFfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = k1.downloadObjectMsg(msg_id)
                     path2 = k2.downloadObjectMsg(msg_id)
                     path3 = k3.downloadObjectMsg(msg_id)
                     path4 = k4.downloadObjectMsg(msg_id)
                     path5 = k5.downloadObjectMsg(msg_id)
                     path6 = k6.downloadObjectMsg(msg_id)
                     path7 = k7.downloadObjectMsg(msg_id)
                     path8 = k8.downloadObjectMsg(msg_id)
                     path9 = k9.downloadObjectMsg(msg_id)
                     path10 = k10.downloadObjectMsg(msg_id)
                     pathsw = sw.downloadObjectMsg(msg_id)                     
                     settings["changePicture"] = False
                     k1.updateProfilePicture(path1)
                     k1.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k2.updateProfilePicture(path2)
                     k2.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k3.updateProfilePicture(path3)
                     k3.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k4.updateProfilePicture(path4)
                     k4.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k5.updateProfilePicture(path5)
                     k5.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k6.updateProfilePicture(path6)
                     k6.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k7.updateProfilePicture(path7)
                     k7.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k8.updateProfilePicture(path8)
                     k8.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k9.updateProfilePicture(path9)
                     k9.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k10.updateProfilePicture(path10)
                     k10.sendMessage(msg.to, "Berhasil mengubah foto profile bot")               
                     sw.updateProfilePicture(pathsw)
                     sw.sendMessage(msg.to, "Berhasil mengubah foto profile bot")               

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        boy.sendChatChecked(msg.to, msg_id)
                        k1.sendChatChecked(msg.to, msg_id)
                        k2.sendChatChecked(msg.to, msg_id)
                        k3.sendChatChecked(msg.to, msg_id)
                        k4.sendChatChecked(msg.to, msg_id)
                        k5.sendChatChecked(msg.to, msg_id)
                        k6.sendChatChecked(msg.to, msg_id)
                        k7.sendChatChecked(msg.to, msg_id)
                        k8.sendChatChecked(msg.to, msg_id)
                        k9.sendChatChecked(msg.to, msg_id)
                        k10.sendChatChecked(msg.to, msg_id)
                        sw.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               boy.sendMessage(msg.to,str(helpMessage))
                               
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                boy.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                boy.sendMessage(msg.to, "Selfbot dinonaktifkan")

                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = help2()
                               boy.sendMessage(msg.to, str(helpMessage2))
                                         
                        elif cmd == "help3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage3 = helpbot()
                               boy.sendMessage(msg.to, str(helpMessage3))

                        elif cmd == "help4":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = help1()
                               boy.sendMessage(msg.to, str(helpMessage1))
                               
                        elif cmd == "meme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage4 = infomeme()
                               boy.sendMessage(msg.to, str(helpMessage4))
                               
                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                boy.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                boy.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")                                

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "  ┏━━━━━━━━━━━━\n┃┃     🤖 S T A T U S 🤖\n┃┣━━━━━━━━━━━━\n"
                                if wait["unsend"] == True: md+="┃┃🐚 ✔️ Unsend「ON」\n"
                                else: md+="┃┃🐚 ✖ Unsend「OFF」\n"                                
                                if wait["sticker"] == True: md+="┃┃🐚 ✔️ Sticker「ON」\n"
                                else: md+="┃┃🐚 ✖ Sticker「OFF」\n"
                                if wait["contact"] == True: md+="┃┃🐚 ✔️ Contact「ON」\n"
                                else: md+="┃┃🐚 ✖ Contact「OFF」\n"
                                if wait["talkban"] == True: md+="┃┃🐚 ✔️ Talkban「ON」\n"
                                else: md+="┃┃🐚 ✖ Talkban「OFF」\n"
                                if wait["Mentionkick"] == True: md+="┃┃🐚 ✔️ Notag「ON」\n"
                                else: md+="┃┃🐚 ✖ Notag「OFF」\n"
                                if wait["detectMention"] == True: md+="┃┃🐚 ✔️ Respon「ON」\n"
                                else: md+="┃┃🐚 ✖ Respon「OFF」\n"
                                if wait["Mentiongift"] == True: md+="┃┃🐚 ✔️ Respongift「ON」\n"
                                else: md+="┃┃🐚 ✖ Respongift「OFF」\n"                                
                                if wait["autoJoin"] == True: md+="┃┃🐚 ✔️ Autojoin「ON」\n"
                                else: md+="┃┃🐚 ✖ Autojoin「OFF」\n"
                                if settings["autoJoinTicket"] == True: md+="┃┃🐚 ✔️ Jointicket「ON」\n"
                                else: md+="┃┃🐚 ✖ Jointicket「OFF」\n"                                
                                if wait["autoAdd"] == True: md+="┃┃🐚 ✔️ Autoadd「ON」\n"
                                else: md+="┃┃🐚 ✖ Autoadd「OFF」\n"                                
                                if wait["Timeline"] == True: md+="┃┃🐚 ✔️ Timeline「ON」\n"
                                else: md+="┃┃🐚 ✖ Timeline「OFF」\n"
                                if msg.to in welcome: md+="┃┃🐚 ✔️ Welcome「ON」\n"
                                else: md+="┃┃🐚 ✖ Welcome「OFF」\n"
                                if msg.to in simisimi: md+="┃┃🐚 ✔️ Simisimi「ON」\n"
                                else: md+="┃┃🐚 ✖ Simisimi「OFF」\n"                                
                                if wait["autoLeave"] == True: md+="┃┃🐚 ✔️ Autoleave「ON」\n"
                                else: md+="┃┃🐚 ✖ Autoleave「OFF」\n"
                                if msg.to in protectqr: md+="┃┃🐚 ✔️ Protecturl「ON」\n"
                                else: md+="┃┃🐚 ✖ Protecturl「OFF」\n"
                                if msg.to in protectjoin: md+="┃┃🐚 ✔️ Protectjoin「ON」\n"
                                else: md+="┃┃🐚 ✖ Protectjoin「OFF」\n"
                                if msg.to in protectkick: md+="┃┃🐚 ✔️ Protectkick「ON」\n"
                                else: md+="┃┃🐚 ✖ Protectkick「OFF」\n"
                                if msg.to in protectcancel: md+="┃┃🐚 ✔️ Protectcancel「ON」\n"
                                else: md+="┃┃🐚 ✖ Protectcancel「OFF」\n"
                                if msg.to in protectinvite: md+="┃┃🐚 ✔️ Protectinvite「ON」\n"
                                else: md+="┃┃🐚 ✖ Protectinvite「OFF」\n" 
                                if msg.to in protectantijs: md+="┃┃🐚 ✔️ Blockjs「ON」\n"
                                else: md+="┃┃🐚 ✖ Blockjs「OFF」\n"
                                if msg.to in ghost: md+="┃┃🐚 ✔️ Ghost「ON」\n"
                                else: md+="┃┃🐚 ✖ Ghost「OFF」\n"                                                
                                boy.sendMessage(msg.to, md+"┃┣━━━━━━━━━━━━\n┃┃🤖 Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃┃🤖 Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n┗━━━━━━━━━━━━")
                                
                        elif cmd == "status translate":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "┏━━━━━━━━━━━━\n┃┃ 🤖 STATUS TRANSLATE 🤖\n┃┣━━━━━━━━━━━━\n"
                                if msg.to in translateen: md+="┃┃🐚 ✔️ English「ON」\n"
                                else: md+="┃┃🐚 ✖ English「OFF」\n"
                                if msg.to in translateid: md+="┃┃🐚 ✔️ Indonesia「ON」\n"
                                else: md+="┃┃🐚 ✖ Indonesia「OFF」\n"
                                if msg.to in translateth: md+="┃┃🐚 ✔️ Thailand「ON」\n"
                                else: md+="┃┃🐚 ✖ Thailand「OFF」\n"
                                if msg.to in translatetw: md+="┃┃🐚 ✔️ Taiwan「ON」\n"
                                else: md+="┃┃🐚 ✖ Taiwan「OFF」\n"
                                if msg.to in translatear: md+="┃┃🐚 ✔️ Arab「ON」\n"
                                else: md+="┃┃🐚 ✖ Arab「OFF」\n"       
                                boy.sendMessage(msg.to, md+"┃┣━━━━━━━━━━━━\n┃┃🤖 Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃┃🤖 Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n┗━━━━━━━━━━━━")
                                
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                boy.sendMessage(msg.to,"「 SELFBOT-BY:MAX 11 Assist 」") 
                                ma = ""
                                for i in creator:
                                    ma = boy.getContact(i)
                                    boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 SELFBOT-BY:MAX 11 Assist 」\n")
                               boy.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd.startswith('penyewa'):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            try:
                                arr = []
                                today = datetime.today()
                                thn = 2025
                                bln = 12    #isi bulannya yg sewa
                                hr = 11    #isi tanggalnya yg sewa
                                future = datetime(thn, bln, hr)
                                days = (str(future - today))
                                comma = days.find(",")
                                days = days[:comma]
                                contact = boy.getContact(mid)
                                favoritelist = boy.getFavoriteMids()
                                grouplist = boy.getGroupIdsJoined()
                                contactlist = boy.getAllContactIds()
                                blockedlist = boy.getBlockedContactIds()
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                start = time.time()
                                sw.sendText("u83211e3b69096f869d545aed2d1724d3", '.')
                                elapsed_time = time.time() - start
                                ryan = boy.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Informasi Selfbot 」\n• User : "
                                ret_ = "• Group : {} Group".format(str(len(grouplist)))
                                ret_ += "\n• Friend : {} Friend".format(str(len(contactlist)))
                                ret_ += "\n• Blocked : {} Blocked".format(str(len(blockedlist)))
                                ret_ += "\n• Favorite : {} Favorite".format(str(len(favoritelist)))
                                ret_ += "\n• Version : 「Self Bots 」"
                                ret_ += "\n• Expired : {} - {} - {}".format(str(hr), str(bln), str(thn))
                                ret_ += "\n• In days : {} again".format(days)
                                ret_ += "\n「 Speed Respon 」\n• {} detik".format(str(elapsed_time))
                                ret_ += "\n「 Selfbot Runtime 」\n• {}".format(str(bot))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boy.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                boy.sendContact(to, "u054c3692f90083a5b1ad23e4a663f676")
                            except Exception as e:
                                boy.sendMessage(msg.to, str(e))

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               boy.sendMessage1(msg)

                        elif text.lower() == "mid":
                            #if msg._from in admin:
                               boy.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = boy.getContact(key1)
                               boy.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               boy.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = boy.getContact(key1)
                               boy.sendMessage(msg.to, "❧ Nama : "+str(mi.displayName)+"\n🐚 Mid : " +key1+"\n🐚 Status : "+str(mi.statusMessage))
                               boy.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(boy.getContact(key1)):
                                   boy.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   boy.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Fmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Hmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Imid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Jmid}
                               boy.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               boy.sendMessage1(msg)

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   boy.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   k1.removeAllMessages(op.param2)
                                   k2.removeAllMessages(op.param2)
                                   k3.removeAllMessages(op.param2)
                                   k4.removeAllMessages(op.param2)
                                   k5.removeAllMessages(op.param2)
                                   k6.removeAllMessages(op.param2)
                                   k7.removeAllMessages(op.param2)
                                   k8.removeAllMessages(op.param2)
                                   k9.removeAllMessages(op.param2)
                                   k10.removeAllMessages(op.param2)
                                   k1.sendText(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = boy.getGroupIdsJoined()
                               for group in saya:
                                   boy.sendMessage(group,"=======[BROADCAST]=======\n\n"+pesan+"\n\nCREATOR : line.me/R/ti/p/~maxbotline")

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   boy.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   boy.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               boy.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               boy.sendMessage(msg.to, "Restart...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               boy.sendMessage(msg.to,bot)
                               
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = boy.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(boy.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                boy.sendMessage(msg.to, "❂➣ BOT Grup Info\n\n❂➣ Nama Group : {}".format(G.name)+ "\n❂➣ ID Group : {}".format(G.id)+ "\n❂➣ Pembuat : {}".format(G.creator.displayName)+ "\n❂➣ Waktu Dibuat : {}".format(str(timeCreated))+ "\n❂➣ Jumlah Member : {}".format(str(len(G.members)))+ "\n❂➣ Jumlah Pending : {}".format(gPending)+ "\n❂➣ Group Qr : {}".format(gQr)+ "\n❂➣ Group Ticket : {}".format(gTicket))
                                boy.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                boy.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                boy.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = boy.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(boy.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "❂➣ BOT Grup Info\n"
                                ret_ += "\n❂➣ Name : {}".format(G.name)
                                ret_ += "\n❂➣ ID : {}".format(G.id)
                                ret_ += "\n❂➣ Creator : {}".format(gCreator)
                                ret_ += "\n❂➣ Created Time : {}".format(str(timeCreated))
                                ret_ += "\n❂➣ Member : {}".format(str(len(G.members)))
                                ret_ += "\n❂➣ Pending : {}".format(gPending)
                                ret_ += "\n❂➣ Qr : {}".format(gQr)
                                ret_ += "\n❂➣ Ticket : {}".format(gTicket)
                                ret_ += ""
                                boy.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem"):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = boy.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "❂➣ "+ str(no) + ". " + mem.displayName
                                boy.sendMessage(to,"❂➣ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = boy.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = boy.getGroup(i)
                                if ginfo == group:
                                    k1.leaveGroup(i)
                                    k2.leaveGroup(i)
                                    k3.leaveGroup(i)
                                    k4.leaveGroup(i)
                                    k5.leaveGroup(i)
                                    k6.leaveGroup(i)
                                    k7.leaveGroup(i)
                                    k8.leaveGroup(i)
                                    k9.leaveGroup(i)
                                    k10.leaveGroup(i)
                                    boy.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = boy.getAllContactIds()
                               for i in gid:
                                   G = boy.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.displayName+ "\n"
                               boy.sendMessage(msg.to,"┏━━[ FRIEND LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = boy.getGroupIdsJoined()
                               for i in gid:
                                   G = boy.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               boy.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = k1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               k1.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")


                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = k1.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   k1.updateGroup(X)
                                   k1.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = k1.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   k1.updateGroup(X)
                                   k1.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = k1.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      k1.updateGroup(x)
                                   gurl = k1.reissueGroupTicket(msg.to)
                                   k1.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                                   
                                   
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              ginvited = boy.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      boy.rejectGroupInvitation(gid)
                                  boy.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  boy.sendMessage(to, "Tidak ada undangan yang tertunda")

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                boy.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "upbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                k1.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "uppro":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["AFfoto"][mid] = True
                                boy.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Amid] = True
                                k1.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Bmid] = True
                                k2.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Cmid] = True
                                k3.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Dmid] = True
                                k4.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot5up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Emid] = True
                                k5.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot6up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Fmid] = True
                                k6.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot7up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Gmid] = True
                                k7.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot8up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Hmid] = True
                                k8.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot9up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Imid] = True
                                k9.sendText(msg.to,"Kirim fotonya.....")
                                 
                        elif cmd == "bot10up":
                            if msg._from in admin:
                                Setmain["AFfoto"][Jmid] = True
                                k10.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "ghostup":
                            if msg._from in admin:
                                Setmain["AFfoto"][Zmid] = True
                                sw.sendText(msg.to,"Kirim fotonya.....")
                               

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = boy.getProfile()
                                profile.displayName = string
                                boy.updateProfile(profile)
                                boy.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                k2.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k3.getProfile()
                                profile.displayName = string
                                k3.updateProfile(profile)
                                k3.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k4.getProfile()
                                profile.displayName = string
                                k4.updateProfile(profile)
                                k4.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k5.getProfile()
                                profile.displayName = string
                                k5.updateProfile(profile)
                                k5.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot6name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k6.getProfile()
                                profile.displayName = string
                                k6.updateProfile(profile)
                                k6.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot7name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k7.getProfile()
                                profile.displayName = string
                                k7.updateProfile(profile)
                                k7.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot8name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k8.getProfile()
                                profile.displayName = string
                                k8.updateProfile(profile)
                                k8.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot9name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k9.getProfile()
                                profile.displayName = string
                                k9.updateProfile(profile)
                                k9.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot10name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k10.getProfile()
                                profile.displayName = string
                                k10.updateProfile(profile)
                                k10.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("botkicker: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "tag" or text.lower() == 'ned':
                          if msg._from in admin:
                               group = boy.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (80, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm4)

                        elif 'mentionall' in msg.text:
                            group = boy.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+0):
                                  txt = ''
                                  s=0
                                  b=[]
                                  for i in group.members[a*20 : (a+1)*20]:
                                      b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                      s += 7
                                      txt += '@Alin \n'
                                  boy.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                  boy.sendMessage(to, "jumlah {} orang".format(str(len(nama)))) 

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"🤖 LIST BOT\n\n"+ma+"\nTotal「%s」BOT" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +boy.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"🤖 LIST Admin\n\n🤖 Creator BOT:\n"+ma+"\n🤖 Admin:\n"+mb+"\n🤖 Staff:\n"+mc+"\n🤖 Total「%s」SELFBOT-BY:MAX" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +boy.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +boy.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +boy.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +boy.getGroup(group).name + "\n"                                    
                                boy.sendMessage(msg.to,"🤖 BOT Protection\n\n🤖 PROTECT URL :\n"+ma+"\n🤖 PROTECT KICK :\n"+mb+"\n🤖 PROTECT JOIN :\n"+md+"\n🤖 PROTECT CANCEL:\n"+mc+"\n🤖 PROTECT INVITE :\n"+me+"\nTotal「%s」Protect yang aktif" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                k1.sendMessage(msg.to,responsename1)
                                k2.sendMessage(msg.to,responsename2)
                                k3.sendMessage(msg.to,responsename3)
                                k4.sendMessage(msg.to,responsename4)
                                k5.sendMessage(msg.to,responsename5)
                                k6.sendMessage(msg.to,responsename6)
                                k7.sendMessage(msg.to,responsename7)
                                k8.sendMessage(msg.to,responsename8)
                                k9.sendMessage(msg.to,responsename9)
                                k10.sendMessage(msg.to,responsename10)

                        elif cmd == "kicker":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Jmid,Imid,Hmid,Gmid,Fmid,Emid,Dmid,Cmid,Bmid,Amid]
                                    boy.inviteIntoGroup(msg.to, anggota)
                                    k1.acceptGroupInvitation(msg.to)
                                    k2.acceptGroupInvitation(msg.to)
                                    k3.acceptGroupInvitation(msg.to)
                                    k4.acceptGroupInvitation(msg.to)
                                    k5.acceptGroupInvitation(msg.to)
                                    k6.acceptGroupInvitation(msg.to)
                                    k7.acceptGroupInvitation(msg.to)
                                    k8.acceptGroupInvitation(msg.to)
                                    k9.acceptGroupInvitation(msg.to)
                                    k10.acceptGroupInvitation(msg.to)
                                    K10.sendText(msg.to, "kicker Done Stay in Room "+str(G.name))
                                except:
                                    pass
                                
    
                        elif cmd == "mjoin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = boy.getGroup(msg.to)
                                ginfo = boy.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                boy.updateGroup(G)
                                invsend = 0
                                Ticket = boy.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k1.updateGroup(G)

                        elif cmd == "mbye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = boy.getGroup(msg.to)
                                k1.sendText(msg.to, "Pamit Sob ayam Sob Buntut... "+str(G.name))
                                k1.leaveGroup(msg.to)
                                k2.leaveGroup(msg.to)
                                k3.leaveGroup(msg.to)
                                k4.leaveGroup(msg.to)
                                k5.leaveGroup(msg.to)
                                k6.leaveGroup(msg.to)
                                k7.leaveGroup(msg.to)
                                k8.leaveGroup(msg.to)
                                k9.leaveGroup(msg.to)
                                k10.leaveGroup(msg.to)
                           
                        elif cmd == "js":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = boy.getGroup(msg.to)
                                    boy.inviteIntoGroup(msg.to, [Zmid])
                                    boy.sendMessage(msg.to,"Grup 「"+str(ginfo.name)+"」 Max Dari JS")
                                except:
                                    pass              

                        elif cmd.startswith("pulang"):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = boy.getGroupIdsJoined()
                                for i in gid:
                                    h = boy.getGroup(i).name
                                    if h == ng:
                                        k1.sendMessage(i, "@! Silahkan admin invite atau masukan kembali")
                                        k1.leaveGroup(i)
                                        k2.leaveGroup(i)
                                        k3.leaveGroup(i)
                                        k4.leaveGroup(i)
                                        k5.leaveGroup(i)
                                        k6.leaveGroup(i)
                                        k7.leaveGroup(i)
                                        k8.leaveGroup(i)
                                        k9.leaveGroup(i)
                                        k10.leaveGroup(i)
                                        boy.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "ghost join":
                            if msg._from in admin:
                                G = boy.getGroup(msg.to)
                                ginfo = boy.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                boy.updateGroup(G)
                                invsend = 0
                                Ticket = boy.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "ghost bye":
                            if msg._from in admin:
                                G = boy.getGroup(msg.to)
                                sw.leaveGroup(msg.to)


                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                boy.sendMessage(msg.to, "Progres speed...")
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                boy.sendMessage(msg.to, "%.10f" % (get_profile_time))
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k1.sendMessage(msg.to, "%.10f" % (get_profile_time))
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k2.sendMessage(msg.to, "%.10f" % (get_profile_time))
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k3.sendMessage(msg.to, "%.10f" % (get_profile_time))
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k4.sendMessage(msg.to, "%.10f" % (get_profile_time))
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k5.sendMessage(msg.to, "%.10f" % (get_profile_time))
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k6.sendMessage(msg.to, "%.10f" % (get_profile_time))
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k7.sendMessage(msg.to, "%.10f" % (get_profile_time))
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k8.sendMessage(msg.to, "%.10f" % (get_profile_time))
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k9.sendMessage(msg.to, "%.10f" % (get_profile_time))
                                get_profile_time_start = time.time()
                                get_profile = boy.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                k10.sendMessage(msg.to, "%.10f" % (get_profile_time))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               boy.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               boy.sendMessage(msg.to, "{} Detik".format(str(elapsed_time)))

                        elif cmd == "speedbot" or cmd == "spb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               k1.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               k2.sendMessage(msg.to, "{} Detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               k3.sendMessage(msg.to, "{} Detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               k4.sendMessage(msg.to, "{} Detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               k5.sendMessage(msg.to, "{} Detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               k6.sendMessage(msg.to, "{} Detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               k7.sendMessage(msg.to, "{} Detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               k8.sendMessage(msg.to, "{} Detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               k9.sendMessage(msg.to, "{} Detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               k10.sendMessage(msg.to, "{} Detik".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['AFreadPoint'][msg.to] = msg_id
                                 Setmain['AFreadMember'][msg.to] = {}
                                 boy.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['AFreadPoint'][msg.to]
                                 del Setmain['AFreadMember'][msg.to]
                                 boy.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['AFreadPoint']:
                                if Setmain['AFreadMember'][msg.to] != {}:
                                    nad = []
                                    for x in Setmain['AFreadMember'][msg.to]:
                                        nad.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(nad)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in nad:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(nad):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(boy.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        boy.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['AFreadPoint'][msg.to]
                                        del Setmain['AFreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['AFreadPoint'][msg.to] = msg.id
                                    Setmain['AFreadMember'][msg.to] = {}
                                else:
                                    boy.sendMessage(msg.to, "User kosong...")
                            else:
                                boy.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  boy.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  boy.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  boy.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                                      
                        elif cmd.startswith("musik: "):
                          if msg._from in admin:    
                            try:
                                search = msg.text.replace("musik: ","")
                                r = requests.get("https://farzain.xyz/api/premium/joox.php?apikey=al11241519&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                boy.sendImageWithURL(msg.to, str(data["gambar"]))
                                boy.sendMessage(msg.to, str(hasil))
                                boy.sendMessage(msg.to, "Downloading...")
                                boy.sendMessage(msg.to, "「 Result MP3 」")
                                boy.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                boy.sendMessage(msg.to, "「 Result M4A 」")
                                boy.sendVideoWithURL(msg.to, str(audio["m4a"]))
                                boy.sendMessage(msg.to, str(data["lirik"]))
                                boy.sendMessage(msg.to, "Success Download...")
                            except Exception as error:
                            	boy.sendMessage(msg.to, "「 Result Error 」\n" + str(error))

                        elif cmd.startswith("randomnumber: "):                            	
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                angka = msg.text.replace(separate[0] + " ","")  
                                tgb = angka.split("-")
                                num1 = tgb[0]
                                num2 = tgb[1]
                                r = requests.get("https://farzain.xyz/api/random.php?min="+num1+"&max="+num2)
                                data = r.json()
                                boy.sendMessage(msg.to,"Hasil : "+str(data["url"]))
                                
                                
                        elif cmd.startswith("1cak"):
                          if msg._from in admin:
                              r=requests.get("https://api-1cak.herokuapp.com/random")
                              data=r.text
                              data=json.loads(data)
                              print(data)
                              hasil = "Result :\n"
                              hasil += "\nID : " +str(data["id"])
                              hasil += "\nTitle : " + str(data["title"])
                              hasil += "\nUrl : " + str(data["url"]) 
                              hasil += "\nVotes : " + str(data["votes"])
                              boy.sendMessage(msg.to, str(hasil))
        
                        elif cmd.startswith("musik2: "):
                          if msg._from in admin:    
                            try:
                                dan = msg.text.replace("musik2: ","")
                                r = requests.get("http://corrykalam.pw/api/joox.php?song={}"+urllib.parse.quote(dan))
                                data = r.json()
                                l = data["lyric"].replace("ti:","Judul: ")
                                i = l.replace("ar:","Penyanyi: ")
                                r = i.replace("al:","Album: ")
                                ii = r.replace("[by:]","")
                                k = ii.replace("[offset:0]","")
                                lirik = k.replace("***Lirik didapat dari pihak ketiga***\n","")
                                boy.sendImageWithURL(msg.to, data["image"])
                                t = "[ Music ]"
                                t += "\n\nJudul: "+str(data["title"])
                                t+="\nPenyanyi: "+str(data["singer"])
                                t+="\n\n[ Finish ]\n\n"+str(lirik)
                                boy.sendMessage(msg.to, str(t))
                                boy.sendAudioWithURL(msg.to, data["url"])
                            except Exception as error:
                                pass
                            
                        elif cmd.startswith("playlist "):
                          if msg._from in admin:    
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lagu ]━━━━"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n🤖「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    ret_ += "\n🤖「 {}Lirik {}:nomor 」 ".format(str(),str(search))
                                    boy.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "┏━━━━[ Detail Musik ]━━━━"
                                            ret_ += "\n┃┃ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n┃┃ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n┃┃ Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n┗━━[ Tunggu Audionya ]━━━"
                                            boy.sendMessage(msg.to, str(ret_))
                                            boy.sendAudioWithURL(msg.to, str(data["result"]["mp3"][0]))
                            except Exception as error:
                                pass
                            
                        elif cmd.startswith("lirik "):
                          if msg._from in admin:    
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lirik ]━━━━"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n🤖「 {}Lirik {}:nomor 」".format(str(),str(search))
                                    ret_ += "\n🤖「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    boy.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        boy.sendMessage(msg.to, str(lyric))
                            except Exception as error:
                                pass                                        
        
                        elif cmd.startswith("img food: "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        boy.sendImageWithURL(msg.to, str(food["url"]))
                                        
                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                boy.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                boy.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                boy.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass                                
                            	
                            	
                        elif cmd.startswith("meme"):
                          if msg._from in admin:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            boy.sendImageWithURL(msg.to, image)
          

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n🤖 Author : ' + str(vid.author)
                                    durasi = '\n🤖 Duration : ' + str(vid.duration)
                                    suka = '\n🤖 Likes : ' + str(vid.likes)
                                    rating = '\n🤖 Rating : ' + str(vid.rating)
                                    deskripsi = '\n🤖 Deskripsi : ' + str(vid.description)
                                boy.sendVideoWithURL(msg.to, me)
                                boy.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                boy.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n🤖 Author : ' + str(vid.author)
                                    durasi = '\n🤖 Duration : ' + str(vid.duration)
                                    suka = '\n🤖 Likes : ' + str(vid.likes)
                                    rating = '\n🤖 Rating : ' + str(vid.rating)
                                    deskripsi = '\n🤖 Deskripsi : ' + str(vid.description)
                                boy.sendImageWithURL(msg.to, me)
                                boy.sendAudioWithURL(msg.to, shi)
                                boy.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                boy.sendMessage(msg.to,str(e))
                                    
                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                boy.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                                boy.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                boy.sendMessage(msg.to, str(njer))
                                
                        elif cmd.startswith("cekig:"):
                            if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/ig_profile.php?apikey=arTdnVbJkW1EuzDNQrIxQDvHARIDcQ&id={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "┏━━[ Profile Instagram ]"
                                        ret_ += "\n┃┃ Nama : {}".format(str(data["info"]["full_name"]))
                                        ret_ += "\n┃┃ Username : {}".format(str(data["info"]["username"]))
                                        ret_ += "\n┃┃ Bio : {}".format(str(data["info"]["bio"]))
                                        ret_ += "\n┃┃ URL Bio : {}".format(str(data["info"]["url_bio"]))
                                        ret_ += "\n┃┃ Pengikut : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃┃ Diikuti : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃┃ Total Post : {}".format(str(data["count"]["post"]))
                                        ret_ += "\n┗━━[ https://www.instagram.com/{} ]".format(search)
                                        path = data["info"]["profile_pict"]
                                        boy.sendMessage(to, str(ret_))
                                        boy.sendImageWithURL(to, str(path))
                                except Exception as e:
                                    boy.sendMessage(msg.to, str(e))                                  

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91ARs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            boy.sendMessage(msg.to,"🐚 I N F O R M A S I 🐚\n\n"+"🐚 Date Of Birth : "+lahir+"\n🐚 Age : "+usia+"\n🐚 Ultah : "+ultah+"\n🐚 Zodiak : "+zodiak)

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["AFlimit"] = num
                                boy.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                boy.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["AFlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                boy.sendMessage1(msg)
                                            except Exception as e:
                                                boy.sendMessage(msg.to,str(e))
                                    else:
                                        boy.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = boy.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                boy.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        boy.sendMessage(msg.to,str(e))
                                else:
                                    boy.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000000000:
                                  for var in range(0,jumlah):
                                      boy.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}, contentType=9)
                                      k1.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k2.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k3.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k4.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k5.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k6.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k7.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k8.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k9.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      k10.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      sw.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      boy.sendMessage(midd, str(Setmain["AFmessage1"]))
                                      k1.sendMessage(midd, str(Setmain["AFmessage1"]))
                                      k2.sendMessage(midd, str(Setmain["AFmessage1"]))
                                      k3.sendMessage(midd, str(Setmain["AFmessage1"]))
                                      k4.sendMessage(midd, str(Setmain["AFmessage1"]))
                                      k5.sendMessage(midd, str(Setmain["AFmessage1"]))
                                      k6.sendMessage(midd, str(Setmain["AFmessage1"]))
                                      k7.sendMessage(midd, str(Setmain["AFmessage1"]))
                                      k8.sendMessage(midd, str(Setmain["AFmessage1"]))
                                      k9.sendMessage(midd, str(Setmain["AFmessage1"]))
                                      k10.sendMessage(midd, str(Setmain["AFmessage1"]))
                                      sw.sendMessage(midd, str(Setmain["AFmessage1"]))

                        elif 'Mybottoken' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                               boy.sendMessage(msg.to,"SELFBOT-BY:MAX\n"+boy.authToken)
                               boy.sendMessage(msg.to,"SELFBOT-BY:MAX 1\n"+k1.authToken)
                               boy.sendMessage(msg.to,"SELFBOT-BY:MAX 2\n"+k2.authToken)
                               boy.sendMessage(msg.to,"SELFBOT-BY:MAX 3\n"+k3.authToken)
                               boy.sendMessage(msg.to,"SELFBOT-BY:MAX 4\n"+k4.authToken)
                               boy.sendMessage(msg.to,"SELFBOT-BY:MAX 5\n"+k5.authToken)
                               boy.sendMessage(msg.to,"SELFBOT-BY:MAX 6\n"+k6.authToken)
                               boy.sendMessage(msg.to,"SELFBOT-BY:MAX 7\n"+k7.authToken)
                               boy.sendMessage(msg.to,"SELFBOT-BY:MAX 8\n"+k8.authToken)
                               boy.sendMessage(msg.to,"SELFBOT-BY:MAX 9\n"+k9.authToken)
                               boy.sendMessage(msg.to,"SELFBOT-BY:MAX 10\n"+k10.authToken)
                               boy.sendMessage(msg.to,"SELFBOT-BY:MAX Ghost\n"+sw.authToken)
#==============================================================================# 
                       

#===========Settings============#
                        elif 'Simi ' in msg.text:
                              spl = msg.text.replace('Simi ','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs) 
                                    
                        elif 'Autotrans th-' in msg.text:
                              spl = msg.text.replace('Autotrans th-','')
                              if spl == 'on':
                                  if msg.to in translateth:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateth.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateth:
                                         translateth.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    
                                    
                        elif 'Autotrans en-' in msg.text:
                              spl = msg.text.replace('Autotrans en-','')
                              if spl == 'on':
                                  if msg.to in translateen:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateen.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateen:
                                         translateen.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Autotrans id-' in msg.text:
                              spl = msg.text.replace('Autotrans id-','')
                              if spl == 'on':
                                  if msg.to in translateid:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateid.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateid:
                                         translateid.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Autotrans tw-' in msg.text:
                              spl = msg.text.replace('Autotrans tw-','')
                              if spl == 'on':
                                  if msg.to in translatetw:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translatetw.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatetw:
                                         translatetw.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Autotrans ar-' in msg.text:
                              spl = msg.text.replace('Autotrans ar-','')
                              if spl == 'on':
                                  if msg.to in translatear:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translatear.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatear:
                                         translatear.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    

                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
#===========Protection============#                                    
                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    boy.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                                                      

                        elif 'Blockjs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Antijs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Anti JS Diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Anti JS Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    boy.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)
                                    
                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = boy.getGroup(msg.to)
                                       msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                  boy.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    boy.sendMessage(msg.to, "Dinonaktifkan\n" + msgs) 

                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectantijs:
                                      msgs = ""
                                  else:
                                      protectantijs.append(msg.to)
                                  if msg.to in ghost:
                                      msgs = ""
                                  else:
                                      ghost.append(msg.to)                                      
                                  if msg.to in protectcancel:
                                      ginfo = boy.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua sudah diaktifkan"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = boy.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protection diaktifkan"
                                  boy.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    else:
                                         ginfo = boy.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    boy.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)

#===========KICKOUT============#
                        elif ("Nk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = boy.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           boy.updateGroup(G)
                                           invsend = 0
                                           Ticket = boy.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = boy.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           boy.updateGroup(X)
                                       except:
                                           pass

                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                        
                        elif cmd == "Max kill":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                  if wait["Kickallmember"]:
                                    _name = msg.text.replace("Masmax","")
                                    gs = boy.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        boy.sendMessage(msg.to,"Target Not found.")
                                    else:
                                       for target in targets:
                                         if target not in Bots and target not in Boy:
                                           try:
                                               klist=[boy,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10]
                                               kicker=random.choice(klist)
                                               kicker.kickoutFromGroup(msg.to,[target])
                                           except Exception as error:
                                               boy.sendMessage(msg.to, str(error))
#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           boy.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           boy.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           boy.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           boy.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Boy:
                                       try:
                                           staff.remove(target)
                                           boy.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Boy:
                                       try:
                                           Bots.remove(target)
                                           boy.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in creator:
                                wait["addadmin"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:delete" or text.lower() == 'admin:delete':
                            if msg._from in creator:
                                wait["delladmin"] = False
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:delete" or text.lower() == 'staff:delete':
                            if msg._from in admin:
                                wait["dellstaff"] = False
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:delete" or text.lower() == 'bot:delete':
                            if msg._from in admin:
                                wait["dellbots"] = False
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                boy.sendMessage(msg.to,"Berhasil di Refresh...")

                        elif cmd == "pro on" or text.lower() == 'pro on':
                            if msg._from in admin:
                                wait["protectqr"] = True
                                k1.sendMessage(msg.to,"KICKER 1 ON")
                                wait["protectkick"] = True
                                k2.sendMessage(msg.to,"KICKER 2 ON")
                                wait["protectjoin"] = True
                                k3.sendMessage(msg.to,"KICKER 3 ON")
                                wait["protectcancel"] = True
                                k4.sendMessage(msg.to,"KICKER 4 ON")
                                wait["protectinvite"] = True
                                k5.sendMessage(msg.to,"KICKER 5 ON")
                                wait["protectantijs"] = True
                                k6.sendMessage(msg.to,"KICKER 6 ON")
                                wait["ghost"] = True
                                k7.sendMessage(msg.to,"KICKER 7 ON")
                                wait["welcome"] = True
                                k8.sendMessage(msg.to,"KICKER 8 ON")
                                k9.sendMessage(msg.to,"KICKER 9 ON")
                                k10.sendMessage(msg.to,"KICKER 10 ON")

                        elif cmd == "pro off" or text.lower() == 'pro off':
                            if msg._from in admin:
                                wait["protectqr"] = False
                                k1.sendMessage(msg.to,"KICKER 1 OFF")
                                wait["protectkick"] = False
                                k2.sendMessage(msg.to,"KICKER 2 OFF")
                                wait["protectjoin"] = False
                                k3.sendMessage(msg.to,"KICKER 3 OFF")
                                wait["protectcancel"] = False
                                k4.sendMessage(msg.to,"KICKER 4 OFF")
                                wait["protectinvite"] = False
                                k5.sendMessage(msg.to,"KICKER 5 OFF")
                                wait["protectantijs"] = False
                                k6.sendMessage(msg.to,"KICKER 6 OFF")
                                wait["ghost"] = False
                                k7.sendMessage(msg.to,"KICKER 7 OFF")
                                wait["welcome"] = False
                                k8.sendMessage(msg.to,"KICKER 8 OFF")
                                k9.sendMessage(msg.to,"KICKER 9 OFF")
                                k10.sendMessage(msg.to,"KICKER 10 OFF")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                                ma = ""
                                for i in admin:
                                    ma = boy.getContact(i)
                                    boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                                ma = ""
                                for i in staff:
                                    ma = boy.getContact(i)
                                    boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                                ma = ""
                                for i in Bots:
                                    ma = boy.getContact(i)
                                    boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                boy.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                boy.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                sendMention(msg.to, sender, "「 Status Timeline 」\nUser ", "\nSilahkan kirim postingannya,\nKetik timeline off jika sudah slesai")

                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                sendMention(msg.to, sender, "「 Status Timeline 」\nUser ", " \nDeteksi timeline dinonaktifkan")
                                
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendMention(msg.to, sender, "「 Status Invite 」\nUser ", "\nSilahkan kirim kontaknya,\nKetik invite off jika sudah slesai")

                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendMention(msg.to, sender, "「 Status Invite 」\nUser ", " \nInvite via contact dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                boy.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                boy.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                boy.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                boy.sendMessage(msg.to,"Auto respon dinonaktifkan")
                                
                        elif cmd == "respongift on" or text.lower() == 'respongift on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = True
                                boy.sendMessage(msg.to,"Auto respon gift diaktifkan")

                        elif cmd == "respongift off" or text.lower() == 'respongift off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = False
                                boy.sendMessage(msg.to,"Auto respon gift dinonaktifkan")                                

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                boy.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                boy.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                boy.sendMessage(msg.to,"Auto Leave Diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                boy.sendMessage(msg.to,"Auto Leave Dimatikan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                boy.sendMessage(msg.to,"Auto Add Diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                boy.sendMessage(msg.to,"Auto Add Dimatikan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                boy.sendMessage(msg.to,"Detect Sticker Diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                boy.sendMessage(msg.to,"Detect Sticker Dimatikan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                boy.sendMessage(msg.to,"Auto Join Ticket Diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                boy.sendMessage(msg.to,"Auto Join Ticket Dimatikan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           boy.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           boy.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = False
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           boy.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           boy.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = False
                                boy.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                boy.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"🤖 Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                boy.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boy.getContact(m_id).displayName + "\n"
                                boy.sendMessage(msg.to,"🤖 Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    boy.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = boy.getContact(i)
                                        boy.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = boy.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              boy.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Pesan Message")
                              else:
                                  wait["message"] = spl
                                  boy.sendMessage(msg.to, "「Pesan Msg」\nPesan Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  boy.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Leave Message")
                              else:
                                  wait["leave"] = spl
                                  boy.sendMessage(msg.to, "「Leave Msg」\nLeave Message diganti jadi :\n\n「{}」".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Respon Message")
                              else:
                                  wait["Respontag"] = spl
                                  boy.sendMessage(msg.to, "「Respon Msg」\nRespon Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["AFmessage1"] = spl
                                  boy.sendMessage(msg.to, "「Spam Msg」\nSpam Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  boy.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  boy.sendMessage(msg.to, "「Sider Msg」\nSider Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Pesan Msg」\nPesan Message lu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message lu :\n\n「 " + str(wait["welcome"]) + " 」")
                               
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Leave Msg」\nLeave Message lu :\n\n「 " + str(wait["leave"]) + " 」")                                 

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Respon Msg」\nRespon Message lu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Spam Msg」\nSpam Message lu :\n\n「 " + str(Setmain["AFmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               boy.sendMessage(msg.to, "「Sider Msg」\nSider Message lu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = boy.findGroupByTicket(ticket_id)
                                     boy.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     boy.sendMessage(msg.to, "😈 JOIN GROUP 😈 : %s" % str(group.name))
                                     group1 = k1.findGroupByTicket(ticket_id)
                                     k1.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     k1.sendMessage(msg.to, "🤖 SELFBOT-BY:MAX 🤖 1 : %s" % str(group.name))
                                     group2 = k2.findGroupByTicket(ticket_id)
                                     k2.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     k2.sendMessage(msg.to, "🤖 SELFBOT-BY:MAX 🤖 2 : %s" % str(group.name))
                                     group3 = k3.findGroupByTicket(ticket_id)
                                     k3.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     k3.sendMessage(msg.to, "🤖 SELFBOT-BY:MAX 🤖 3 : %s" % str(group.name))
                                     group4 = k4.findGroupByTicket(ticket_id)
                                     k4.acceptGroupInvitationByTicket(group4.id,ticket_id)
                                     k4.sendMessage(msg.to, "🤖 SELFBOT-BY:MAX 🤖 4 : %s" % str(group.name))
                                     group5 = k5.findGroupByTicket(ticket_id)
                                     k5.acceptGroupInvitationByTicket(group5.id,ticket_id)
                                     k5.sendMessage(msg.to, "🤖 SELFBOT-BY:MAX 🤖 5 : %s" % str(group.name))
                                     group6 = k6.findGroupByTicket(ticket_id)
                                     k6.acceptGroupInvitationByTicket(group6.id,ticket_id)
                                     k6.sendMessage(msg.to, "🤖 SELFBOT-BY:MAX 🤖 6 : %s" % str(group.name))
                                     group7 = k7.findGroupByTicket(ticket_id)
                                     k7.acceptGroupInvitationByTicket(group7.id,ticket_id)
                                     k7.sendMessage(msg.to, "🤖 SELFBOT-BY:MAX 🤖 7 : %s" % str(group.name))
                                     group8 = k8.findGroupByTicket(ticket_id)
                                     k8.acceptGroupInvitationByTicket(group8.id,ticket_id)
                                     k8.sendMessage(msg.to, "🤖 SELFBOT-BY:MAX 🤖 8 : %s" % str(group.name))
                                     group9 = k9.findGroupByTicket(ticket_id)
                                     k9.acceptGroupInvitationByTicket(group9.id,ticket_id)
                                     k9.sendMessage(msg.to, "🤖 SELFBOT-BY:MAX 🤖 9 : %s" % str(group.name))
                                     group10 = k10.findGroupByTicket(ticket_id)
                                     k10.acceptGroupInvitationByTicket(group10.id,ticket_id)
                                     k10.sendMessage(msg.to, "🤖 SELFBOT-BY:MAX 🤖 10 : %s" % str(group.name))


    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
