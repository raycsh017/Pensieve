# Realm with Swift
## Basics
A `Realm` is an instance of Realm Mobile Database container. Realms can be *local* or *synchronized*.

A synchronized Realm uses the Realm Object Server to transparently synchronize its contents with other devices. Synchronization requires authorization separately across different devices.

## Models
Realm data models are defined as regular Swift classes with regular properties. To create one, simply subclass `Object` or an existing Realm model class. Use them like you would any other object, on the thread which it was created.

For example:
```
class Dog: Object {
    @objc dynamic var name = ""
    @objc dynamic var owner: Person? // Properties can be optional
}

class Person: Object {
    @objc dynamic var name = ""
    @objc dynamic var birthdate = Date(timeIntervalSince1970: 1)
    let dogs = List<Dog>()
}
```

### Supported property types
Supported property types in Realm are: `Bool`, `Int`, `Int8`, `Int16`, `Int32`, `Int64`, `Double`, `Float`, `String`, `Date`, and `Data`.

`String`, `Date`, and `Data` can be optional. `Object` properties *must* be optional. String optional numbers is done using `RealmOptional` (ex. `let age = RealmOptional<Int>()`).

### Primary keys
Override `Object.primaryKey()` to set the model's primary key. Note that once an object with a primary key is added to a Realm, the primary key cannot be changed.

```
class Person: Object {
    @objc dynamic var id = 0
    @objc dynamic var name = ""

    override static func primaryKey() -> String? {
        return "id"
    }
}
```

### Indexing properties
To index a property, override `Object.indexedProperties()`. Indexing is available for string, integer, boolean, and `Date` properties.

## Basic Operations
### Opening Realms
Simply instantiate a new `Realm` object:
```
let realm = try! Realm()
```

### Read
#### Characteristics
- Queries return a `Results` instance, which contains a collection of `Object`s. 
- Once the query has been executed, `Results` is kept up to date with changes made in the Realm, with the query execution performed on a background thread when possible.
- All queries are lazy in Realm. Data is only read when the properties are accessed.

#### Fetching all Object instances of a subclass type
```
let dogs = realm.objects(Dog.self)
```

### Write
#### Characteristics
- All changes to an object(addition, modification, and deletion) must be done within a write transaction.
- When you commit a write transaction to a Realm, all other instances of that Realm will be notified, and be updated automatically.
- Realm write operations are *synchronous* and *blocking*, not asynchronous. Also write operations always refresh automatically on `beginWrite()`, so no race condition is created by overlapping writes. On the other hand, read operations are not blocked by write operations.

#### Adding an Object instance
```
try! realm.write {
    realm.add(myDog)
}
```

#### Updating properties of an Object instance
```
try! realm.write {
    author.name = "Thomas Pynchon"
}
```

#### Removing an Object instance
```
try! realm.write {
    realm.delete(cheeseBook)
}
```

## Tips
### Recommended place to store data
According to [Apple doc on data storage](https://developer.apple.com/icloud/documentation/data-storage/index.html), for data that is user-generated or that cannot otherwise be recreated by your application, should be stored in the `<Application_Home>/Documents` directory.

By default, Realm saves data in a file named `default.realm` in the Documents folder of your app.

### Improving write performance
For large transactions, unless you need to make simultaneous writes from many threads at once, it is preferred to do more larger write transactions over many fine-grained write transactions.

## References
- [Realm Doc: Getting Started](https://realm.io/docs/swift/latest)