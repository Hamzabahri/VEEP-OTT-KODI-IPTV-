import xbmc, xbmcgui, xbmcplugin, xbmcaddon, time, sys, urllib, urllib2
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import os
import zipfile 
import os.path 
import glob 
import re
import sys

try:
    import json
except:
    import simplejson as json

my_api = "plugin.veep.ott"
addon = xbmcaddon.Addon(my_api)
profile = xbmc.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
dest = os.path.join(profile, 'live')
category = os.path.join(profile, 'category')
url_sygma = addon.getSetting('url_sygma')
port_sygma = addon.getSetting('port_sygma')
username = addon.getSetting('username')
password = addon.getSetting('password')
dialog = xbmcgui.Dialog()
name_cate = addon.getSetting('category_name')
epg = os.path.join(profile, 'epg')
player_api = addon.getSetting('player_api')
short_epg = os.path.join(profile, 'short_epg')
option_lecture = addon.getSetting('option')
with open(dest) as f:
    data = json.load(f)
    if len(data) >= 1:
        name = ""
        stream_id = ""
        numero=1
        cover=""
        tv_archive=""
        listch = []       
        for i in data:                      
            if i.has_key('stream_id'):
                stream_id = i['stream_id']
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
                if numero < 10:
                    numero = "00"+str(numero)
                elif numero < 100:
                    numero = "0"+str(numero)
                name = str(numero)+"  "+ name 
                numero = int(numero)
                listch.append(name)
            numero+=1
        numeroCH = xbmc.getInfoLabel('Player.Title')
        splitnumeroCH= numeroCH.split(' ')
        numerochannel=int(splitnumeroCH[0])-1
        listchannel=dialog.select(name_cate,listch , preselect=numerochannel )

        if  listchannel >= 0  :
            num = int(listchannel)+1
            name = data[listchannel]['name']
            cover = data[listchannel]['stream_icon'] 
            stream_id = data[listchannel]['stream_id']

            if option_lecture == "MPEG":      
                urla = url_sygma+":"+port_sygma+"/"+username+"/"+password+"/"+str(stream_id) 
            elif option_lecture == "TS":
                urla = url_sygma+":"+port_sygma+"/live/"+username+"/"+password+"/"+str(stream_id) +".ts"
            elif option_lecture == "Default(HLS)":
                urla = url_sygma+":"+port_sygma+"/live/"+username+"/"+password+"/"+str(stream_id) +".m3u8"
            try:
                xbmcgui.Dialog().notification(str(num), str(name), str(cover), 8000 , False)
            except:pass              
            if listchannel == numerochannel:
                sys.exit()
            else:
                playlist = xbmc.PlayList(1)
                playlist.clear()
                name = str(num)+" "+ name
                info = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=cover)
                playlist.add(urla,info)
                xbmc.executebuiltin('playlist.playoffset(video,0)')
                addon.setSetting("stream_id",str(stream_id))  
        else:
            sys.exit()
    
