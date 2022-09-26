# -*- coding: utf-8 -*-
from __future__ import absolute_import, division
import sys
import base64
import urllib
import urllib2
import os
import xbmcvfs
import socket 
from datetime import datetime
import time
import _strptime
import urllib,urllib2,re
import xbmc, xbmcgui, xbmcplugin, xbmcaddon,sys
from httplib import HTTP
from urlparse import urlparse
import StringIO
import urllib2,urllib
import httplib,itertools
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib
import shutil
import glob
import ctypes
import struct
import random
import textwrap
import pyxbmct
import string
import time
import requests
import inputstreamhelper
pyxbmct.skin.estuary = False
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
from xml.etree import ElementTree as ET
try:
    import json
except:
    import simplejson as json
import SimpleDownloader as downloader

from uuid import getnode as get_mac

my_api = "plugin.veep.ott"
addon = xbmcaddon.Addon(my_api)
addon_version = addon.getAddonInfo('version')
profile = xbmc.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
icon = os.path.join(home, 'icon.png')
FANART = os.path.join(home, 'fanart.png')
None_icon_movie = os.path.join(home, 'img/icon_none_film.jpg')
play_fanart = "sygma/Fanart_Play.png"
tv_fanart = "sygma/Fanart_Tv.jpg"
downloader = downloader.SimpleDownloader()
domainename = "http://hamza-kodi.ddns.net"
langue = addon.getLocalizedString
profile_skin=os.path.join(xbmc.translatePath('special://userdata/addon_data/'), 'skin.confluence')
skinsettings_xml = os.path.join(profile_skin,'settings.xml')
logo = os.path.join(xbmc.translatePath("special://home/addons/"+my_api+"/Skin"), 'settings.xml')
RSSOF = os.path.join(xbmc.translatePath("special://home/addons/"+my_api+"/Skin"), 'RssFeeds.xml')
RSS = os.path.join(xbmc.translatePath('special://userdata/'), 'RssFeeds.xml')
dest = os.path.join(profile, 'live')
info = os.path.join(profile, 'info')
source_api = os.path.join(xbmc.translatePath("special://home/addons/"+my_api+"/resources"), 'source_file')
dir_profile=os.path.join(xbmc.translatePath('special://userdata/addon_data'), my_api)
mac_adresse = addon.getSetting('mac_adresse')
version = addon.getSetting('version')
debug = addon.getSetting('debug')
theme_ok = addon.getSetting('theme_ok')
code_active = domainename+"/source/client/index.php"
genXml = os.path.join(xbmc.translatePath('special://userdata/keymaps'), 'gen.xml')
nevbarof=os.path.join(xbmc.translatePath("special://home/addons/"+my_api+"/skin"), 'Home.xml')
navbar = os.path.join(xbmc.translatePath("special://home/addons/skin.confluence/720p"), 'Home.xml')
MayVideoNavOF=os.path.join(xbmc.translatePath("special://home/addons/"+my_api+"/skin"), 'MyVideoNav.xml')
image_home = os.path.join(xbmc.translatePath("special://home/addons/"+my_api+"/skin"), 'SKINDEFAULT.jpg')
image_home_of = os.path.join(xbmc.translatePath("special://home/addons/skin.confluence/backgrounds"), 'SKINDEFAULT.jpg')
MayVideoNav = os.path.join(xbmc.translatePath("special://home/addons/skin.confluence/720p"), 'MyVideoNav.xml')
ViewsVideoLibraryOF=os.path.join(xbmc.translatePath("special://home/addons/"+my_api+"/skin"), 'ViewsVideoLibrary.xml')
ViewsVideoLibrary = os.path.join(xbmc.translatePath("special://home/addons/skin.confluence/720p"), 'ViewsVideoLibrary.xml')
IncludesBackgroundBuilding = os.path.join(xbmc.translatePath("special://home/addons/skin.confluence/720p"), 'ViewsFileMode.xml')
TexturesLogo = os.path.join(xbmc.translatePath("special://home/addons/skin.confluence/media"), 'Textures.xbt')
IncludesBackgroundBuildingOF = os.path.join(xbmc.translatePath("special://home/addons/"+my_api+"/Skin"), 'ViewsFileMode.xml')
TexturesLogoOF = os.path.join(xbmc.translatePath("special://home/addons/"+my_api+"/skin"), 'Textures.xbt')
service = os.path.join(xbmc.translatePath("special://home/addons/"+my_api+"/skin"), 'service.py')
serviceOF = os.path.join(xbmc.translatePath("special://home/addons/service.xbmc.versioncheck/resources/lib"), 'runner.py')
url_sygma = addon.getSetting('url_sygma')
check_apk = addon.getSetting('check_apk')
port_sygma = addon.getSetting('port_sygma')
kodi_image = addon.getSetting('kodi_image')
player_api = addon.getSetting('player_api')
username = addon.getSetting('username')
password = addon.getSetting('password')
serieal_nb = addon.getSetting('serieal_nb')
option_lecture = addon.getSetting('option')
source = os.path.join(xbmc.translatePath("special://home/addons/"+my_api+"/resources"), 'source')
coded = addon.getSetting('coded')
pin = addon.getSetting('pin')

def RemotePlay(val):
    keyplayapp=os.path.join(xbmc.translatePath('special://home/addons/'+my_api+'/remote'), 'gen.xml')
    keyplayTV=os.path.join(xbmc.translatePath('special://home/addons/'+my_api+'/remote'), 'genTV.xml')
    keyplayMovie=os.path.join(xbmc.translatePath('special://home/addons/'+my_api+'/remote'), 'genMovies.xml')
    keyplayReplay=os.path.join(xbmc.translatePath('special://home/addons/'+my_api+'/remote'), 'genReplay.xml')
    if   val == 1:
        shutil.copy(keyplayTV,genXml)
    elif val == 2:
        shutil.copy(keyplayMovie,genXml)
    elif val == 0:
        shutil.copy(keyplayapp,genXml) 
    elif val == 3:
         shutil.copy(keyplayReplay,genXml)    
    xbmc.executebuiltin('action(reloadkeymaps)')

def ErrerConextionServeur():
    xbmcgui.Dialog().ok("[COLOR white]"+langue(32003)+"[/COLOR] [COLOR red]![/COLOR]","[COLOR red]"+langue(32021)+"[/COLOR] ") 
    sys.exit()   

def ErrerConextion():
    xbmcgui.Dialog().ok(langue(32003)+"!",langue(32007) +":",'',langue(32008)+    "   -   "    +langue(32009)+    "   -   "    +langue(32010)) 
    sys.exit()
def yes():
    yes = xbmcgui.Dialog().yesno(langue(32000),langue(32001),"\r\n"+langue(32002)) 
    if yes :

        getInfoAbo()  
    else:
        sys.exit()

def newskin():
    if os.path.exists(profile_skin)==False:
        os.mkdir(profile_skin)
           
    shutil.copy(logo,skinsettings_xml)
    # xbmc.executebuiltin("Container.Refresh")
    shutil.copy(nevbarof,navbar)
    shutil.copy(RSSOF,RSS)
    xbmc.executebuiltin("XBMC.RunScript(script.embuary.helper,action=setkodisetting,setting=lookandfeel.enablerssfeeds,value=true)")
    shutil.copy(service,serviceOF)
    shutil.copy(image_home,image_home_of)
    shutil.copy(MayVideoNavOF,MayVideoNav)            
    shutil.copy(ViewsVideoLibraryOF,ViewsVideoLibrary)
    shutil.copy(IncludesBackgroundBuildingOF,IncludesBackgroundBuilding)
    shutil.copy(TexturesLogoOF,TexturesLogo)
    xbmc.executebuiltin("XBMC.ReloadSkin()")
    xbmc.executebuiltin("Container.Refresh")
    urllink = domainename+"/source/update"    
    try:
        response = urllib2.urlopen(urllink)
        urllink = json.load(response)

    except urllib2.URLError as err:
        return ErrerConextionServeur()

    if len(urllink) >= 1:
        versionup=""
        delateImg=""
        if urllink[0].has_key('versionup'):
            versionup = urllink[0]['versionup']            
            addon.setSetting("version",versionup)
            
        if urllink[0].has_key('delateImg'):
            delateImg = urllink[0]['delateImg']
            addon.setSetting("delateImg",delateImg)   

def getInfoAbo():
    urlInfo = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password
    try:
        response = urllib2.urlopen(urlInfo)
        Infoclient = json.load(response)
        information = json.dumps(Infoclient)
        fichier = open(info, "w")                
        fichier.write(information)      
        fichier.close()

    except urllib2.URLError as err:
        if os.path.exists(info)==False:
            return ErrerConextionServeur()
        else:
            pass
   
    with open(info) as f:
        Infoclient = json.load(f)
        if len(Infoclient) >= 1:  
            if Infoclient['user_info'].has_key('username'):
                datexpire = time.gmtime(int(Infoclient['user_info']['exp_date']))
                datecreation = time.gmtime(int(Infoclient['user_info']['created_at']))
                exp=time.strftime("%d-%m-%Y %H:%M:%S", datexpire)
                creat=time.strftime("%d-%m-%Y %H:%M:%S", datecreation)
                maxconex=Infoclient['user_info']['max_connections']
                url = Infoclient['server_info']['url']
                port = Infoclient['server_info']['port']
                if Infoclient['user_info']['is_trial'] == "0":
                    typeaccess = "Official"
                else:
                    typeaccess = "Trial"
                active_cons = Infoclient['user_info']['active_cons']
                data =''
                data += "[COLOR dimgray]"+langue(32006)+ " : [/COLOR] "+Infoclient['user_info']['username']+"\n\r"+"\n\r"
                data +="[COLOR dimgray]"+langue(32089)+ " : [/COLOR] "+coded+"\n\r"+"\n\r"
                data +="[COLOR dimgray]"+langue(32089)+" PIN"+ " : [/COLOR] "+pin+"\n\r"+"\n\r"
                data +="[COLOR dimgray]"+langue(32011)+ " : [/COLOR] "+Infoclient['user_info']['status']+"\n\r"+"\n\r"
                data +="[COLOR dimgray]"+langue(32020)+ " : [/COLOR] "+creat+"\n\r"+"\n\r"
                data +="[COLOR dimgray]"+langue(32019)+ " : [/COLOR] "+exp+"\n\r"+"\n\r"
                data +="[COLOR dimgray]"+langue(32018)+ " : [/COLOR] "+typeaccess+"\n\r"+"\n\r"
                data +="[COLOR dimgray]"+langue(32017)+ " : [/COLOR] "+active_cons+"\n\r"+"\n\r"
                data +="[COLOR dimgray]"+langue(32016)+ " : [/COLOR] "+maxconex+"\n\r"+"\n\r"
                data +="[COLOR dimgray]"+langue(32015)+ " : [/COLOR] " +version+"\n\r"+"\n\r"            
                xbmcgui.Dialog().textviewer(langue(32014),data)
        sys.exit()

