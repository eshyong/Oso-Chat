import select
import socket
import sys
from collections import deque

host = ''
port = 8080
backlog = 5

class Server():
	def __init__(self):
		"""initialize the server socket and any data structures 
		for names"""
		# messages to send
		self.messages = deque([])

		# names of each client
		self.names = {}

		# server socket
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.bind((host, port))
		self.socket.listen(5)

		print 'server listening...'
		
		# inputs to read from, outputs to write to
		self.inputs = [self.socket, sys.stdin]
		self.outputs = []

	def connectClient(self):
		"""accept new connections and add clients"""
		# register client name
		conn, addr = self.socket.accept()
		name = conn.recv(1024)

		# add new client to each one
		self.names[conn] = name
		self.inputs.append(conn)
		self.outputs.append(conn)

		print self.names[conn] + ' says: \"play ball!\"' 

	def authenticate(self, name, password):
		return

	def getMessage(self, conn):
		"""receive messages from each client to send out"""
		data = conn.recv(1024)
		if data:
			# append message to queue, to read and send later
			self.messages.append((self.names[conn], data))
		else:
			# assume dead connection
			print 'boink: ' + self.names[conn] + ' exiting'
			conn.close()
			self.names.pop(conn)
			self.inputs.remove(conn)
			self.outputs.remove(conn)

	def run(self):
		"""normal operations for server"""
		# select polls all sockets, ignore write list as we send to all
		read, write, error = \
			select.select(self.inputs, self.outputs, self.inputs)

		# read messages from all inputs
		for r in read:
			# CLI command allows user to shutdown server
			if r == sys.stdin:
				cmd = sys.stdin.readline()
				if cmd == 'exit\n':
					self.shutdown()
			# server socket accepts new connections
			elif r == self.socket:
				self.connectClient()
			# client socket retrieves chat messages
			else:
				self.getMessage(r)

		# send messages to everyone connected
		while self.messages:
			tup = self.messages.popleft()
			msg = tup[0] + ' says: ' + tup[1]
			for conn in self.names.keys():
				conn.send(msg)

		# errors
		for e in error:
			print 'ABORT'
			e.close()

			# check for socket in other lists
			if e in read:
				read.remove(e)
			if e in write:
				write.remove(e)

			# finally, remove socket from error list
			error.remove(e)

	def shutdown(self):
		"""shutdowns all communications"""
		# close server socket
		self.socket.close()

		# close client connections
		for conn in self.names.keys():
			conn.close()

		# remove from lists
		while self.names:
			self.names.popitem()

		while self.inputs:
			self.inputs.pop()

		while self.outputs:
			self.outputs.pop()

		# exit application
		sys.exit()

def main():
	server = Server()
	running = 1
	while running:
		server.run()

if __name__ == "__main__":
	main()

