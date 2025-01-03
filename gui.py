# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QListView, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import res_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(550, 419)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftmenu = QWidget(Widget)
        self.leftmenu.setObjectName(u"leftmenu")
        self.verticalLayout = QVBoxLayout(self.leftmenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.leftmenu)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.widget_2 = QWidget(self.leftmenu)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.info_but = QPushButton(self.widget_2)
        self.info_but.setObjectName(u"info_but")

        self.verticalLayout_3.addWidget(self.info_but)

        self.help_but = QPushButton(self.widget_2)
        self.help_but.setObjectName(u"help_but")

        self.verticalLayout_3.addWidget(self.help_but)


        self.verticalLayout.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.leftmenu, 0, Qt.AlignmentFlag.AlignLeft)

        self.rightpanel = QWidget(Widget)
        self.rightpanel.setObjectName(u"rightpanel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightpanel.sizePolicy().hasHeightForWidth())
        self.rightpanel.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.rightpanel)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_5 = QWidget(self.rightpanel)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.widget_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.main_search_line = QLineEdit(self.frame)
        self.main_search_line.setObjectName(u"main_search_line")

        self.horizontalLayout_3.addWidget(self.main_search_line)

        self.launch_but = QPushButton(self.frame)
        self.launch_but.setObjectName(u"launch_but")

        self.horizontalLayout_3.addWidget(self.launch_but)


        self.verticalLayout_7.addWidget(self.frame)

        self.listView = QListView(self.widget_5)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_7.addWidget(self.listView)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout_7.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignVCenter)

        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.widget_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.start_line = QLineEdit(self.frame_4)
        self.start_line.setObjectName(u"start_line")

        self.horizontalLayout_5.addWidget(self.start_line)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stop_line = QLineEdit(self.frame_2)
        self.stop_line.setObjectName(u"stop_line")

        self.horizontalLayout_4.addWidget(self.stop_line)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.set_but = QPushButton(self.frame_3)
        self.set_but.setObjectName(u"set_but")

        self.verticalLayout_8.addWidget(self.set_but)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_7.addWidget(self.widget_4)


        self.verticalLayout_4.addWidget(self.widget_5)


        self.horizontalLayout.addWidget(self.rightpanel)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.info_but.setText(QCoreApplication.translate("Widget", u"Info", None))
        self.help_but.setText(QCoreApplication.translate("Widget", u"Help", None))
        self.main_search_line.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter model name", None))
        self.launch_but.setText(QCoreApplication.translate("Widget", u"Launch Model", None))
        self.start_line.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter start time in seconds", None))
        self.stop_line.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter stop time in seconds", None))
        self.set_but.setText(QCoreApplication.translate("Widget", u"Set", None))
    # retranslateUi