def makeRequest(url, headers=None):
    try:
        if headers is None:
            headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        data = response.read()
        response.close()
        return data
    except:
        pass
        sys.exit()

def getSoup(url):
    if url.startswith('http://'):
        data = makeRequest(url)
    else:
        addon_log(langue(32022))
        return
    return BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES) 

def getData(url):
    getSoup(url)
    getItems(url)
def getItems(sources):
    try:
        response = urllib2.urlopen(sources)
        sources = json.load(response)

    except urllib2.URLError as err:
        return ErrerConextionServeur()
    if len(sources) >= 1:
        for i in sources:
            cover = icon
            name = ""
            series_id =""
            stream_type = ""
            stream_id = ""
            cover = None_icon_movie
            category_id = ""
            direct_source = ""
            rating = ""
            container_extension = ""
            fanart = play_fanart
            plot=""
            cast=""
            director=""
            genre=""
            releaseDate=""
            backdrop_path=""
            youtube_trailer=""       
            try:
                if i.has_key('name'):
                    name = i['name'] 
            except: pass
            try:                     
                if i.has_key('stream_type'):
                    stream_type = i['stream_type']
            except: pass        
            try:            
                if i.has_key('stream_id'):
                    stream_id = str(i['stream_id'])
            except: pass         
            try:
                if i.has_key('stream_icon'):
                    cover = i['stream_icon']
            except: pass        
            try:
                if i.has_key('direct_source'):
                    direct_source = i['direct_source']
            except: pass        
            try:
                if i.has_key('container_extension'):
                    container_extension ='.'+i['container_extension'] 
            except: pass        
            try:
                if i.has_key('series_id'):
                    series_id = str(i['series_id'])
            except: pass         
            try:
                if i.has_key('director'):
                    director = i['director']
            except: pass        
            try:
                if i.has_key('rating'):
                    rating = i['rating']
            except: pass        
            try:
                if i.has_key('cover'):
                    cover = i['cover']
            except: pass        
            try:
                if i.has_key('plot'):
                    plot = i['plot']
            except: pass        
            try:
                if i.has_key('category_id'):
                    category_id = i['category_id'] 
            except: pass        
            try:
                if i.has_key('genre'):
                    genre = i['genre'] 
            except: pass        
            try:
                if i.has_key('releaseDate'):
                    releaseDate = i['releaseDate'] 
            except: pass        
            try:
                if i.has_key('backdrop_path'):
                    backdrop_path = i['backdrop_path']
            except: pass        
            try:
                if i.has_key('youtube_trailer'):
                    youtube_trailer = i['youtube_trailer']
            except: pass            
            if mode == 6:
                url = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action=get_vod_info&vod_id="+stream_id 
                addDirFilm(url.encode('utf-8'),name.encode('utf-8', 'ignore'),cover,stream_id,fanart,container_extension)       
            elif mode == 9:
                try:
                    if isinstance(backdrop_path, list):
                        fanart = backdrop_path[0]
                    else:
                       fanart = play_fanart
                except: pass

                try:
                    fanart = fanart.encode('utf-8')
                except: pass

                try:
                    director = director.encode('utf-8')
                except: pass

                try:
                    url = url.encode('utf-8')
                except: pass

                try:
                    name = name.encode('utf-8', 'ignore')
                except: pass

                try:
                    cover = cover.encode('utf-8', 'ignore')
                except: pass

                    
                url = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action=get_series_info&series_id="+series_id
                addDirSerie(url,name,cover,category_id,fanart,series_id,genre,plot,youtube_trailer,releaseDate,director,rating)               
                
def addDirSerie(url,name,cover,category_id,fanart,series_id,genre,plot,youtube_trailer,releaseDate,director,rating):
    if not fanart:
        fanart = play_fanart
    if not name:
        name= langue(32050)
    if not director:
        director= langue(32050) 
    if not rating:
        rating= "0"       
    mode = "10"  
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&serieId="+str(series_id)+"&director="+urllib.quote_plus(director)+"&rating="+urllib.quote_plus(rating)
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=cover)
    liz.setInfo(type="Video", infoLabels={ "title": name})
    liz.setProperty("Fanart_Image", fanart)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

def addDirFilm(url,name,iconimage,stream_id,fanart,extension):
    
    if not iconimage:
        iconimage = icon
    if not name:
        title= langue(32050)    
    title =  name
    logoimage = iconimage
    try:
        name = name.encode('utf-8')
    except: pass
    try:
        iconimage = iconimage.encode('utf-8')
    except: pass                       
    mode = "7"
    u=sys.argv[0]+"?"
    u += "url="+urllib.quote_plus(url)+"&mode="+mode+"&streamId="+str(stream_id)+"&extension="+extension+"&iconimage="+urllib.quote_plus(logoimage)+"&name="+urllib.quote_plus(title)
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "title": name })
    liz.setProperty("Fanart_Image", play_fanart)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

def getInfoFilm(url):
    try:
        response = urllib2.urlopen(url)
        infoplus = json.load(response)

    except urllib2.URLError as err:
        return ErrerConextionServeur()
    FanartStream = FANART
    genre = ""
    movie_image = iconimage
    director = ""
    rating = ""
    episode_run_time = ""
    youtube_trailer = ""
    description = ""
    releasedate = ""
    stream_id = streamId
    if not extension :
        url = url_sygma+":"+port_sygma+"/movie/"+username+"/"+password+"/"+streamId
    else:
        url = url_sygma+":"+port_sygma+"/movie/"+username+"/"+password+"/"+streamId+extension

    if len(infoplus) >= 1:
        
        if infoplus['info'].has_key('genre'):
            genre= infoplus['info']['genre']
            genre = genre.replace(" ","")
            genre = genre.replace(",","/")
            try:
               genre = genre.encode('utf-8')
            except: pass

        if infoplus['info'].has_key('backdrop_path'):
            FanartStream= infoplus['info']['backdrop_path']
            try:
                if isinstance(FanartStream, list):
                    FanartStream = FanartStream[0]
            except: pass        
            try:
                FanartStream = FanartStream.encode('utf-8')
            except: pass

        if infoplus['info'].has_key('director'):
            director = infoplus['info']['director']
            try:
               director = director.encode('utf-8')
            except: pass
        if infoplus['info'].has_key('rating'):
            rating = infoplus['info']['rating']
            try:
               rating = rating.encode('utf-8')
            except: pass
        if infoplus['info'].has_key('releasedate'):
            releasedate = infoplus['info']['releasedate']
            releasedate = releasedate.replace(" ","")
            releasedate = releasedate.replace("Date","")
            releasedate = releasedate.replace(":","")
            releasedate = releasedate.replace("-","/")
            releasedate = releasedate.rstrip()
        if infoplus['info'].has_key('episode_run_time'):
            episode_run_time = infoplus['info']['episode_run_time']
        if infoplus['info'].has_key('youtube_trailer'):
            youtube_trailer = infoplus['info']['youtube_trailer']
            try:
               youtube_trailer = youtube_trailer.encode('utf-8')
            except: pass
            try:
                if "youtube" in youtube_trailer : 
                    a = urlparse(youtube_trailer)
                    youtube_trailer=os.path.basename(a.path)
                    youtube_trailer="plugin://plugin.video.youtube/play/?video_id="+youtube_trailer
                elif "http://" in youtube_trailer :
                    youtube_trailer = youtube_trailer
                elif  len(youtube_trailer) > 4  :
                    youtube_trailer="plugin://plugin.video.youtube/play/?video_id="+youtube_trailer    
            except: pass        

        if infoplus['info'].has_key('description'):
            description = infoplus['info']['description']
            try:
               description = description.encode('utf-8')
            except: pass 
        if not rating : 
            rating="0"
        if not description :
            description= langue(32050)
        if not director :   
            director = langue(32050)
        
        addLinkfilm(url,name,movie_image,stream_id,FanartStream,episode_run_time,releasedate,rating,director,genre,description,"0")    
        if not youtube_trailer:
            pass
        else:
            addLinkfilm(youtube_trailer,name,movie_image,stream_id,FanartStream,episode_run_time,releasedate,rating,director,genre,description,"1")

        # addLinkfilm(youtube_trailer,name,movie_image,stream_id,FanartStream,episode_run_time,releasedate,rating,director,genre,description,"2")

