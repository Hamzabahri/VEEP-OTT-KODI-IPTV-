# -*- coding: utf-8 -*-
#https://kodi.wiki/view/tList_of_built-in_functions
import sys
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
# from urllib.parse import urlparse 
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

import string
try:
    import json
except:
    import simplejson as json

domainename = "http://hamza-kodi.ddns.net"
my_api = "plugin.veep.ott"
addon = xbmcaddon.Addon(my_api)
langue = addon.getLocalizedString
boot = addon.getSetting('boot')
version = addon.getSetting('version')
deletimage = addon.getSetting('delateImg')
urllink = domainename+"/source/update"
DossierIMG = os.path.join(xbmc.translatePath('special://userdata/Thumbnails'))
def ErrerConextionServeur():
    xbmcgui.Dialog().ok("[COLOR white]"+langue(32003)+"[/COLOR] [COLOR red]![/COLOR]","[COLOR red]"+langue(32021)+"[/COLOR] ") 
    sys.exit()
def misajour(version,urllink):
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
			
			
		if urllink[0].has_key('delateImg'):
			delateImg = urllink[0]['delateImg']	
				
	if  versionup > version:

		xbmcgui.Dialog().ok(langue(32023),"\n\r"+"\n\r" +langue(32024)  +versionup)   
		addon.setSetting("version",versionup)
	if deletimage < delateImg :
		if os.path.exists(DossierIMG)==True :
			shutil.rmtree(DossierIMG)
			xbmc.executebuiltin("Container.Refresh")
			xbmc.executebuiltin('Skin.ToggleSetting(DebugGrid)')
			addon.setSetting("delateImg",delateImg)
			xbmcgui.Dialog().ok('redémarrage ','votre application doit être redémarré')
			xbmc.executebuiltin("Quit")
			raise
			sys.exit()

def download (urllink):
    dp = xbmcgui.DialogProgress()
    dp.create(langue(32001),langue(32002))
    urllib.urlretrieve(urllink,dest,lambda nb, bs, fs, urllink=urllink: barretelechargemnet(nb,bs,fs,urllink,dp)) 

def barretelechargemnet(numblocks, blocksize, filesize, lin=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)# variabl
        print (percent)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        dp.close()
 
ok=misajour(version,urllink)
if ok:
	if boot =="true":
		xbmc.executebuiltin("RunAddon(plugin.veep.ott)")
else:
	if boot =="true":
		xbmc.executebuiltin("RunAddon(plugin.veep.ott)")		

	

	
