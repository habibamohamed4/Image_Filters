# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'images_filtering.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1633, 915)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(218, 218, 218);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("background-image: url(:/newPrefix/f1.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.normal_image = QtWidgets.QLabel(self.centralwidget)
        self.normal_image.setText("")
        self.normal_image.setObjectName("normal_image")
        self.verticalLayout.addWidget(self.normal_image)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/ff3.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.after_filter = QtWidgets.QLabel(self.centralwidget)
        self.after_filter.setText("")
        self.after_filter.setObjectName("after_filter")
        self.verticalLayout.addWidget(self.after_filter)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("background-image: url(:/newPrefix/NEW1.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("background-image: url(:/newPrefix/ff2.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.after_frequency_filter = QtWidgets.QLabel(self.centralwidget)
        self.after_frequency_filter.setText("")
        self.after_frequency_filter.setObjectName("after_frequency_filter")
        self.verticalLayout_2.addWidget(self.after_frequency_filter)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setStyleSheet("background-image: url(:/newPrefix/pic4.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.histogram = QtWidgets.QLabel(self.centralwidget)
        self.histogram.setText("")
        self.histogram.setObjectName("histogram")
        self.verticalLayout_3.addWidget(self.histogram)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setStyleSheet("background-image: url(:/newPrefix/ff1.png);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.after_histogram = QtWidgets.QLabel(self.centralwidget)
        self.after_histogram.setStyleSheet("")
        self.after_histogram.setText("")
        self.after_histogram.setObjectName("after_histogram")
        self.verticalLayout_3.addWidget(self.after_histogram)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1633, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFilter = QtWidgets.QMenu(self.menubar)
        self.menuFilter.setObjectName("menuFilter")
        self.menuHigh_Filter = QtWidgets.QMenu(self.menuFilter)
        self.menuHigh_Filter.setObjectName("menuHigh_Filter")
        self.menuSpatial = QtWidgets.QMenu(self.menuHigh_Filter)
        self.menuSpatial.setObjectName("menuSpatial")
        self.menuFrequency = QtWidgets.QMenu(self.menuHigh_Filter)
        self.menuFrequency.setObjectName("menuFrequency")
        self.menuLow_Filter = QtWidgets.QMenu(self.menuFilter)
        self.menuLow_Filter.setObjectName("menuLow_Filter")
        self.menuSpatial_2 = QtWidgets.QMenu(self.menuLow_Filter)
        self.menuSpatial_2.setObjectName("menuSpatial_2")
        self.menuFrequency_2 = QtWidgets.QMenu(self.menuLow_Filter)
        self.menuFrequency_2.setObjectName("menuFrequency_2")
        self.menuMedian_Filter = QtWidgets.QMenu(self.menuFilter)
        self.menuMedian_Filter.setObjectName("menuMedian_Filter")
        self.menuSpatial_3 = QtWidgets.QMenu(self.menuMedian_Filter)
        self.menuSpatial_3.setObjectName("menuSpatial_3")
        self.menuLa_placian_Filter = QtWidgets.QMenu(self.menuFilter)
        self.menuLa_placian_Filter.setObjectName("menuLa_placian_Filter")
        self.menuSpatial_4 = QtWidgets.QMenu(self.menuLa_placian_Filter)
        self.menuSpatial_4.setObjectName("menuSpatial_4")
        self.menuHistogram = QtWidgets.QMenu(self.menubar)
        self.menuHistogram.setObjectName("menuHistogram")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionGray_Scale = QtWidgets.QAction(MainWindow)
        self.actionGray_Scale.setObjectName("actionGray_Scale")
        self.actionColor = QtWidgets.QAction(MainWindow)
        self.actionColor.setObjectName("actionColor")
        self.actionGray_Scale_2 = QtWidgets.QAction(MainWindow)
        self.actionGray_Scale_2.setObjectName("actionGray_Scale_2")
        self.actionColor_2 = QtWidgets.QAction(MainWindow)
        self.actionColor_2.setObjectName("actionColor_2")
        self.actionGray_Scale_3 = QtWidgets.QAction(MainWindow)
        self.actionGray_Scale_3.setObjectName("actionGray_Scale_3")
        self.actionColor_3 = QtWidgets.QAction(MainWindow)
        self.actionColor_3.setObjectName("actionColor_3")
        self.actionGrary_Scale = QtWidgets.QAction(MainWindow)
        self.actionGrary_Scale.setObjectName("actionGrary_Scale")
        self.actionColor_4 = QtWidgets.QAction(MainWindow)
        self.actionColor_4.setObjectName("actionColor_4")
        self.actionGray_Scale_4 = QtWidgets.QAction(MainWindow)
        self.actionGray_Scale_4.setObjectName("actionGray_Scale_4")
        self.actionColor_5 = QtWidgets.QAction(MainWindow)
        self.actionColor_5.setObjectName("actionColor_5")
        self.actionGray_Scale_5 = QtWidgets.QAction(MainWindow)
        self.actionGray_Scale_5.setObjectName("actionGray_Scale_5")
        self.actionColor_6 = QtWidgets.QAction(MainWindow)
        self.actionColor_6.setObjectName("actionColor_6")
        self.actionGray_Scale_6 = QtWidgets.QAction(MainWindow)
        self.actionGray_Scale_6.setObjectName("actionGray_Scale_6")
        self.actionColor_7 = QtWidgets.QAction(MainWindow)
        self.actionColor_7.setObjectName("actionColor_7")
        self.actionGray_Scale_7 = QtWidgets.QAction(MainWindow)
        self.actionGray_Scale_7.setObjectName("actionGray_Scale_7")
        self.actionColor_8 = QtWidgets.QAction(MainWindow)
        self.actionColor_8.setObjectName("actionColor_8")
        self.actionHistogram_equlizer = QtWidgets.QAction(MainWindow)
        self.actionHistogram_equlizer.setObjectName("actionHistogram_equlizer")
        self.menuFile.addAction(self.actionOpen)
        self.menuSpatial.addAction(self.actionGray_Scale)
        self.menuFrequency.addAction(self.actionGray_Scale_2)
        self.menuHigh_Filter.addAction(self.menuSpatial.menuAction())
        self.menuHigh_Filter.addAction(self.menuFrequency.menuAction())
        self.menuSpatial_2.addAction(self.actionGray_Scale_3)
        self.menuFrequency_2.addAction(self.actionGrary_Scale)
        self.menuLow_Filter.addAction(self.menuSpatial_2.menuAction())
        self.menuLow_Filter.addAction(self.menuFrequency_2.menuAction())
        self.menuSpatial_3.addAction(self.actionGray_Scale_4)
        self.menuMedian_Filter.addAction(self.menuSpatial_3.menuAction())
        self.menuSpatial_4.addAction(self.actionGray_Scale_6)
        self.menuLa_placian_Filter.addAction(self.menuSpatial_4.menuAction())
        self.menuFilter.addAction(self.menuHigh_Filter.menuAction())
        self.menuFilter.addAction(self.menuLow_Filter.menuAction())
        self.menuFilter.addAction(self.menuMedian_Filter.menuAction())
        self.menuFilter.addAction(self.menuLa_placian_Filter.menuAction())
        self.menuHistogram.addAction(self.actionHistogram_equlizer)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())
        self.menubar.addAction(self.menuHistogram.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.menuHigh_Filter.setTitle(_translate("MainWindow", "High Filter"))
        self.menuSpatial.setTitle(_translate("MainWindow", "Spatial"))
        self.menuFrequency.setTitle(_translate("MainWindow", "Frequency"))
        self.menuLow_Filter.setTitle(_translate("MainWindow", "Low Filter"))
        self.menuSpatial_2.setTitle(_translate("MainWindow", "Spatial "))
        self.menuFrequency_2.setTitle(_translate("MainWindow", "Frequency"))
        self.menuMedian_Filter.setTitle(_translate("MainWindow", "Median Filter"))
        self.menuSpatial_3.setTitle(_translate("MainWindow", "Spatial "))
        self.menuLa_placian_Filter.setTitle(_translate("MainWindow", "La placian Filter"))
        self.menuSpatial_4.setTitle(_translate("MainWindow", "Spatial"))
        self.menuHistogram.setTitle(_translate("MainWindow", "Histogram"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionGray_Scale.setText(_translate("MainWindow", "Gray Scale"))
        self.actionColor.setText(_translate("MainWindow", "Color"))
        self.actionGray_Scale_2.setText(_translate("MainWindow", "Gray Scale"))
        self.actionColor_2.setText(_translate("MainWindow", "Color"))
        self.actionGray_Scale_3.setText(_translate("MainWindow", "Gray Scale"))
        self.actionColor_3.setText(_translate("MainWindow", "Color"))
        self.actionGrary_Scale.setText(_translate("MainWindow", "Grary Scale"))
        self.actionColor_4.setText(_translate("MainWindow", "Color"))
        self.actionGray_Scale_4.setText(_translate("MainWindow", "Gray Scale"))
        self.actionColor_5.setText(_translate("MainWindow", "Color"))
        self.actionGray_Scale_5.setText(_translate("MainWindow", "Gray Scale"))
        self.actionColor_6.setText(_translate("MainWindow", "Color"))
        self.actionGray_Scale_6.setText(_translate("MainWindow", "Gray Scale"))
        self.actionColor_7.setText(_translate("MainWindow", "Color"))
        self.actionGray_Scale_7.setText(_translate("MainWindow", "Gray Scale"))
        self.actionColor_8.setText(_translate("MainWindow", "Color"))
        self.actionHistogram_equlizer.setText(_translate("MainWindow", "Perform Histogram"))
import style



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
