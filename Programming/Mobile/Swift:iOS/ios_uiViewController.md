# iOS: UIViewController

## Overview
Main responsibilities of a view controller:
- Updating the contents of the views, usually in response to changes to the underlying data.
- Responding to user interactions with views.
- Resizing views and managing the layout of the overall interface.

## View Management
### Loading views for the first time
View controllers load their views lazily. Accessing the `view` property for the first time loads or creates the view controller’s views. There are several ways to specify the views for a view controller:

**Using Storyboard**
With a storyboard, you specify the views and their connections to the view controller. You also specify the relationships and segues between your view controllers, which makes it easier to see and modify your app's behavior.

To load a view controller from a storyboard (using code), call the `instantiateViewController(withIdentifier:)` method of the appropriate `UIStoryboard` object. The storyboard object creates the view controller and returns it to your code.

**Using Nib file**
Specify the views for a view controller using a Nib file. A nib file lets you specify the views of a single view controller but does not let you define segues or relationships between view controllers. The nib file also stores only minimal information about the view controller itself.

To initialize a view controller object using a nib file, create your view controller class programmatically and initialize it using the `init(nibName:bundle:)` method. When its views are requested, the view controller loads them from the nib file.

**Using `loadView()`**
Specify the views for a view controller using the `loadView()` method. In that method, create your view hierarchy programmatically and assign the root view of that hierarchy to the view controller’s `view` property.

### View-Related Notifications
When the visibility of its views changes, a view controller automatically calls its own methods so that subclasses can respond to the change.

`viewWillAppear(_:)`
- Notifies the view controller that its view is about to be added to a view hierarchy.
- Called before any animations are configured for showing the view.
- Override this method to perform custom tasks associated with displaying the view.

`viewDidAppear(_:)`
- Notifies the view controller that its view was added to a view hierarchy.
- Override this method to perform additional tasks associated with presenting the view.

`viewWillDisappear(_:)`
- Notifies the view controller that its view is about to be removed from a view hierarchy.
- Called before any animations are configured.
- Override this method to save changes or other state information.

`viewDidDisappear(_:)`
- Notifies the view controller that its view was removed from a view hierarchy.
- Override this method to perform additional tasks associated with dismissing or hiding the view.

`viewDidLoad()`
- Called after the controller's view is loaded into memory.
- You usually override this method to perform additional initialization on views that were loaded from nib files.

`loadView()`
- Loads or creates a view and assigns it to the `view` property.
- Called when the view controller's `view` property is requested but is currently `nil`.
- Override this method to create your views manually. If so, assign the root view of your view hierarchy to the `view` property. Be careful not to call `super`. If you want to do any additional view initializations, use `viewDidLoad` instead.

#### View Notification Order
After calling `UIViewController()` (unless specified, the notifications are from the new view controller we are moving into):
1. `init()`?
2. `loadView`
3. `viewDidLoad`
4. `viewWillDisappear` - prev VC
5. `viewWillAppear`
6. `updateViewConstraints` - prev VC
7. `updateViewConstraints` 
8. `viewWillLayoutSubviews`
9. `viewDidLayoutSubviews` 
10. `viewWillLayoutSubviews` - prev VC
11. `viewDidLayoutSubviews` - prev VC
12. `viewWillLayoutSubviews`
13. `viewDidLayoutSubviews`
14. `viewDidAppear` 
15. `viewDidDisappear` - prev VC
16. Completion block of `present` called from the previous view controller