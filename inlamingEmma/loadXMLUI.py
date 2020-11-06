import pymel.core as pm
from maya import OpenMayaUI as omui
from PySide2 import QtGui, QtCore, QtWidgets, QtUiTools
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
import AnimationTransferCode5

def getMayaWin():
	mayaWinPtr = omui.MQtUtil.mainWindow( )
	mayaWin = wrapInstance( long( mayaWinPtr ), QWidget )


def loadUI( path ):
	loader = QUiLoader()
	uiFile = QFile( path )
	
	dirIconShapes = ""
	buff = None

	if uiFile.exists():
		dirIconShapes = path
		uiFile.open( QFile.ReadOnly )

		buff = QByteArray( uiFile.readAll() )
		uiFile.close()
	else:
		print "UI file missing! Exiting..."
		exit(-1)
	
	fixXML( path, buff )
	qbuff = QBuffer()
	qbuff.open( QBuffer.ReadOnly | QBuffer.WriteOnly )
	qbuff.write( buff )
	qbuff.seek( 0 )
	ui = loader.load( qbuff, parentWidget = getMayaWin() )
	ui.path = path
	
	return ui


def fixXML( path, qbyteArray ):
	# first replace forward slashes for backslashes
	if path[-1] != '/':
		path += '/'
	path = path.replace( "/", "\\" )
	
	# construct whole new path with <pixmap> at the begining
	tempArr = QByteArray( "<pixmap>" + path + "\\" )
	
	# search for the word <pixmap>
	lastPos = qbyteArray.indexOf( "<pixmap>", 0 )
	while lastPos != -1:
		qbyteArray.replace( lastPos, len( "<pixmap>" ), tempArr )
		lastPos = qbyteArray.indexOf( "<pixmap>", lastPos + 1 )
	return



class UIController:
        def __init__( self, ui ):

                # Connect each signal to it's slot one by one
                self.phat = "C:/Users/BTH/Documents/maya/projects/default/scenes"
                self.listS = ""
                ui.rootSource.editingFinished.connect( self.RootSourceEnter )
                ui.rootTarget.editingFinished.connect( self.RootTargetEnter )
                ui.upSource.clicked.connect(self.UpBottonSource)
                ui.upTarget.clicked.connect(self.UpBottonTarget)
                ui.downSource.clicked.connect(self.DownBottonSource)
                ui.downTarget.clicked.connect(self.DownBottonTarget)
                ui.deleteSource.clicked.connect(self.DeletBottonSource)
                ui.deleteTarget.clicked.connect(self.DeletBottonTarget)
                ui.tranferAnimation.clicked.connect(self.TransferAnimation)

                self.ui = ui
                ui.setWindowFlags( Qt.WindowStaysOnTopHint )
                ui.show()

        def RootSourceEnter(self):
                self.listS = AnimationTransferCode5.jointList(self.ui.rootSource.text())
                self.ui.listSource.clear()
                for i in range(0, len(self.listS)):
                    self.ui.listSource.addItem(str(self.listS[i]))

        def RootTargetEnter(self):
                self.listS = AnimationTransferCode5.jointList(self.ui.rootTarget.text())
                self.ui.listTarget.clear()
                for i in range(0, len(self.listS)):
                    self.ui.listTarget.addItem(str(self.listS[i]))
                print self.ui.listTarget.item(1)


        def UpBottonSource(self):
                itemNr = self.ui.listSource.row(self.ui.listSource.selectedItems()[0])
                print itemNr
                if(itemNr > 0):
                    self.ui.listSource.insertItem(itemNr - 1, self.ui.listSource.takeItem(itemNr))

        def UpBottonTarget(self):
                itemNr = self.ui.listTarget.row(self.ui.listTarget.selectedItems()[0])
                print itemNr
                if(itemNr > 0):
                    self.ui.listTarget.insertItem(itemNr - 1, self.ui.listTarget.takeItem(itemNr))


        def DownBottonSource(self):
                itemNr = self.ui.listSource.row(self.ui.listSource.selectedItems()[0])
                print itemNr
                if(itemNr < self.ui.listSource.count()-1):
                    self.ui.listSource.insertItem(itemNr + 1, self.ui.listSource.takeItem(itemNr))

        def DownBottonTarget(self):
                itemNr = self.ui.listTarget.row(self.ui.listTarget.selectedItems()[0])
                print itemNr
                if(itemNr < self.ui.listTarget.count()-1):
                    self.ui.listTarget.insertItem(itemNr + 1, self.ui.listTarget.takeItem(itemNr))

        def DeletBottonSource(self):
            itemNr = self.ui.listSource.row(self.ui.listSource.selectedItems()[0])
            print itemNr
            self.ui.listSource.takeItem(itemNr)

        def DeletBottonTarget(self):
            itemNr = self.ui.listTarget.row(self.ui.listTarget.selectedItems()[0])
            print itemNr
            self.ui.listTarget.takeItem(itemNr)


        def TransferAnimation(self):
            if(self.ui.listTarget.count() != 0 and self.ui.listSource.count() != 0):
                jointListT = []
                jointListS = []
                for x in range(0, self.ui.listSource.count()):
                    aItem = self.ui.listSource.takeItem(0)
                    jointListS.append(aItem.text())
                for x in range(0, self.ui.listTarget.count()):
                    aItem = self.ui.listTarget.takeItem(0)
                    jointListT.append(aItem.text())
                print jointListS
                print jointListT
                AnimationTransferCode5.theTransferAnimation (jointListS, jointListT)








