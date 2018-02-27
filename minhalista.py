from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MinhaLista(object):
    def setupUi(self, MinhaLista):
        MinhaLista.setObjectName(_fromUtf8("MinhaLista"))
        MinhaLista.resize(478, 398)
        self.centralwidget = QtGui.QWidget(MinhaLista)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lista = QtGui.QListWidget(self.centralwidget)
        self.lista.setGeometry(QtCore.QRect(50, 30, 381, 241))
        self.lista.setObjectName(_fromUtf8("lista"))
        self.campoTexto = QtGui.QLineEdit(self.centralwidget)
        self.campoTexto.setGeometry(QtCore.QRect(50, 281, 381, 31))
        self.campoTexto.setObjectName(_fromUtf8("campoTexto"))
        self.btInserir = QtGui.QPushButton(self.centralwidget)
        self.btInserir.setGeometry(QtCore.QRect(50, 320, 99, 31))
        self.btInserir.setObjectName(_fromUtf8("btInserir"))
        self.btApagar = QtGui.QPushButton(self.centralwidget)
        self.btApagar.setGeometry(QtCore.QRect(190, 320, 99, 31))
        self.btApagar.setObjectName(_fromUtf8("btApagar"))
        self.btLimpar = QtGui.QPushButton(self.centralwidget)
        self.btLimpar.setGeometry(QtCore.QRect(330, 320, 99, 31))
        self.btLimpar.setObjectName(_fromUtf8("btLimpar"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(56, 10, 371, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        MinhaLista.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MinhaLista)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MinhaLista.setStatusBar(self.statusbar)

        self.retranslateUi(MinhaLista)
        QtCore.QObject.connect(self.btLimpar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.campoTexto.clear)
        QtCore.QMetaObject.connectSlotsByName(MinhaLista)

    def retranslateUi(self, MinhaLista):
        MinhaLista.setWindowTitle(_translate("MinhaLista", "Minha Lista", None))
        self.btInserir.setText(_translate("MinhaLista", "Inserir", None))
        self.btApagar.setText(_translate("MinhaLista", "Apagar", None))
        self.btLimpar.setText(_translate("MinhaLista", "Limpar", None))
        self.label.setText(_translate("MinhaLista", "Minha Lista", None))