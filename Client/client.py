import sys, socket
from PyQt4 import QtGui, QtCore

errmsg = 'Could not connect to server.'
emptymsg = 'Please enter a server and port to connect to.'

class Client(QtGui.QMainWindow):
	"""user interface for chat program"""
	def __init__(self):
		"""init method"""
		super(Client, self).__init__()

		self.initUI()

	def initUI(self):
		"""initializes windows and any contained widgets"""
		self.btn = QtGui.QPushButton('Connect', self)
		self.btn.move(120, 150)
		self.btn.clicked.connect(self.getServer)

		self.lbl = QtGui.QLabel('Server: ', self)
		self.lbl.move(30, 58)

		self.lbl2 = QtGui.QLabel('Port: ', self)
		self.lbl2.move(30, 98)

		self.server = QtGui.QLineEdit(self)
		self.server.setGeometry(100, 62, 150, 22)

		self.port = QtGui.QLineEdit(self)
		self.port.setGeometry(100, 102, 150, 22)

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

def main():
	app = QtGui.QApplication(sys.argv)
	c = Client()
	sys.exit(app.exec_())

if __name__ == "__main__": 
	main()

