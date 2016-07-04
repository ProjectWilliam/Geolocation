#!/usr/bin/python
# Author: William Guerrero
# Date: 15 March 2015
#
# Geolocation service top level program. Run it like this:
#   ./geolocation.py <host> <port>
# or like this:
#   python geolocation.py <host> <port>
# where <host> is the DNS name of the host that will be the central coordinator,
# and <port> is the port on which the central coordinator will serve HTTP
# requests from users.

import sys, os                  # for sys.argv
from socket import * 
from urlparse import urlparse
from time import gmtime, strftime

global pingers = []


def headers():
	# headers for websever
	t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	return("HTTP/1.1 200 OK" + "\r\n" + "Date: " + t + "\r\n") 
          

# Get the central_host name and port number from the command line
central_host = sys.argv[1]
central_port = int(sys.argv[2])


def fetch_url(url):
    # TODO: Write code to fetch the contents of the url. Split the URL into pieces,
    # issue an HTTP GET, receive the response, strip off the headers. The body
    # should be returned as the result of the function. If any errors are encountered,
    # raise an exception or simply exit the program with an error message.

	
	connectionSocket = socket(AF_INET, SOCK_STREAM) # socket initialization
	
	parse_object = urlparse(url)

	hostname = parse_object.netloc

	path = parse_object.path

	connectionSocket.connect(("",central_port))
	
	message = 'GET' + ' ' + path + ' ' + 'HTTP/1.1' + '\r\n' + "Host: " + hostname + '\r\n\r\n' 

	print(message)
	
	connectionSocket.sendall(message)

	httpresponse = connectionSocket.recv(1024)

	headers, payload = httpresponse.split('\r\n\r\n')

	print(payload)

	return payload
	

	
  
# Figure out our own host name. 
dns_name = fetch_url('http://169.254.169.254/latest/meta-data/public-hostname')

# Figure out our own ec2 region
region = fetch_url('http://169.254.169.254/latest/meta-data/placement/availability-zone/')

test = fetch_url('http://holycross.edu/index.html')

if dns_name == central_host:
    # If we are the central coordinator host...
    # then call some function that implements the front end and central coordinator.
    # This code assumes there is a file named central.py containing a function 
    # named run_central_coordinator(). Alternatively, you can delete these two lines and
    # put your central coordinator code right here.
	def central_coordinator():
		serverSocket = socket(AF_INET,SOCK_STREAM) # socket initialization
		serverSocket.bind(("",int(serverPort))) # socket bind
		serverSocket.listen(1) # one queued connection
		connectionSocket, addr = serverSocket.accept() # accept connection
		message = connectionSocket.recv(1024)
		
		if message.startswith('Hello'):
	
			#put socket on a list
			
			pingers.append(connectionSocket)
			
			print('test')
	
			#dont close the connection
	
			#dont reply
	
		elif message.startswith('GET'):
	
			if path == '/' or '/index.html':
	
				#send form request
	
				filepath = '~/networks/project2/form.html'

			if(os,path.isfile(filepath)):
				text = open(filepath,'r')
				text_string = text.read()

				ContentNumbers = len(text_string)

			if (path.endswith('.txt')):
				ctype = 'text/plain'
			if (path.endswith('.html')):
				ctype = 'text/html'
			if (path.endswith('.jpg')):
				ctype = 'image/jpg'
			if (path.endswith('.png')):
				ctype = 'image/png'
			if (path.endswith('.css')):
				ctype = 'text/css'
			if (path.endswith('.js')):
				ctype = 'application/javascript'
		
			message = headers() + "Content-Type: " + ctype + "\r\n" + "Content-Length: " + str(ContentNumbers)+ "\r\n\r\n" + text_string
			print(message)
			connectionSocket.sendall(message)

		elif path == ('/geolocate'):

			#extract the target URL

			targetURL = url.split('=')

			#send this URL to every pinger using list
			
			for x in pingers

				x.sendall(targetURL)

			#receive a response from every pinger
			
			li = []
			
			for x in len(pingers)

				li.append((RTT,region))

				

			#summarize result to produce a single result 

			
			#send this result back to the browser in a proper HTTP response
			
			connectionSocket.sendall(li)
	

else:
    # Otherwise, we are one of the pinger server hosts...
    # then call some function that implements the pinger server.
    # This code assumes there is a file named pinger.py containing a function 
    # named run_pinger_server(). Alternatively, you can delete these two lines and
    # put your pinger server code right here.
	def pinger_server():
		
		
