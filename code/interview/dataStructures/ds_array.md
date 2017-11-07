# Array
## Characteristics
- Wastes memory if size is too large
- Requires reallocation if too small

## Common Operation Time Complexity
| Operation | Time Complexity |
|:--|:--|
| Random Access | O(1) |
| Sequential Access | O(1) |
| Search | O(n) |
| Insertion | O(n) |
| Append | O(n) |
| Deletion | O(n) |

## Declaration
In C++:
```cpp
char s1[15] = "Hello ";	
char s2[] = "World";
char *x = "Hello ";
```

- Arrays allocate space for the number of elements specified + 1, where the last one is for the null character to mark the end of an array.
- Unless declared with dynamic memory allocation using new, arrays allocate memory on the stack (not heap).

## 2D Arrays
### 1D to 2D
- column = index % num_cols
- row = index / num_cols

### 2D to 1D
index = row * num_cols + col

## A Word of Caution
- Avoid fixed-length buffers for variable-length input, as they are often the source of security breaches. 