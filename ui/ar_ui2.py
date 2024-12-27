# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '自动发布界面设计cPXlgh.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(960, 796)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 941, 781))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 71, 41))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.comboBox_file = QComboBox(self.tab)
        self.comboBox_file.setObjectName(u"comboBox_file")
        self.comboBox_file.setGeometry(QRect(120, 30, 651, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.comboBox_file.setFont(font1)
        self.toolButton_file_select = QToolButton(self.tab)
        self.toolButton_file_select.setObjectName(u"toolButton_file_select")
        self.toolButton_file_select.setGeometry(QRect(790, 30, 111, 41))
        self.toolButton_file_select.setFont(font)
        self.toolButton_file_select.setCursor(QCursor(Qt.OpenHandCursor))
        self.toolButton_file_select.setFocusPolicy(Qt.NoFocus)
        self.toolButton_file_select.setAutoFillBackground(True)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 160, 81, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.comboBox_account = QComboBox(self.tab)
        self.comboBox_account.setObjectName(u"comboBox_account")
        self.comboBox_account.setGeometry(QRect(120, 150, 201, 41))
        self.pushButton_release = QPushButton(self.tab)
        self.pushButton_release.setObjectName(u"pushButton_release")
        self.pushButton_release.setGeometry(QRect(790, 660, 101, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton_release.setFont(font2)
        self.pushButton_release.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_release.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton_release.setAutoFillBackground(True)
        self.plainTextEdit_tags = QPlainTextEdit(self.tab)
        self.plainTextEdit_tags.setObjectName(u"plainTextEdit_tags")
        self.plainTextEdit_tags.setGeometry(QRect(30, 240, 391, 381))
        self.plainTextEdit_descris = QPlainTextEdit(self.tab)
        self.plainTextEdit_descris.setObjectName(u"plainTextEdit_descris")
        self.plainTextEdit_descris.setGeometry(QRect(450, 240, 451, 381))
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 210, 191, 16))
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(450, 210, 141, 16))
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 100, 41, 31))
        self.label_5.setFont(font)
        self.lineEdit_title = QLineEdit(self.tab)
        self.lineEdit_title.setObjectName(u"lineEdit_title")
        self.lineEdit_title.setGeometry(QRect(120, 90, 641, 41))
        self.pushButton_add_ks = QPushButton(self.tab)
        self.pushButton_add_ks.setObjectName(u"pushButton_add_ks")
        self.pushButton_add_ks.setGeometry(QRect(330, 150, 81, 41))
        self.pushButton_add_ks.setFont(font)
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 670, 211, 31))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u5730\u5740", None))
        self.toolButton_file_select.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5feb\u624b\u8d26\u53f7", None))
        self.comboBox_account.setPlaceholderText(QCoreApplication.translate("Form", u"\u9009\u62e9\u53d1\u5e03\u7684\u8d26\u53f7", None))
        self.pushButton_release.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u53d1\u5e03", None))
        self.plainTextEdit_tags.setPlainText(QCoreApplication.translate("Form", u"#\u6cbb\u6108\u7cfb\u52a8\u753b\n"
"#\u70ed\u8840\u52a8\u6f2b\n"
"#\u840c\u5ba0\u52a8\u753b\n"
"#\u52a8\u753b\u77ed\u7247\n"
"#\u52a8\u753b\u7535\u5f71\n"
"", None))
        self.plainTextEdit_descris.setPlainText(QCoreApplication.translate("Form", u"$$\u5feb\u4e50\u82f1\u8bed\uff0c\u8f7b\u677e\u5b66\u4e60\uff01$$\n"
"$$\u575a\u6301\u5b66\u4e60\uff0c\u6210\u5c31\u672a\u6765\uff01$$\n"
"$$\u82f1\u8bed\u5b66\u4e60\uff0c\u4e50\u8da3\u65e0\u7a77\uff01$$\n"
"$$\u548c\u6211\u4e00\u8d77\uff0c\u5feb\u4e50\u5b66\u82f1\u8bed\uff01$$", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u77ed\u89c6\u9891\u5e26\u7684\u6807\u7b7e#-\u6bcf\u6b21\u968f\u673a\u4e09\u4e2a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u53d1\u5e03\u6587\u6848-\u6bcf\u6b21\u968f\u673a\u4e00\u4e2a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6807\u9898", None))
        self.lineEdit_title.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u9700\u8981\u53d1\u5e03\u7684\u89c6\u9891\u6807\u9898\u548c\u7b80\u77ed\u4ecb\u7ecd", None))
        self.pushButton_add_ks.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u8d26\u53f7", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u6ce8\u610f:\u53d1\u5e03\u524d\u8bf7\u5148\u81ea\u884c\u6dfb\u52a0\u4e00\u4e2a\u5408\u96c6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u5355\u89c6\u9891", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u591a\u89c6\u9891", None))
    # retranslateUi

