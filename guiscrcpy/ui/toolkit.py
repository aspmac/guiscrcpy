# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolkit_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ToolbarPanel(object):
	def setupUi(self, ToolbarPanel):
		ToolbarPanel.setObjectName("ToolbarPanel")
		ToolbarPanel.resize(30, 600)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.MinimumExpanding,
			QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			ToolbarPanel.sizePolicy().hasHeightForWidth())
		ToolbarPanel.setSizePolicy(sizePolicy)
		ToolbarPanel.setMinimumSize(QtCore.QSize(30, 337))
		ToolbarPanel.setMaximumSize(QtCore.QSize(30, 600))
		ToolbarPanel.setBaseSize(QtCore.QSize(30, 403))
		ToolbarPanel.setWindowTitle("guiscrcpy")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"),
		               QtGui.QIcon.Normal, QtGui.QIcon.Off)
		ToolbarPanel.setWindowIcon(icon)
		ToolbarPanel.setWindowOpacity(1.0)
		ToolbarPanel.setStyleSheet("QDialog{\n"
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
		self.layoutWidget = QtWidgets.QWidget(ToolbarPanel)
		self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 31, 601))
		self.layoutWidget.setObjectName("layoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
		self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.screenfreeze = QtWidgets.QPushButton(self.layoutWidget)
		self.screenfreeze.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.screenfreeze.sizePolicy().hasHeightForWidth())
		self.screenfreeze.setSizePolicy(sizePolicy)
		self.screenfreeze.setMouseTracking(True)
		self.screenfreeze.setTabletTracking(True)
		self.screenfreeze.setAutoFillBackground(False)
		self.screenfreeze.setStyleSheet("")
		self.screenfreeze.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(
			":/icons/icons/cross-mark-on-a-black-circle-background.svg"),
			QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.screenfreeze.setIcon(icon1)
		self.screenfreeze.setFlat(True)
		self.screenfreeze.setObjectName("screenfreeze")
		self.verticalLayout.addWidget(self.screenfreeze)
		self.fullscreenUI = QtWidgets.QPushButton(self.layoutWidget)
		self.fullscreenUI.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.fullscreenUI.sizePolicy().hasHeightForWidth())
		self.fullscreenUI.setSizePolicy(sizePolicy)
		self.fullscreenUI.setMouseTracking(True)
		self.fullscreenUI.setTabletTracking(True)
		self.fullscreenUI.setAutoFillBackground(False)
		self.fullscreenUI.setStyleSheet("")
		self.fullscreenUI.setText("")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(
			":/icons/icons/increase-size-option.svg"), QtGui.QIcon.Normal,
			QtGui.QIcon.Off)
		self.fullscreenUI.setIcon(icon2)
		self.fullscreenUI.setFlat(True)
		self.fullscreenUI.setObjectName("fullscreenUI")
		self.verticalLayout.addWidget(self.fullscreenUI)
		self.notif_pull = QtWidgets.QPushButton(self.layoutWidget)
		self.notif_pull.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.notif_pull.sizePolicy().hasHeightForWidth())
		self.notif_pull.setSizePolicy(sizePolicy)
		self.notif_pull.setMouseTracking(True)
		self.notif_pull.setTabletTracking(True)
		self.notif_pull.setAutoFillBackground(False)
		self.notif_pull.setStyleSheet("")
		self.notif_pull.setText("")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(
			":/icons/icons/bell-musical-tool.svg"), QtGui.QIcon.Normal,
			QtGui.QIcon.Off)
		self.notif_pull.setIcon(icon3)
		self.notif_pull.setFlat(True)
		self.notif_pull.setObjectName("notif_pull")
		self.verticalLayout.addWidget(self.notif_pull)
		self.notif_collapse = QtWidgets.QPushButton(self.layoutWidget)
		self.notif_collapse.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.notif_collapse.sizePolicy().hasHeightForWidth())
		self.notif_collapse.setSizePolicy(sizePolicy)
		self.notif_collapse.setMouseTracking(True)
		self.notif_collapse.setTabletTracking(True)
		self.notif_collapse.setAutoFillBackground(False)
		self.notif_collapse.setStyleSheet("")
		self.notif_collapse.setText("")
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(
			":/icons/icons/bell-musical-tool(2).svg"), QtGui.QIcon.Normal,
			QtGui.QIcon.Off)
		self.notif_collapse.setIcon(icon4)
		self.notif_collapse.setFlat(True)
		self.notif_collapse.setObjectName("notif_collapse")
		self.verticalLayout.addWidget(self.notif_collapse)
		self.clipD2PC = QtWidgets.QPushButton(self.layoutWidget)
		self.clipD2PC.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.clipD2PC.sizePolicy().hasHeightForWidth())
		self.clipD2PC.setSizePolicy(sizePolicy)
		self.clipD2PC.setMouseTracking(True)
		self.clipD2PC.setTabletTracking(True)
		self.clipD2PC.setAutoFillBackground(False)
		self.clipD2PC.setStyleSheet("")
		self.clipD2PC.setText("")
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap(
			":/icons/icons/copy-document.svg"), QtGui.QIcon.Normal,
			QtGui.QIcon.Off)
		self.clipD2PC.setIcon(icon5)
		self.clipD2PC.setFlat(True)
		self.clipD2PC.setObjectName("clipD2PC")
		self.verticalLayout.addWidget(self.clipD2PC)
		self.clipPC2D = QtWidgets.QPushButton(self.layoutWidget)
		self.clipPC2D.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.clipPC2D.sizePolicy().hasHeightForWidth())
		self.clipPC2D.setSizePolicy(sizePolicy)
		self.clipPC2D.setMouseTracking(True)
		self.clipPC2D.setTabletTracking(True)
		self.clipPC2D.setAutoFillBackground(False)
		self.clipPC2D.setStyleSheet("")
		self.clipPC2D.setText("")
		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap(
			":/icons/icons/copy-document(1).svg"), QtGui.QIcon.Normal,
			QtGui.QIcon.Off)
		self.clipPC2D.setIcon(icon6)
		self.clipPC2D.setFlat(True)
		self.clipPC2D.setObjectName("clipPC2D")
		self.verticalLayout.addWidget(self.clipPC2D)
		self.vup = QtWidgets.QPushButton(self.layoutWidget)
		self.vup.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.vup.sizePolicy().hasHeightForWidth())
		self.vup.setSizePolicy(sizePolicy)
		self.vup.setMouseTracking(True)
		self.vup.setTabletTracking(True)
		self.vup.setAutoFillBackground(False)
		self.vup.setStyleSheet("")
		self.vup.setText("")
		icon7 = QtGui.QIcon()
		icon7.addPixmap(QtGui.QPixmap(
			":/icons/icons/volume-up-interface-symbol.svg"),
			QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.vup.setIcon(icon7)
		self.vup.setFlat(True)
		self.vup.setObjectName("vup")
		self.verticalLayout.addWidget(self.vup)
		self.vdown = QtWidgets.QPushButton(self.layoutWidget)
		self.vdown.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.vdown.sizePolicy().hasHeightForWidth())
		self.vdown.setSizePolicy(sizePolicy)
		self.vdown.setMouseTracking(True)
		self.vdown.setTabletTracking(True)
		self.vdown.setAutoFillBackground(False)
		self.vdown.setStyleSheet("")
		self.vdown.setText("")
		icon8 = QtGui.QIcon()
		icon8.addPixmap(QtGui.QPixmap(
			":/icons/icons/reduced-volume.svg"), QtGui.QIcon.Normal,
			QtGui.QIcon.Off)
		self.vdown.setIcon(icon8)
		self.vdown.setFlat(True)
		self.vdown.setObjectName("vdown")
		self.verticalLayout.addWidget(self.vdown)
		self.powerUI = QtWidgets.QPushButton(self.layoutWidget)
		self.powerUI.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.powerUI.sizePolicy().hasHeightForWidth())
		self.powerUI.setSizePolicy(sizePolicy)
		self.powerUI.setMouseTracking(True)
		self.powerUI.setTabletTracking(True)
		self.powerUI.setAutoFillBackground(False)
		self.powerUI.setStyleSheet("")
		self.powerUI.setText("")
		icon9 = QtGui.QIcon()
		icon9.addPixmap(QtGui.QPixmap(":/icons/icons/power.svg"),
		                QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.powerUI.setIcon(icon9)
		self.powerUI.setIconSize(QtCore.QSize(16, 16))
		self.powerUI.setCheckable(False)
		self.powerUI.setFlat(True)
		self.powerUI.setObjectName("powerUI")
		self.verticalLayout.addWidget(self.powerUI)
		self.home = QtWidgets.QPushButton(self.layoutWidget)
		self.home.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.home.sizePolicy().hasHeightForWidth())
		self.home.setSizePolicy(sizePolicy)
		self.home.setMouseTracking(True)
		self.home.setTabletTracking(True)
		self.home.setAutoFillBackground(False)
		self.home.setStyleSheet("")
		self.home.setText("")
		icon10 = QtGui.QIcon()
		icon10.addPixmap(QtGui.QPixmap(":/icons/icons/home.svg"),
		                 QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.home.setIcon(icon10)
		self.home.setFlat(True)
		self.home.setObjectName("home")
		self.verticalLayout.addWidget(self.home)
		self.back = QtWidgets.QPushButton(self.layoutWidget)
		self.back.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.back.sizePolicy().hasHeightForWidth())
		self.back.setSizePolicy(sizePolicy)
		self.back.setMouseTracking(True)
		self.back.setTabletTracking(True)
		self.back.setAutoFillBackground(False)
		self.back.setStyleSheet("")
		self.back.setText("")
		icon11 = QtGui.QIcon()
		icon11.addPixmap(QtGui.QPixmap(
			":/icons/icons/chevron-sign-left.svg"), QtGui.QIcon.Normal,
			QtGui.QIcon.Off)
		self.back.setIcon(icon11)
		self.back.setFlat(True)
		self.back.setObjectName("back")
		self.verticalLayout.addWidget(self.back)
		self.menuUI = QtWidgets.QPushButton(self.layoutWidget)
		self.menuUI.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.menuUI.sizePolicy().hasHeightForWidth())
		self.menuUI.setSizePolicy(sizePolicy)
		self.menuUI.setMouseTracking(True)
		self.menuUI.setTabletTracking(True)
		self.menuUI.setAutoFillBackground(False)
		self.menuUI.setStyleSheet("")
		self.menuUI.setText("")
		icon12 = QtGui.QIcon()
		icon12.addPixmap(QtGui.QPixmap(
			":/icons/icons/reorder-option.svg"), QtGui.QIcon.Normal,
			QtGui.QIcon.Off)
		self.menuUI.setIcon(icon12)
		self.menuUI.setFlat(True)
		self.menuUI.setObjectName("menuUI")
		self.verticalLayout.addWidget(self.menuUI)
		self.appswi = QtWidgets.QPushButton(self.layoutWidget)
		self.appswi.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.appswi.sizePolicy().hasHeightForWidth())
		self.appswi.setSizePolicy(sizePolicy)
		self.appswi.setMouseTracking(True)
		self.appswi.setTabletTracking(True)
		self.appswi.setAutoFillBackground(False)
		self.appswi.setStyleSheet("")
		self.appswi.setText("")
		icon13 = QtGui.QIcon()
		icon13.addPixmap(QtGui.QPixmap(
			":/icons/icons/four-black-squares.svg"), QtGui.QIcon.Normal,
			QtGui.QIcon.Off)
		self.appswi.setIcon(icon13)
		self.appswi.setFlat(True)
		self.appswi.setObjectName("appswi")
		self.verticalLayout.addWidget(self.appswi)
		self.pinchinUI = QtWidgets.QPushButton(self.layoutWidget)
		self.pinchinUI.setEnabled(False)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.pinchinUI.sizePolicy().hasHeightForWidth())
		self.pinchinUI.setSizePolicy(sizePolicy)
		self.pinchinUI.setStyleSheet("")
		self.pinchinUI.setText("")
		icon14 = QtGui.QIcon()
		icon14.addPixmap(QtGui.QPixmap(":/icons/icons/zoom-in.svg"),
		                 QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pinchinUI.setIcon(icon14)
		self.pinchinUI.setFlat(True)
		self.pinchinUI.setObjectName("pinchinUI")
		self.verticalLayout.addWidget(self.pinchinUI)
		self.pinchoutUI = QtWidgets.QPushButton(self.layoutWidget)
		self.pinchoutUI.setEnabled(False)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.pinchoutUI.sizePolicy().hasHeightForWidth())
		self.pinchoutUI.setSizePolicy(sizePolicy)
		self.pinchoutUI.setStyleSheet("")
		self.pinchoutUI.setText("")
		icon15 = QtGui.QIcon()
		icon15.addPixmap(QtGui.QPixmap(":/icons/icons/zoom-out.svg"),
		                 QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pinchoutUI.setIcon(icon15)
		self.pinchoutUI.setFlat(True)
		self.pinchoutUI.setObjectName("pinchoutUI")
		self.verticalLayout.addWidget(self.pinchoutUI)
		self.potraitUI = QtWidgets.QPushButton(self.layoutWidget)
		self.potraitUI.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.potraitUI.sizePolicy().hasHeightForWidth())
		self.potraitUI.setSizePolicy(sizePolicy)
		self.potraitUI.setToolTipDuration(2)
		self.potraitUI.setStyleSheet("")
		self.potraitUI.setText("")
		icon16 = QtGui.QIcon()
		icon16.addPixmap(QtGui.QPixmap(
			":/icons/icons/vertical-resizing-option.svg"), QtGui.QIcon.Normal,
			QtGui.QIcon.Off)
		self.potraitUI.setIcon(icon16)
		self.potraitUI.setFlat(True)
		self.potraitUI.setObjectName("potraitUI")
		self.verticalLayout.addWidget(self.potraitUI)
		self.landscapeUI = QtWidgets.QPushButton(self.layoutWidget)
		self.landscapeUI.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.landscapeUI.sizePolicy().hasHeightForWidth())
		self.landscapeUI.setSizePolicy(sizePolicy)
		self.landscapeUI.setToolTipDuration(2)
		self.landscapeUI.setStyleSheet("")
		self.landscapeUI.setText("")
		icon17 = QtGui.QIcon()
		icon17.addPixmap(QtGui.QPixmap(
			":/icons/icons/horizontal-resize-option.svg"), QtGui.QIcon.Normal,
			QtGui.QIcon.Off)
		self.landscapeUI.setIcon(icon17)
		self.landscapeUI.setFlat(True)
		self.landscapeUI.setObjectName("landscapeUI")
		self.verticalLayout.addWidget(self.landscapeUI)
		self.label = QtWidgets.QLabel(self.layoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setScaledContents(True)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.verticalLayout.addWidget(self.label)
		self.label_2 = QtWidgets.QLabel(self.layoutWidget)
		sizePolicy = QtWidgets.QSizePolicy(
			QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(
			self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setScaledContents(True)
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.verticalLayout.addWidget(self.label_2)

		self.retranslateUi(ToolbarPanel)
		QtCore.QMetaObject.connectSlotsByName(ToolbarPanel)

	def retranslateUi(self, ToolbarPanel):
		_translate = QtCore.QCoreApplication.translate
		self.fullscreenUI.setToolTip(_translate("ToolbarPanel", "Fullscreen"))
		self.notif_pull.setToolTip(_translate(
			"ToolbarPanel", "Expand notification panel"))
		self.notif_collapse.setToolTip(_translate(
			"ToolbarPanel", "Expand notification panel"))
		self.clipD2PC.setToolTip(_translate(
			"ToolbarPanel", "Copy device clipbioard to PC"))
		self.clipPC2D.setToolTip(_translate(
			"ToolbarPanel", "Copy PC clipboard to Device"))
		self.vup.setToolTip(_translate("ToolbarPanel", "Volume Up"))
		self.powerUI.setToolTip(_translate("ToolbarPanel", "Power on/off"))
		self.home.setToolTip(_translate("ToolbarPanel", "Home key"))
		self.back.setToolTip(_translate("ToolbarPanel", "Back key"))
		self.menuUI.setToolTip(_translate("ToolbarPanel", "Menu key"))
		self.appswi.setToolTip(_translate(
			"ToolbarPanel", "press the APP_SWITCH button"))
		self.pinchinUI.setToolTip(_translate(
			"ToolbarPanel", "Pinch in the screen"))
		self.pinchoutUI.setToolTip(_translate(
			"ToolbarPanel", "Pinch out in the screen"))
		self.potraitUI.setToolTip(_translate("ToolbarPanel", "Potrait"))
		self.landscapeUI.setToolTip(_translate("ToolbarPanel", "Landscape"))
		self.label.setText(_translate("ToolbarPanel", "::::"))
		self.label_2.setText(_translate("ToolbarPanel", "::::"))
