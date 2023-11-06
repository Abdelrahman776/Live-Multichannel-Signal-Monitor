# Form implementation generated from reading ui file 'front.ui'
# Created by: PyQt5 UI code generator 5.15.9
# pyuic5
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MplGraph import MplCanvas
import pandas as pd
from custom_slider import CustomSlider
from create_pdf import generate_pdf


class Ui_MainWindow(QMainWindow):

   
    def __init__(self):
        
        """Initializer."""
        super().__init__()
        self.resize(1920, 1080)
        # setting icon to the window
        self.setWindowIcon(QIcon('images/icon.png'))
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.graph_background = QtWidgets.QGraphicsView(self.centralwidget)
        self.graph_background.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.graph_background.setStyleSheet("background-color:#555;")
        self.setStyleSheet("background-color: #888;color:#111;font-size:16px;") 
        self.graph_background.setObjectName("graph_background")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setEnabled(True)
        self.tabs.setGeometry(QtCore.QRect(0, 600, 1920, 450))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 255, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 255, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tabs.setPalette(palette)
        self.tabs.setAutoFillBackground(False)
        self.tabs.setObjectName("tabs")
        self.channel_1 = QtWidgets.QWidget()
        self.channel_1.setObjectName("channel_1")
        self.isplayed=False
        self.pause_play_button_1 = QtWidgets.QPushButton(self.channel_1)
        self.pause_play_button_1.setGeometry(QtCore.QRect(290, 160, 211, 28))
        self.pause_play_button_1.setObjectName("pause_play_button_1")
        self.hide_check_1 = QtWidgets.QPushButton(self.channel_1)
        self.hide_check_1.setGeometry(QtCore.QRect(690, 170, 100, 25))
        self.hide_check_1.setObjectName("hide_check_1")
        self.zoom_in_1 = QtWidgets.QPushButton(self.channel_1)
        self.zoom_in_1.setGeometry(QtCore.QRect(10, 160, 61, 28))
        self.zoom_in_1.setObjectName("zoom_in_1")
        self.zoom_out_1 = QtWidgets.QPushButton(self.channel_1)
        self.zoom_out_1.setGeometry(QtCore.QRect(110, 160, 61, 28))
        self.zoom_out_1.setObjectName("zoom_out_1")
        self.speed_label = QtWidgets.QLabel(self.channel_1)
        self.speed_label.setGeometry(QtCore.QRect(600, 110, 71, 20))
        self.speed_label.setObjectName("speed_label")
        self.rewind_1 = QtWidgets.QPushButton(self.channel_1)
        self.rewind_1.setGeometry(QtCore.QRect(520, 160, 51, 28))
        self.rewind_1.setObjectName("rewind_1")
        self.plot_box_1 = QtWidgets.QComboBox(self.channel_1)
        self.plot_box_1.setGeometry(QtCore.QRect(10, 30, 161, 22))
        self.plot_box_1.setObjectName("plot_box_1")
        #self.plot_box_1.placeholderText("plots name")
        self.colour_1 = QtWidgets.QPushButton(self.channel_1)
        self.colour_1.setGeometry(QtCore.QRect(50, 90, 71, 28))
        self.colour_1.setObjectName("colour_1")
        self.shift_1 = QtWidgets.QPushButton(self.channel_1)
        self.shift_1.setGeometry(QtCore.QRect(340, 80, 93, 28))
        self.shift_1.setObjectName("shift_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.channel_1)
        self.lineEdit_1.setGeometry(QtCore.QRect(290, 30, 191, 22))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.speedUp_1 = QtWidgets.QPushButton(self.channel_1)
        self.speedUp_1.setGeometry(QtCore.QRect(650, 50, 61, 41))
        self.speedUp_1.setObjectName("speedUp_1")
        self.speedDown_1 = QtWidgets.QPushButton(self.channel_1)
        self.speedDown_1.setGeometry(QtCore.QRect(720, 50, 61, 41))
        self.speedDown_1.setObjectName("speedDown_1")
        self.speedDisp_1 = QtWidgets.QLCDNumber(self.channel_1)
        self.speedDisp_1.setGeometry(QtCore.QRect(680, 100, 64, 31))
        self.speedDisp_1.setObjectName("speedDisp_1")

        self.snapshot_1 = QtWidgets.QPushButton(self.channel_1)
        self.snapshot_1.setGeometry(QtCore.QRect(510, 20, 61, 51))
        self.snapshot_1.setObjectName("snapshot_1")
        self.tabs.addTab(self.channel_1, "")
        self.channel_2 = QtWidgets.QWidget()
        self.channel_2.setObjectName("channel_2")
        self.hide_check_2 = QtWidgets.QPushButton(self.channel_2)
        self.hide_check_2.setGeometry(QtCore.QRect(690, 170, 100, 25))
        self.hide_check_2.setObjectName("hide_check_2")
        self.pause_play_button_2 = QtWidgets.QPushButton(self.channel_2)
        self.pause_play_button_2.setGeometry(QtCore.QRect(290, 160, 211, 28))
        self.pause_play_button_2.setObjectName("pause_play_button_2")
        self.zoom_in_2 = QtWidgets.QPushButton(self.channel_2)
        self.zoom_in_2.setGeometry(QtCore.QRect(10, 160, 61, 28))
        self.zoom_in_2.setObjectName("zoom_in_2")
        self.zoom_out_2 = QtWidgets.QPushButton(self.channel_2)
        self.zoom_out_2.setGeometry(QtCore.QRect(110, 160, 61, 28))
        self.zoom_out_2.setObjectName("zoom_out_2")
        self.speed_label_2 = QtWidgets.QLabel(self.channel_2)
        self.speed_label_2.setGeometry(QtCore.QRect(600, 110, 71, 20))
        self.speed_label_2.setObjectName("speed_label_2")
        self.rewind_2 = QtWidgets.QPushButton(self.channel_2)
        self.rewind_2.setGeometry(QtCore.QRect(520, 160, 51, 28))
        self.rewind_2.setObjectName("rewind_2")
        self.plot_box_2 = QtWidgets.QComboBox(self.channel_2)
        self.plot_box_2.setGeometry(QtCore.QRect(10, 30, 161, 22))
        self.plot_box_2.setObjectName("plot_box_2")
        #self.plot_box_2.addItem("")
        self.colour_2 = QtWidgets.QPushButton(self.channel_2)
        self.colour_2.setGeometry(QtCore.QRect(50, 90, 71, 28))
        self.colour_2.setObjectName("colour_2")
        self.shift_2 = QtWidgets.QPushButton(self.channel_2)
        self.shift_2.setGeometry(QtCore.QRect(340, 80, 93, 28))
        self.shift_2.setObjectName("shift_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.channel_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 30, 191, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.speedUp_2 = QtWidgets.QPushButton(self.channel_2)
        self.speedUp_2.setGeometry(QtCore.QRect(650, 50, 61, 41))
        self.speedUp_2.setObjectName("speedUp_2")
        self.speedDown_2 = QtWidgets.QPushButton(self.channel_2)
        self.speedDown_2.setGeometry(QtCore.QRect(720, 50, 61, 41))
        self.speedDown_2.setObjectName("speedDown_2")
        self.speedDisp_2 = QtWidgets.QLCDNumber(self.channel_2)
        self.speedDisp_2.setGeometry(QtCore.QRect(680, 100, 64, 31))
        self.speedDisp_2.setObjectName("speedDisp_2")
        self.snapshot_2 = QtWidgets.QPushButton(self.channel_2)
        self.snapshot_2.setGeometry(QtCore.QRect(510, 20, 61, 51))
        self.snapshot_2.setObjectName("snapshot_2")
        self.tabs.addTab(self.channel_2, "")
        self.link_button = QtWidgets.QPushButton(self.centralwidget)
        self.link_button.setGeometry(QtCore.QRect(340, 350, 111, 25))
        self.link_button.setObjectName("link_button")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(360, 0, 81, 351))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 330, 361, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 172, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 172, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.graphicsView.setPalette(palette)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(410, 330, 361, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 172, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 172, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.graphicsView_2.setPalette(palette)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 20, 21, 301))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 172, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 172, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.graphicsView_3.setPalette(palette)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(410, 20, 21, 301))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 172, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 172, 172))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.graphicsView_4.setPalette(palette)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.yslider_1 = QtWidgets.QSlider(self.centralwidget)
        self.yslider_1.setGeometry(QtCore.QRect(10, 30, 22, 291))
        self.yslider_1.setOrientation(QtCore.Qt.Vertical)
        self.yslider_1.setObjectName("yslider_1")
        self.yslider_2 = QtWidgets.QSlider(self.centralwidget)
        self.yslider_2.setGeometry(QtCore.QRect(910, 30, 22, 291))
        self.yslider_2.setOrientation(QtCore.Qt.Vertical)
        self.yslider_2.setObjectName("yslider_2")
        self.xslider_1 = CustomSlider(self.centralwidget)
        self.xslider_1.setGeometry(QtCore.QRect(10, 555, 361, 25))
        self.xslider_1.setOrientation(QtCore.Qt.Horizontal)
        self.xslider_1.setObjectName("xslider_1")
        self.xslider_2 = CustomSlider(self.centralwidget)
        self.xslider_2.setGeometry(QtCore.QRect(410, 555, 361, 25))
        self.xslider_2.setOrientation(QtCore.Qt.Horizontal)
        self.xslider_2.setObjectName("xslider_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 0, 850, 550))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(970, 0, 850, 550))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 226))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.actionopen = QtWidgets.QAction()
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction()
        self.actionsave.setObjectName("actionsave")
        self.actionsave_as = QtWidgets.QAction()
        self.actionsave_as.setObjectName("actionsave_as")
        self.actionReport = QtWidgets.QAction()
        self.actionReport.setObjectName("actionReport")
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionReport)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi()
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        #list of names of snapshots
        self.lst_snapshots_img=[]

        #list of statistics 
        self.lst_snapshots_statistics=[]

        #create canvas to plot in it
        self.canvas_1 = MplCanvas(self, width=16, height=16, dpi=100)
        self.canvas_2 = MplCanvas(self, width=16, height=16, dpi=100)
        self.link_2_channels=False

        #current canvas
        self.current_canvas=self.canvas_1

        #add canvas to verticalLayouts
        self.verticalLayout_1.addWidget(self.canvas_1)
        self.verticalLayout_2.addWidget(self.canvas_2)

        #vertical slider
        self.yslider_1.setRange(-10,10)
        self.yslider_1.setValue(0)
        ##* :) *##
        self.yslider_2.setRange(-10,10)
        self.yslider_2.setValue(0)

        #horizontal slider
        self.xslider_1.setRange(-10,10)
        self.xslider_1.setValue(0)
        ##* :) *##
        self.xslider_2.setRange(-10,10)
        self.xslider_2.setValue(0)

        #### signals ####
        #change tab
        self.tabs.currentChanged.connect(self.change_current_tab)

        #open file
        self.actionopen.triggered.connect(self.upload_csv)

        #function change_current_tab

        #zoom in button signal
       
        self.zoom_in_1.clicked.connect(self.canvas_1.zoom_in)
        self.zoom_in_2.clicked.connect(self.canvas_2.zoom_in)

        #zoom out button signal

        self.zoom_out_1.clicked.connect(self.canvas_1.zoom_out)
        self.zoom_out_2.clicked.connect(self.canvas_2.zoom_out)

        
        #control speed
        self.speedUp_1.clicked.connect(self.canvas_1.increase_speed)
        self.speedDown_1.clicked.connect(self.canvas_1.decrease_speed)
        self.speedUp_2.clicked.connect(self.canvas_2.increase_speed)
        self.speedDown_2.clicked.connect(self.canvas_2.decrease_speed)

        #Vertical slider signals
        self.yslider_1.valueChanged.connect(self.canvas_1.vertical_scroll)
        self.yslider_2.valueChanged.connect(self.canvas_2.vertical_scroll)
        #Horizontal slider signals
        self.xslider_1.differenceChanged.connect(self.canvas_1.horizontal_scroll)
        self.xslider_2.differenceChanged.connect(self.canvas_2.horizontal_scroll)

        
        self.shift_1.pressed.connect(self.move_from_channel1_to_channel2)
        self.shift_2.pressed.connect(self.move_from_channel2_to_channel1)

        #take the string input from lineEdit_ and set it as a name for selected signal
        self.lineEdit_1.returnPressed.connect(self.change_plot_legend)
        self.lineEdit_2.returnPressed.connect(self.change_plot_legend)

        #signal of change color buuton
        self.colour_2.clicked.connect(self.open_color_picker)
        self.colour_1.clicked.connect(self.open_color_picker)

        #signal of hide buuton
        self.hide_check_1.clicked.connect(self.change_visibility)
        self.hide_check_2.clicked.connect(self.change_visibility)
        
        #link 2 channels
        self.link_button.clicked.connect(self.link_channels)

        #rewind signal
        self.rewind_1.clicked.connect(self.rewind_signal)
        self.rewind_2.clicked.connect(self.rewind_signal)

        #take snapshot
        self.snapshot_1.clicked.connect(self.take_snapshot)
        self.snapshot_2.clicked.connect(self.take_snapshot)

        #save pdf
        self.actionReport.triggered.connect(self.make_pdf)

        # Connect the Speed+ and Speed-buttons to the functions
        self.speedDisp_1.display(self.canvas_1.counter)
        self.speedUp_1.clicked.connect(self.increase_counter_1)
        self.speedDown_1.clicked.connect(self.decrease_counter_1)

        self.speedDisp_2.display(self.canvas_2.counter)
        self.speedUp_2.clicked.connect(self.increase_counter_2)
        self.speedDown_2.clicked.connect(self.decrease_counter_2)
        #pause and play button signal
        # self.pause_play_button_1.clicked.connect(self.toggle_playpause_icon1)
        # self.pause_play_button_2.clicked.connect(self.toggle_playpause_icon2)
        self.pause_play_button_1.clicked.connect(lambda:self.toggle_playpause_icon(self.canvas_1,self.pause_play_button_1,self.isplayed))
        self.pause_play_button_2.clicked.connect(lambda:self.toggle_playpause_icon(self.canvas_2,self.pause_play_button_2,self.isplayed))


    #Ui_MainWindow functions------------------------------------------------------
    def toggle_playpause_icon(self,canvas,btn,isplayed):
            canvas.pause_or_paly()
            isplayed=canvas.played
            if isplayed:
                btn.setIcon(QIcon("images/pause1.png"))
                isplayed=False
            else:
                btn.setIcon(QIcon("images/play.ico"))       
                isplayed=True


            ######

    def change_current_tab(self,index):
        if index == 0:
            self.current_canvas=self.canvas_1
        else:
            self.current_canvas=self.canvas_2
    
    def move_from_channel1_to_channel2(self):
        self.canvas_1.move_plot_from_canvas(self.plot_box_1.currentIndex(),self.canvas_2)
        self.plot_box_1.removeItem(self.plot_box_1.currentIndex())
        self.plot_box_2.addItem(self.canvas_2.lst_df_names[self.canvas_2.get_plots_number()-1])
        return

    def move_from_channel2_to_channel1(self):
        self.canvas_2.move_plot_from_canvas(self.plot_box_2.currentIndex(),self.canvas_1)
        self.plot_box_2.removeItem(self.plot_box_2.currentIndex())
        self.plot_box_1.addItem(self.canvas_1.lst_df_names[self.canvas_1.get_plots_number()-1])
        return
    

    def upload_csv(self):
         
        file_path, _ = QFileDialog.getOpenFileName(None, 'Open CSV File', '', 'CSV Files (*.csv)')
        if file_path:
            df = pd.read_csv(file_path)
            self.current_canvas.upload_data(df)
            if(self.current_canvas==self.canvas_1):
                self.plot_box_1.addItem(self.current_canvas.lst_df_names[self.current_canvas.get_plots_number()-1])
            else:
                self.plot_box_2.addItem(self.current_canvas.lst_df_names[self.current_canvas.get_plots_number()-1])

    def change_plot_legend(self):
        if(self.current_canvas==self.canvas_1):
            self.canvas_1.rename_sig_from_canvas(self.plot_box_1.currentIndex(),self.lineEdit_1.text())
            self.plot_box_1.setItemData(self.plot_box_1.currentIndex(), self.lineEdit_1.text())
            self.plot_box_1.addItem(self.current_canvas.lst_df_names[self.current_canvas.get_plots_number() - 1])###
            self.plot_box_1.removeItem(self.plot_box_1.currentIndex())  ###
        else:
            self.canvas_2.rename_sig_from_canvas(self.plot_box_2.currentIndex(),self.lineEdit_2.text())
            self.plot_box_2.setItemData(self.plot_box_2.currentIndex(), self.lineEdit_2.text())
            self.plot_box_2.addItem(self.current_canvas.lst_df_names[self.current_canvas.get_plots_number() - 1])  ###
            self.plot_box_2.removeItem(self.plot_box_2.currentIndex())  ###

    def open_color_picker(self):
        if(self.canvas_1.get_plots_number()==0 and self.canvas_2.get_plots_number()==0):
            return
        color = QColorDialog.getColor()
        if color.isValid():
            self.selected_color = color
            if(self.current_canvas==self.canvas_1):
                self.canvas_1.change_color_of_siganl(self.plot_box_1.currentIndex(),self.selected_color.name())
            else:
                self.canvas_2.change_color_of_siganl(self.plot_box_2.currentIndex(),self.selected_color.name())
                

    def change_visibility(self):
        if(self.canvas_1.get_plots_number()==0 and self.canvas_2.get_plots_number()==0):
            return
        if(self.current_canvas==self.canvas_1):
            self.canvas_1.change_visibility(self.plot_box_1.currentIndex())
        else:
            self.canvas_2.change_visibility(self.plot_box_2.currentIndex())

    def link_channels(self):
        if(self.canvas_1.get_plots_number()==0 and self.canvas_2.get_plots_number()==0):
            return
        self.link_2_channels= not self.link_2_channels
        if(self.link_2_channels):
            self.link_button.setText("stop linking")
            self.link_button.setStyleSheet("background-color: red;")
            self.canvas_1.is_linked_with_canvas=True
        else:
            self.link_button.setText("link")
            self.link_button.setStyleSheet("background-color: green;")
            self.canvas_1.is_linked_with_canvas=False
            self.canvas_2.is_linked_with_canvas=False
            return
        if(self.current_canvas==self.canvas_1):
            self.canvas_1.link_canvas(self.canvas_2)
        else:
            self.canvas_2.link_canvas(self.canvas_1)

    def rewind_signal(self):
        if(self.canvas_1.get_plots_number()==0 and self.canvas_2.get_plots_number()==0):
            return
        if(self.current_canvas==self.canvas_1):
            self.canvas_1.rewind_signal(self.plot_box_1.currentIndex())
        else:
            self.canvas_2.rewind_signal(self.plot_box_2.currentIndex())
    def take_snapshot(self):
        if(self.current_canvas==self.canvas_1):
            snapshot = self.canvas_1.grab()
            statistics=self.canvas_1.get_statistics()
        else:
            snapshot = self.canvas_2.grab()
            statistics=self.canvas_2.get_statistics()
        snapshot.save("snapshot"+str(len(self.lst_snapshots_img))+".png")
        self.lst_snapshots_img.append("snapshot"+str(len(self.lst_snapshots_img))+".png")
        self.lst_snapshots_statistics.append(statistics)
    def make_pdf(self):
        generate_pdf(self.lst_snapshots_img,self.lst_snapshots_statistics,"snapshots.pdf")



    def increase_counter_1(self):
        # Increment the counter and update the display
        self.canvas_1.counter += 1
        self.speedDisp_1.display(self.canvas_1.counter)

    def decrease_counter_1(self):
        # Decrement the counter and update the display
        self.canvas_1.counter -= 1
        self.speedDisp_1.display(self.canvas_1.counter)


    def increase_counter_2(self):
        # Increment the counter and update the display
        self.canvas_2.counter += 1
        self.speedDisp_2.display(self.canvas_2.counter)

    def decrease_counter_2(self):
        # Decrement the counter and update the display
        self.canvas_2.counter -= 1
        self.speedDisp_2.display(self.canvas_2.counter)
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("", "Live-Multichannel-Signal-Monitor"))
        self.pause_play_button_1.setIcon(QIcon("images/pause.ico"))
        # setText(_translate("", "Pause/Play"))
        self.hide_check_2.setText(_translate("", "Hide / Show"))
        self.zoom_in_1.setIcon(QIcon("images/zoomin.png"))
        self.zoom_out_1.setIcon(QIcon("images/zoomout.png"))
        self.speed_label.setText(_translate("MainWindow", "Speed"))
        self.rewind_1.setIcon(QIcon("images/rewind.png"))
        self.plot_box_1.setItemText(0, _translate("MainWindow", "Plot1"))
        self.colour_1.setText(_translate("MainWindow", "Colour"))
        self.shift_1.setText(_translate("MainWindow", "Shift plot"))
        self.lineEdit_1.setText(_translate("MainWindow", "Edit Plot Name"))
        self.speedUp_1.setText(_translate("MainWindow", "Speed+"))
        self.speedDown_1.setText(_translate("MainWindow", "Speed-"))
        self.snapshot_1.setText(_translate("MainWindow", "Snapshot"))
        self.tabs.setTabText(self.tabs.indexOf(self.channel_1), _translate("MainWindow", "Channel 1"))
        self.hide_check_1.setText(_translate("MainWindow", "Hide / Show"))
        self.pause_play_button_2.setIcon(QIcon("images/pause1.png"))
        self.zoom_in_2.setIcon(QIcon("images/zoomin.png"))
        self.zoom_out_2.setIcon(QIcon("images/zoomout.png"))
        self.speed_label_2.setText(_translate("MainWindow", "Speed"))
        self.rewind_2.setIcon(QIcon("images/rewind.png"))
        self.plot_box_2.setItemText(0, _translate("MainWindow", "Plot1"))
        self.colour_2.setText(_translate("MainWindow", "Colour"))
        self.shift_2.setText(_translate("MainWindow", "Shift plot"))
        self.lineEdit_2.setText(_translate("MainWindow", "Edit Plot Name"))
        self.speedUp_2.setText(_translate("MainWindow", "Speed+"))
        self.speedDown_2.setText(_translate("MainWindow", "Speed-"))
        self.snapshot_2.setText(_translate("MainWindow", "Snapshot"))
        self.tabs.setTabText(self.tabs.indexOf(self.channel_2), _translate("MainWindow", "Channel 2"))
        self.link_button.setText(_translate("MainWindow", "Link Channels"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionopen.setText(_translate("MainWindow", "open "))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave_as.setText(_translate("MainWindow", "save as\'"))
        self.actionReport.setText(_translate("MainWindow", "Report"))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Create the application instance
    app.setStyle('Fusion')
    ui = Ui_MainWindow()  # Create an instance of the UI class
    ui.show()  # Set up the UI for the main window
   
    sys.exit(app.exec_())  # Run the application event loop

