# iOS: Encoding / Decoding



### Method 1: `NSCoding`

#### Overview (from Apple)

The `NSCoding` protocol has two methods that a class must implement so that instances of that class can be encoded and decoded. This capability provides the basis for archiving (where objects and other structures are stored on disk) and distribution (where objects are copied to different address spaces).

- `init(coder:)` is for decoding, the initializer instructs the object to initialize itself from data in the coder provided. This replaces any other initialization method.
- `encode(with:)` is for encoding, the method instructs the object to encode its instance variables to the coder provided. An object can receive this method any number of times.

#### Example

```swift
class User: NSObject, NSCoding {
    var name: String?
    var phoneNumber: Int?

    required init?(coder aDecoder: NSCoder) {
        // Returns an object initialized from data in a provided unarchiver.
        self.name = aDecoder.decodeObject(forKey: "name") as? String
        self.phoneNumber = aDecoder.decodeObject(forKey: "phoneNumber") as? Int
    }

    func encode(with aCoder: NSCoder) {
        // Encodes the given object using provided archiver.
        aCoder.encode(self.name, forKey: "name")
        aCoder.encode(self.phoneNumber, forKey: "phoneNumber")
    }
}
```

#### Drawbacks

- Encoder and decoder methods must have code for each property - lots of redundant code
- Only supports classes, so you have to write a class even if your requirements do not need the same.



### Method 2: `Codable`

#### Encodable / Decodable / Codable

- `Encodable`: for encoding, contains `encode(to:)`
- `Decodable`: for decoding, contains `init(from:)`
- `Codable`: for both encoding/decoding, it's basically `Encodable` and `Decodable` combined, typealiased
  - Built-in `Codable` types: `String`, `Int`, `Double`, `Data`, `URL`
  - `Array`, `Dictionary`, `Optional` are `Codable` if they contain `Codable` types
  - A type is codable if its properties are using types that are already `Codable`, and thus you do not need to implement `init(from:)` and/or `encode(to:)` methods

#### JSONEncoder / JSONDecoder

These are objects used to encode/decode instances of data types as JSON objects.

#### CodingKey

`CodingKey` is a protocol you can use to define special nested enums within codable types, to help with the encoding/decoding process. The cases within the enums serve as the authoritative list of properties that must be included when instances of a codable type are encoded or decoded.

Other things to note:

- *CodingKeys* is the conventional name for the enum
- The names of the enum cases should exactly match the property names of the codable type
- Omit the properties from *CodingKeys* if you want to omit them from encoding/decoding process
- *Raw Value* is the thing you need if the property names of codable type doesn't match the keys in the serialized data. Provide alternative string keys used in the serialized data.

#### Example

```swift
/* JSON Structure
{
    brands = {
        brand = ({
                id = apple;
                name = Apple;
            }, {
                id = canon;
                name = Canon;
            }, {
                id = nikon;
                name = Nikon;
			},
		);
	};
}
*/

struct CameraBrands: Codable {
    let brands: [CameraBrand]

    enum BrandsKey: CodingKey {
        case brands
    }

    enum BrandKey: CodingKey {
        case brand
    }

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: BrandsKey.self)
        let brandDictionary = try container.nestedContainer(
        	keyedBy: BrandKey.self, 
        	forKey: .brands
        )
        var brandsArray = try brandDictionary.nestedUnkeyedContainer(forKey: .brand)

        var brands: [CameraBrand] = []
        while !brandsArray.isAtEnd {
            brands.append(try brandsArray.decode(CameraBrand.self))
        }
        self.brands = brands
    }
}

struct CameraBrand: Codable {
    let id: String
    let name: String

    enum CodingKeys: String, CodingKey {
        case id
        case name
    }
}

let decoder = JSONDecoder()
let decodedCameraBrands = try decoder.decode(CameraBrands.self, from: data)

```



## Reference

- [Everything about codable in Swift 4](https://hackernoon.com/everything-about-codable-in-swift-4-97d0e18a2999)
- [Essentials of Codable Protocol in Swift 4](https://medium.com/@multidots/essentials-of-codable-protocol-in-swift-4-c795a645c3e1)