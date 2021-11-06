# requires pip install torpy or torpy[requests]

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