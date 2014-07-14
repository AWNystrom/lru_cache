import unittest
from lru_cache import LruCache

def plan_b_func(x):
	return x**2
	
class TestLruCache(unittest.TestCase):

	def setUp(self):
		pass
		
	def test_instantiation(self):
		c = LruCache(0, lambda n: n**2)
		self.assertIsInstance(c, LruCache)
		
		with self.assertRaises(ValueError):
			LruCache(-1, lambda n: n**2)
		
		with self.assertRaises(TypeError):
			LruCache(2, 0)
		
	def test_unique_adds(self):
		#Add a bunch of the same item to the cache.
		for size in xrange(0, 5):
			c = LruCache(size, plan_b_func)
			for enum, i in enumerate([4 for j in xrange(10)]):
				val, found_in_cache = c.lookup(i)
				self.assertTrue(found_in_cache or enum is 0 or size is 0)
				self.assertEqual(val, plan_b_func(i))
				self.assertEqual(len(c.ht), len(c.ll))
				self.assertEqual(min(size, 1), len(c.ht))
				self.assertEqual(min(size, 1), c.size())
	
	def test_non_unique_adds(self):
		#Add a bunch of the same item to the cache.
		for size in xrange(0, 5):
			c = LruCache(size, plan_b_func)
			for enum, i in enumerate(xrange(10)):
				val, found_in_cache = c.lookup(i)
				self.assertFalse(found_in_cache)
				self.assertEqual(val, plan_b_func(i))
				self.assertEqual(len(c.ht), len(c.ll))
				self.assertEqual(min(size, enum+1), len(c.ht))
				self.assertEqual(min(size, enum+1), c.size())
	
	def test_update(self):
		squared = lambda n: n**2
		c = LruCache(5, squared)
		
		for i in xrange(10):
			val, found = c.lookup(i)
		
		val, found = c.lookup(7)
		self.assertEqual(val, squared(7))
		self.assertTrue(found)
		
		c.update(7, 0)
		val, found = c.lookup(7)
		self.assertEqual(val, 0)
		self.assertTrue(found)
	
	def test_overfill(self):
		squared = lambda n: n**2
		c = LruCache(5, squared)
		
		for i in xrange(10):
			val, found = c.lookup(i)
		
		val, found = c.lookup(3)
		self.assertEqual(val, squared(3))
		self.assertFalse(found)
		
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestLruCache)
	unittest.TextTestRunner(verbosity=2).run(suite)