import socket, getpass

class Client():
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connected = False
		self.username = self.authenticate()

	def authenticate(self):
		username = getpass.getpass('username: ')
		password = getpass.getpass('password: ')
		return username

	def connect(self):
		print 'please enter the server and port you wish to connect to.'
		host = raw_input('server: ')
		port = raw_input('port: ')
		try:
			self.socket.connect((host, port))
			print 'success!'
		except socket.error:
			print 'error connecting to server. try again.'

def main():
	c = Client()
	while not c.connected:
		c.connect()
	while True:
		c.recv(1024)

if __name__ == '__main__':
	main()

