#
"""
GUISCRCPY by srevinsaju
Get it on : https://github.com/sevinsaju/guiscrcpy
Licensed under GNU Public License

Build 1.10.0

CHANGELOG:

Build 1.9.7-release
16072019 1512
* Fixed many bugs
* Added configuration file
* Migrated from PyQt5 to PyQt5 due to KDE Plasma incompatibility
* Added config file save and read
* Edited ProgressBar thread locking to progressive type
* Separated  to linear and horizontal toolkit for easy use
* Added experimental autorotate orientage support change

Build 1.9.6
* Minor fixes

Build 1.9.5
25062019 2159
* MEGA CHANGE :: Migrated from `PyQt4` to `PyQt5` due to late realization that PyQt4 support
for Windows is unfortunately discontinued.
* `mainwindow.ui` >> xml parsed file loaded in uic loader has been compiled to `mainui.py` as UI
* toolkit.py is deprecated. toolkit class is restructured into mainwindow class with multiprocesing.
* After `PyQt5` update, GTK-LTK-KDE no longer raises pixmap errors


Build 1.9.4
23062018 1615 GMT+300
* Dumped terminal QTextEdit for multiprocessing to prevent QThread hang.
* Restructured StartScrcpy Class as two threads.

Build 1.9.3
22062019 1948 GMT+3
* Fixed GUI hang (issue reported by @rom1v)
(code has been restructured. the old code is placed in `/backup/` folder as `main 1.9.2.py`. But however, terminal ui QTextEdit
is not functional.


1.9.2
* Added GUIScrcpy icon
* Added pixmap icons
* Added check scrcpy process running or not
* Added GUIScrcpy Toolkit Experimental Support

1.9.1
* Initial Build :)


Syntax for the config file
ln1:: dial value
ln2:: dimensionCheckBox
ln3:: dimension value
ln4:: fullScreen
ln5:: showTouches


Icon made by Dave Gandy from www.flaticon.com used under Creative Commons 3.0 Unported.
The original SVG black work by Dave Gandy has ben re-oriented, flipped or color-changed.
The rest of Terms and Conditions put formward by CC-3.0:Unported has been feverently followed
by the debeloper. Icons have been adapeted in all the three windows.

Icons pack obtained from www.flaticon.com
All rights reserved.

"""
import sys
import os


# removed multiprocess modules

# import pdb
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import qdarkstyle


from subprocess import Popen as po, STDOUT
from subprocess import PIPE

import time
from PyQt5.QtWidgets import QMessageBox
# from toolUI import Ui_Dialog
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow
# from bottompanelUI import Ui_Panel
# import breeze_resources
try:
    import psutil
except ModuleNotFoundError:
    print("psutil is not installed in the python3 directory. "
          "Install with \n $ pip3 install psutil")

"""
try:
    import pyautogui as auto
except ModuleNotFoundError:
    print("PyAutoGUI is not installed. Please install it with pip install pyautogui."
          "Read the README.md on github.com/srevinsaju/guiscrcpy. \n You might want to continue without "
          "pyAutoGUI limited functionality")
try:
    from pygetwindow import getWindowsWithTitle
except NotImplementedError:
    pass
"""
from mainui import Ui_MainWindow

build = "1.10.0.27082019-1254"
print("guiscrcpy v1.10.0-release")
print("by srevinsaju")
print("************************************")
print("released on 24082019 GMT+0300 2048 ")
print("************************************")
bitrate0 = 8000
try:
	cfg = open(os.path.expanduser("~/guiscrcpy.cfg"), "r")
	fileExist = True
	print("User configuration file found!")
except FileNotFoundError or FileExistsError:
    print("User configuration file not found!")
    cfg = open(os.path.expanduser("~/guiscrcpy.cfg"), "w+")
    fileExist = False

    cfg.close()

if not fileExist:
	cfg = open(os.path.expanduser("~/guiscrcpy.cfg"), "r+")
	cfg.writelines(("#" * 25 + "\n", "Created by Srevin Saju\n", "#" * 25 + "\n", str(time.time()) + "\n"))

	cfg.close()
elif fileExist:
	cfg = open(os.path.expanduser("~/guiscrcpy.cfg"), "r")
	"""
        the cfg file struct::
        :bitrate0 [4]
        :dimension0 [5]
        :swtouches0 [6]
        :fullscreen0 [7]
        :dispRO0 [8]



	"""
	a = cfg.readlines()
	cfg.close()
	# print("cfg:", cfg.readlines())
	print("cfg:", a)

	try:
		bitrate0 = a[4].strip("\n")
	except IndexError:
		bitrate0 = 8000
	try:
		dimension0 = a[5].strip("\n")
	except IndexError:
		dimension0 = None
	try:
		fullscreen0 = a[7].strip("\n")
	except IndexError:
		fullscreen0 = "False"
	try:
	    swtouches0 = a[6].strip("\n")
	except IndexError:
	    swtouches0 = "False"

	try:
		dispRO0= a[8].strip("\n")
		print("SUCCESS dispRO")
	except IndexError:
		dispRO0 = "False"
		print("FAILED dispRO")
	print("Bitrate : ", bitrate0, " + Dimensions", dimension0, "")
	print(bitrate0)
	print("dispRO:", dispRO0)