def addLinkfilm(url,name,iconimage,stream_id,fanart,episode_run_time,releasedate,rating,director,genre,description,option): 
    try:
        name = name.encode('utf-8')
    except: pass
    try:
        iconimage = iconimage.encode('utf-8')
    except: pass 
    try:
        fanart = fanart.encode('utf-8')
    except: pass

    if option =="0": #movie
        mode = "3"
        u=sys.argv[0]+"?"
        u += "url="+urllib.quote_plus(url)+"&mode="+mode+"&streamId="+str(stream_id)
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setProperty('IsPlayable', 'true')
        
    elif option =="1": # trailer
        mode = "3"
        u=sys.argv[0]+"?"
        u += "url="+urllib.quote_plus(url)+"&mode="+mode+"&streamId="+str(stream_id)
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage="sygma/Trailer_eye.jpg")
        liz.setProperty('IsPlayable', 'true')
        
    # elif option =="2": # alert
    #     mode = "0"
    #     u=sys.argv[0]+"?"
    #     u += "url="+urllib.quote_plus(url)+"&mode="+mode+"&streamId="+str(stream_id)
    #     liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage="sygma/Alert_eye.jpg")

    else:
        sys.exit()

    liz.setInfo(type="Video", infoLabels={ "title": name, "status": option, "set":rating, "genre":genre, "director":releasedate, "plot":description, "trailer":iconimage})
    liz.setProperty("Fanart_Image", str(fanart))
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)

def getBouquet(url):
    getSoup(url)
    getTV(url)

def getTV(sources):

    name = ""
    try:
        response = urllib2.urlopen(sources)        
        sources = json.load(response)
        json_live = json.dumps(sources)
        fichier = open(dest, "w")                
        fichier.write(json_live)      
        fichier.close()
        data = json.loads(open(dest).read())
        if len(data) >= 1:
            i=0
            for index in data:
                if index.has_key('name'):
                    name = index['name']
                    try:
                        name = name.encode('utf-8')
                    except: pass
                    if "--" in name:
                        del data[i]
                        b = open(dest, "w")
                        b.write(json.dumps(data))
                        b.close()
                    i+=1

    except urllib2.URLError as err:
        return ErrerConextionServeur()
    with open(dest) as f:
        data = json.load(f)
        if len(data) >= 1:
            num = 1
            for i in data:
                name = ""
                stream_id = ""
                thumbnail = ""
                if i.has_key('name'):
                    name = i['name']            	
                if i.has_key('stream_id'):
                    stream_id = str(i['stream_id'])       
                if i.has_key('stream_icon'):
                    thumbnail = i['stream_icon']   
                if option_lecture == "MPEG":      
                    url = url_sygma+":"+port_sygma+"/"+username+"/"+password+"/"+stream_id
                elif option_lecture == "TS":
                    url = url_sygma+":"+port_sygma+"/live/"+username+"/"+password+"/"+stream_id+".ts"
                elif option_lecture == "Default(HLS)":
                    url = url_sygma+":"+port_sygma+"/live/"+username+"/"+password+"/"+stream_id+".m3u8"
                
                addLinkTv(url.encode('utf-8'),name.encode('utf-8', 'ignore'),thumbnail.encode('utf-8'),num,stream_id)
                num+=1                   
def addLinkTv(url,name,iconimage,num,stream_id):
    if not name:
        name= langue(32050)
    try:
        name = name.encode('utf-8')
    except: pass

    if not iconimage:
        iconimage= icon         
    
    try:
        iconimage = iconimage.encode('utf-8')
    except: pass
    
    if num <= 9:
        num = "00"+str(num)
    elif num <=99:
        num = "0"+str(num)
    namenum = str(num)+"  "+ name   
    if option_lecture == "Default(HLS)":
        mode = '19'
    else:
        mode = "18"      
    u=sys.argv[0]+"?"
    u += "url="+urllib.quote_plus(url)+"&mode="+mode+"&streamId="+str(stream_id)
    liz=xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "Title": namenum })
    liz.setProperty("Fanart_Image", tv_fanart)
    liz.setProperty('IsPlayable', 'true')
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)

def getSources(sources): 
    sourcefinal=source_api
    with open(sourcefinal) as f:
        sources = json.load(f)
        if len(sources) >= 1:            
            for i in sources:
                thumb = icon
                mode_show = '1'
                mode_lecture = '1'
                fanart = FANART
                title = langue(32050)
                if i.has_key('mode'):
                    mode_show = int(i['mode'])
                if i.has_key('type_select'):
                    mode_lecture = i['type_select']
                if i.has_key('thumbnail'):
                    thumb = i['thumbnail']
                if i.has_key('fanart'):
                    fanart = i['fanart']
                if i.has_key('title'):
                    title = i['title']
                    if "++"in title :
                        title=title.replace('++','')
                        title = langue(int(title))
                addDir(title.encode('utf-8'),i['url'].encode('utf-8'),mode_show,mode_lecture,thumb,fanart,'source') 

def addDir(name,url,mode,mode_lecture,iconimage,fanart,showcontext=False): 

    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "Title": name,"tracknumber": mode_lecture })
    liz.setProperty("Fanart_Image", fanart)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

def getCategorie(source): 
    try:
        response = urllib2.urlopen(source)
        sources = json.load(response)
    except urllib2.URLError as err:
        return ErrerConextionServeur()                       
    if len(sources) >= 1:
        if "user_info" in sources:
            yes()
        num =1
        numero =0
        for i in sources:
            category_id =''
            category_name = ''
            parent_id = ''
            thumb = icon
            fanart = play_fanart
            if i.has_key('category_id'):
                category_id =i['category_id']
            if i.has_key('category_name'):
                category_name = i['category_name']
            if i.has_key('parent_id'):
                parent_id = i['parent_id']
            numero+=1             
            if mode==1: #LIVE 
                mode2 = "2"
                url = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action=get_live_streams&category_id="+category_id
                addDirCat(i['category_name'].encode('utf-8'),url.encode('utf-8'),category_id,parent_id,thumb,tv_fanart,mode2,numero,i['category_name'].encode('utf-8'))           
            elif mode==5: # MOVIE 
                mode2 = "6"
                url = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action=get_vod_streams&category_id="+category_id
                addDirCat(i['category_name'].encode('utf-8'),url.encode('utf-8'),category_id,parent_id,thumb,play_fanart,mode2,numero,i['category_name'].encode('utf-8'))            
            elif mode==8: #SERIES
                mode2 = "9"
                url = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action=get_series&category_id="+category_id       
                addDirCat(i['category_name'].encode('utf-8'),url.encode('utf-8'),category_id,parent_id,thumb,fanart,mode2,numero,i['category_name'].encode('utf-8'))
            elif mode == 20:
                mode2 = "12"
                mylistreplay = addon.getSetting("category")                
                if category_id in mylistreplay:
                    url = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action=get_live_streams&category_id="+category_id                                    
                    addDirCat(i['category_name'].encode('utf-8'),url.encode('utf-8'),category_id,parent_id,thumb,tv_fanart,mode2,num,i['category_name'].encode('utf-8'))
                    num+=1
                                    
def addDirCat(name,url,category_id,parent_id,iconimage,fanart,mode2,numero,title):
    if numero < 10 :
        numero = "0"+str(numero)
    name = str(numero)+"  "+str(name)
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode2)+"&name="+urllib.quote_plus(title)+"&fanart="+urllib.quote_plus(fanart)
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=icon)
    liz.setInfo(type="Video", infoLabels={ "Title": name, "code": parent_id})
    liz.setProperty("Fanart_Image", fanart)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True) 

def ouvertureSource():
    addon_log("getSources")
    getSources(source_api)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True) 
    getViewMode(508,"Fanart")
    xbmc.executebuiltin("Container.SetSortMethod(1)")

def TestDeConextionclient():
    try:  
        response=urllib2.urlopen('http://google.fr') 
        return   
    except urllib2.URLError as err: pass
    return ErrerConextion()

def getAdressMac():
    macaddress = xbmc.getInfoLabel('Network.MacAddress')
    if (":") in macaddress :
        addon.setSetting("mac_adresse",macaddress)
    else :
        macaddress = xbmc.getInfoLabel('Network.MacAddress')
        if (":") in macaddress :
            addon.setSetting("mac_adresse",macaddress)
        else :
           time.sleep(1)
           getAdressMac()
def getViewMode(mode,name):
        
    time.sleep(0.1)
    xbmc.executebuiltin("Container.SetViewMode("+str(mode)+")")
    modeview=xbmc.getInfoLabel('Container.Viewmode') 
    time.sleep(0.3)
    i = 0
    while i < 5 :       
        if name == modeview :
            sys.exit() 
        else :
            getViewMode(mode,name)
            i+=1

def getSerialNumber():
    letters = string.ascii_letters
    result_str = ''.join(random.sample(letters, 1))
    numeriques = string.digits
    result_int_1 = ''.join(random.sample(numeriques, 5))
    result_int_2 = ''.join(random.sample(numeriques, 5))
    resultat= "K"+result_int_1+result_str+result_int_2
    addon.setSetting("serieal_nb",resultat) 

def textview():
    data = langue(32054)
    dialog = xbmcgui.Dialog()
    dialog.textviewer(langue(32051),data)
    sys.exit()

def addon_log(string):
    if debug == 'true':
        xbmc.log("["+my_api+"-%s]: %s" %(addon_version, string)) 
def getParametre():
    xbmcaddon.Addon(id=my_api).openSettings()
    # xbmcaddon.Addon(id=my_api).openSettings()s
    xbmc.executebuiltin("RunPlugin(plugin://"+my_api+"/?mode=None)")
    SleepTime(40)
    # ouvertureSource()
    sys.exit()

def SleepTime(toolbar_width):
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))
    for i in xrange(toolbar_width):
       time.sleep(0.1) 
       sys.stdout.write("-")
       sys.stdout.flush()
    sys.stdout.write("\n") 

