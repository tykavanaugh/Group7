# requires pip install torpy

# Easy way to do requests:
#  Get a new session every time you open the app,
#  get a new IP for the whole session. Once you
#  close the app and restart, new IP again.

from torpy.http.requests import TorRequests

with TorRequests() as tor_requests:
	print("build circuit")
	with tor_requests.get_session() as sess:
		print(sess.get("http://httpbin.org/ip").json()) # new session, new IP
		print(sess.get("http://httpbin.org/ip").json())
	print("renew circuit")
	with tor_requests.get_session() as sess:
		print(sess.get("http://httpbin.org/ip").json())
		print(sess.get("http://httpbin.org/ip").json())

# Harder/more customizable way to do requests below.

# from torpy import TorClient

# hostname = 'ifconfig.me'  # It's possible use onion hostname here as well
# with TorClient() as tor:
#     # Choose random guard node and create 3-hops circuit
#     with tor.create_circuit(3) as circuit:
#         print('initialized circuit')
#         # Create tor stream to host
#         with circuit.create_stream((hostname, 80)) as stream:
#             # Now we can communicate with host
#             stream.send(b'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % hostname.encode())
#             recv = stream.recv(1024)
#             print(recv)