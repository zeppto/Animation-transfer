import sys

#path = r"C:\Users\BTH\Desktop\PySide_ExampleCode\Maya2017_PySide2/"
#path = r"D:/bth_year_1/python/PyMel/inlamningsuppgift_3/"
path = r"E:\Animation_transfer\Qt-animation\inlamingEmma/"

if sys.path.count(path) < 1:
    sys.path.append(path)

import loadXMLUI
#reload(loadXMLUI) #Use this to update the module when changes has been made in loadXMLUI
#ui = loadXMLUI.loadUI(path + "aTransferUI.ui")
#ui = loadXMLUI.loadUI(path + "example.ui")
ui = loadXMLUI.loadUI(path + "aTransferUI.ui")
cont =	loadXMLUI.UIController(ui)
print "# GUI Loaded #"


# C:\Users\BTH\Documents\maya\projects\default\scenes defalt path