def changeLanguage():
    country = addon.getSetting('country')
    if country == "ENGLISH":
        xbmc.executebuiltin("XBMC.RunScript(script.embuary.helper,action=setkodisetting,setting=locale.language,value=resource.language.en_gb)")

    elif country == "FRANCE":
        xbmc.executebuiltin("XBMC.RunScript(script.embuary.helper,action=setkodisetting,setting=locale.language,value=resource.language.fr_fr)")

    elif country == "ENGLISH (US)":
        xbmc.executebuiltin("XBMC.RunScript(script.embuary.helper,action=setkodisetting,setting=locale.language,value=resource.language.en_us)")
  
    elif country == "DUTCH":
        xbmc.executebuiltin("XBMC.RunScript(script.embuary.helper,action=setkodisetting,setting=locale.language,value=resource.language.nl_nl)")
    
    elif country == "ITALIAN":
        xbmc.executebuiltin("XBMC.RunScript(script.embuary.helper,action=setkodisetting,setting=locale.language,value=resource.language.it_it)")
        
    elif country == "PORTUGUESE":
        xbmc.executebuiltin("XBMC.RunScript(script.embuary.helper,action=setkodisetting,setting=locale.language,value=resource.language.pt_pt)")
        
    elif country == "SPANISH":
        xbmc.executebuiltin("XBMC.RunScript(script.embuary.helper,action=setkodisetting,setting=locale.language,value=resource.language.es_es)")
           
def get_params():       
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]

    return param

def getDataSaison(url):
    getSoup(url)
    getItemsSaisons(url) 

def getItemsSaisons(source):
    try:
        response = urllib2.urlopen(source)
        infoplus = json.load(response)
    except urllib2.URLError as err:
        return ErrerConextionServeur() 

    serie_id = serieId
    Titel = ""
    cover = ""
    genre = ""
    plot = ""
    releasedate = ""
    backdrop_path = ""
    youtube_trailer = ""
    fanart=play_fanart
    if len(infoplus) >= 1:
        
        if "info" in infoplus:
            series = infoplus['info']
            if series.has_key('name'):
                try:
                    Titel = series['name'].encode('utf-8', 'ignore') 
                except: pass    
            if series.has_key('cover'):
                try:
                    cover = series['cover'].encode('utf-8')
                except: pass    
            if series.has_key('genre'):
                try:
                    genre = series['genre'].encode('utf-8')
                except: pass    
            if series.has_key('plot'):
                try:
                    plot = series['plot'].encode('utf-8')
                except: pass    
            if series.has_key('releaseDate'):
                releasedate = series['releaseDate']
            if series.has_key('backdrop_path'):
                backdrop_path = series['backdrop_path']
            if series.has_key('youtube_trailer'):
                youtube_trailer = series['youtube_trailer']

        elif "series" in infoplus:
            series = infoplus['series']
            if series.has_key('title'):
                try:
                    Titel = series['title'].encode('utf-8', 'ignore')
                except: pass     
            if series.has_key('cover'):
                try:
                    cover = series['cover'].encode('utf-8')
                except: pass    
            if series.has_key('genre'):
                try:
                    genre = series['genre'].encode('utf-8')
                except: pass    
            if series.has_key('plot'):
                try:
                    plot = series['plot'].encode('utf-8')
                except: pass    
            if series.has_key('releaseDate'):
                releasedate = series['releaseDate']
            if series.has_key('backdrop_path'):
                backdrop_path = series['backdrop_path']
            if series.has_key('youtube_trailer'):
                youtube_trailer = series['youtube_trailer']
           
            releasedate = releasedate.replace(" ","")
            releasedate = releasedate.replace("Date","")
            releasedate = releasedate.replace(":","")
            releasedate = releasedate.replace("-","/")
            releasedate = releasedate.rstrip()
            genre = genre.replace(" ","")
            genre = genre.replace(",","/")
       
        if isinstance(backdrop_path, list):
            try:
                fanart = backdrop_path[0].encode('utf-8')
            except: pass    
        else:
           fanart = play_fanart                             

        try:
            if "youtube" in youtube_trailer : 
                a = urlparse(youtube_trailer)
                youtube_trailer=os.path.basename(a.path)
                youtube_trailer="plugin://plugin.video.youtube/play/?video_id="+youtube_trailer
            elif "http://" in youtube_trailer :
                youtube_trailer = youtube_trailer
            elif  len(youtube_trailer) > 4  :
                youtube_trailer="plugin://plugin.video.youtube/play/?video_id="+youtube_trailer
        except: pass
        
        if not youtube_trailer:
            addDirSeason(youtube_trailer,Titel,cover,serie_id,plot,releasedate,fanart,genre,rating,director,option="2",nbr="")
        else:      
            addDirSeason(youtube_trailer,Titel,cover,serie_id,plot,releasedate,fanart,genre,rating,director,option="0",nbr="")

    if len(infoplus) >= 1:
        if "episodes" in infoplus :
            if len(infoplus["episodes"]) >= 1:
                total_season = len(infoplus["episodes"])
                list_season = infoplus["episodes"]
            i = 0
            while i < total_season:
                n = i+1
                title = "Season "+str(n)
                addDirSeason(source,title,cover,serie_id,plot,releasedate,fanart,genre,rating,director,option="1",nbr=str(n))
                i = i +1

def addDirSeason(url,name,cover,series_id,plot,releaseDate,fanart,genre,rating,director,option,nbr):
    releaseDate = releaseDate.replace("-","/")
    if option == "0": 
        mode ="3"
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideoCover.png", thumbnailImage="sygma/Trailer_eye.jpg")
        liz.setInfo(type="Video", infoLabels={ "title": name, "trailer":cover, "status":"3", "Plot":plot, "genre":genre,"set":rating, "director":releaseDate})
        liz.setProperty("Fanart_Image", play_fanart)
        liz.setProperty('IsPlayable', 'true')
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz) 

    elif option == "1":
        mode = "11" 
        try:   
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&saisonId="+str(nbr)
        except:  
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&saisonId="+int(nbr)
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideoCover.png", thumbnailImage="sygma/Saison_"+str(nbr)+".jpg")
        liz.setInfo(type="Video", infoLabels={ "title": name, "trailer":cover,"status":"4"}) 
        liz.setProperty("Fanart_Image", play_fanart)
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

    if option == "2": 
        mode ="3"  
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideoCover.png", thumbnailImage="sygma/Info_eye.jpg")
        liz.setInfo(type="Video", infoLabels={ "title": name, "trailer":cover, "status":"5", "Plot":plot, "genre":genre,"set":rating, "director":releaseDate})
        liz.setProperty("Fanart_Image", play_fanart)
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz) 

def getEpisode():
    stream_id = ""
    title =langue(32050)
    plot =""
    movie_image = icon
    releasedate = ""
    container_extension =""
    fanart = play_fanart
    IdS = str(saisonId)
    try:
        response = urllib2.urlopen(url)
        infoplus = json.load(response)
    except urllib2.URLError as err:
        return ErrerConextionServeur()    

    if len(infoplus) >= 1:
        if "info" in infoplus:
            series= infoplus["info"]
            try:
                if series.has_key('backdrop_path'):

                    backdrop_path = series['backdrop_path']
                    if isinstance(backdrop_path, list):
                        try:
                            fanart = backdrop_path[0].encode('utf-8')
                        except: pass    
                    else:
                       fanart = play_fanart
            except: pass
        
        if "episodes" in infoplus :
            if len(infoplus["episodes"]) >= 1:
                list_season = infoplus["episodes"]
        else:
            xbmcgui.Dialog().ok(langue(32030),langue(32031))
            sys.exit()        
    else:
        xbmcgui.Dialog().ok(langue(32030),langue(32031))
        sys.exit()
    if len(list_season) >= 1:
            
            try:
                mysaisson = list_season[IdS]
            except :
                try:
                    ids =int(IdS)-1
                    mysaisson = list_season[ids]
                except :
                    sys.exit() 

            if len(mysaisson) >= 1:
                
                for i in mysaisson:
                    try:
                        if i.has_key('id'):
                            stream_id = i['id']
                    except: pass        
                    try:    
                        if i.has_key('title'):
                            title = i['title'].encode('utf-8', 'ignore')
                    except: pass

                    try:        
                        if i.has_key('container_extension'):
                            container_extension = "."+i['container_extension']
                    except: pass

                    try:        
                        if i.has_key('stream_icon'):
                            movie_image = "."+i['stream_icon']
                    except: pass
                    
                    try:     
                        if i.has_key('info'):
                            info = i['info']
                            try:
                                if info.has_key("movie_image"):
                                    movie_image = info['movie_image'].encode('utf-8')   
                            except: pass    
                        
                            try:
                                if info.has_key("plot"):
                                    plot = info['plot'].encode('utf-8', 'ignore')
                            except: pass    
                            
                            try:
                                if info.has_key("releasedate"):
                                    releasedate = info['releasedate'].encode('utf-8') 
                            except: pass 
                    except: pass
                    if  stream_id !="" :         
                        addDirEpisode(title,stream_id,movie_image,plot,releasedate,container_extension,fanart)
            else:
                xbmcgui.Dialog().ok(langue(32030),langue(32031))
                sys.exit()                   
    else:
        xbmcgui.Dialog().ok(langue(32030),langue(32031))
        sys.exit()                                  
                            
