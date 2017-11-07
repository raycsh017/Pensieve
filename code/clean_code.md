# Clean Code

## Chapter 2: Meaningful Names
### Use Intention-Revealing Names
Choosing good names takes time but saves more than it takes. So take time to name things. The name of a variable, function, or class, should tell you why it exists, what it does, and how it is used. If a name requires a comment, then maybe the name does not reveal its intent. 

```
// Bad
int d; // elapsed time in days

// Good
int elapsedTimeInDays;
```

### Avoid Disinformation
Avoid leaving false clues that obscure the meaning of code. For example, `hp`, `aix`, and `eco` are poor variable names because they are the names of Unix platforms or variants.

Do not refer to a grouping of things as a `List` unless it's actually a `List` (in programmatical sense). For example, `accounts` is preferable over `accountList`.

Beware of using names which vary in small ways. For example, how long does it take you to spot the subtle difference between `XYZControllerforEfficientHandlingOfStrings` and `XYZControllerforEfficientStorageOfStrings`.

Spelling similar concepts similarly is *information*. Using inconsistent spellings is *disinformation*. For example, an object that has a name prefixed with the module it is in, may be an information, because all of the objects used in that module are grouped together with the same prefix in the names.

### Make Meaningful Distinctions
Avoid noninformative naming such as naming variables using numbers (ex. `a1`, `a2`, ..., `aN`). They provide no clue to the author's intention.

Noise words are another meaningless distinction. For example, if you have a `Product` class and another class named `ProductInfo` or `ProductData`, adding `Info` or `Data` to `Product` doesn't really make the names distinct. Therefore the noise words like `Info` or `Data` can be dismissed. 

Noise words are redundant. For example, the word `variable` should never appear in a variable name, because it doesn't provide useful information (we know from declaration that the variable is indeed a variable).

Distinguish names in such a way that the reader knows what the differences offer.

### Use Pronounceable Names
Make your names pronounceable. For example, using `genymdhms` as a variable name for a variable that represents generation date, year, month, day, hour, minute, second isn't very illuminating. Instead, use something like `generationTimestamp`, that is easy to understand.

### Use Searchable Names
Single-letter names and numeric constants have a particular problem in that they are not easy to locate across a body of text. For example, `MAX_CLASSES_PER_STUDENT` is better than the number `7` or letter `e`, because searching for either `7` or `e` could get you a number of matching variables/values.

### Avoid Encodings
#### Hungarian Notation
Hungarian Notation is a variable naming convention that includes information about the variable in its name. An example would be `strFirstName`, where `str` denotes that the variable is of type `String`. It makes it hard to change the name or type of a variable, function, or class, makes it harder to read the code, and creates the possibility that the encoding will mislead the reader.

#### Member Prefixes
You shouldn't need to prefix member variables with `m_` anymore. Your classes and functions should be small enough that you don't need them.

### Mental Mapping
Readers shouldn't have to mentally translate your name into other names they already know.

### Class Names
Classes and objects should have noun or noun phrase names like `Customer`, `WikiPage`, or `AddressParser`. Avoid words like `Manager`, `Processor`, or `Data`.

### Method Names
Methods should have verb or verb phrases like `postPayment` or `deletePage`. Accessors, mutators, and predicates should be named for their value and prefixed with `get`, `set`, and `is`. 

When constructors are overloaded, use static factory methods with names that describe the arguments. For example,
```
Complex fulcrumPoint = Complex.FromRealNumber(23.0)
```
is preferred over
```
Complex fulcrumPoint = new Complex(23.0)
```