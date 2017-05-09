

import socket
import Utils as utils

class Netconx(object):
	"""this is just have internet connection and any other nework jobs"""


	def __init__(self):
		pass

	def checkNet_Exists(self):
		try:
			host=socket.gethostbyname(utils.REMOTE_SERVER__FOR__CONNECTION_CHECKING)			
			s=socket.create_connection((host,80),2)
			return True
		except:
			pass
		return False
		


print (Netconx().checkNet_Exists())