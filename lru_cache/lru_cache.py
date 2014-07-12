"""
c = LRUCache(5000, hard_work_func)

c['andrew'] += 5
"""

from doubly_linked_list import DoublyLinkedList

class LRUCache:
	def __init__(self, max_size, plan_b_func):
	
		if max_size < 0:
			raise ValueError("max_size must be positive.")
		if not callable(plan_b_func):
			raise TypeError("plan_b_func must be callable.")
			
		self.max_size = max_size
		self.ht = {}
		self.ll = DoublyLinkedList()
		self.plan_b_func = plan_b_func
		
	def lookup(self, query):
		"If the query is in the cache, move it to the front of the linked list"
		"then return it. If it's not in the cache, remove the last query in the"
		"linked list, queries the plan_b_func for the result, adds it to the"
		"cache, and returns it. This should be a decorator."
		"data is the count, query is the token"
		
		found_in_cache = None
		if query not in self.ht:
			found_in_cache = False
			result = self.plan_b_func(query)
			if len(self.ht) == self.max_size and self.max_size is not 0:
				if self.ll.tail is not None:
					del self.ht[self.ll.tail.query]
					self.ll.removeTail()
			if self.max_size != 0:
				self.ll.addToHead(result)
				self.ll.head.query = query
				self.ht[query] = self.ll.head
		else:
			#The query was in the cache. Move it to the front of 
			#the linked list.
			found_in_cache = True
			node = self.ht[query]
			result = node.data
		
		return result, found_in_cache
		
	def update(self, query, val):
		"Update the value stored in the cache pointed to by query. If query "
		"isn't cached, nothing happens."
		
		if query not in self.ht:
			return
		
		node = self.ht[query]
		node.data = val
		
	def size(self):
		return len(self.ht)
		
if __name__ == '__main__':
	test_cache()