def addDirEpisode(name,stream_id,iconimage,plot,releasedate,container_extension,fanart):
    url = url_sygma+":"+port_sygma+"/series/"+username+"/"+password+"/"+str(stream_id)+container_extension 
    mode = "3"
    if releasedate == '':
        releasedate = None
    else:
        plot += '\n\nDate: %s' %releasedate
    u=sys.argv[0]+"?"
    u += "url="+urllib.quote_plus(url)+"&mode="+mode    
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "Title": name, "plot": plot})
    liz.setProperty("Fanart_Image", fanart)
    liz.setProperty('IsPlayable', 'true')
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)

def theMovie():    
    
    dialog = xbmcgui.Dialog()
    type_vod = []
    type_vod.append(langue(32037))
    type_vod.append(langue(32038))
    type_info=dialog.select("Type",type_vod)
    if type_info == 0:
        namefilme = dialog.input(langue(32035), type=xbmcgui.INPUT_ALPHANUM)

        if namefilme != "":
            searchByName(namefilme,1) 
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
            time.sleep(0.1)
            xbmc.executebuiltin("Container.SetViewMode(500)")
        else :
            
            xbmcgui.Dialog().ok(langue(32045),langue(32052))
            sys.exit()
        
    elif type_info == 1:
        nameserie = dialog.input(langue(32044), type=xbmcgui.INPUT_ALPHANUM)

        if nameserie != "":
            searchByNameserie(nameserie,1) 
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
            time.sleep(0.1)
            xbmc.executebuiltin("Container.SetViewMode(500)")
        else:
            xbmcgui.Dialog().ok(langue(32045),langue(32053))
            sys.exit()
    else:
        sys.exit()        
####################################### sa se pour la demande de serie ################################################
def rechercheSerie(val,option,country): #recherche serie par id
    backdrop_path=FANART
    poster_path=icon
    nbr_saisson = ""
    number_of_episodes = ""
    date = ""
    id_serie = ""
    genre = ""
    title = ""
    desc = ""
    rating = ""
    video = ""
    id_key = ""
    urltrailar = ""
    name = ""
    nbr_episode = ""
    icon_saison = ""    
    urlserie = "http://hamza-kodi.ddns.net/source/api.php"
    if option == 1 :

        urlserie+="?idtv="+str(val)+"&country="+country 
        try:
            response = urllib2.urlopen(urlserie)
            urlserie = json.load(response)
        except urllib2.URLError as err:
            return ErrerConextionServeur()   
    else:
        sys.exit()
    if len(urlserie) >= 1:
        if "success" in urlserie:
            xbmcgui.Dialog().ok(langue(32045),langue(32046))            
            sys.exit()           
        else:            
            if urlserie.has_key('backdrop_path'):        
                backdrop_path = "https://image.tmdb.org/t/p/w533_and_h300_bestv2"+str(urlserie['backdrop_path'])
            if urlserie.has_key('poster_path'):
                poster_path ="https://image.tmdb.org/t/p/w220_and_h330_face"+str(urlserie['poster_path'])
                
            if urlserie.has_key("number_of_seasons"):
                nbr_saisson = urlserie['number_of_seasons']
            if urlserie.has_key("number_of_episodes"):
                number_of_episodes = urlserie['number_of_episodes']
            if urlserie.has_key("first_air_date"):
                date = urlserie['first_air_date']
                try:
                    date = date.encode('utf-8', 'ignore')
                except: pass
            if urlserie.has_key("id"):
                id_serie = str(urlserie['id'])
            if urlserie.has_key("genres"):
                gen = urlserie['genres']
                if not genre:
                    genre= langue(32050)

                if isinstance(gen, list):
                    for i in gen:
                        if i.has_key('name'):
                            genre+=i['name']+"/"
                            try:
                                genre = genre.encode('utf-8', 'ignore')
                            except: pass
                    
            if urlserie.has_key("original_name"):
                title = urlserie['original_name']
            if urlserie.has_key("overview"):
                desc = urlserie['overview']
                try:
                    desc = desc.encode('utf-8', 'ignore')
                except: pass
               
            if urlserie.has_key("vote_average"):
                rating = urlserie['vote_average']
                try:
                    rating = rating.encode('utf-8', 'ignore')
                except: pass
            if urlserie.has_key("videos"):
                if urlserie['videos'].has_key("results"):
                    video=urlserie['videos']['results']
                    if isinstance(video, list):                        
                        try:
                            if video[0].has_key('key'):
                                id_key = video[0]['key']
                            if video[0].has_key('name'):
                                urltrailar = video[0]['name']
                        except: pass
                    if  urltrailar !="":

                        addDirSeriedemande(title,id_serie,backdrop_path,poster_path,id_key,date,rating,genre,desc,lecture=True,nbr="")

            if urlserie.has_key("seasons"):
                seasons = urlserie['seasons']
                if isinstance(seasons, list):
                   n =  1
                   for i in seasons:
                        if i.has_key('name'):
                            name=i['name']
                            
                        if i.has_key('episode_count'):
                            nbr_episode=i['episode_count']
                        if i.has_key('poster_path'):
                            icon_saison="https://image.tmdb.org/t/p/w220_and_h330_face"+str(i['poster_path'])
                        if i.has_key('air_date'):
                            air_date=i['air_date'] 
                            try:
                                air_date = air_date.encode('utf-8', 'ignore')
                            except: pass                                       
                        if name != "":
                            titre= title+ " ( [COLOR red] "+name+" [/COLOR])"
                                                    
                            addDirSeriedemande(titre,id_serie,icon_saison,poster_path,id_key,air_date,rating,genre,desc,lecture=False,nbr=str(n))
                            n +=1   
            addDirSeriedemande("Demande serie",id_serie,backdrop_path,poster_path,id_key,date,rating,genre,desc,lecture="False",nbr="")        
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
            time.sleep(0.1)
            xbmc.executebuiltin("Container.SetViewMode(508)")
            sys.exit()

def addDirSeriedemande(title,idthe,icon,fanart,key,date,rating,genre,desc,lecture,nbr):    
    if not date:
        date= langue(32050)
    if not genre:
        genre= langue(32050) 
    if not rating:
        rating= langue(32050)
    if not desc:
        desc= langue(32050)
    if lecture == True:
        mode = "3"
        url = "plugin://plugin.video.youtube/play/?video_id="+str(key)

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(title)+"&serieId="+str(idthe)
        if genre != "":
            genre = genre[0:-1]
        liz=xbmcgui.ListItem(title, iconImage="DefaultFolder.png", thumbnailImage="sygma/Trailer_eye.jpg") 
        liz.setInfo(type="Video", infoLabels={ "title": title , "set":rating, "genre":genre, "director":date, "plot":desc, "trailer":icon, "status": "1"})
        liz.setProperty("Fanart_Image", str(fanart))
        liz.setProperty('IsPlayable', 'true')
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)

    elif lecture == False:
        mode = "100"        
        u=sys.argv[0]+"?mode="+str(mode)+"&name="+title+"&serieId="+str(idthe)
        if genre != "":
            genre = genre[0:-1]
        if not iconimage :
            pass   
        else:
            icon = iconimage               
        liz=xbmcgui.ListItem(title, iconImage="DefaultFolder.png", thumbnailImage="sygma/Saison_"+str(nbr)+".jpg")       
        liz.setInfo(type="Video", infoLabels={ "title": title , "set":rating, "genre":genre, "director":date, "plot":desc, "trailer":icon ,"status": "4"})
        liz.setProperty("Fanart_Image", fanart)
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)

    else:
        mode = "20"   
        u=sys.argv[0]+"?mode="+str(mode)+"&name="+urllib.quote_plus(title)+"&serieId="+str(idthe)
        if genre != "":
            genre = genre[0:-1]
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage="sygma/Alert_eye.jpg")
        liz.setInfo(type="Video", infoLabels={ "title": title , "set":rating, "genre":genre, "director":date, "plot":desc, "trailer":icon ,"status": "2"})
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)

def searchByNameserie(val,nb):#recherche serie par name

    total_pages=""
    page_nbr=""
    results=""
    poster_path=icon
    idthe=""
    backdrop_path=FANART
    title=""    
    urlbyname = "http://hamza-kodi.ddns.net/source/api.php"
 
    try:
        resp = requests.post(urlbyname,{'npage': nb, 'search': val})
        response = resp.json()
    except urllib2.URLError as err:
        return ErrerConextionServeur()
    if "success"  in response :

        xbmcgui.Dialog().ok(langue(32045),langue(32047))
        sys.exit()
    if "total_pages" in response and "page" in response and "results" in response:
        total_pages = response["total_pages"]
        page_nbr = response["page"]
        results = response["results"]
        
    else:
        sys.exit()   
    for i in results:
        if i.has_key('poster_path'):
            try:
               poster_path = i["poster_path"].encode('utf-8')
            except: pass    
        
        if i.has_key('id'):
            try:
               idthe = i["id"]
            except: pass
        
        if i.has_key('backdrop_path'):
            try:
               backdrop_path = i["backdrop_path"].encode('utf-8')
            except: pass 

        if i.has_key('original_title'):    
            try:
               title = i["original_title"].encode('utf-8','ignore')
            except: pass 
            
        if idthe != "":
            adddemendeserie(title,poster_path,backdrop_path,idthe,page_nbr,val)

    if total_pages > page_nbr :
        page_nbr = page_nbr +1
        adddemendeserie("Next",icon,FANART,"none",page_nbr,val)
    
