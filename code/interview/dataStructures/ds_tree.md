# Tree

## Characteristics
- Each tree has a root node
- Each node has zero or more child nodes
- Nodes may or may not be in a particular order
- Nodes could have any data types as values
- Nodes may or may not have links back to parent nodes
- Trees cannot contain cycles


## Simple Class Definition for a Node
```cpp
class Node{
	string name;
	Node children[];
}
```


## Types of Trees
### Binary Tree
A binary tree is a tree in which each node has up to two children

### Binary Search Tree
A binary tree in which every node fits a specific ordering property: all left descendants <= n < all right descendants

**!!!** Do not naively assume a binary tree is a binary search tree!

### Balanced Tree
A tree in which every node keeps the difference in the heights of its subtrees to be at most 1. Refer to `AVL tree` for an example.

### Complete Binary Tree
A binary tree in which every level of the tree is fully filled, except for perhaps the last level. The last level should be filled left to right.

### Full Binary Tree
A binary tree in which every node has either zero or two children.

### Perfect Binary Tree
A binary tree that is both full and complete


## Binary Tree Traversal
Note that these are a form of DFS!

### In-Order Traversal
Visit in order of **left - current - right** nodes

```
// pseudocode
void inOrderTraversal(Node node){
	if(node != null){
		inOrderTraversal(node->left);
		visit(node);
		inOrderTraversal(node->right);
	}
}
```

### Pre-Order Traversal
Visit in order of **current - left - right** nodes

```
// pseudocode
void preOrderTraversal(Node node){
	if(node != null){
		visit(node);
		preOrderTraversal(node->left);
		preOrderTraversal(node->right);
	}
}
```

### Post-Order Traversal
Visit in order of **left - right - current** nodes

```
// pseudocode
void postOrderTraversal(Node node){
	if(node != null){
		postOrderTraversal(node->left);
		postOrderTraversal(node->right);
		visit(node);
	}
}
```

**!!!** For Pre-Order Traversal and Post-Order Traversal, the order we visit children nodes can change


## Binary Heaps
### Min-Heap (and Max-Heap)
A **complete** binary tree where **each node is smaller than its children**. The root therefore, is the minimum element in the tree. 

Max-Heap is just the opposite, with the maximum element at the top.

#### Insertion (O(log n))
1. Insert at the end of the tree (bottom-most, right-most spot in the tree)
2. "Fix-up" by swapping the new element with its parent, until we find an appropriate spot for the element.

#### Extraction (O(log n))
1. Pop out the element at the top. 
2. Swap the root element with the last element in the heap.
3. Bubble down this element, swapping it with one of the children until the heap property is restored. Make sure to swap with the right child (choose the child with a smaller value if it's a min-heap, for example)


## Tries
A trie is a variant of n-ary tree in which characters are stored at each node. Each path down the tree may represent a word.

`*` nodes are often used to indicate complete words.

A trie is often used to store the entire English language for quick prefix lookups. While a hash table can quickly look up whether a string is a valid word, it cannot tell us if a string is a prefix of any valid words. 

O(n) time, where n is the length of a string


## Reference
- Cracking the Coding Interview by Gayle LaakMann McDowell
