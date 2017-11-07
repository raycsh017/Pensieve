# Functional Programming

## Overview
Functional programming: a programming paradigm that emphasizes calculations via mathematical-style functions, immutability and expressiveness, and minimizes the use of variables and state.

**Pros:**
- Because there's minimal shared state, things are easier to test
- Makes concurrency and parallel processing easier to work with

## Imperative vs Functional

### Imperative Programming
```swift
var evenNumbers: [Int] = []
for i in 1...10 {
	if i % 2 == 0 {
		evenNumbers.append(i)
	}
}
// This produces: [2, 4, 6, 8, 10]
```

Notice that:
There is some tight coupling, where the desired action of adding the number to the array is inside the condition. There's no good way to reuse code without resorting to copy-and-paste.

### Functional Programming

#### Method 1
```
func isEven(number: Int) -> Bool {
  return number % 2 == 0
}
var evenNumbers = Array(1...10).filter(isEven)
print(evenNumbers)
```

#### Method 2
```
var evenNumbers = Array(1...10).filter { (number) in number % 2 == 0 }
print(evenNumbers)
```

#### Method 3
```
var evenNumbers = Array(1...10).filter { $0 % 2 == 0 }
print(evenNumbers)
```

## Common Methods

### Map
```
func map<U>(transform: (T) -> U) -> Array<U>
```

Returns an array containing the results of mapping the given closure over the sequence’s elements.

> Note that `map` doesn't change elements in-place.

For example:
```
var numbers = Array(1...10)
numbers = numbers.map { (i) -> Int in
	return i + 1
}
print(numbers) // 2...11
```

The above code can be simplified further:
```
var numbers = Array(1...10).map({ i -> Int in i + 1 })
print(numbers) // 2...11
```

even further:
```
var numbers = Array(1...10).map({ i in i + 1 })
print(numbers) // 2...11
```

still:
```
var numbers = Array(1...10).map({ $0 + 1 })
print(numbers) // 2...11
```

finally:
```
var numbers = Array(1...10).map{ $0 + 1 }
print(numbers) // 2...11
```

### Filter
```
func filter(includeElement: (T) -> Bool) -> Array<T>
```

Returns an array containing, in order, the elements of the sequence that satisfy the given predicate. The elements that return `true` to the given predicate are included in the result array.

```
let oddNumbers = Array(1...10).filter({ (i) -> Bool in
	return i % 2 != 0
})
print(oddNumbers) // [1,3,5,7,9]
```

### Reduce
```
func reduce<U>(initial: U, combine: (U, T) -> U) -> U
```

Returns the result of combining the elements of the sequence using the given closure.

This is what's happening under the hood:
1. The given closure is called with the initial result and the first element of the given collection. Returns the result of the computation.
2. The closure is called again repeatedly with the previous call’s return value and each element of the sequence.
3. When the sequence is exhausted, the last value returned from the closure is returned to the caller.

```
let number = Array(1...10).reduce(0, { (result, i) -> Int in
	return result + i
})
print(number) // 55
```

## Reference
- [Raywenderlich: Swift Functional Programming Tutorial](https://www.raywenderlich.com/82599/swift-functional-programming-tutorial)