def adddemendeserie(name,icon,fanart,idthe,page,val):
    
    if idthe == "none":
        mode = "17"  #sa ce pour page suivant serie    
        u=sys.argv[0]+"?mode="+str(mode)+"&name="+urllib.quote_plus(val)+"&serieId="+str(page)
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage="sygma/PageNext2_eye.jpg")
        liz.setInfo(type="Video", infoLabels={ "title": name })
        liz.setProperty("Fanart_Image", fanart)
         
    else:
        fanart = "https://image.tmdb.org/t/p/w533_and_h300_bestv2"+fanart
        icon = "https://image.tmdb.org/t/p/w220_and_h330_face"+icon
        mode = "16" #pour appeler le fileme par id appel function rechercheSerie
        u=sys.argv[0]+"?mode="+str(mode)+"&name="+urllib.quote_plus(val)+"&serieId="+str(idthe)+"&iconimage="+icon   
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=icon)
        liz.setInfo(type="Video", infoLabels={ "title": name  })
        liz.setProperty("Fanart_Image", fanart)
           
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

####################################### sa se pour la demande de film ################################################ 
def recherchemovie(val,option,country):#recherche movie par id 
    backdrop_path=FANART
    poster_path=icon
    id_film=""
    title=""
    id_db=""
    rating=""
    date=""
    desc=""
    genre=""
    id_key=""
    urltrailar=""
    urlmovie = "http://hamza-kodi.ddns.net/source/api.php"
    if option == 0 :
        urlmovie+="?id="+str(val)+"&country="+country 
        try:
            response = urllib2.urlopen(urlmovie)
            urlmovie = json.load(response)
        except urllib2.URLError as err:
            return ErrerConextionServeur()        
    else:
        sys.exit()
                
    if len(urlmovie) >= 1:
            
        if "success" in urlmovie:
            xbmcgui.Dialog().ok(langue(32045),langue(32046))            
            sys.exit()           
        else:
            if urlmovie.has_key('id'):
                id_film = str(urlmovie['id'])
            else:
                xbmcgui.Dialog().ok(langue(32045),langue(32046))  
                sys.exit()
            if urlmovie.has_key('backdrop_path'):        
                backdrop_path = "https://image.tmdb.org/t/p/w533_and_h300_bestv2"+str(urlmovie['backdrop_path'])
            if urlmovie.has_key('poster_path'):
                poster_path ="https://image.tmdb.org/t/p/w220_and_h330_face"+str(urlmovie['poster_path'])     
            if urlmovie.has_key("title"):
                title = urlmovie['title']
            if urlmovie.has_key("imdb_id"):
                id_db = urlmovie['imdb_id']
            if urlmovie.has_key("overview"):
                desc = urlmovie['overview']
            if urlmovie.has_key("vote_average"):
                rating = str(urlmovie['vote_average'])
            if urlmovie.has_key("release_date"):
                date = urlmovie['release_date']
                date = date.replace(" ","")
                date = date.replace("Date","")
                date = date.replace(":","")
                date = date.replace("-","/")
                date = date.rstrip()
            if urlmovie.has_key("genres"):
                gen = urlmovie['genres']
                if isinstance(gen, list):
                    for i in gen:
                        if i.has_key('name'):
                            genre+=i['name']+"/"
            if urlmovie.has_key("videos"):
                if urlmovie['videos'].has_key("results"):
                    video=urlmovie['videos']['results']
                    if isinstance(video, list):                        
                        try:
                            if video[0].has_key('key'):
                                id_key = video[0]['key']
                            if video[0].has_key('name'):
                                urltrailar = video[0]['name']
                        except: pass
                              
            if  urltrailar !="":
                addDirfilmdemande(title,id_film,poster_path,backdrop_path,date,rating,id_db,id_key,genre,urltrailar,desc,lecture=True)

            addDirfilmdemande(title,id_film,poster_path,backdrop_path,date,rating,id_db,id_key,genre,urltrailar,desc,lecture=False)
            addDirfilmdemande("Demande film",id_film,poster_path,backdrop_path,date,rating,id_db,id_key,genre,urltrailar,desc,lecture="False")
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
            time.sleep(0.1)
            xbmc.executebuiltin("Container.SetViewMode(508)")
            sys.exit()


def addDirfilmdemande(title,idthe,icon,fanart,date,rating,id_db,key,genre,urltrailar,desc,lecture):
    if not date:
        date= langue(32050)
    if not genre:
        genre= langue(32050) 
    if not rating:
        rating= langue(32050)
    if not desc:
        desc= langue(32050)
    if lecture == True:
        mode = "3"
        url = "plugin://plugin.video.youtube/play/?video_id="+str(key)

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(title)+"&serieId="+str(idthe)
        if genre != "":
            genre = genre[0:-1]
        liz=xbmcgui.ListItem(title, iconImage="DefaultFolder.png", thumbnailImage="sygma/Trailer_eye.jpg") 
        liz.setInfo(type="Video", infoLabels={ "title": title , "set":rating, "genre":genre, "director":date, "plot":desc, "trailer":icon, "status": "1"})
        liz.setProperty("Fanart_Image", str(fanart))
        liz.setProperty('IsPlayable', 'true')
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)

    elif lecture == False:
        mode = "100"        
        u=sys.argv[0]+"?mode="+str(mode)+"&name="+urllib.quote_plus(title)+"&serieId="+str(idthe)
        if genre != "":
            genre = genre[0:-1]
        if not iconimage :
            pass   
        else:
            icon = iconimage    
        liz=xbmcgui.ListItem(title, iconImage="DefaultFolder.png", thumbnailImage=icon)         
        liz.setInfo(type="Video", infoLabels={ "title": title , "set":rating, "genre":genre, "director":date, "plot":desc, "trailer":icon ,"status": "5"})
        liz.setProperty("Fanart_Image", fanart)
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)

    else:
        mode = "20"   
        u=sys.argv[0]+"?mode="+str(mode)+"&name="+urllib.quote_plus(title)+"&serieId="+str(idthe)
        if genre != "":
            genre = genre[0:-1]
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage="sygma/Alert_eye.jpg")
        liz.setInfo(type="Video", infoLabels={ "title": title , "set":rating, "genre":genre, "director":date, "plot":desc, "trailer":icon ,"status": "2"})

        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)

def searchByName(val,nb):#recherche movie par name
    total_pages=""
    page_nbr=""
    results=""
    poster_path=""
    idthe=""
    backdrop_path=""
    title=""    
    urlbyname = "http://hamza-kodi.ddns.net/source/api.php"
    try:
        resp = requests.post(urlbyname,{'page': nb, 'search': val})
        response = resp.json()
    except urllib2.URLError as err:
        return ErrerConextionServeur()   
    if "success"  in response :
        xbmcgui.Dialog().ok(langue(32045),langue(32047))
        sys.exit()
    if "total_pages" in response and "page" in response and "results" in response:
        total_pages = response["total_pages"]
        page_nbr = response["page"]
        results = response["results"]
        
    else:
        sys.exit()   
    for i in results:
        if i.has_key('poster_path'):
            try:
               poster_path = i["poster_path"].encode('utf-8')
            except: pass    
        
        if i.has_key('id'):
            try:
               idthe = i["id"]
            except: pass
        
        if i.has_key('backdrop_path'):
            try:
               backdrop_path = i["backdrop_path"].encode('utf-8')
            except: pass 

        if i.has_key('original_title'):    
            try:
               title = i["original_title"].encode('utf-8','ignore')
            except: pass 
        

        if idthe != "":
            adddemendeFilm(title,poster_path,backdrop_path,idthe,page_nbr,val)

    if total_pages > page_nbr :
        page_nbr = page_nbr +1
        adddemendeFilm("Next",icon,FANART,"none",page_nbr,val)

def adddemendeFilm(name,icon,fanart,idthe,page,val):
    
    if idthe == "none":
        mode = "15"  #sa ce pour page suivant     
        u=sys.argv[0]+"?mode="+str(mode)+"&name="+urllib.quote_plus(val)+"&serieId="+str(page)
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage="sygma/PageNext2_eye.jpg")
        liz.setInfo(type="Video", infoLabels={ "title": name })
        liz.setProperty("Fanart_Image", fanart)
         
    else:
        fanart = "https://image.tmdb.org/t/p/w533_and_h300_bestv2"+fanart
        icon = "https://image.tmdb.org/t/p/w220_and_h330_face"+icon
        mode = "14" #pour appeler le fileme par id appel function rechercheparid
        u=sys.argv[0]+"?mode="+str(mode)+"&name="+urllib.quote_plus(val)+"&serieId="+str(idthe)+"&iconimage="+icon   
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=icon)
        liz.setInfo(type="Video", infoLabels={ "title": name  })
        liz.setProperty("Fanart_Image", fanart)
            
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

def getreplay(sources):

    try:
        response = urllib2.urlopen(sources)        
        sources = json.load(response)
        json_live = json.dumps(sources)
        fichier = open(dest, "w")                
        fichier.write(json_live)      
        fichier.close()
    except urllib2.URLError as err:
        return ErrerConextionServeur()

    if len(sources) >= 1:
        num = 1
        for i in sources:
            name = ""
            stream_id = ""
            thumbnail = ""
            tv_archive = ""
            if i.has_key('tv_archive'):
                tv_archive = i['tv_archive']
            if i.has_key('name'):
                name = i['name']
            if i.has_key('stream_id'):
                stream_id = str(i['stream_id'])       
            if i.has_key('stream_icon'):
                thumbnail = i['stream_icon']            
            if tv_archive == 1 :
                url = url_sygma+":"+port_sygma+"/"+username+"/"+password+"/"+stream_id            
                addLinkReplay(url.encode('utf-8'),name.encode('utf-8', 'ignore'),thumbnail.encode('utf-8'),num,stream_id)
                num+=1 

def addLinkReplay(url,name,iconimage,num,stream_id):
    if not name:
        name= langue(32050)
    if not iconimage:
        iconimage= icon         
    try:
        name = name.encode('utf-8')
    except: pass
    try:
        iconimage = iconimage.encode('utf-8')
    except: pass
    namenum = str(num)+"  "+ name
    mode = '13'
    u=sys.argv[0]+"?"
    u += "url="+urllib.quote_plus(url)+"&mode="+mode+"&streamId="+str(stream_id)
    liz=xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "Title": namenum })
    liz.setProperty("Fanart_Image", tv_fanart)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

