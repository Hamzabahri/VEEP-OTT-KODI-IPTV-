#PLAY
import xbmc, xbmcgui, xbmcplugin, xbmcaddon, time
import sys
my_api = "plugin.veep.ott"
addon = xbmcaddon.Addon(my_api)
langue = addon.getLocalizedString
# hhh=xbmc.getInfoLabel('Container(id).FolderPath')
# xbmcgui.Dialog().ok("ok",str(hhh))
# sys.exit()
Idback=xbmc.getInfoLabel('Container(id).CurrentItem') 
if str(Idback) == "0":
  sys.exit() 
if xbmc.getCondVisibility('VideoPlayer.IsFullscreen'):
  dialog = xbmcgui.Dialog()
  
  Bouquet_TV = dialog.select(langue(32077), [langue(32078), langue(32079), langue(32080), langue(32081),langue(32082)])
 


  if Bouquet_TV==0:
      xbmc.executebuiltin("ActivateWindow(10123,return)")       

  elif Bouquet_TV==1:
      xbmc.executebuiltin("ActivateWindow(10124,return)")

  elif Bouquet_TV==2:
      xbmc.executebuiltin("ActivateWindow(10159,return)")    

  elif Bouquet_TV==3 :
      xbmc.executebuiltin("Action(stop)")

  elif Bouquet_TV ==4 :
      xbmc.executebuiltin("ActivateWindow(12005,return)")#PLAINE ECRANT
          
else :

  PlayerTitleIN="nul"
  IdURL=xbmc.getInfoLabel('Container(id).CurrentItem')
  Titel_TV=xbmc.getInfoLabel('Container(id).ListItemAbsolute('+IdURL+').Label')

  if xbmc.getCondVisibility('Player.HasVideo')==True: 
    PlayerTitleIN=xbmc.getInfoLabel('Player.Title')


  if PlayerTitleIN == Titel_TV:
    xbmc.executebuiltin("ActivateWindow(12005,return)")#PLAINE ECRANT

  else:
    xbmc.executebuiltin("Action(Select)")


sys.exit()




    