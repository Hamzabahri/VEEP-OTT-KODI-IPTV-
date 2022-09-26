# -*- coding: utf-8 -*-
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

addon = xbmcaddon.Addon('plugin.veep.ott')
profile = xbmc.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
dest = os.path.join(profile, 'live')
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
icon = os.path.join(home, 'icon.png')
numch=addon.getSetting('numch')
timech=addon.getSetting('timech')
dialog = xbmcgui.Dialog()
langue = addon.getLocalizedString
time.sleep(1.5)
if xbmc.getCondVisibility('VideoPlayer.IsFullscreen'):
  xbmc.executebuiltin("Action(FullScreen)")
time.sleep(1.5)
with open(dest) as f:
    data = json.load(f)
    if len(data) >= 1:
        num = ""    
        for i in data:                      
            if i.has_key('num'):
                num = i['num']
  
numch=addon.getSetting('numch')
intnumch=int(numch) 
numeroid=xbmc.getInfoLabel('Container(id).CurrentItem')
if intnumch == 0:
  xbmcgui.Dialog().notification(langue(32083), str(numch), icon, 8000 ,False)
  xbmc.executebuiltin("ActivateWindow(12005,return)")
  addon.setSetting('timech','0')
  addon.setSetting("numch","")
  sys.exit()

if intnumch <= num:
   numeroid=int(numeroid)     
   if intnumch < numeroid :
     totalnum=(int(numeroid)-int(intnumch))
     suy=str(totalnum)
     i = 0
     y = int(suy)
     while i < y:         
       xbmc.executebuiltin("Action(Up)")
       i = i +1
       if(i==y):
         xbmc.executebuiltin("Action(Select)")
         addon.setSetting('timech','0')
         addon.setSetting("numch","")
         sys.exit()           
   elif intnumch > numeroid :
     totalnum=(int(intnumch)-int(numeroid))
     suy=str(totalnum)   
     i = 0
     y= int(suy)
     while i < y:
       xbmc.executebuiltin("Action(Down)")         
       i = i +1
       if(i==y):
           xbmc.executebuiltin("Action(Select)")
           addon.setSetting('timech','0')
           addon.setSetting("numch","")
           sys.exit()
   elif intnumch == numeroid:
        xbmc.executebuiltin("Action(Select)")
        addon.setSetting('timech','0')
        addon.setSetting("numch","")
        sys.exit()    
   else :
     if xbmc.getCondVisibility('Player.HasVideo')==False:
        xbmc.executebuiltin("Action(Select)")
        addon.setSetting('timech','0')
        addon.setSetting("numch","")
        sys.exit()
     else:        
      xbmc.executebuiltin("ActivateWindow(12005,return)")
      addon.setSetting('timech','0')
      addon.setSetting("numch","")
      sys.exit() 
else:
  if xbmc.getCondVisibility('Player.HasVideo')==True:
    xbmc.executebuiltin("ActivateWindow(12005,return)")
    xbmcgui.Dialog().notification(langue(32083), str(numch), icon, 8000 , False)
    addon.setSetting('timech','0')
    addon.setSetting("numch","")
    sys.exit()      
sys.exit()