# ===================



# BEGIN TOOLKIT.UI

def clipd2pc():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "c")
    except NameError:
        os.system("wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+c")


def power():
    print("POWER")
    adb_power = po("adb shell input keyevent 26", shell=True, stdout=PIPE,
                                 stderr=PIPE)


def menu():
    print("MENU")
    adb_menu = po("adb shell input keyevent 82", shell=True, stdout=PIPE,
                                stderr=PIPE)


def Back():
    print("BACK")
    adb_back = po("adb shell input keyevent 4", shell=True, stdout=PIPE,
                                stderr=PIPE)


def volUP():
    print("BACK")
    adb_back = po("adb shell input keyevent 24", shell=True, stdout=PIPE,
                                stderr=PIPE)


def volDN():
    print("BACK")
    adb_back = po("adb shell input keyevent 25", shell=True, stdout=PIPE,
                                stderr=PIPE)


def homekey():
    print("HOME")
    adb_home = po("adb shell input keyevent 3", shell=True, stdout=PIPE,
                                stderr=PIPE)


def switch():
    print("APP_SWITCH")
    adb_home = po("adb shell input keyevent KEYCODE_APP_SWITCH", shell=True,
                                stdout=PIPE,
                                stderr=PIPE)


def reorientP():
    print("REORIENT [POTRAIT]")
    adb_reo = po("adb shell settings put system accelerometer_rota"
                               "tion 0; adb shell settings put system"
                               " user_rotation 0", shell=True)


def reorientL():
    print("REORIENT [LANDSCAPE]")
    adb_reoo = po("adb shell settings put system accelerometer_rota"
                                "tion 0; adb shell settings put system"
                                " user_rotation 1", shell=True)


def notifExpand():
    print("NOTIF EXPAND")
    adb_dim = po("adb shell wm size", shell=True, stdout=PIPE, stderr=PIPE)
    out = adb_dim.stdout.read()
    out_decoded = out.decode("utf-8")
    out_decoded = out_decoded[:-1]
    dimVal = out_decoded.split(": ")
    dimensions_ = dimVal[1]
    dimValues = dimensions_.split("x")
    adb_pull = po("adb shell input swipe 0 0 0 " + str(int(dimValues[1]) - 1),
                                shell=True, stdout=PIPE,
                                stderr=PIPE)


def notifCollapse():
    print("NOTIF COLLAPSE")
    adb_dim = po("adb shell wm size", shell=True, stdout=PIPE, stderr=PIPE)
    out = adb_dim.stdout.read()
    out_decoded = out.decode("utf-8")
    out_decoded = out_decoded[:-1]
    dimVal = out_decoded.split(": ")
    dimensions_ = dimVal[1]
    dimValues = dimensions_.split("x")
    adb_pull = po("adb shell input swipe 0 " + str(int(dimValues[1]) - 1) + " 0 0",
                                shell=True, stdout=PIPE,
                                stderr=PIPE)


def clippc2d():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "shift", "c")
        print("NOT SUPPORTED ON WINDOWS")
    except NameError:
        os.system("wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+shift+c")


def fullscreen():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "f")
    except NameError:
        os.system("wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+f")


