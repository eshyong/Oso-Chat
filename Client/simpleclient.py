from collections import deque
import getpass
import select
import socket
import sys

class Client():
	def __init__(self):
		"""create client socket, get user name"""
		# this will connect directly to server
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# TODO: authentication
		self.username = self.authenticate()

		# outgoing messages
		self.msgqueue = deque()

		# inputs: server socket and stdin, outputs: server socket
		self.inputs = [sys.stdin, self.socket]
		self.outputs = [self.socket]

	def authenticate(self):
		"""sends credentials to server to authenticate user/password"""
		username = getpass.getpass('username: ')
		password = getpass.getpass('password: ')
		return username

	def connect(self):
		"""accepts user input, authenticates, and then connects"""
		# print 'please enter the server and port you wish to connect to.'
		# host = raw_input('server: ')
		# port = int(raw_input('port: '))
		"""for testing"""
		host = '127.0.0.1'
		port = 8080
		try:
			self.socket.connect((host, port))
			self.socket.send(self.username)
			print 'success!'
			return True
		except socket.error:
			print 'error connecting to server. try again.'
			return False

	def run(self):
		"""normal operation"""
		# poll for available sockets to read from
		read, write, error = \
			select.select(self.inputs, self.outputs, self.inputs)

		# read messages from terminal and server socket
		for r in read:
			if r == sys.stdin:
				msg = sys.stdin.readline()
				if msg == 'exit\n':
					# quit message is sent to client
					self.shutdown()
				else:
					self.msgqueue.append(msg)
			elif r == self.socket:
				# receive messages from server
				data = self.socket.recv(1024)

				# broken connection
				if not data:
					self.shutdown()
				else:
					print data,

		# send messages
		for w in write:
			if w == self.socket:
				# send data to server
				while self.msgqueue:
					self.socket.send(self.msgqueue.popleft())

		# some error
		for e in error:
			if e == self.socket:
				# some error in connection
				self.shutdown()

	def shutdown(self):
		# close socket and exit
		print 'boink'
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

