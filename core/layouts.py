# -*- coding: utf-8 *-*
#Frame2.py
import wx
from core.constants import *
 
class Frame2(wx.Frame):

    def __init__(self, none, dia, mes, ano):
        wx.Frame.__init__(
            self,
            None,
            title="Informacion de "+str(dia)+" "+FECHA_MES[mes]+" "+str(ano)+" - "+APP_TITLE,           #........................................................................................Titulo de la Ventana
            size=(1024, 750),       #........................................................................................Tamano de la Ventana
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
        )
        self.run(None, dia, mes, ano)
        self.Centre(True)


    def  run(self, none, dia, mes, ano):
    	self.favicon = wx.Icon(
            IMAGENES[0],           #........................................................................................Ruta del Icono a mostrar
            wx.BITMAP_TYPE_ICO,    #........................................................................................Tipo de imagen
            16,                    #........................................................................................Ancho
            16                     #........................................................................................Alto
        )

        wx.Frame.SetIcon(
            self,
            self.favicon           #........................................................................................Invocamos el Icono
        )

        self.panel = wx.Panel(
            self                   #........................................................................................Panel Principal
        )

        self.panel.SetBackgroundColour(
            "#F1F1F1"                  #........................................................................................Color de fondo para el panel
        )

        kinrev = int(ANOS[str(ano)]) + int(MESES[str(mes)]) + int(dia)
        if kinrev > 260:
        	kinrev = kinrev-260
        	tonorev = TONO[kinrev]
        else:
        	tonorev = TONO[kinrev]
        	
        sellorev = SELLO[str(kinrev)]

        nombsello = NAMESELLO[int(sellorev)]

        calantipoda = sellorev + 10
        calanalogo = 19 - sellorev
        caloculto = 21 - sellorev

        nobantipoda = NAMESELLO[int(calantipoda)]
        nobanalogo = NAMESELLO[int(calanalogo)]
        noboculto = NAMESELLO[int(caloculto)]

        self.kin = wx.StaticText(self.panel, label="KIN: "+str(kinrev), pos=(71.1, 125.733))
        self.sello = wx.StaticText(self.panel, label="SELLO: "+nombsello, pos=(150.1, 125.733))
        self.tono = wx.StaticText(self.panel, label="TONO: "+str(tonorev), pos=(250.1, 125.733))
        self.antipoda = wx.StaticText(self.panel, label="ANTIPODA: "+nobantipoda, pos=(450.1, 125.733))
        self.analogo = wx.StaticText(self.panel, label="ANALOGO: "+nobanalogo, pos=(550.1, 125.733))
        self.oculto = wx.StaticText(self.panel, label="OCULTO: "+noboculto, pos=(650.1, 125.733))


    def OnExit(self, evt):
        self.Close(True)
		