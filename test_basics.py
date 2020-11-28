import unittest
from flaskapp import app
from redis import Redis

class CounterTest(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	# actual tests
	def test_welcome_page(self):
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)

	# another test for the visit counter
	def rest_redis_connection(self)
		redis = Redis(host = "redis-server",db=0)
		self.app.get('/visit')
		self.app.get('/visit')
		self.app.get('/visit')
		self.app.get('/visit')
		self.app.get('/visit')
		self.assertEqual(int(redis.get("counter")),5)
