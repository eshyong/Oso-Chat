import sys, socket
from PyQt4 import QtGui, QtCore

errormsg = 'Could not connect to server.'
emptymsg = 'Please enter a server to connect to.'
port = 8000

class ConnectWindow(QtGui.QWidget):

	def __init__(self):
		"""init method"""
		super(ConnectWindow, self).__init__()

		self.initUI()

	def initUI(self):
		"""initializes windows and any contained widgets"""
		self.btn = QtGui.QPushButton('Connect', self)
		self.btn.move(190, 20)
		self.btn.clicked.connect(self.getServer)

		self.server = QtGui.QLineEdit(self)
		self.server.move(20, 22)

		self.error = QtGui.QErrorMessage()

		self.setGeometry(300, 300, 300, 200)
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

		if not servername:
			self.error.showMessage(emptymsg)
		else:
			s = socket.socket()
			host = servername
			s.connect((host, port))

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