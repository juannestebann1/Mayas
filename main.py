# -*- coding: utf-8 *-*
import datetime
import wx
from core.constants import *
#from core.layouts import *


class SincronarioMaya(wx.Frame):

    def __init__(self, none, title):
        wx.Frame.__init__(
            self,
            none,
            title=title,           #........................................................................................Titulo de la Ventana
            size=(700, 400),       #........................................................................................Tamano de la Ventana
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
        )

        self.run()
        self.Centre(True)

    def run(self):

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
            FONDO                  #........................................................................................Color de fondo para el panel
        )

        self.logo = wx.StaticBitmap(self.panel, pos=(244.163, 29.673)) #....................................................logotipo
        self.logo.SetFocus()       #........................................................................................Enfoque
        self.logo.SetBitmap(wx.Bitmap(IMAGENES[1])) #.......................................................................LLamamos el Logotipo

        self.dia = wx.StaticText(self.panel, label="Dia:", pos=(71.1, 125.733)) #...........................................Dias
        self.mes = wx.StaticText(self.panel, label="Mes:", pos=(257.63, 125.733)) #.........................................Mes
        self.ano = wx.StaticText(self.panel, label="A&#241;o:", pos=(444.16, 125.733)) #.........................................Año

        self.TBDia = wx.TextCtrl(self.panel, pos=(71.1, 158.733), size=(176.53, 44))
        self.TBMes = wx.TextCtrl(self.panel, pos=(257.63, 158.733), size=(176.53, 44))
        self.TBA = wx.TextCtrl(self.panel, pos=(444.16,158.733), size=(176.53, 44))

        self.boton = wx.Button(self.panel, label="enviar", pos=(70.2, 270.066), size=(559.6, 44.6))

        self.fontD = self.dia.GetFont()
        self.fontD.SetPointSize(18)
        self.dia.SetFont(self.fontD)
        self.fontM = self.mes.GetFont()
        self.fontM.SetPointSize(18)
        self.mes.SetFont(self.fontM)
        self.fontA = self.ano.GetFont()
        self.fontA.SetPointSize(18)
        self.ano.SetFont(self.fontA)
        self.fontAs = self.TBA.GetFont()
        self.fontAs.SetPointSize(18)
        self.TBA.SetFont(self.fontAs)
        self.fontMs = self.TBMes.GetFont()
        self.fontMs.SetPointSize(18)
        self.TBMes.SetFont(self.fontMs)
        self.fontDs = self.TBDia.GetFont()
        self.fontDs.SetPointSize(18)
        self.TBDia.SetFont(self.fontDs)

        self.panel.Bind(wx.EVT_BUTTON, self.valores, self.boton)


    def valores(self, event):
        self.VALORDIA = int(self.TBDia.GetValue())
        self.VALORMES = int(self.TBMes.GetValue())
        self.VALORANO = int(self.TBA.GetValue())

        type(self.VALORDIA)

        if (self.VALORMES <= 12 and self.VALORMES >= 1):
            if (self.VALORMES != 2):
                if (self.VALORDIA <= 31 and self.VALORDIA >= 1):
                    if (self.VALORANO > 1900 and self.VALORANO < 2030):
                        #importar la clase MyFrame2 del modulo frame2.py
                        from core.layouts import Frame2
                        frame2 = Frame2(None, self.VALORDIA, self.VALORMES, self.VALORANO)
                        frame2.Show()
                        self.Close(True)
                    else:
                        dialog = wx.MessageDialog(self, "El año que intentas buscar no es valido", "Alerta!!!!", wx.OK)
                        dialog.ShowModal()  # mostrar diálogo
                        dialog.Destroy()  # finalizar diálogo
                else:
                    dialog = wx.MessageDialog(self, "El dia no se encuentra en el rango indicado", "Alerta!!!!", wx.OK)
                    dialog.ShowModal()  # mostrar diálogo
                    dialog.Destroy()  # finalizar diálogo
            else:
                if (self.VALORDIA <= 28 and self.VALORDIA >= 1):
                    if (self.VALORANO > 1900 and self.VALORANO < 2030):
                        #importar la clase MyFrame2 del modulo frame2.py
                        from core.layouts import Frame2
                        frame2 = Frame2(None, self.VALORDIA, self.VALORMES, self.VALORANO)
                        frame2.Show()
                        self.Close(True)
                    else:
                        dialog = wx.MessageDialog(self, "El año que intentas buscar no es valido", "Alerta!!!!", wx.OK)
                        dialog.ShowModal()  # mostrar diálogo
                        dialog.Destroy()  # finalizar diálogo
                else:
                        dialog = wx.MessageDialog(self, "El dia es MAYOR a 28", "Alerta!!!!", wx.OK)
                        dialog.ShowModal()  # mostrar diálogo
                        dialog.Destroy()  # finalizar diálogo
        else:
            dialog = wx.MessageDialog(self, "El mes no se encuentra en el rango", "Alerta!!!!", wx.OK)
            dialog.ShowModal()  # mostrar diálogo
            dialog.Destroy()  # finalizar diálogo



    def confirmar(self, file):
        """Mostrar mensaje de confirmación al guardar una carta"""
        confirmar = CONFIRMAR + file
        dialog = wx.MessageDialog(self, confirmar, CONFIRM_TITLE, wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def on_about(self, event):
        """Mostrar un diálogo acerca de"""
        dialog = wx.MessageDialog(self, ABOUT_CONTENT, ABOUT_TITLE, wx.OK)
        dialog.ShowModal()  # mostrar diálogo
        dialog.Destroy()  # finalizar diálogo

    def on_exit(self, event):
        """Salir del programa"""
        self.Close(True)  # Cierra la ventana


app = wx.App(None)
frame = SincronarioMaya(None, APP_TITLE)
frame.Show(True)  # Mostrar la ventana
app.MainLoop()
