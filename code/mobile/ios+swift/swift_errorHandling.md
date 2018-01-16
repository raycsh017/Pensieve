# Error Handling

## Representing and Throwing Errors
## Representing Errors
In Swift, errors are represented by values of types that conform to the `Error` protocol. This empty protocol indicated that a type can be used for error handling.

An example:
```
enum DatabaseOperationError: Error {
	case failedToRead
	case failedToWrite
	case failedToInitialize
}
```

### Throwing Errors
Throwing an error lets you indicate that something unexpected happened and the normal flow of execution can't continue. When throwing an error, use `throw` with an error conforming to `Error`.

For example:
`throw RealmError.failedToRead`

### Handling Errors
When an error is thrown, some surrounding piece of code must handle the error. And this can be done in four ways:
1. propagate the error from a function to the code that calls that function,
2. handle the error using a `do-catch` statement,
3. handle the error as an optional value, or
4. assert that the error will not occur.

To identify these places in code where you need to handle errors, mark them with `try` keyword. 

## Reference
[Apple's Swift official documentation on Error Handling](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/ErrorHandling.html)