class MyAppv(QMainWindow):
    def __init__(self):
        super(MyAppv, self).__init__()
        # Ui_Dialog.__init__(self)
        print("Class entered : MyAppv")
        self.setObjectName("Dialog")
        self.resize(104, 457)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(30, 340))
        self.setMaximumSize(QtCore.QSize(104, 600))
        self.setBaseSize(QtCore.QSize(30, 403))
        self.setWindowTitle("guiscrcpy")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowOpacity(1.0)
        self.setStyleSheet("QDialog{\n"
            "width: 30px\n"
            "}\n"
            "QPushButton {\n"
            "                        \n"
            "\n"
            "border-radius: 1px;\n"
            "        background-color: qlineargradient(spread:pad, x1:0, y1:0.915182, x2:0, y2:0.926, stop:0.897059 rgba(41, 41, 41, 255), stop:1 rgba(30, 30, 30, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "                        \n"
            "                    }\n"
            "\n"
            "QPushButton:pressed {\n"
            "border-radius: 5px;\n"
            "                      \n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "                        }\n"
            "QPushButton:hover {\n"
            "border-radius: 5px;\n"
            "                      \n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "                        }\n"
            "")
        self.notif_collapse = QtWidgets.QPushButton(self)
        self.notif_collapse.setEnabled(True)
        self.notif_collapse.setGeometry(QtCore.QRect(0, 75, 30, 25))
        self.notif_collapse.setMouseTracking(True)
        self.notif_collapse.setTabletTracking(True)
        self.notif_collapse.setAutoFillBackground(False)
        self.notif_collapse.setStyleSheet("")
        self.notif_collapse.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/bell-musical-tool(2).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notif_collapse.setIcon(icon1)
        self.notif_collapse.setFlat(True)
        self.notif_collapse.setObjectName("notif_collapse")
        self.menuUI = QtWidgets.QPushButton(self)
        self.menuUI.setEnabled(True)
        self.menuUI.setGeometry(QtCore.QRect(0, 275, 30, 25))
        self.menuUI.setMouseTracking(True)
        self.menuUI.setTabletTracking(True)
        self.menuUI.setAutoFillBackground(False)
        self.menuUI.setStyleSheet("")
        self.menuUI.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/reorder-option.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuUI.setIcon(icon2)
        self.menuUI.setFlat(True)
        self.menuUI.setObjectName("menuUI")
        self.appswi = QtWidgets.QPushButton(self)
        self.appswi.setEnabled(True)
        self.appswi.setGeometry(QtCore.QRect(0, 300, 30, 25))
        self.appswi.setMouseTracking(True)
        self.appswi.setTabletTracking(True)
        self.appswi.setAutoFillBackground(False)
        self.appswi.setStyleSheet("")
        self.appswi.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/four-black-squares.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.appswi.setIcon(icon3)
        self.appswi.setFlat(True)
        self.appswi.setObjectName("appswi")
        self.pinchoutUI = QtWidgets.QPushButton(self)
        self.pinchoutUI.setEnabled(False)
        self.pinchoutUI.setGeometry(QtCore.QRect(0, 350, 30, 25))
        self.pinchoutUI.setStyleSheet("")
        self.pinchoutUI.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/zoom-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pinchoutUI.setIcon(icon4)
        self.pinchoutUI.setFlat(True)
        self.pinchoutUI.setObjectName("pinchoutUI")
        self.screenfreeze = QtWidgets.QPushButton(self)
        self.screenfreeze.setEnabled(True)
        self.screenfreeze.setGeometry(QtCore.QRect(0, 0, 30, 25))
        self.screenfreeze.setMouseTracking(True)
        self.screenfreeze.setTabletTracking(True)
        self.screenfreeze.setAutoFillBackground(False)
        self.screenfreeze.setStyleSheet("")
        self.screenfreeze.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/cross-mark-on-a-black-circle-background.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.screenfreeze.setIcon(icon5)
        self.screenfreeze.setFlat(True)
        self.screenfreeze.setObjectName("screenfreeze")
        self.back = QtWidgets.QPushButton(self)
        self.back.setEnabled(True)
        self.back.setGeometry(QtCore.QRect(0, 250, 30, 25))
        self.back.setMouseTracking(True)
        self.back.setTabletTracking(True)
        self.back.setAutoFillBackground(False)
        self.back.setStyleSheet("")
        self.back.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-sign-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon6)
        self.back.setFlat(True)
        self.back.setObjectName("back")
        self.notif_pull = QtWidgets.QPushButton(self)
        self.notif_pull.setEnabled(True)
        self.notif_pull.setGeometry(QtCore.QRect(0, 50, 30, 25))
        self.notif_pull.setMouseTracking(True)
        self.notif_pull.setTabletTracking(True)
        self.notif_pull.setAutoFillBackground(False)
        self.notif_pull.setStyleSheet("")
        self.notif_pull.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/bell-musical-tool.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notif_pull.setIcon(icon7)
        self.notif_pull.setFlat(True)
        self.notif_pull.setObjectName("notif_pull")
        self.powerUI = QtWidgets.QPushButton(self)
        self.powerUI.setEnabled(True)
        self.powerUI.setGeometry(QtCore.QRect(0, 200, 30, 25))
        self.powerUI.setMouseTracking(True)
        self.powerUI.setTabletTracking(True)
        self.powerUI.setAutoFillBackground(False)
        self.powerUI.setStyleSheet("")
        self.powerUI.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/power.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.powerUI.setIcon(icon8)
        self.powerUI.setIconSize(QtCore.QSize(16, 16))
        self.powerUI.setCheckable(False)
        self.powerUI.setFlat(True)
        self.powerUI.setObjectName("powerUI")
        self.pinchinUI = QtWidgets.QPushButton(self)
        self.pinchinUI.setEnabled(False)
        self.pinchinUI.setGeometry(QtCore.QRect(0, 325, 30, 25))
        self.pinchinUI.setStyleSheet("")
        self.pinchinUI.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/zoom-in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pinchinUI.setIcon(icon9)
        self.pinchinUI.setFlat(True)
        self.pinchinUI.setObjectName("pinchinUI")
        self.clipD2PC = QtWidgets.QPushButton(self)
        self.clipD2PC.setEnabled(True)
        self.clipD2PC.setGeometry(QtCore.QRect(0, 100, 30, 25))
        self.clipD2PC.setMouseTracking(True)
        self.clipD2PC.setTabletTracking(True)
        self.clipD2PC.setAutoFillBackground(False)
        self.clipD2PC.setStyleSheet("")
        self.clipD2PC.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/copy-document.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clipD2PC.setIcon(icon10)
        self.clipD2PC.setFlat(True)
        self.clipD2PC.setObjectName("clipD2PC")
        self.potraitUI = QtWidgets.QPushButton(self)
        self.potraitUI.setEnabled(True)
        self.potraitUI.setGeometry(QtCore.QRect(0, 375, 30, 25))
        self.potraitUI.setToolTipDuration(2)
        self.potraitUI.setStyleSheet("")
        self.potraitUI.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/vertical-resizing-option.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.potraitUI.setIcon(icon11)
        self.potraitUI.setFlat(True)
        self.potraitUI.setObjectName("potraitUI")
        self.landscapeUI = QtWidgets.QPushButton(self)
        self.landscapeUI.setEnabled(True)
        self.landscapeUI.setGeometry(QtCore.QRect(0, 400, 30, 25))
        self.landscapeUI.setToolTipDuration(2)
        self.landscapeUI.setStyleSheet("")
        self.landscapeUI.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/horizontal-resize-option.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.landscapeUI.setIcon(icon12)
        self.landscapeUI.setFlat(True)
        self.landscapeUI.setObjectName("landscapeUI")
        self.home = QtWidgets.QPushButton(self)
        self.home.setEnabled(True)
        self.home.setGeometry(QtCore.QRect(0, 225, 30, 25))
        self.home.setMouseTracking(True)
        self.home.setTabletTracking(True)
        self.home.setAutoFillBackground(False)
        self.home.setStyleSheet("")
        self.home.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home.setIcon(icon13)
        self.home.setFlat(True)
        self.home.setObjectName("home")
        self.vup = QtWidgets.QPushButton(self)
        self.vup.setEnabled(True)
        self.vup.setGeometry(QtCore.QRect(0, 150, 30, 25))
        self.vup.setMouseTracking(True)
        self.vup.setTabletTracking(True)
        self.vup.setAutoFillBackground(False)
        self.vup.setStyleSheet("")
        self.vup.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/icons/volume-up-interface-symbol.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vup.setIcon(icon14)
        self.vup.setFlat(True)
        self.vup.setObjectName("vup")
        self.vdown = QtWidgets.QPushButton(self)
        self.vdown.setEnabled(True)
        self.vdown.setGeometry(QtCore.QRect(0, 175, 30, 25))
        self.vdown.setMouseTracking(True)
        self.vdown.setTabletTracking(True)
        self.vdown.setAutoFillBackground(False)
        self.vdown.setStyleSheet("")
        self.vdown.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/icons/reduced-volume.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vdown.setIcon(icon15)
        self.vdown.setFlat(True)
        self.vdown.setObjectName("vdown")
        self.fullscreenUI = QtWidgets.QPushButton(self)
        self.fullscreenUI.setEnabled(True)
        self.fullscreenUI.setGeometry(QtCore.QRect(0, 25, 30, 25))
        self.fullscreenUI.setMouseTracking(True)
        self.fullscreenUI.setTabletTracking(True)
        self.fullscreenUI.setAutoFillBackground(False)
        self.fullscreenUI.setStyleSheet("")
        self.fullscreenUI.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/icons/increase-size-option.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fullscreenUI.setIcon(icon16)
        self.fullscreenUI.setFlat(True)
        self.fullscreenUI.setObjectName("fullscreenUI")
        self.clipPC2D = QtWidgets.QPushButton(self)
        self.clipPC2D.setEnabled(True)
        self.clipPC2D.setGeometry(QtCore.QRect(0, 125, 30, 25))
        self.clipPC2D.setMouseTracking(True)
        self.clipPC2D.setTabletTracking(True)
        self.clipPC2D.setAutoFillBackground(False)
        self.clipPC2D.setStyleSheet("")
        self.clipPC2D.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/icons/copy-document(1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clipPC2D.setIcon(icon17)
        self.clipPC2D.setFlat(True)
        self.clipPC2D.setObjectName("clipPC2D")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 410, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(0, 420, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.setFixedSize(30, 460)
        _translate = QtCore.QCoreApplication.translate
        self.notif_collapse.setToolTip(_translate("self", "Expand notification panel"))
        self.menuUI.setToolTip(_translate("self", "Menu key"))
        self.appswi.setToolTip(_translate("self", "press the APP_SWITCH button"))
        self.pinchoutUI.setToolTip(_translate("self", "Pinch out in the screen"))
        self.back.setToolTip(_translate("self", "Back key"))
        self.notif_pull.setToolTip(_translate("self", "Expand notification panel"))
        self.powerUI.setToolTip(_translate("self", "Power on/off"))
        self.pinchinUI.setToolTip(_translate("self", "Pinch in the screen"))
        self.clipD2PC.setToolTip(_translate("self", "Copy device clipbioard to PC"))
        self.potraitUI.setToolTip(_translate("self", "Potrait"))
        self.landscapeUI.setToolTip(_translate("self", "Landscape"))
        self.home.setToolTip(_translate("self", "Home key"))
        self.vup.setToolTip(_translate("self", "Volume Up"))
        self.fullscreenUI.setToolTip(_translate("self", "Fullscreen"))
        self.clipPC2D.setToolTip(_translate("self", "Copy PC clipboard to Device"))
        self.label.setText(_translate("self", "...."))
        self.label_2.setText(_translate("self", "...."))
        self.oldPos = self.pos()




        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        # self.setupUi(Dialog)
        self.clipD2PC.clicked.connect(clipd2pc)
        self.clipPC2D.clicked.connect(clippc2d)
        self.back.clicked.connect(Back)
        self.screenfreeze.clicked.connect(self.quitn)
        self.appswi.clicked.connect(switch)
        self.menuUI.clicked.connect(menu)
        self.home.clicked.connect(homekey)
        self.notif_pull.clicked.connect(notifExpand)
        self.notif_collapse.clicked.connect(notifCollapse)
        self.fullscreenUI.clicked.connect(fullscreen)
        self.powerUI.clicked.connect(power)
        self.vup.clicked.connect(volUP)
        self.vdown.clicked.connect(volDN)
        self.potraitUI.clicked.connect(reorientP)
        self.landscapeUI.clicked.connect(reorientL)
        self.show()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def quitn(self):
        print("Quitting")
        sys.exit()



class Panel(QMainWindow):
    # there was a Dialog in the bracket
    def __init__(self):

        super(Panel, self).__init__()
        print("POSITION OF PANEL:")
        # ---------------------------------
        # BETA test
        # -----------------------------------
        # imported bottompanelUI.py into main module
        # -----------------------------------

        self.setObjectName("self")
        self.resize(328, 26)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("\n"
            ".QPushButton {\n"
            "border-radius: 1px;\n"
            "color: rgb(0, 0, 0);\n"
            " \n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.915182, x2:0, y2:0.926, stop:0.897059 rgba(41, 41, 41, 255), stop:1 rgba(30, 30, 30, 255));\n"
            "                    }\n"
            "\n"
            "QPushButton:pressed {\n"
            "border-radius: 5px;\n"
            "                      \n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "                        }\n"
            "QPushButton:hover {\n"
            "border-radius: 5px;\n"
            "                      \n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "                        }\n"
            "")
        self.backk = QtWidgets.QPushButton(self)
        self.backk.setEnabled(True)
        self.backk.setGeometry(QtCore.QRect(210, 0, 51, 25))
        self.backk.setStyleSheet("")
        self.backk.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-sign-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backk.setIcon(icon1)
        self.backk.setObjectName("backk")
        self.powerUII = QtWidgets.QPushButton(self)
        self.powerUII.setEnabled(True)
        self.powerUII.setGeometry(QtCore.QRect(20, 0, 61, 25))
        self.powerUII.setStyleSheet("")
        self.powerUII.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/power.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.powerUII.setIcon(icon2)
        self.powerUII.setCheckable(False)
        self.powerUII.setObjectName("powerUII")
        self.menuUII = QtWidgets.QPushButton(self)
        self.menuUII.setEnabled(True)
        self.menuUII.setGeometry(QtCore.QRect(90, 0, 51, 25))
        self.menuUII.setStyleSheet("")
        self.menuUII.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/reorder-option.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuUII.setIcon(icon3)
        self.menuUII.setObjectName("menuUII")
        self.vdownn = QtWidgets.QPushButton(self)
        self.vdownn.setEnabled(True)
        self.vdownn.setGeometry(QtCore.QRect(270, 0, 31, 25))
        self.vdownn.setStyleSheet("")
        self.vdownn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/reduced-volume.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vdownn.setIcon(icon4)
        self.vdownn.setObjectName("vdownn")
        self.homee = QtWidgets.QPushButton(self)
        self.homee.setEnabled(True)
        self.homee.setGeometry(QtCore.QRect(140, 0, 71, 25))
        self.homee.setStyleSheet("")
        self.homee.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homee.setIcon(icon5)
        self.homee.setObjectName("homee")
        self.vupp = QtWidgets.QPushButton(self)
        self.vupp.setEnabled(True)
        self.vupp.setGeometry(QtCore.QRect(300, 0, 31, 25))
        self.vupp.setStyleSheet("")
        self.vupp.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/volume-up-interface-symbol.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vupp.setIcon(icon6)
        self.vupp.setObjectName("vupp")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, -10, 20, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.homee.raise_()
        self.backk.raise_()
        self.powerUII.raise_()
        self.menuUII.raise_()
        self.vdownn.raise_()
        self.vupp.raise_()
        self.label.raise_()
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Panel", "guiscrcpy"))
        self.backk.setToolTip(_translate("Panel", "Back key"))
        self.powerUII.setToolTip(_translate("Panel", "Power on/off"))
        self.menuUII.setToolTip(_translate("Panel", "Menu key"))
        self.vdownn.setToolTip(_translate("Panel", "Volume Up"))
        self.homee.setToolTip(_translate("Panel", "Home key"))
        self.label.setText(_translate("Panel", "::"))

        # -----------------------------------
        self.oldpos = self.pos()
        # Ui_Panel.__init__(self)
        # Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        # self.setupUi(Dialog)
        self.backk.clicked.connect(Back)
        self.menuUII.clicked.connect(menu)
        self.homee.clicked.connect(homekey)
        self.powerUII.clicked.connect(power)
        self.vupp.clicked.connect(volUP)
        self.vdownn.clicked.connect(volDN)

        self.show()
        print("self.oldpos", self.oldpos)
        print("FINE TILL HERE")
        # pdb.set_trace()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        print("HIT")

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)

        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    """
        def __init__(self, Dialog):
        super(Panel, self).__init__()

        Ui_Panel.__init__(self)
        # Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        self.setupUi(Dialog)
        self.backk.clicked.connect(Back)
        self.menuUII.clicked.connect(menu)
        self.homee.clicked.connect(homekey)
        self.powerUII.clicked.connect(power)
        self.vupp.clicked.connect(volUP)
        self.vdownn.clicked.connect(volDN)





        self.mwidget = Ui_Panel()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


        #size
        self.setFixedSize(320, 450)
        self.center()
        self.oldPos = self.pos()

        self.show()

    #center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


    def __init__(self, Dialog):
        super(Panel, self).__init__()

        Ui_Panel.__init__(self)
        # Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        self.setupUi(Dialog)
        self.backk.clicked.connect(Back)
        self.menuUII.clicked.connect(menu)
        self.homee.clicked.connect(homekey)
        self.powerUII.clicked.connect(power)
        self.vupp.clicked.connect(volUP)
        self.vdownn.clicked.connect(volDN)
        self.oldPos = self.pos()


    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        print("LOG: Delta: ", delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)
    """
