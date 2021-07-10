#from GAppleGame import *
#import GMyFirstGame
import os
import wx
from PIL import Image
#exec(open("GAppleGame\game.py").read())
#C:\WINDOWS\system32\output\game

#os.chdir('C:/WINDOWS/system32/output/game')
#os.system("C:/WINDOWS/system32/output/game/game.exe")
directory = os.getcwd()

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.pnl = wx.Panel(self)
        self.imgsnake_dir = directory +  "/Snake_game_image.png"
        self.snakeimage = Image.open(self.imgsnake_dir)#Image.open(image_file)
        self.snakeimage = self.snakeimage.resize((200,200))
        self.simage = wx.EmptyImage(self.snakeimage.size[0], self.snakeimage.size[1])
        self.simage.SetData(self.snakeimage.convert('RGB').tobytes())
        self.simage.SetAlpha(self.snakeimage.convert("RGBA").tobytes()[3::4])
        self.sbitmap = wx.BitmapFromImage(self.simage)
        self.simg=wx.StaticBitmap(self.pnl, 0, self.sbitmap,pos=(15,10))

        self.imghangman_dir = directory +  "/Hangman_game_image.png"
        self.hangmanimage = Image.open(self.imghangman_dir)#Image.open(image_file)
        self.hangmanimage = self.hangmanimage.resize((200,200))
        self.himage = wx.EmptyImage(self.hangmanimage.size[0], self.hangmanimage.size[1])
        self.himage.SetData(self.hangmanimage.convert('RGB').tobytes())
        self.himage.SetAlpha(self.hangmanimage.convert("RGBA").tobytes()[3::4])
        self.hbitmap = wx.BitmapFromImage(self.himage)
        self.himg=wx.StaticBitmap(self.pnl, 0, self.hbitmap,pos=(365,10))

        self.imgpong_dir = directory +  "/Pong_game_image.png"
        self.pongimage = Image.open(self.imgpong_dir)#Image.open(image_file)
        self.pongimage = self.pongimage.resize((200,200))
        self.pimage = wx.EmptyImage(self.pongimage.size[0], self.pongimage.size[1])
        self.pimage.SetData(self.pongimage.convert('RGB').tobytes())
        self.pimage.SetAlpha(self.pongimage.convert("RGBA").tobytes()[3::4])
        self.pbitmap = wx.BitmapFromImage(self.pimage)
        self.pimg=wx.StaticBitmap(self.pnl, 0, self.pbitmap,pos=(15,250))

        self.imgapple_dir = directory +  "/Apple_game_image.jpg"
        self.appleimage = Image.open(self.imgapple_dir)#Image.open(image_file)
        self.appleimage = self.appleimage.resize((200,200))
        self.aimage = wx.EmptyImage(self.appleimage.size[0], self.appleimage.size[1])
        self.aimage.SetData(self.appleimage.convert('RGB').tobytes())
        self.aimage.SetAlpha(self.appleimage.convert("RGBA").tobytes()[3::4])
        self.abitmap = wx.BitmapFromImage(self.aimage)
        self.aimg=wx.StaticBitmap(self.pnl, 0, self.abitmap,pos=(365,250))

        self.txt = wx.StaticText(self.pnl, label = "Choose a game:", pos = (250, 185))
        self.playbtn = wx.Button(self.pnl, label = "Play", pos = (250, 245))
        self.playbtn.Bind(wx.EVT_BUTTON, self.Play)
    
        self.games = ["Apple Game", "Snake Game", "Hangman", "Pong Game"]
        self.combo = wx.ComboBox(self.pnl, choices = self.games, pos=(250,210))
        self.InitUI()
    def Play(self, e):
        value = self.combo.GetValue()
        
        if value == "Apple Game":
            cwd = directory
            #os.chdir('C:/WINDOWS/system32/output/game')
            #cwd = os.getcwd()
            cwd = cwd.replace("\\", "/")
            cwd = cwd + "/game"
            os.chdir(cwd)
            cwd = cwd + "/game.exe"
            os.system(cwd)
            #print(cwd)
        elif value == "Hangman":
            #os.chdir("C:/WINDOWS/system32/output/F98280_L7_T2")
            #os.system("C:/WINDOWS/system32/output/F98280_L7_T2/F98280_L7_T2.exe")
            #cwd = os.getcwd()
            cwd = directory
            cwd = cwd.replace("\\", "/")
            cwd = cwd + "/F98280_L7_T2"
            os.chdir(cwd)
            cwd = cwd + "/F98280_L7_T2.exe"
            os.system(cwd)
        elif value == "Pong Game":
            #os.chdir("C:/WINDOWS/system32/output/ponggame")
            #os.system("C:/WINDOWS/system32/output/ponggame/ponggame.exe")
            #cwd = os.getcwd()
            cwd = directory
            cwd = cwd.replace("\\", "/")
            cwd = cwd + "/ponggame"
            os.chdir(cwd)
            cwd = cwd + "/ponggame.exe"
            os.system(cwd)
        elif value == "Snake Game":
            #os.chdir("C:/WINDOWS/system32/output/solo_snake")
            #os.system("C:/WINDOWS/system32/output/solo_snake/solo_snake.exe")
            #cwd = os.getcwd()
            cwd = directory
            cwd = cwd.replace("\\", "/")
            cwd = cwd + "/solo_snake"
            os.chdir(cwd)
            cwd = cwd + "/solo_snake.exe"
            os.system(cwd)

        print(directory)
    def InitUI(self):
        self.SetSize((600, 500)) #width, height
        self.SetTitle('Mini Games')
        self.Centre()
        self.Show(True)

ex = wx.App()
Example(None)
ex.MainLoop()