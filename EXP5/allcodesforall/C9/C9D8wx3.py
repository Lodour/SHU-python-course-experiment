#coding:utf-8
## -*- coding : gbk -*-

import wx
import random
random.seed()

class myImageWindow(wx.Window):
    def __init__(self, parent, imgbgd, imgfgd):
        wx.Window.__init__(self, parent)
        self.bgd = imgbgd.ConvertToBitmap()# 创建位图
        self.fgd  = imgfgd.ConvertToBitmap()# 创建位图
        # choose some random positions to draw the image at:
        # 创建随机的位置
        self.positions = [(10,10)]
        for x in range(20):
            x = random.randint(0, 560)
            y = random.randint(0, 400)
            self.positions.append( (x,y) )
            # Bind the Paint event
            self.Bind(wx.EVT_PAINT, self.OnPaint)
            
    def OnPaint(self, evt):
        # create and clear the DC
        dc = wx.PaintDC(self)
        brush = wx.Brush("sky blue")
        dc.SetBackground(brush)
        dc.Clear()# 使用背景画刷清除设备上下文中的内容
        # draw the image in random locations
        dc.DrawBitmap(self.bgd, 0, 0, False)
        for x,y in self.positions:# 绘制位图
            dc.DrawBitmap(self.fgd, x, y, True)

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Loading Images",size=(640,480))
        imgbgd = wx.Image("bgd.bmp",  wx.BITMAP_TYPE_ANY)
        imgfgd  = wx.Image("fgd.bmp",  wx.BITMAP_TYPE_ANY)
        imgfgd.SetMaskColour(255,255,255)
        win = myImageWindow(self, imgbgd, imgfgd)

        
app = wx.App()
frm = TestFrame()
frm.Show()
app.MainLoop()
