#!/usr/bin/env ~/.local/bin/python3
#-*- coding:utf-8 -*-
import os
import wx


# app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
# frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
# frame.Show(True)     # Show the frame.
# app.MainLoop()

# class MyFrame(wx.Frame):
#     """ We simply derive a new class of Frame. """
#     def __init__(self, parent, title):
#         wx.Frame.__init__(self, parent, title=title, size=(200,100))
#         self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
#         self.Show(True)

# app = wx.App(False)
# frame = MyFrame(None, 'Small editor')
# app.MainLoop()

# class MainWindow(wx.Frame):
#     def __init__(self, parent, title):
#         wx.Frame.__init__(self, parent, title=title, size=(200,100))
#         self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
#         self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
#         filemenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
#         filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
#         filemenu.AppendSeparator()
#         filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
#         menuBar = wx.MenuBar()
#         menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
#         self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
#         self.Show(True)

# app = wx.App(False)
# frame = MainWindow(None, "Sample editor")
# app.MainLoop()


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A StatusBar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()
#        filemenu2= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
#        menuBar.Append(filemenu2,"&TEST") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def OnOpen(self,e):
        """ Open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
#            content = self.contral.GetValue(f.read#())
#            print(content)
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()
