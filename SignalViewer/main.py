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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        MainWindow.setObjectName("MainWindow")
        self.MainWindow.setWindowIcon(QIcon('icons/icon.png'))
        MainWindow.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWindow.setStyleSheet("font-family:sans-serif;color:#111;font-size:16px;")
        self.MainWindow.graph_background = QtWidgets.QGraphicsView(self.centralwidget)
        self.MainWindow.graph_background.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.MainWindow.graph_background.setStyleSheet("background-color:#eee;")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.xslider_2 = CustomSlider(self.frame_4)
        self.xslider_2.setOrientation(QtCore.Qt.Horizontal)
        self.xslider_2.setObjectName("xslider_2")
        self.gridLayout_4.addWidget(self.xslider_2, 1, 1, 1, 1)
        self.yslider_2 = QtWidgets.QSlider(self.frame_4)
        self.yslider_2.setOrientation(QtCore.Qt.Vertical)
        self.yslider_2.setObjectName("yslider_2")
        self.gridLayout_4.addWidget(self.yslider_2, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.yslider_1 = QtWidgets.QSlider(self.frame_3)
        self.yslider_1.setOrientation(QtCore.Qt.Vertical)
        self.yslider_1.setObjectName("yslider_1")
        self.gridLayout_3.addWidget(self.yslider_1, 0, 0, 1, 1)
        self.xslider_1 = CustomSlider(self.frame_3)
        self.xslider_1.setOrientation(QtCore.Qt.Horizontal)
        self.xslider_1.setObjectName("xslider_1")
        self.gridLayout_3.addWidget(self.xslider_1, 1, 1, 1, 1)
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.gridLayout_3.addLayout(self.verticalLayout_1, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        

        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabs = QtWidgets.QTabWidget(self.frame_2)
        self.tabs.setEnabled(True)
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
        self.gridLayout_8 = QtWidgets.QGridLayout(self.channel_1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.channel_1)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.plot_box_1 = QtWidgets.QComboBox(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_box_1.sizePolicy().hasHeightForWidth())
        self.plot_box_1.setSizePolicy(sizePolicy)
        self.plot_box_1.setObjectName("plot_box_1")
        self.gridLayout_5.addWidget(self.plot_box_1, 1, 0, 1, 2)
        self.speed_label_1 = QtWidgets.QLabel(self.frame_7)
        self.speed_label_1.setObjectName("speed_label_1")
        self.gridLayout_5.addWidget(self.speed_label_1, 3, 3, 1, 1)
        self.zoom_in_1 = QtWidgets.QPushButton(self.frame_7)
        self.zoom_in_1.setObjectName("zoom_in_1")
        self.gridLayout_5.addWidget(self.zoom_in_1, 5, 0, 1, 1)
        self.speedDisp_1 = QtWidgets.QLCDNumber(self.frame_7)
        self.speedDisp_1.setObjectName("speedDisp_1")
        self.gridLayout_5.addWidget(self.speedDisp_1, 2, 4, 3, 3)
        self.pause_play_button_1 = QtWidgets.QPushButton(self.frame_7)
        self.pause_play_button_1.setObjectName("pause_play_button_1")
        self.gridLayout_5.addWidget(self.pause_play_button_1, 5, 2, 1, 1)
        self.rewind_1 = QtWidgets.QPushButton(self.frame_7)
        self.rewind_1.setObjectName("rewind_1")
        self.gridLayout_5.addWidget(self.rewind_1, 5, 3, 1, 1)
        self.zoom_out_1 = QtWidgets.QPushButton(self.frame_7)
        self.zoom_out_1.setObjectName("zoom_out_1")
        self.gridLayout_5.addWidget(self.zoom_out_1, 5, 1, 1, 1)
        self.hide_check_1 = QtWidgets.QPushButton(self.frame_7)
        self.hide_check_1.setObjectName("hide_check_1")
        self.gridLayout_5.addWidget(self.hide_check_1, 5, 5, 1, 3)
        self.snapshot_1 = QtWidgets.QPushButton(self.frame_7)
        self.snapshot_1.setObjectName("snapshot_1")
        self.gridLayout_5.addWidget(self.snapshot_1, 1, 3, 1, 1)
        self.speedDown_1 = QtWidgets.QPushButton(self.frame_7)
        self.speedDown_1.setObjectName("speedDown_1")
        self.gridLayout_5.addWidget(self.speedDown_1, 1, 6, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout_5.addWidget(self.lineEdit_1, 1, 2, 1, 1)
        self.colour_1 = QtWidgets.QPushButton(self.frame_7)
        self.colour_1.setObjectName("colour_1")
        self.gridLayout_5.addWidget(self.colour_1, 2, 1, 3, 1)
        self.shift_1 = QtWidgets.QPushButton(self.frame_7)
        self.shift_1.setObjectName("shift_1")
        self.gridLayout_5.addWidget(self.shift_1, 2, 0, 3, 1)
        self.speedUp_1 = QtWidgets.QPushButton(self.frame_7)
        self.speedUp_1.setObjectName("speedUp_1")
        self.gridLayout_5.addWidget(self.speedUp_1, 1, 4, 1, 1)
        self.gridLayout_8.addWidget(self.frame_7, 0, 0, 1, 1)
        self.tabs.addTab(self.channel_1, "")
        self.channel_2 = QtWidgets.QWidget()
        self.channel_2.setObjectName("channel_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.channel_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_8 = QtWidgets.QFrame(self.channel_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.plot_box_2 = QtWidgets.QComboBox(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_box_2.sizePolicy().hasHeightForWidth())
        self.plot_box_2.setSizePolicy(sizePolicy)
        self.plot_box_2.setObjectName("plot_box_2")
        self.gridLayout_6.addWidget(self.plot_box_2, 1, 0, 1, 2)
        self.speed_label_2 = QtWidgets.QLabel(self.frame_8)
        self.speed_label_2.setObjectName("speed_label_2")
        self.gridLayout_6.addWidget(self.speed_label_2, 3, 3, 1, 1)
        self.zoom_in_2 = QtWidgets.QPushButton(self.frame_8)
        self.zoom_in_2.setObjectName("zoom_in_2")
        self.gridLayout_6.addWidget(self.zoom_in_2, 5, 0, 1, 1)
        self.speedDisp_2 = QtWidgets.QLCDNumber(self.frame_8)
        self.speedDisp_2.setObjectName("speedDisp_2")
        self.gridLayout_6.addWidget(self.speedDisp_2, 2, 4, 3, 3)
        self.pause_play_button_2 = QtWidgets.QPushButton(self.frame_8)
        self.pause_play_button_2.setObjectName("pause_play_button_2")
        self.gridLayout_6.addWidget(self.pause_play_button_2, 5, 2, 1, 1)
        self.rewind_2 = QtWidgets.QPushButton(self.frame_8)
        self.rewind_2.setObjectName("rewind_2")
        self.gridLayout_6.addWidget(self.rewind_2, 5, 3, 1, 1)
        self.zoom_out_2 = QtWidgets.QPushButton(self.frame_8)
        self.zoom_out_2.setObjectName("zoom_out_2")
        self.gridLayout_6.addWidget(self.zoom_out_2, 5, 1, 1, 1)
        self.hide_check_2 = QtWidgets.QPushButton(self.frame_8)
        self.hide_check_2.setObjectName("hide_check_2")
        self.gridLayout_6.addWidget(self.hide_check_2, 5, 5, 1, 3)
        self.snapshot_2 = QtWidgets.QPushButton(self.frame_8)
        self.snapshot_2.setObjectName("snapshot_2")
        self.gridLayout_6.addWidget(self.snapshot_2, 1, 3, 1, 1)
        self.speedDown_2 = QtWidgets.QPushButton(self.frame_8)
        self.speedDown_2.setObjectName("speedDown_2")
        self.gridLayout_6.addWidget(self.speedDown_2, 1, 6, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_6.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.colour_2 = QtWidgets.QPushButton(self.frame_8)
        self.colour_2.setObjectName("colour_2")
        self.gridLayout_6.addWidget(self.colour_2, 2, 1, 3, 1)
        self.shift_2 = QtWidgets.QPushButton(self.frame_8)
        self.shift_2.setObjectName("shift_2")
        self.gridLayout_6.addWidget(self.shift_2, 2, 0, 3, 1)
        self.speedUp_2 = QtWidgets.QPushButton(self.frame_8)
        self.speedUp_2.setObjectName("speedUp_2")
        self.gridLayout_6.addWidget(self.speedUp_2, 1, 4, 1, 1)
        self.gridLayout_9.addWidget(self.frame_8, 0, 0, 1, 1)
        self.tabs.addTab(self.channel_2, "")
        self.gridLayout_2.addWidget(self.tabs, 0, 0, 1, 1)
        self.link_button = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.link_button.sizePolicy().hasHeightForWidth())
        self.link_button.setSizePolicy(sizePolicy)
        self.link_button.setObjectName("link_button")
        self.gridLayout_2.addWidget(self.link_button, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 2)
        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionReport = QtWidgets.QAction(MainWindow)
        self.actionReport.setObjectName("actionReport")
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionReport)
        self.menubar.addAction(self.menuFile.menuAction())
        self.isplayed=False

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.plot_box_1_items=[]
        self.plot_box_2_items=[]
        #list of names of snapshots
        self.lst_snapshots_img=[]

        #list of statistics 
        self.lst_snapshots_statistics=[]

        #create canvas to plot in it
        self.canvas_1 = MplCanvas(self, width=6, height=6, dpi=100)
        self.canvas_2 = MplCanvas(self, width=6, height=6, dpi=100)
        self.link_2_channels=False

        #current canvas
        self.current_canvas=self.canvas_1

        #add canvas to verticalLayouts
        self.verticalLayout_1.addWidget(self.canvas_1)
        self.verticalLayout_2.addWidget(self.canvas_2)

        #vertical slider
        self.yslider_1.setRange(-6,6)
        self.yslider_1.setValue(0)
        ##* :) *##
        self.yslider_2.setRange(-6,6)
        self.yslider_2.setValue(0)

        #horizontal slider
        self.xslider_1.setRange(-6,6)
        self.xslider_1.setValue(0)
        ##* :) *##
        self.xslider_2.setRange(-6,6)
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

        #pause and play button signal
        self.pause_play_button_1.clicked.connect(lambda:self.toggle_playpause_icon(self.canvas_1,self.pause_play_button_1,self.isplayed))
        self.pause_play_button_2.clicked.connect(lambda:self.toggle_playpause_icon(self.canvas_2,self.pause_play_button_2,self.isplayed))

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


    #Ui_MainWindow functions---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def toggle_playpause_icon(self,canvas,btn,isplayed):
            canvas.pause_or_paly()
            isplayed=canvas.played
            if isplayed:
                btn.setIcon(QIcon("icons/pause.ico"))
                isplayed=False
            else:
                btn.setIcon(QIcon("icons/play.ico"))       
                isplayed=True 




    def change_current_tab(self,index):
        if index == 0:
            self.current_canvas=self.canvas_1
        else:
            self.current_canvas=self.canvas_2
    
    def move_from_channel1_to_channel2(self):
        self.canvas_1.move_plot_from_canvas(self.plot_box_1.currentIndex(),self.canvas_2)
        moved_plot_index=self.plot_box_1.currentIndex()
        self.plot_box_1.removeItem(moved_plot_index)
        self.plot_box_1_items.pop(moved_plot_index)
        self.plot_box_2.addItem(self.canvas_2.lst_df_names[self.canvas_2.get_plots_number()-1])
        self.plot_box_2_items.append(self.canvas_2.lst_df_names[self.canvas_2.get_plots_number()-1])
        

    def move_from_channel2_to_channel1(self):
        self.canvas_2.move_plot_from_canvas(self.plot_box_2.currentIndex(),self.canvas_1)
        moved_plot_index=self.plot_box_2.currentIndex()
        self.plot_box_2.removeItem(moved_plot_index)
        self.plot_box_2_items.pop(moved_plot_index)
        self.plot_box_1.addItem(self.canvas_1.lst_df_names[self.canvas_1.get_plots_number()-1])
        self.plot_box_1_items.append(self.canvas_1.lst_df_names[self.canvas_1.get_plots_number()-1])
        
    

    def upload_csv(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.MainWindow, 'Open CSV File', '', 'CSV Files (*.csv)')
        if file_path:
            df = pd.read_csv(file_path)
            self.current_canvas.upload_data(df)
            if(self.current_canvas==self.canvas_1):
                self.plot_box_1.addItem(self.current_canvas.lst_df_names[self.current_canvas.get_plots_number()-1])
                self.plot_box_1_items.append(self.current_canvas.lst_df_names[self.current_canvas.get_plots_number()-1])
            else:
                self.plot_box_2.addItem(self.current_canvas.lst_df_names[self.current_canvas.get_plots_number()-1])
                self.plot_box_2_items.append(self.current_canvas.lst_df_names[self.current_canvas.get_plots_number()-1])

    def change_plot_legend(self):
        if(self.current_canvas==self.canvas_1):
            self.canvas_1.rename_sig_from_canvas(self.plot_box_1.currentIndex(),self.lineEdit_1.text())
            self.plot_box_1.setItemData(self.plot_box_1.currentIndex(), self.lineEdit_1.text())
            self.plot_box_1_items[self.plot_box_1.currentIndex()]=self.lineEdit_1.text()
            self.plot_box_1.clear()
            self.plot_box_1.addItems(self.plot_box_1_items)
            #self.plot_box_1.addItem(self.current_canvas.lst_df_names[self.current_canvas.get_plots_number() - 1])###
            #self.plot_box_1.removeItem(self.plot_box_1.currentIndex())  ###
        else:
            self.canvas_2.rename_sig_from_canvas(self.plot_box_2.currentIndex(),self.lineEdit_2.text())
            self.plot_box_2.setItemData(self.plot_box_2.currentIndex(), self.lineEdit_2.text())
            self.plot_box_2_items[self.plot_box_2.currentIndex()]=self.lineEdit_2.text()
            self.plot_box_2.clear()
            self.plot_box_2.addItems(self.plot_box_2_items)
            #self.plot_box_2.addItem(self.current_canvas.lst_df_names[self.current_canvas.get_plots_number() - 1])  ###
            #self.plot_box_2.removeItem(self.plot_box_2.currentIndex())  ###

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

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Live-Multichannel-Signal-Monitor"))
        self.plot_box_1.setItemText(0, _translate("MainWindow", "Plot1"))
        self.speed_label_1.setText(_translate("MainWindow", "Speed"))
        self.zoom_in_1.setText(_translate("MainWindow", "Zoom In"))
        self.zoom_in_1.setIcon(QtGui.QIcon("icons/icons8-zoom-in-50.png"))
        self.zoom_in_1.setIconSize(QtCore.QSize(30,30))
        # self.pause_play_button_1.setText(_translate("MainWindow", "Pause/Play"))
        self.pause_play_button_1.setIcon(QtGui.QIcon("icons/pause.ico"))
        self.pause_play_button_1.setIconSize(QtCore.QSize(30,30))
        self.rewind_1.setText(_translate("MainWindow", "Rewind"))
        self.rewind_1.setIcon(QtGui.QIcon("icons/icons8-rewind-50.png"))
        self.rewind_1.setIconSize(QtCore.QSize(30,30))
        self.zoom_out_1.setText(_translate("MainWindow", "Zoom Out"))
        
        self.zoom_out_1.setIcon(QtGui.QIcon("icons/icons8-zoom-out-50.png"))
        self.zoom_out_1.setIconSize(QtCore.QSize(30,30))
        self.hide_check_1.setText(_translate("MainWindow", "Hide / Show"))
        self.hide_check_1.setIcon(QtGui.QIcon("icons/icons8-hide-24.png"))
        self.hide_check_1.setIconSize(QtCore.QSize(30,30))
        self.snapshot_1.setText(_translate("MainWindow", "Snapshot"))
        self.snapshot_1.setIcon(QtGui.QIcon("icons/icons8-screenshot-30.png"))
        self.snapshot_1.setIconSize(QtCore.QSize(30,30))
        self.speedDown_1.setText(_translate("MainWindow", "Speed-"))
        self.speedDown_1.setIcon(QtGui.QIcon("icons/icons8-down-30 (1).png"))
        self.speedDown_1.setIconSize(QtCore.QSize(30,30))
        self.lineEdit_1.setText(_translate("MainWindow", "Edit Plot Name"))
        self.colour_1.setText(_translate("MainWindow", "Colour"))
        self.colour_1.setIcon(QtGui.QIcon("icons/icons8-color-palette-48.png"))
        self.colour_1.setIconSize(QtCore.QSize(30,30))
        self.shift_1.setText(_translate("MainWindow", "Shift plot"))
        self.shift_1.setIcon(QtGui.QIcon("icons/icons8-move-right-50.png"))
        self.shift_1.setIconSize(QtCore.QSize(30,30))
        self.speedUp_1.setText(_translate("MainWindow", "Speed+"))
        self.speedUp_1.setIcon(QtGui.QIcon("icons/icons8-up-30.png"))
        self.speedUp_1.setIconSize(QtCore.QSize(30,30))
        self.tabs.setTabText(self.tabs.indexOf(self.channel_1), _translate("MainWindow", "Channel 1"))
        self.plot_box_2.setItemText(0, _translate("MainWindow", "Plot1"))
        self.speed_label_2.setText(_translate("MainWindow", "Speed"))
        self.zoom_in_2.setText(_translate("MainWindow", "Zoom In"))
        self.zoom_in_2.setIcon(QtGui.QIcon("icons/icons8-zoom-in-50.png"))
        self.zoom_in_2.setIconSize(QtCore.QSize(30,30))
        # self.pause_play_button_2.setText(_translate("MainWindow", "Pause/Play"))
        self.pause_play_button_2.setIcon(QtGui.QIcon("icons/pause.ico"))
        self.pause_play_button_2.setIconSize(QtCore.QSize(30,30))
        self.rewind_2.setText(_translate("MainWindow", "Rewind"))
        self.rewind_2.setIcon(QtGui.QIcon("icons/icons8-rewind-50.png"))
        self.rewind_2.setIconSize(QtCore.QSize(30,30))
        self.zoom_out_2.setText(_translate("MainWindow", "Zoom Out"))
        
        self.zoom_out_2.setIcon(QtGui.QIcon("icons/icons8-zoom-out-50.png"))
        self.zoom_out_2.setIconSize(QtCore.QSize(30,30))
        self.hide_check_2.setText(_translate("MainWindow", "Hide / Show"))
        self.hide_check_2.setIcon(QtGui.QIcon("icons/icons8-hide-24.png"))
        self.hide_check_2.setIconSize(QtCore.QSize(30,30))
        self.snapshot_2.setText(_translate("MainWindow", "Snapshot"))
        self.snapshot_2.setIcon(QtGui.QIcon("icons/icons8-screenshot-30.png"))
        self.snapshot_2.setIconSize(QtCore.QSize(30,30))
        self.speedDown_2.setText(_translate("MainWindow", "Speed-"))
        self.speedDown_2.setIcon(QtGui.QIcon("icons/icons8-down-30 (1).png"))
        self.speedDown_2.setIconSize(QtCore.QSize(30,30))
        self.lineEdit_2.setText(_translate("MainWindow", "Edit Plot Name"))
        self.colour_2.setText(_translate("MainWindow", "Colour"))
        self.colour_2.setIcon(QtGui.QIcon("icons/icons8-color-palette-48.png"))
        self.colour_2.setIconSize(QtCore.QSize(30,30))
        self.shift_2.setText(_translate("MainWindow", "Shift plot"))
        self.shift_2.setIcon(QtGui.QIcon("icons/icons8-move-right-50.png"))
        self.shift_2.setIconSize(QtCore.QSize(30,30))
        self.speedUp_2.setText(_translate("MainWindow", "Speed+"))
        self.speedUp_2.setIcon(QtGui.QIcon("icons/icons8-up-30.png"))
        self.speedUp_2.setIconSize(QtCore.QSize(30,30))
        self.tabs.setTabText(self.tabs.indexOf(self.channel_2), _translate("MainWindow", "Channel 2"))
        self.link_button.setText(_translate("MainWindow", "link"))
        self.link_button.setStyleSheet("background-color: green;")
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionopen.setText(_translate("MainWindow", "Open"))
        self.actionReport.setText(_translate("MainWindow", "Report"))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Create the application instance
    MainWindow = QtWidgets.QMainWindow()  # Create the main window
    # app.setStyle('Fusion')
    ui = Ui_MainWindow()  # Create an instance of the UI class
    ui.setupUi(MainWindow)  # Set up the UI for the main window
    MainWindow.show()  # Display the main window
    sys.exit(app.exec_())  # Run the application event loop

main()