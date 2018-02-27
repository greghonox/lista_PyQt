#coding: utf-8
from PyQt4 import QtGui, QtCore
import sys, minhalista
'''
Created on 28/06/2013
@author: jonathan
'''

class MinhaListaAdmin(QtGui.QMainWindow, minhalista.Ui_MinhaLista):
    def __init__(self, parent=None):
        super(MinhaListaAdmin, self).__init__(parent)
        self.setupUi(self)
        
        #Bindings
        self.btInserir.clicked.connect(self.inserir)
        self.btApagar.clicked.connect(self.apagar)
        
    def inserir(self):
        if self.campoTexto.text():
            self.lista.addItem(self.campoTexto.text())
            self.campoTexto.clear()
            
    def apagar(self):
        if self.lista.currentItem():
            if QtGui.QMessageBox.question(self, "Atenção", "Tem certeza que deseja apagar este item?", "Não", "Sim"):
                item = self.lista.takeItem(self.lista.currentRow())
                item = None

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    admin = MinhaListaAdmin()
    admin.show()
    app.exec_()