# END TOOLKIT


def update_terminal():
    """
        self.new_thread = Terminal()
        self.connect(self.new_thread, SIGNAL("line"), self.show_variable)
        self.new_thread.start()
    """
    tmpTerminal = open("usercfgGUISCRCPY.cfg", "r")
    tmpRead = tmpTerminal.read()
    return tmpRead

"""
class StartScrcpy(QThread):
    print("Hello")

    def __init__(self, options):
        QThread.__init__(self)
        print("SCRCPY launch")
        # backup = po("scrcpy" + str(options),
        #                          shell=True,
        #                          stdin=PIPE,
        #                          stdout=PIPE,
        #                          stderr=STDOUT)

    def __del__(self):
        self.wait()

    def startSact(self):
        # TODO FIX OPTIONS
        # this block is for instantaneous reading the output
        # block ends out
        if checkProcessRunning("scrcpy"):
            print("SCRCPY RUNNING")
            # self.runningNot.setText("SCRCPY SERVER RUNNING")
        else:
            print("SCRCPY SERVER IS INACTIVE")
            # self.runningNot.setText("SCRCPY SERVER NOT RUNNING")

    def run(self):
        pass
"""

def readThreadStdOut():
    someFile = open("user.history", "w+")
    out, err = StartScrcpy.backup.stdout, StartScrcpy.backup.stderr
    out_decoded = out.decode("utf-8")
    someFile.write(str(out_decoded))
    someFile.flush()


