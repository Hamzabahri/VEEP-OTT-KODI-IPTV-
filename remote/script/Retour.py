# -*- coding: utf-8 -*-
import xbmc
import sys
import os
import shutil
import xbmcgui, xbmcplugin, xbmcaddon, time
my_api = "plugin.veep.ott"
addon = xbmcaddon.Addon(my_api)
langue = addon.getLocalizedString
genXml = os.path.join(xbmc.translatePath('special://userdata/keymaps'), 'gen.xml')
keyplayTV=os.path.join(xbmc.translatePath('special://home/addons/'+my_api+'/remote'), 'gen.xml')
xbmc.executebuiltin("Action(Back)")

shutil.copy(keyplayTV,genXml)
if xbmc.getCondVisibility('Player.HasVideo')==True:
	xbmc.executebuiltin("Action(Stop)")

  