def replay():
    chplusid=xbmc.getInfoLabel('Container(id).CurrentItem')
    name=xbmc.getInfoLabel('Container(id).ListItemAbsolute('+chplusid+').Label')                    
    try:
        sourcesepg = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action=get_simple_data_table&stream_id="+str(streamId)
        response = urllib2.urlopen(sourcesepg)        
        sources = json.load(response)
    except urllib2.URLError as err:
        return ErrerConextionServeur() 
    if len(sources) >= 1:                                                   
        title = ""
        datedebut = ""
        playing = ""
        archive = ""
        if sources.has_key("epg_listings"):
            gen = sources['epg_listings']
            cn=0
            listepg = []
            if gen == []: 
                with open(dest) as f:
                    data = json.load(f)
                    if len(data) >= 1:
                        name = ""
                        stream_id = "" 
                        cover=icon    
                        for i in data:                                          
                            if i.has_key('stream_id'):
                                stream_id = i['stream_id']
                            if str(streamId) == str(stream_id):
                                if i.has_key('tv_archive_duration'):
                                    duration_day = i['tv_archive_duration']
                date=[]
                z = 0
                m=1
                y =int(duration_day)
                today = time.time()
                aujouduit = today
                aujouduit = datetime.fromtimestamp(aujouduit)
                aujouduit = str(aujouduit)
                aujouduit = aujouduit[0:10]
                date.append(str(aujouduit))
                while z < y:
                    
                    day_moins = int(86400)
                    day = int(today)-day_moins*m
                    day = datetime.fromtimestamp(day)
                    day = str(day)
                    day = day[0:10]
                    date.append(str(day))
                    z+=1
                    m+=1
                dateday = xbmcgui.Dialog().select(langue(32095),date)
                
                if dateday >=0:
                    if dateday ==0:
                        today = time.time()
                        heusmain = datetime.fromtimestamp(today)
                        heusmain = str(heusmain)
                        heusmain = heusmain[11:13]
                        heusmain = int(heusmain)
                        heurs=[]
                        m = 0                  
                        while m < heusmain-1 :
                            if int(m) <= 9:
                                y = "0"+str(m)
                                heurs.append(str(y))
                            else:
                                heurs.append(str(m))
                            m+=1
                        heurdate = xbmcgui.Dialog().select(langue(32096),heurs)
                    else:
                        heurs=[]
                        m = 0
                        x=24                    
                        while m < x :
                            if int(m) <= 9:
                                y = "0"+str(m)
                                heurs.append(str(y))
                            else:
                                heurs.append(str(m))
                            m+=1
                        heurdate = xbmcgui.Dialog().select(langue(32096),heurs)                                 
                    if heurdate >=0:
                        minute=[]
                        a = 0
                        b=60                    
                        while a < b :
                            if int(a) <= 9:
                                c = "0"+str(a)
                                minute.append(str(c))
                            else:
                                minute.append(str(a))
                            a+=1
                        mindate = xbmcgui.Dialog().select(langue(32097),minute)
                        if mindate >= 0 :
                            duration = xbmcgui.Dialog().numeric(0, langue(32098))
                            if duration :
                                datefinale = str(date[dateday])+":"+str(heurs[heurdate])+"-"+str(minute[mindate])
                                url = url_sygma+":"+port_sygma+"/streaming/timeshift.php?username="+username+"&password="+password+"&stream="+streamId+"&start="+datefinale+"&duration="+str(duration)
                                with open(dest) as f:
                                    data = json.load(f)
                                    if len(data) >= 1:
                                        name = ""
                                        stream_id = "" 
                                        cover=icon    
                                        for i in data:                                          
                                            if i.has_key('stream_id'):
                                                stream_id = i['stream_id']
                                            if str(streamId) == str(stream_id):
                                                if i.has_key('name'):
                                                    name =i['name']                                            
                                                if i.has_key('stream_icon'):
                                                    cover =i['stream_icon']     
                                playlist = xbmc.PlayList(1)
                                playlist.clear()
                                name =  name+" REPLAY" 
                                info = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=cover)
                                playlist.add(url,info)
                                xbmc.executebuiltin('playlist.playoffset(video,0)')
                                sys.exit()
                            else:
                                sys.exit()    
                        else:
                            sys.exit()
                    else:
                        sys.exit()       
                else:
                    sys.exit()                                                               
            else:
                for i in gen:

                    if i.has_key('has_archive'):
                        archive =i['has_archive']

                    if i.has_key('title'):
                        title = base64.b64decode(i['title'])
                        try: 
                            title = title.encode("utf-8")
                        except:
                            pass                               
                    if i.has_key('now_playing'):
                        playing =i['now_playing']
                    if archive == 1 :
                        if i.has_key('start'):
                            datedebut = i['start']
                            datedebut = str(datedebut)
                            datedebuttitle = datedebut[0:16]
                            datedebuttitlefin = datedebuttitle.replace("-","/")
                            datedebuturl = datedebuttitle.replace(":","-")
                            datedebuturl = datedebuturl.replace(" ",":")
                            title = str(datedebuttitlefin) +" "+title
                            if i.has_key('stop_timestamp'):
                                stoptime = i['stop_timestamp']
                            if i.has_key('start_timestamp'):
                                starttime = i['start_timestamp']
                            dur=int(stoptime)-int(starttime)
                            duration = int(dur)/60
                            with open(dest) as f:
                                data = json.load(f)
                                if len(data) >= 1:
                                    name = ""
                                    stream_id = "" 
                                    cover=icon    
                                    for i in data:                                          
                                        if i.has_key('stream_id'):
                                            stream_id = i['stream_id']
                                        if str(streamId) == str(stream_id):
                                            if i.has_key('stream_icon'):
                                                cover =i['stream_icon']  
                        url = url_sygma+":"+port_sygma+"/streaming/timeshift.php?username="+username+"&password="+password+"&stream="+streamId+"&start="+datedebuturl+"&duration="+str(duration)
                        addLinkT(url.encode('utf-8'),title,cover)
                               
def addLinkT(url,name,cover):
    mode = "3"
    u=sys.argv[0]+"?"
    u += "url="+urllib.quote_plus(url)+"&mode="+mode
    liz=xbmcgui.ListItem(name, iconImage=icon , thumbnailImage=cover)
    liz.setInfo(type="Video", infoLabels={ "Title": name })
    liz.setProperty("Fanart_Image", tv_fanart)
    liz.setProperty('IsPlayable', 'true')
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False) 


def activecode():
    coded = addon.getSetting('coded')
    pin = addon.getSetting('pin')
    try:
	    urlcode = check_apk+"?code="+str(coded)+"&pin="+str(pin)
	    response = urllib2.urlopen(urlcode,timeout=20)        
	    sources = json.load(response)
    except:
        xbmcgui.Dialog().ok("Error","About time to come")
        sys.exit()
    username=""
    password=""
    msg=""
    code=""
    typpe=""
    if len(sources) >= 1:       
        code = sources['code']
        username = sources['username']
        password = sources['password']   
        msg = sources['msg']
        addon.setSetting("coded",str(code))
        addon.setSetting("username",username)
        addon.setSetting("password",password)
        if not password:
        	xbmcgui.Dialog().notification("Error",str(msg), xbmcgui.NOTIFICATION_ERROR, 13000 , True)
    	else:	
    		xbmcgui.Dialog().notification(str(coded),str(msg), xbmcgui.NOTIFICATION_INFO, 13000 , False)
 
def changLangue(option):
                      
    dialog = xbmcgui.Dialog()    
    lang=[]
    lang.append("original")
    lang.append("fr")
    lang.append("en")
    lang.append("it")
    lang.append("es")
    lang.append("de")    
    country = dialog.select(langue(32042),lang)
    if country == 0 :
        country=""
    elif country == 1 or country == 2 or country == 3 or country == 4 or country == 5  :
        country = lang[country] 
    else:
        sys.exit()
    if option == 0:
        recherchemovie(serieId,0,country)
    else:
        rechercheSerie(serieId,1,country)

def clearCash():
    path = xbmc.translatePath('special://temp')

    if os.path.exists(path):
        for f in os.listdir(path):
            fpath = os.path.join(path, f)
            try:
                if os.path.isfile(fpath):
                    if not fpath.lower().endswith('.log'):
                        os.unlink(fpath)
                elif os.path.isdir(fpath):
                    shutil.rmtree(fpath)
            except Exception as e:
                print e
   
    path = xbmc.translatePath('special://home/addons/packages')

    if os.path.exists(path):
        for f in os.listdir(path):
            fpath = os.path.join(path, f)
            try:
                if os.path.isfile(fpath):
                    os.unlink(fpath)
            except Exception as e:
                print e
    
    sys.exit()
    
xbmcplugin.setContent(int(sys.argv[1]), 'movies')
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_DATE)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_GENRE)
except:
    pass
params=get_params()
url=None
show=None
mode_lecture=None
name=None
mode=None
iconimage=None
fanart=FANART
playlist=None
fav_mode=None
serieId=None
streamId=None
saisonId=None
extension=None
director=None
rating=None
numid=None
try:
    url=urllib.unquote_plus(params["url"]).decode('utf-8')
except:
    pass
try:
    name=urllib.unquote_plus(params["name"])
    try:
        name.decode('utf-8',"ignore")
    except:
        pass  
except:
    pass
try:
    iconimage=urllib.unquote_plus(params["iconimage"])
    try:
        iconimage.decode('utf-8',"ignore")
    except:
        pass    
except:
    pass    
