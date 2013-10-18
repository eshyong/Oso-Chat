import getpass
import select
import socket
import sys

class Client():
	def __init__(self):
		"""create client socket, get user name"""
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.username = self.authenticate()

	def authenticate(self):
		"""TODO: authenticate user"""
		username = getpass.getpass('username: ')
		password = getpass.getpass('password: ')
		return username

	def connect(self):
		"""accepts user input, authenticates, and then connects"""
		print 'please enter the server and port you wish to connect to.'
		host = raw_input('server: ')
		port = int(raw_input('port: '))
		try:
			self.socket.connect((host, port))
			self.socket.send(self.username)
			print 'success!'
			return True
		except socket.error:
			print 'error connecting to server. try again.'

	def run(self):
		"""normal operation"""
		# read and send messages from CLI
		msg = sys.stdin.readline()
		if msg == 'exit':
			# quit message is sent to client
			self.shutdown()
		else:
			self.socket.send(msg)

		# receive messages from server
		data = self.socket.recv(1024)

		# broken connection
		if not data:
			self.shutdown()
		else:
			print data,

	def shutdown(self):
		# close socket and exit
		self.socket.close()
		sys.exit()

def main():
	"""client is initialized and connected here"""
	c = Client()
	connected = False
	while not connected:
		connected = c.connect()
	
	# operation loop
	while 1:
		c.run()

if __name__ == '__main__':
	main()

