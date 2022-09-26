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
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
icon = os.path.join(home, 'icon.png')
url_sygma = addon.getSetting('url_sygma')
port_sygma = addon.getSetting('port_sygma')
username = addon.getSetting('username')
password = addon.getSetting('password')
timech=addon.getSetting('timech')
numch=addon.getSetting('numch')
player_api = addon.getSetting('player_api')
dialog = xbmcgui.Dialog()
id_stream = addon.getSetting('stream_id')
option_lecture = addon.getSetting('option')
langue = addon.getLocalizedString
if numch =="":
    addon.setSetting('timech','0')
    addon.setSetting('numch','')
    sys.exit()
addon.setSetting('timech','1')
with open(dest) as f:
    data = json.load(f)
    if len(data) >= 1:
        name = ""
        cover=""
        cn = 1
        num = 1
        for i in data:
            stream_id = ""
            if i.has_key('stream_id'):
                stream_id = i['stream_id']
            if i.has_key('stream_icon'):
                cover=i['stream_icon']
            if cn == int(numch):
                name = i['name']
                if option_lecture == "MPEG":      
                    urla = url_sygma+":"+port_sygma+"/"+username+"/"+password+"/"+str(i['stream_id'])
                elif option_lecture == "TS":
                    urla = url_sygma+":"+port_sygma+"/live/"+username+"/"+password+"/"+str(i['stream_id'])+".ts"
                elif option_lecture == "Default(HLS)":
                    urla = url_sygma+":"+port_sygma+"/live/"+username+"/"+password+"/"+str(i['stream_id'])+".m3u8"
                break
            if "--" not in name:    
                cn+=1 
                num+=1                      
        if str(id_stream) == str(stream_id):
            addon.setSetting('timech','0')
            addon.setSetting('numch','')
            try:
                xbmcgui.Dialog().notification(str(numch), str(name), str(cover), 8000 , False)
            except:pass
            sys.exit()
        if not name :
            xbmcgui.Dialog().notification(langue(32083), str(numch), xbmcgui.NOTIFICATION_INFO, 8000 , False)
            addon.setSetting('timech','0')
            addon.setSetting('numch','')
            sys.exit()
        try:
            xbmcgui.Dialog().notification(str(numch), str(name), str(cover), 8000 , False) 
        except:pass
        name = str(num)+" "+ name
        playlist = xbmc.PlayList(1)
        playlist.clear()
        item = cn
        info = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=cover)
        playlist.add(urla,info)
        xbmc.executebuiltin('playlist.playoffset(video,0)')        
        addon.setSetting('timech','0')
        addon.setSetting('numch','')
        addon.setSetting("stream_id",str(stream_id))


sys.exit()        

        
        

               