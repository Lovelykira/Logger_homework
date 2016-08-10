import logging 
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

class SpaceHandler(logging.Handler):
	def __init__(self, src, *args, **kwargs):
		self.src = src
		super().__init__(*args, **kwargs)

	def emit(self, record):
		resp = requests.post('http://127.0.0.1:8000/accounts/login/', data=dict(username='kira', password='rollwithit'))

		cookies = dict(sessionid=resp.cookies['sessionid'])

		response_two = requests.post('http://127.0.0.1:8000/', cookies=cookies, data={"message": record.msg, "name":record.name, "levelname":record.levelname})


		#ans = requests.post(self.src, data={"message": record.msg})
		#requests.post(self.src, auth=HTTPDigestAuth('kira', 'rollwithit'), data={"message": record.msg})
		#with requests.Session() as s:
		#	s.auth = ('kira', 'rollwithit')
		#	headers = {}
		#	headers['content-type']='text/html; charset=utf-8'
		#	ans = s.post(self.src, data={"message": record.msg}, verify=False, headers=headers)
		#print(ans)



logger = logging.getLogger('main')
logger.setLevel("DEBUG")

space_handler = SpaceHandler('http://127.0.0.1:8000')
space_handler.setLevel("DEBUG")
formatter = logging.Formatter()
space_handler.setFormatter(formatter)
logger.addHandler(space_handler)

logger.info('podvezli')
