# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcplugin, xbmcaddon, time, sys, urllib, urllib2, os
my_api = "plugin.veep.ott"
addon = xbmcaddon.Addon(my_api)
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
icon = os.path.join(home, 'icon.png')
numch=addon.getSetting('numch')
timech=addon.getSetting('timech')
dialog = xbmcgui.Dialog()
numbr=str(sys.argv[1])
N = numch+numbr
addon.setSetting("numch",N)
dialog.notification('', N,icon, 3000,False)
time.sleep(3)
if timech == "0":  
    xbmc.executebuiltin("RunScript(special://home/addons/plugin.veep.ott/remote/script/numero.py)")

    

