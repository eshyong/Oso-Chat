import sys, socket
from PyQt4 import QtGui, QtCore

errormsg = 'Could not connect to server.'
emptymsg = 'Please enter a server and port to connect to.'

class ConnectWindow(QtGui.QWidget):

	def __init__(self):
		"""init method"""
		super(ConnectWindow, self).__init__()

		self.initUI()

	def initUI(self):
		"""initializes windows and any contained widgets"""
		self.btn = QtGui.QPushButton('Connect', self)
		self.btn.move(140, 150)
		self.btn.clicked.connect(self.getServer)

		self.lbl1 = QtGui.QLabel('Please enter the server name\n'
			'and port that you wish to connect to', self)
		self.lbl1.move(30, 14)

		self.lbl2 = QtGui.QLabel('Server: ', self)
		self.lbl2.move(30, 62)

		self.lbl3 = QtGui.QLabel('Port: ', self)
		self.lbl3.move(30, 102)

		self.server = QtGui.QLineEdit(self)
		self.server.move(140, 62)

		self.port = QtGui.QLineEdit(self)
		self.port.move(140, 102)

		self.error = QtGui.QErrorMessage()

		self.setGeometry(300, 300, 340, 200)
		self.setWindowTitle('Talk')
		self.center()
		self.show()

	def center(self):
		"""centers window"""
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def getServer(self):
		"""tries to connect to server"""
		servername = self.server.text()
		port = self.port.text()

		if not servername or not port:
			self.error.showMessage(emptymsg)
		else:
			print servername + ':' + port

class Client():

	def __init__(self, username):
		self.username = username

	def sendMessage(self, message):
		return

def main():
	app = QtGui.QApplication(sys.argv)
	d = ConnectWindow()
	sys.exit(app.exec_())

if __name__ == "__main__": 
	main()