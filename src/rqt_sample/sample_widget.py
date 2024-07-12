# coding: UTF-8

import os

from ament_index_python.resources import get_resource

from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget
from python_qt_binding.QtGui import QPainter, QFont
from python_qt_binding.QtCore import Qt

import numpy as np
import matplotlib

# specify using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets

#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.figure import Figure



class SampleWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Tenpa Interface")

        self.main_widget = QtWidgets.QWidget(self)
        self.slider_group = QtWidgets.QGroupBox('Desired values:')
        self.slider_form = QtWidgets.QFormLayout()
        self.labellist = []
        self.combolist = []
        self.N_ch = 10

        # flags
        self.sample_pub_flag = False
        
        # each channel
        for i in range(self.N_ch):
            self.labellist.append( QtWidgets.QLabel('value No. %d' %(i)) )

            self.combolist.append( QtWidgets.QSlider(QtCore.Qt.Horizontal, self) )
            self.combolist[i].setMaximum( 255 )
            #self.combolist[i].valueChanged.connect( self.generateSliderCallback(i) )
            self.slider_form.addRow(self.labellist[i], self.combolist[i])
        
        '''
        # macro
        self.labellist.append( QtWidgets.QLabel('Set all channels'))
        self.combolist.append( QtWidgets.QSlider(QtCore.Qt.Horizontal, self) )
        self.combolist[].setMaximum( 255 )
        self.slider_form.addRow(self.labellist[48], self.combolist[48])
        '''

        self.slider_group.setLayout(self.slider_form)
        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(self.slider_group)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(200)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        #ac = AnimationCanvas(self.main_widget, width=5, height=12, dpi=100) # create a graph canvas
        self.btn_p = QtWidgets.QPushButton('Publish', self) # create a publish button
        self.btn_p.resize(self.btn_p.sizeHint())
        self.btn_p.clicked.connect( self.updatePublishFlag )
        
        # create Qt layout
        l.addWidget(scroll)
        l.addWidget(self.btn_p)
        
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

    
    def updatePublishFlag(self):
        self.sample_pub_flag = True