# Python: Class
## Characteristics
- All objects in Python are implemented with references

## Sample
```python
class Node:
	# Object initializer to set attributes
	def __init__(self):
		self.val = 0
		self.right = None
		self.left = None

node = Node()
node.val = 0
node.left = Node()
```

## `None`
Python equivalent of `NULL` is `None`. However, unlike `NULL` in C, `None` is not a "pointer to nowhere". It is actually a singleton instance of class `NoneType`.
