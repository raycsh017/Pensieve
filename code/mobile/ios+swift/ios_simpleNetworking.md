# iOS: Simple Networking

### A. (Optional) Allow arbitrary loads 

1. Open your project's `plist` file
2. Add following keys and values to `Information Property List`
   - `App Transport Security Settings` Dictionary with key `Allow Arbitrary Loads` and value `YES`



### B. Make Network Request

1. Form url for making an API request:

```swift
// Define url with query params
let baseUrl = "https://generateapi.com/services/rest"

// Query Params
let apiKeyParamKey = "api_key"
let apiKey = "exampleApiKey"
let apiKeyQueryItem = URLQueryItem(name: apiKeyParamKey, value: apiKey)

let methodParamKey = "method"
let method = "getData"
let methodQueryItem = URLQueryItem(name: methodParamKey, value: method)

let formatParamKey = "format"
let format = "json"
let formatQueryItem = URLQueryItem(name: formatParamKey, value: format)

var urlComponents = URLComponents(string: baseUrl)
urlComponents?.queryItems = [
    methodQueryItem,
    apiKeyQueryItem,
    formatQueryItem
]
```

2. Make actual API request, receive response, and deserialize data into JSON object:

```swift
guard let url = urlComponents?.url else { return }

URLSession.shared.dataTask(with: url) { (data, response, error) in
    guard let data = data, error == nil else {
        return
    }

    do {
        let json = try JSONSerialization.jsonObject(with: data, options: [])
        print(json)
    } catch let parseError {
        print(parseError)
    }
}.resume()
```



### C. Parse JSON

Example:

```swift
guard let jsonArray = json as? [[String: Any]] else { return }

let title = jsonArray[0]["title] as? String ?? ""
```

