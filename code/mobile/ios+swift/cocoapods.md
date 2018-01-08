# CocoaPods
## Using CocoaPods
### Command
#### `pod install`
To install new pods in your project. If you already have a `Podfile` and ran `pod install` before, it would be just adding/removing pods to a project already using CocoaPods.

#### `pod update {pod name}`
To update pods to a newer version

### Podfile
A very simple Podfile would look something like: 
```
target 'MyApp' do
  use_frameworks!
  pod 'Alamofire', '~> 3.0'
end
```

To add a pod/project: 
`pod '{pod name}'`

To specify version of a pod/project:
`pod '{pod name}', '{operator} {version number}'`

Some of the logic operators available for specifying the pod/project version are (0.1 is just a sample version):
- `> 0.1`: Any version higher than 0.1
- `>= 0.1`: Version number and any higher version
- `< 0.1`: Any version lower than 0.1
- `<= 0.1`: Version 0.1 and any lower version
- `~> 0.1.2`: Version 0.1.2 and the versions up to 0.2, not including 0.2 and higher
- `~> 0.1`: Version 0.1 and the versions up to 1.0, not including 1.0 and higher
- `~> 0`: Version 0 and higher, this is basically the same as not having it





