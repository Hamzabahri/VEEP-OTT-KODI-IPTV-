# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcplugin, xbmcaddon,sys
import base64
import urllib
import urllib2
import os
import time
import shutil
from datetime import datetime
try:
    import json
except:
    import simplejson as json

my_api = "plugin.veep.ott"
addon = xbmcaddon.Addon(my_api)
url_sygma = addon.getSetting('url_sygma')
port_sygma = addon.getSetting('port_sygma')
kodi_image = addon.getSetting('kodi_image')
player_api = addon.getSetting('player_api')
username = addon.getSetting('username')
password = addon.getSetting('password')
profile = xbmc.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
epg = os.path.join(profile, 'epg')
short_epg = os.path.join(profile, 'short_epg')
stream = addon.getSetting('stream_id')
dialog = xbmcgui.Dialog()
dest = os.path.join(profile, 'live')
langue = addon.getLocalizedString

with open(dest) as f:
    data = json.load(f)
    if len(data) >= 1:
        name = ""
        stream_id = ""
        archive=""      
        for i in data:   
                                   
            if i.has_key('stream_id'):
                stream_id = i['stream_id']
            if str(stream) == str(stream_id):
                if i.has_key('name'):
                    name =i['name']
                    archive = i['tv_archive'] 
    sourcesepg = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action=get_short_epg&stream_id="+str(stream)
    response = urllib2.urlopen(sourcesepg)        
    sources = json.load(response)  
    if len(sources) >= 1:           
        if sources.has_key("epg_listings"):
            gen = sources['epg_listings']

if gen == []: 
    xbmcgui.Dialog().notification(str(name), langue(32088), xbmcgui.NOTIFICATION_INFO, 8000 ,False)
    sys.exit()
else: 
    epglist = []                                
    titles = []
    titles.append(name+langue(32085))
    titles.append(name+langue(32086))
    epglist=dialog.select(name,titles)
    

    if epglist == 0:
        sourcesepg = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action=get_short_epg&stream_id="+str(stream)
        response = urllib2.urlopen(sourcesepg)        
        sources = json.load(response)   
        if len(sources) >= 1:
            date = "" 
            desc = ""                                                  
            title = ""
            start_timestamp = ""
            stop_timestamp = ""
            if sources.has_key("epg_listings"):
                gen = sources['epg_listings']                    
                date = gen[0]['start']
                date = date [0:10]
                date = date.replace("-","/")
                try:
                    date = date.encode('utf-8')
                except:
                    pass
                var =date+"\n\r"
                for i in gen:
                    if i.has_key('description'):
                        desc = base64.b64decode(i['description'])
                        try: 

                            desc = desc.encode("utf-8")
                        except:
                            pass

                    if i.has_key('title'):

                        title = base64.b64decode(i['title'])

                        try: 
                            title = title.encode("utf-8")
                        except:
                            pass   
                        
                        title = title.upper()
                    if i.has_key('start_timestamp'):
                        start_timestamp = i['start_timestamp']
                        start_timestamp = datetime.fromtimestamp(int(start_timestamp))
                        start_timestamp = str(start_timestamp)
                        start_timestamp = start_timestamp[11:16]

                    if i.has_key('stop_timestamp'):
                        stop_timestamp = i['stop_timestamp'] 
                        stop_timestamp = datetime.fromtimestamp(int(stop_timestamp))
                        stop_timestamp = str(stop_timestamp)
                        stop_timestamp = stop_timestamp[11:16]
                    var+="\n\r"+str(start_timestamp)+" - "+str(stop_timestamp)+"  "+"[COLOR darkorange]"+title+"[/COLOR]"+"\n\r"+desc+"\n\r"+"\n\r"                      
                xbmcgui.Dialog().textviewer(str(name),var)
     

    elif epglist == 1:
        sourcesepg = url_sygma+":"+port_sygma+"/"+player_api+"?username="+username+"&password="+password+"&action=get_simple_data_table&stream_id="+str(stream)
        response = urllib2.urlopen(sourcesepg)        
        sources = json.load(response)        
        if len(sources) >= 1:                                                   
            title = ""
            desc = ""
            start_timestamp = ""
            stop_timestamp = ""
            if sources.has_key("epg_listings"):
                gen = sources['epg_listings']
                var =""
                for i in gen:
                    if i.has_key('description'):
                        desc = base64.b64decode(i['description'])
                        try: 

                            desc = desc.encode("utf-8")
                        except:
                            pass

                    if i.has_key('title'):
                        title = base64.b64decode(i['title'])
                        try: 
                            title = title.encode("utf-8")
                        except:
                            pass   
                        title = title.upper()

                    if i.has_key('start_timestamp'):
                        time_star = i['start_timestamp']
                        start_timestamp = datetime.fromtimestamp(int(time_star))
                        start_timestamp = str(start_timestamp)
                        start_timestamp = start_timestamp[0:16]
                        start_timestamp = start_timestamp.replace("-","/")
                        start_timestamp = start_timestamp.replace(" ","  ")

                    if i.has_key('stop_timestamp'):
                        stop_timestamp = i['stop_timestamp'] 
                        stop_timestamp = datetime.fromtimestamp(int(stop_timestamp))
                        stop_timestamp = str(stop_timestamp)
                        stop_timestamp = stop_timestamp[11:16]
                        ts = time.time()
                    if float(time_star) >= float(ts) :        
                        var+="\n\r"+str(start_timestamp)+" - "+str(stop_timestamp)+"  "+"[COLOR darkorange]"+title+"[/COLOR]"+"\n\r"+desc+"\n\r"+"\n\r"  
                xbmcgui.Dialog().textviewer(str(name),var)
    else:
        sys.exit()
    
                            
                            

            
            
                