try:
    serieId=urllib.unquote_plus(params["serieId"])
except:
    pass
try:
    extension=urllib.unquote_plus(params["extension"])
except:
    pass    
try:
    streamId=urllib.unquote_plus(params["streamId"])
except:
    pass        
try:
    fanart=urllib.unquote_plus(params["fanart"])
except:
    pass
try:
    mode=int(params["mode"])  
except:
    pass
try:
    saisonId=int(params["saisonId"])  
except:
    pass   
try:
    playlist=eval(urllib.unquote_plus(params["playlist"]).replace('|',','))
except:
    pass
try:
    fav_mode=int(params["fav_mode"])
except:
    pass
try:
    director=urllib.unquote_plus(params["director"])
except:
    pass
try:
    rating =urllib.unquote_plus(params["rating"])
except:
    pass
try:
    numid =urllib.unquote_plus(params["numid"])
except:
    pass
      
addon_log("Mode: "+str(mode))
if not url is None:
    addon_log("URL: "+str(url.encode('utf-8')))
    if url == "++info++":  
        getInfoAbo()
        sys.exit()
    if url == "++raccourcis++":
        textview()
        sys.exit()
    if url == "++settings++":
        getParametre()
        sys.exit()   
    if url == "++play++":
        url = source_api = os.path.join(xbmc.translatePath("special://home/addons/"+my_api+"/resources"), 'play')
    if url == "++fm++":
        url = domainename+"/source/fm"
    if url =="++demande++" :
        TestDeConextionclient()
        theMovie()
        sys.exit() 
    if url =="++active_code++" :
        activecode()
               
addon_log("Name: "+str(name))

if mode==None:
    changeLanguage()     
    if theme_ok == "0" :        
        newskin()
        getAdressMac()
        getSerialNumber()
        addon.setSetting("theme_ok",'1')
        addon.setSetting('category','0')
        xbmc.executebuiltin("RunAddon(plugin."+my_api+")")               
    else:
    	if coded == "" or pin == "" or coded =="None":
    		xbmcaddon.Addon(id=my_api).openSettings()
    		sys.exit()
        elif password == "" :
            activecode()

        nameSkin=xbmc.getSkinDir()
        if nameSkin == "skin.confluence" :			
	        ouvertureSource()              
	        RemotePlay(0)
	        xbmc.executebuiltin("roload.Refresh")
        else:
        	 xbmc.executebuiltin("XBMC.RunScript(script.embuary.helper,action=setkodisetting,setting=lookandfeel.skin,value=skin.confluence)")
        	 sys.exit()

elif mode==1:
    TestDeConextionclient()
    try:
        sources = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action="+url
    except :
        ErrerConextionServeur()
    mode_lecture=xbmc.getInfoLabel('ListItem.TrackNumber')
    xbmc.executebuiltin("XBMC.RunScript(script.embuary.helper,action=setkodisetting,setting=myvideos.selectaction,value="+mode_lecture+")")
    addon_log("getCategorie")
    getCategorie(sources)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)    
    getViewMode(503,"Media info 2")

elif mode==2:
    addon_log("getBouquet")
    getBouquet(url)
    addon.setSetting('category_name',str(name))
    addon.setSetting("numch","")
    addon.setSetting("timech","0")
    RemotePlay(1)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True) 
    getViewMode(504,"Media info")

        
elif mode==3:

    # file = open(dir_profile+"/replay.strm", "w") 
    # file.write(url) 
    # file.close()
    # sys.exit()
    addon_log("setResolvedUrl")    
    item = xbmcgui.ListItem(path=url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)

      
elif mode==4:    
    addon_log("getSources")
    getSources(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True) 
    getViewMode(508,"Fanart") 

elif mode==5:
    TestDeConextionclient() 
    try:
        sources = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action="+url
    except :
        ErrerConextionServeur()
    mode_lecture=xbmc.getInfoLabel('ListItem.TrackNumber')
    xbmc.executebuiltin("XBMC.RunScript(script.embuary.helper,action=setkodisetting,setting=myvideos.selectaction,value="+mode_lecture+")")
    addon_log("getCategorie")
    getCategorie(sources)   
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)    
    getViewMode(503,"Media info 2")
    RemotePlay(2)

elif mode==6:
    addon_log("getData")
    getData(url)  
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True) 
    getViewMode(500,"Thumbnail")

elif mode==7:
    addon_log("getInfoFilm")
    getInfoFilm(url)
    RemotePlay(2)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True) 
    getViewMode(508,"Fanart")
 
elif mode==8:
    TestDeConextionclient() 
    try:
        sources = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action="+url
    except :
        ErrerConextionServeur()
    addon_log("getCategorie")
    getCategorie(sources) 
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)       
    getViewMode(503,"Media info 2")

elif mode==9:
    addon_log("getData")
    getData(url)  
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True) 
    getViewMode(500,"Thumbnail")
   
elif mode==10:
    addon_log("getDataSaison")
    getDataSaison(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)   
    getViewMode(508,"Fanart")

   
elif mode==11: 
    addon_log("getDataSaison")
    getEpisode()  
    RemotePlay(2)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True) 
    getViewMode(515,"Media info 3")
   
elif mode==12:
    addon_log("getreplay")
    getreplay(url) 
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)
    addon.setSetting('category_name',str(name))
    RemotePlay(3)
    getViewMode(504,"Media info")

elif mode == 13:
    replay()
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True) 
    getViewMode(504,"Media info")
    
elif mode==14:
    changLangue(0) 
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True) 
    getViewMode(508,"Fanart")

elif mode==15:       
    searchByName(name,serieId)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True) 
    getViewMode(500,"Thumbnail")

elif mode==16:
    changLangue(1)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True) 
    getViewMode(508,"Fanart")

elif mode==17:   
    searchByNameserie(name,serieId)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True) 
    getViewMode(500,"Thumbnail")

elif mode==18:
    num=xbmc.getInfoLabel('Container(id).CurrentItem')                  
    with open(dest) as f:
        data = json.load(f)
        if len(data) >= 1:
            name = ""
            stream_id = ""
            cover=icon    
            for i in data:                                          
                if i.has_key('stream_id'):
                    stream_id = i['stream_id']
                if str(streamId) == str(stream_id):
                    if i.has_key('name'):
                        name =i['name']
                        name = name.replace("u00a0","")
                        try:
                            name = name.encode("utf-8")
                        except:pass
                    if i.has_key('stream_icon'):
                        cover =i['stream_icon']
                        try:
                            cover = cover.encode("utf-8")
                        except:pass  
    
    if "--"  in name:
        sys.exit()           
    try:
        xbmcgui.Dialog().notification(str(num), str(name), str(cover), 8000 , False) 
    except:pass 
    addon_log("setResolvedUrl")    
    item = xbmcgui.ListItem(path=url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    addon.setSetting("stream_id",streamId)
elif mode == 19:

    is_helper = inputstreamhelper.Helper('hls', drm="com.widevine.alpha")
    if is_helper.check_inputstream():
        play_item = xbmcgui.ListItem(path=url)
        play_item.setContentLookup(False)
        if int(xbmc.getInfoLabel('System.BuildVersion').split('.')[0]) >= 19:
            play_item.setProperty('inputstream', is_helper.inputstream_addon)
        else:
	        play_item.setProperty('inputstreamaddon', is_helper.inputstream_addon)
        play_item.setProperty('inputstream.adaptive.manifest_type', 'hls')
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, play_item)
        addon.setSetting("stream_id",streamId)        
    
    # xbmcgui.Dialog().ok("ok",str(num)) 
    with open(dest) as f:
        data = json.load(f)
        if len(data) >= 1:
            # name = ""
            stream_id = ""
            # num=""  
            cover=icon    
            for i in data:                                          
                if i.has_key('stream_id'):
                    stream_id = i['stream_id']
                if str(streamId) == str(stream_id):
                    if i.has_key('name'):
                        name =i['name']
                    # if i.has_key('num'):
                        # num =i['num']
                    if i.has_key('stream_icon'):
                        cover =i['stream_icon']  
    if "--"  in name:
        sys.exit()
    try:
        num=xbmc.getInfoLabel('Container(id).CurrentItem')
        xbmcgui.Dialog().notification(str(num), str(name), str(cover), 8000, False)
    except:pass
elif mode==20:
    TestDeConextionclient()
    try:    
        sources = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action=get_live_streams" 
        response = urllib2.urlopen(sources)        
        sources = json.load(response)       
    except:
        ErrerConextionServeur()
    
    if len(sources) >= 1:
        cn=0
        my_list = []
        for i in sources:              
            name = ""
            stream_id = ""
            thumbnail = ""
            tv_archive = ""
            if i.has_key('tv_archive'):
                tv_archive = i['tv_archive']                                              
                if tv_archive == 1:
                    if i.has_key('category_id'):
                        category_id = i['category_id']
                        my_list.append(str(category_id))                                               
        mylist = list(dict.fromkeys(my_list))
        mylist=str(mylist)
        mylist = mylist.replace("'","")
        mylist = mylist.replace("[","")
        mylist = mylist.replace("]","")
        mylist = mylist.split(", ")
        addon.setSetting('category',str(mylist))
    try:    
        sources = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action="+url
    except :
        ErrerConextionServeur()
    mode_lecture=xbmc.getInfoLabel('ListItem.TrackNumber')
    xbmc.executebuiltin("XBMC.RunScript(script.embuary.helper,action=setkodisetting,setting=myvideos.selectaction,value="+mode_lecture+")")
    addon_log("getCategorie")
    getCategorie(sources)
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)        
    getViewMode(503,"Media info 2")


elif mode == 21:
    xbmc.executebuiltin("PlayMedia("+url+"),1")