runme = True
full = []

"""
def loop():
    for line in iter(StartScrcpy.backup.stdout.readline, b''):  # TODO NOT IMPLEMENTED
        line = line.rstrip().decode('utf8')
        print(">>>", line)
        full.append(line)
        output = '\n'.join(full)


loopprocess = multiprocessing.Process(target=loop)
loopprocess.start()
loopprocess.join()
print("Scrcpy proceed")
print(StartScrcpy.backup.stdout)
"""""


def checkProcessRunning(processName):
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


class MyApp(Ui_MainWindow):
    def __init__(self, MainWindow):

        super(MyApp, self).__init__()
        # uic.loadUi(qtCreatorFile, self)

        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        # self.setupUi(self)
        # self.menuAbout.itemPressed.connect(self.menu_about)

        # check if process Scrcpy is running right now in while loop
        """
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));
color: rgb(0, 0, 0);
border-radius: 10px;
border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(255, 0, 255, 255));
        """



        bit_rate = bitrate0
        dimensions = dimension0
        swtouches = swtouches0
        dispRO = dispRO0
        fullscreen_opt = fullscreen0
        print("OPTS:", bit_rate, dimensions, swtouches, dispRO, fullscreen_opt)
        self.dial.setValue(int(bit_rate))
        if (swtouches.find("True")>-1):
            self.showTouches.setChecked(True)
        else:
            self.showTouches.setChecked(False)
        if (dispRO.find("True")>-1):
            self.displayForceOn.setChecked(True)
        else:
            self.displayForceOn.setChecked(False)
        if dimensions != None:
            self.dimensionDefaultCheckbox.setChecked(False)
            try:
            	self.dimensionSlider.setValue(dimensions)
            except TypeError:
            	self.dimensionDefaultCheckbox.setChecked(True)
        if (fullscreen_opt.find("True")>-1):
            self.fullscreen.setChecked(True)
        else:
            self.fullscreen.setChecked(False)
        if checkProcessRunning("scrcpy"):
            print("SCRCPY RUNNING")
            self.runningNot.setText("SCRCPY SERVER RUNNING")
        else:
            print("SCRCPY SERVER IS INACTIVE")
            self.runningNot.setText("SCRCPY SERVER NOT RUNNING")

        # CONNECT DIMENSION CHECK BOX TO STATE CHANGE
        self.dimensionDefaultCheckbox.stateChanged.connect(self.dimensionChange)
        self.build_label.setText("Build " + str(build))

        # DIAL CTRL GRP
        self.dial.sliderMoved.connect(self.dial_text_refresh)
        self.dial.sliderReleased.connect(self.dial_text_refresh)
        # DIAL CTRL GRP

        # MAIN EXECUTE ACTION
        self.executeaction.clicked.connect(self.start_act)

        self.quit.clicked.connect(self.quitAct)
        self.dimensionText.setText("DEFAULT")
        bit_rate = int(self.dial.value())
        self.bitrateText.setText(" " + str(bit_rate) + "KB/s")
        self.pushButton.setText("RESET")
        self.pushButton.clicked.connect(self.reset)
        self.abtme.clicked.connect(self.openme)
        self.abtgit.clicked.connect(self.opengit)

    def openme(self):
        webbrowser.open("https://srevinsaju.wixsite.com/srevinsaju")
    def opengit(self):
        webbrowser.open("https://github.com/srevinsaju/guiscrcpy")
    def about(self):
        abtBox = QMessageBox().window()
        abtBox.about(self.pushButton, "Info", "Please restart GUIscrcpy to reset the settings. GUIscrcpy will now exit")
        abtBox.addButton("OK", abtBox.hide())
        abtBox.show()

    def reset(self):
        cfg = open(os.path.expanduser("~/guiscrcpy.cfg"), "w+")
        cfg.write("RESET" + str(time.time()))
        cfg.close()
        msgBox = QMessageBox().window()
        msgBox.about(self.pushButton, "Info", "Please restart GUIscrcpy to reset the settings. GUIscrcpy will now exit")
        msgBox.addButton("OK", self.quitAct())
        msgBox.show()

    def quitAct(self):

        sys.exit()

    def menu_about(self):
        pass

    def dimensionChange(self):

        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            dimension = None
            self.dimensionText.setText("DEFAULT")
            dimension0 = None

        else:
            self.dimensionSlider.setEnabled(True)
            dimension = int(self.dimensionSlider.value())
            dimension0 = int(self.dimensionSlider.value())
            self.dimensionText.setText(" "+str(dimension) + "px")
            self.dimensionSlider.sliderMoved.connect(self.slider_text_refresh)
            self.dimensionSlider.sliderReleased.connect(self.slider_text_refresh)

    def slider_text_refresh(self):
        dimension = int(self.dimensionSlider.value())
        dimension0 = int(self.dimensionSlider.value())
        self.dimensionText.setText(str(dimension) + "px")
        pass

    def dial_text_refresh(self):
        bit_rate = int(self.dial.value())
        bitrate0 = bit_rate
        print("xcx" + str(bitrate0))
        self.bitrateText.setText(str(bit_rate) + "KB/s")
        pass

    def start_act(self):


        self.runningNot.setText("CHECKING DEVICE CONNECTION")
        timei = time.time()
        self.progressBar.setValue(5)
        adb_chk = po("adb devices", shell=True, stdout=PIPE)
        output = adb_chk.stdout.readlines()
        print("ADB:", output)
        needed_output = output[1]

        deco = needed_output.decode("utf-8")
        det = deco.split("\t")

        if det[0] == "\n":
            self.runningNot.setText("DEVICE IS NOT CONNECTED")
            self.progressBar.setValue(0)
            return 0
        try:
            exc = det[1].find("device")
        except IndexError:
            self.runningNot.setText("DEVICE IS NOT CONNECTED")
            self.progressBar.setValue(0)
            return 0

        if det[1].find("device")>-1:
            self.runningNot.setText("DEVICE " + str(det[0]) + " IS CONNECTED")
            self.progressBar.setValue(10)

        elif det[1][:-1] == "unauthorized":
            self.runningNot.setText("DEVICE IS UNAUTHORIZED. PLEASE CLICK 'OK' ON DEVICE WHEN ASKED FOR")
            self.progressBar.setValue(0)
            return 0

        else:
            self.runningNot.setText("DEVICE CONNECTED BUT FAILED TO ESTABLISH CONNECTION")
            self.progressBar.setValue(0)
            return 0
        # check if the defaultDimension is checked or not for giving signal
        # ADB READ DIMENSIONS :: BEGIN
        adb_dim = po("adb shell wm size", shell=True, stdout=PIPE, stderr=PIPE)
        out = adb_dim.stdout.read()
        out_decoded = out.decode("utf-8")
        out_decoded = out_decoded[:-1]
        dimVal = out_decoded.split(": ")
        dimensions_ = dimVal[1]
        dimValues = dimensions_.split("x")

        self.progressBar.setValue(15)

        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            self.dimensionText.setText("DEFAULT")
            dimension = None
            dimension0 = None

        else:
            self.dimensionSlider.setEnabled(True)
            dimension = int(self.dimensionSlider.value())
            dimension0 = int(self.dimensionSlider.value())
            self.dimensionText.setText(str(dimension) + "px")

        # check if the defaultDimension is checked or not for giving signal
        self.progressBar.setValue(20)
        """
        proc =run(["scrcpy"], stdout=PIPE,
                                stderr=PIPE)
        out, err = proc.stdout, proc.stderr
        out_decoded = out.decode("utf-8")
        tmp.append(out_decoded)
        self.terminal.setText(str(tmp))
        """

        # process dimension
        if dimension is None:
            self.options = " "
            pass
        elif dimension is not None:
            self.options = " -m " + str(dimension)
        else:
            self.options = ""

        self.progressBar.setValue(25)
        # CHECK BOX GROUP CONNECT
        if self.aotop.isChecked():
            self.options += " --always-on-top"
        if self.fullscreen.isChecked():
            self.options += " -f"
            fullscreen0 = True
        else:
        	fullscreen0 = False
        """
        if self.keepdisplayRO.isChecked():
            self.options += " --no-control"
        """
        self.progressBar.setValue(30)
        if self.showTouches.isChecked():
            self.options += " --show-touches"
            swtouches0 = True

            """        if self.keepdisplayRO.isChecked():
            self.options += " --turn-screen-off"
            """

        else:
            swtouches0 = False
        if self.recScui.isChecked():
            self.options += " -r "+str(int(time.time()))+".mp4 "

            """        if self.keepdisplayRO.isChecked():
            self.options += " --turn-screen-off"
            """
        if self.displayForceOn.isChecked():
            self.options += " -S"
            dispRO0 = True
            """        if self.keepdisplayRO.isChecked():
            self.options += " --turn-screen-off"
            """

        else:
            dispRO0 = False


        self.options += " -b " + str(int(self.dial.value())) + "K"
        bitrate0 = str(int(self.dial.value()))
        self.progressBar.setValue(40)

        # implies program not idle

        """
        if(value == 91):
            print("DEVICE NOT DETECTED [ERROR]")
            self.runningNot.setText("DEVICE NOT DETECTED")
        else:
            print("DEVICE DETECTED")
            self.runningNot.setText("SCRCPY CONNECTED")
        """
        # TODO

        # self.myLine = startScrcpy(self.options)
        # self.connect(self.myLine, SIGNAL("update_terminal(QString)"), self.update_terminal)
        print("CONNECTION ESTABLISHED")
        self.progressBar.setValue(50)
        """
        for line in iter(backup.stdout.readline, b''): # TODO NOT IMPLEMENTED
            line = line.rstrip().decode('utf8')
            print(">>>", line)
            full.append(line)
            output = '\n'.join(full)
            self.terminal.setText(str(output))
        """
        print("FLAGS PASSED : " + self.options)
        self.progressBar.setValue(75)
        backup = po("scrcpy " + str(self.options),
                                  shell=True,
                                  stdin=PIPE,
                                  stdout=PIPE,
                                  stderr=STDOUT)
        # StartScrcpy(options=self.options)

        timef = time.time()
        eta = timef-timei
        print("SCRCPY is launched in", eta, "seconds")
        self.progressBar.setValue(100)

        # self.terminal.setText(full)
        cfg = open(os.path.expanduser("~/guiscrcpy.cfg"), "w+")
        print("writing: #" * 25 + "\n", "Created by Srevin Saju\n", "#" * 25 + "\n", str(time.time()) + "\n",
                        str(bitrate0) + "\n", str(dimension0) + "\n", str(swtouches0) + "\n",
                        str(fullscreen0) + "\n" + str(dispRO0) + "\n")
        cfg.writelines(("#" * 25 + "\n", "Created by Srevin Saju\n", "#" * 25 + "\n", str(time.time()) + "\n",
                        str(bitrate0) + "\n", str(dimension0) + "\n", str(swtouches0) + "\n",
                        str(fullscreen0) + "\n" + str(dispRO0) + "\n"))

        cfg.close()
        """
        p5 = multiprocessing.Process(target=update_terminal)
        p5.start()
        p5.join()
        """










if __name__ == "__main__":

        app = QtWidgets.QApplication(sys.argv)

        # file = QFile(":/dark.qss")
        # file.open(QFile.ReadOnly | QFile.Text)
        # stream = QTextStream(file)
        # app.setStyleSheet(stream.readAll())
        splash_pix = QPixmap(':/res/ui/guiscrcpy-branding.png')
        splash = QtWidgets.QSplashScreen(splash_pix)
        splash.setMask(splash_pix.mask())
        splash.show()
        app.processEvents()
        adb_chk0 = po("adb start-server", shell=True, stdout=PIPE, stderr=PIPE)
        time.sleep(1)
        app.processEvents()
        print("output:", adb_chk0.stdout)
        """
	Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
	Ui_Dialog = uic.loadUiType(qtCreatorFile)
	"""

        window = QtWidgets.QMainWindow()
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        # windoww = QtWidgets.QMainWindow()
        # windowww = QtWidgets.QMainWindow()
        prog = MyApp(window)
        # panel = Panel(windoww)
        panel = Panel()
        progg = MyAppv()
        window.show()
        splash.hide()
        # windowww.show()
        # windoww.show()
        app.exec_()
        # appo.exec_()
        sys.exit()