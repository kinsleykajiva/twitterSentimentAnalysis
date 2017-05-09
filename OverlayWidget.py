import math, sys
from PyQt4 import QtCore, QtGui , Qt

class Overlay(QtGui.QWidget):

    def __init__(self, parent = None):
    
        QtGui.QWidget.__init__(self, parent)
        palette = QtGui.QPalette(self.palette())

        #palette.setColor(QtGui.QPalette::Window, Qt::black)
        #palette.setColor(palette.Background,  0, 0, 0, 0)
        self.setPalette(palette)
    
    def paintEvent(self, event):
    
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.fillRect(event.rect(), QtGui.QBrush(QtGui.QColor(255, 255, 255, 127)))
        painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        
        for i in range(6):
            if (self.counter / 5) % 6 == i:
                painter.setBrush(QtGui.QBrush(QtGui.QColor(127 + (self.counter % 5)*32, 127, 127)))
            else:
                painter.setBrush(QtGui.QBrush(QtGui.QColor(127, 127, 127)))
            painter.drawEllipse(
                self.width()/2 + 30 * math.cos(2 * math.pi * i / 6.0) - 10,
                self.height()/2 + 30 * math.sin(2 * math.pi * i / 6.0) - 10,
                20, 20)
        
        painter.end()
    
    def showEvent(self, event):
    
        self.timer = self.startTimer(150)
        self.counter = 0
    
    def timerEvent(self, event):
    
        self.counter += 1
        self.update()
        if self.counter == 160:
            self.killTimer(self.timer)
            self.hide()