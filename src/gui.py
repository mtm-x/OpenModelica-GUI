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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import res_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(480, 330)
        Widget.setMinimumSize(QSize(480, 330))
        Widget.setMaximumSize(QSize(480, 330))
        self.help_but = QPushButton(Widget)
        self.help_but.setObjectName(u"help_but")
        self.help_but.setGeometry(QRect(30, 190, 51, 51))
        icon = QIcon()
        icon.addFile(u":/icons/res/question.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.help_but.setIcon(icon)
        self.help_but.setIconSize(QSize(22, 22))
        self.info_but = QPushButton(Widget)
        self.info_but.setObjectName(u"info_but")
        self.info_but.setGeometry(QRect(30, 260, 51, 51))
        icon1 = QIcon()
        icon1.addFile(u":/icons/res/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.info_but.setIcon(icon1)
        self.info_but.setIconSize(QSize(21, 21))
        self.main_search_line = QLineEdit(Widget)
        self.main_search_line.setObjectName(u"main_search_line")
        self.main_search_line.setGeometry(QRect(130, 30, 321, 41))
        font = QFont()
        font.setFamilies([u"Product Sans"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.main_search_line.setFont(font)
        self.main_search_line.setStyleSheet(u"font: 9pt \"Product Sans\";\n"
"")
        self.main_search_line.setClearButtonEnabled(True)
        self.folder_but = QPushButton(Widget)
        self.folder_but.setObjectName(u"folder_but")
        self.folder_but.setGeometry(QRect(130, 90, 161, 41))
        self.folder_but.setStyleSheet(u"font: 8pt \"Poppins\";")
        icon2 = QIcon()
        icon2.addFile(u":/icons/res/folder (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.folder_but.setIcon(icon2)
        self.folder_but.setIconSize(QSize(24, 24))
        self.launch_but = QPushButton(Widget)
        self.launch_but.setObjectName(u"launch_but")
        self.launch_but.setGeometry(QRect(290, 90, 161, 41))
        self.launch_but.setStyleSheet(u"font: 8pt \"Poppins\";")
        icon3 = QIcon()
        icon3.addFile(u":/icons/res/rocket.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.launch_but.setIcon(icon3)
        self.launch_but.setIconSize(QSize(22, 22))
        self.start_line = QLineEdit(Widget)
        self.start_line.setObjectName(u"start_line")
        self.start_line.setGeometry(QRect(130, 190, 191, 41))
        self.start_line.setStyleSheet(u"font: 9pt \"Product Sans\";")
        self.start_line.setClearButtonEnabled(True)
        self.stop_line = QLineEdit(Widget)
        self.stop_line.setObjectName(u"stop_line")
        self.stop_line.setGeometry(QRect(130, 270, 191, 41))
        self.stop_line.setStyleSheet(u"font: 9pt \"Product Sans\";\n"
"")
        self.stop_line.setClearButtonEnabled(True)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 51, 51))
        self.label.setPixmap(QPixmap(u":/icons/res/openmodelica.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 81, 21))
        self.label_2.setStyleSheet(u"\n"
"font: 600 9pt \"Poppins\";")
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 165, 81, 21))
        self.label_3.setStyleSheet(u"font: 10pt \"Poppins\";")
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 240, 81, 21))
        self.label_4.setStyleSheet(u"font: 10pt \"Poppins\";")
        self.set_but = QPushButton(Widget)
        self.set_but.setObjectName(u"set_but")
        self.set_but.setGeometry(QRect(330, 190, 121, 121))
        self.set_but.setStyleSheet(u"font: 9pt \"Poppins\";")
        icon4 = QIcon()
        icon4.addFile(u":/icons/res/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.set_but.setIcon(icon4)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.help_but.setText("")
#if QT_CONFIG(tooltip)
        self.info_but.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>Information</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.info_but.setWhatsThis(QCoreApplication.translate("Widget", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.info_but.setText("")
        self.main_search_line.setPlaceholderText(QCoreApplication.translate("Widget", u"Choose model .exe", None))
        self.folder_but.setText(QCoreApplication.translate("Widget", u"  Choose Model", None))
        self.launch_but.setText(QCoreApplication.translate("Widget", u"  Launch Model", None))
        self.start_line.setText("")
        self.start_line.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter start time in seconds", None))
#if QT_CONFIG(tooltip)
        self.stop_line.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>hiii</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stop_line.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter stop time in seconds", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-style:italic; color:#000000;\">LAUNCHER</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Start time:", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Stop time:", None))
        self.set_but.setText(QCoreApplication.translate("Widget", u"  Set Time", None))
    # retranslateUi

