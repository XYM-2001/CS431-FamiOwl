# Form implementation generated from reading ui file 'signin_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QMovie


class Ui_Signin_Window(object):
    def setupUi(self, Signin_Window):
        Signin_Window.setObjectName("Signin_Window")
        Signin_Window.resize(800, 450)
        Signin_Window.setMinimumSize(QtCore.QSize(800, 450))
        Signin_Window.setMaximumSize(QtCore.QSize(800, 450))
        Signin_Window.setStyleSheet("background-color: black;\n"
                                    "color: white")
        self.centralwidget = QtWidgets.QWidget(Signin_Window)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 450))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 450))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.title_layout = QtWidgets.QHBoxLayout()
        self.title_layout.setObjectName("title_layout")
        self.place_holder_layout = QtWidgets.QVBoxLayout()
        self.place_holder_layout.setObjectName("place_holder_layout")
        self.place_holder_button = QtWidgets.QPushButton(self.centralwidget)
        self.place_holder_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.place_holder_button.sizePolicy().hasHeightForWidth())
        self.place_holder_button.setSizePolicy(sizePolicy)
        self.place_holder_button.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.place_holder_button.setFont(font)
        self.place_holder_button.setStyleSheet("background-color: transparent;\n"
                                               "color: transparent;")
        self.place_holder_button.setObjectName("place_holder_button")
        self.place_holder_layout.addWidget(self.place_holder_button)
        spacerItem = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.place_holder_layout.addItem(spacerItem)
        self.title_layout.addLayout(self.place_holder_layout)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.title_layout.addItem(spacerItem1)
        self.famiowl_title_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.famiowl_title_label.sizePolicy().hasHeightForWidth())
        self.famiowl_title_label.setSizePolicy(sizePolicy)
        self.famiowl_title_label.setText("")
        self.famiowl_title_label.setPixmap(QtGui.QPixmap("src/resource/famiowl_title.png"))
        self.famiowl_title_label.setScaledContents(False)
        self.famiowl_title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.famiowl_title_label.setObjectName("famiowl_title_label")
        self.title_layout.addWidget(self.famiowl_title_label)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.title_layout.addItem(spacerItem2)
        self.exit_layout = QtWidgets.QVBoxLayout()
        self.exit_layout.setObjectName("exit_layout")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)
        self.exit_button.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("background-color: transparent;\n"
                                       "color: white;")
        self.exit_button.setObjectName("exit_button")
        self.exit_layout.addWidget(self.exit_button)
        spacerItem3 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        self.exit_layout.addItem(spacerItem3)
        self.title_layout.addLayout(self.exit_layout)
        self.verticalLayout_9.addLayout(self.title_layout)
        self.owl_gif_layout = QtWidgets.QVBoxLayout()
        self.owl_gif_layout.setObjectName("owl_gif_layout")
        self.owl_gif = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.owl_gif.sizePolicy().hasHeightForWidth())
        self.owl_gif.setSizePolicy(sizePolicy)
        self.owl_gif.setMaximumSize(QtCore.QSize(16777215, 179))
        self.owl_gif.setText("")
        self.owl_gif_movie = QMovie("src/resource/owl_gif.gif")
        self.owl_gif.setMovie(self.owl_gif_movie)
        self.owl_gif_movie.start()
        # self.owl_gif.setPixmap(QtGui.QPixmap(":/owl_gif/owl_gif.gif"))
        #         # self.owl_gif.setObjectName("owl_gif")
        self.owl_gif_layout.addWidget(self.owl_gif)
        self.signin_layout = QtWidgets.QGridLayout()
        self.signin_layout.setObjectName("signin_layout")
        self.signup_button = QtWidgets.QPushButton(self.centralwidget)
        self.signup_button.setStyleSheet("background-color: transparent;\n"
                                         "color: white;")
        self.signup_button.setObjectName("signup_button")
        self.signin_layout.addWidget(self.signup_button, 3, 2, 1, 1)
        # self.forget_pwd_button = QtWidgets.QPushButton(self.centralwidget)
        # self.forget_pwd_button.setStyleSheet("background-color: transparent;\n"
        #                                      "color: white;\n"
        #                                      "\n"
        #                                      "")
        # self.forget_pwd_button.setObjectName("forget_pwd_button")
        # self.signin_layout.addWidget(self.forget_pwd_button, 2, 2, 1, 1)
        self.user_input_layout = QtWidgets.QVBoxLayout()
        self.user_input_layout.setObjectName("user_input_layout")
        self.userid_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userid_line.sizePolicy().hasHeightForWidth())
        self.userid_line.setSizePolicy(sizePolicy)
        self.userid_line.setMinimumSize(QtCore.QSize(300, 0))
        self.userid_line.setMaximumSize(QtCore.QSize(300, 16777215))
        self.userid_line.setStyleSheet("background-color: white;\n"
                                       "color: black;")
        self.userid_line.setText("")
        self.userid_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.userid_line.setObjectName("userid_line")
        self.user_input_layout.addWidget(self.userid_line)
        self.pwd_line = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd_line.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwd_line.sizePolicy().hasHeightForWidth())
        self.pwd_line.setSizePolicy(sizePolicy)
        self.pwd_line.setMinimumSize(QtCore.QSize(300, 0))
        self.pwd_line.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pwd_line.setAutoFillBackground(False)
        self.pwd_line.setStyleSheet("background-color: white;\n"
                                    "color: black;")
        self.pwd_line.setText("")
        self.pwd_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pwd_line.setObjectName("pwd_line")
        self.user_input_layout.addWidget(self.pwd_line)
        self.signin_layout.addLayout(self.user_input_layout, 1, 2, 1, 1)
        self.signin_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signin_button.sizePolicy().hasHeightForWidth())
        self.signin_button.setSizePolicy(sizePolicy)
        self.signin_button.setMaximumSize(QtCore.QSize(60, 60))
        self.signin_button.setStyleSheet("background-color: transparent;")
        self.signin_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/resource/login_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.signin_button.setIcon(icon)
        self.signin_button.setIconSize(QtCore.QSize(60, 60))
        self.signin_button.setObjectName("signin_button")
        self.signin_layout.addWidget(self.signin_button, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.signin_layout.addItem(spacerItem4, 1, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.signin_layout.addItem(spacerItem5, 1, 1, 1, 1)
        self.owl_gif_layout.addLayout(self.signin_layout)
        self.verticalLayout_9.addLayout(self.owl_gif_layout)
        Signin_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Signin_Window)
        QtCore.QMetaObject.connectSlotsByName(Signin_Window)

    def retranslateUi(self, Signin_Window):
        _translate = QtCore.QCoreApplication.translate
        Signin_Window.setWindowTitle(_translate("Signin_Window", "FamiOwl Sign In"))
        self.place_holder_button.setText(_translate("Signin_Window", "X"))
        self.exit_button.setText(_translate("Signin_Window", "X"))
        self.signup_button.setText(_translate("Signin_Window", "Sign up ->"))
        # self.forget_pwd_button.setText(_translate("Signin_Window", "Forget your password?"))
        self.userid_line.setPlaceholderText(_translate("Signin_Window", "User ID"))
        self.pwd_line.setPlaceholderText(_translate("Signin_Window", "Password"))
