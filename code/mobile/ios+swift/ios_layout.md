# iOS: Layout

## The Layout Process
Auto Layout introduces two additional steps to the process before views can be displayed: 
1. Updating constraints
2. Laying out views

Each step is dependent on the one before; display depends on layout, and layout depends on updating constraints.

### Updating Constraints
This happens bottom-up, **from subview to superview** and prepares the information needed for the layout pass to actually set the views’ frame. You can trigger this pass by calling `setNeedsUpdateConstraints`. Any changes you make to the system of constraints itself will automatically trigger this. However, it is useful to notify Auto Layout about changes in custom views that could affect the layout. Speaking of custom views, you can override `updateConstraints` to add the local constraints needed for your view in this phase.

### Laying out Views
This happens top-down, **from superview to subview**. This layout pass actually applies the solution of the constraint system to the views by setting their frames (on OS X) or their center and bounds (on iOS). You can trigger this pass by calling `setNeedsLayout`, which does not actually go ahead and apply the layout immediately, but takes note of your request for later. This way you don’t have to worry about calling it too often, since all the layout requests will be coalesced into one layout pass.

To force the system to update the layout of a view tree immediately, you can call `layoutIfNeeded`/`layoutSubtreeIfNeeded` (on iOS and OS X respectively). This can be helpful if your next steps rely on the views’ frame being up to date. In your custom views you can override `layoutSubviews`/`layout` to gain full control over the layout pass.

### Display
Finally, the display pass renders the views to screen and is independent of whether you’re using Auto Layout or not. It operates top-down and can be triggered by calling `setNeedsDisplay`, which results in a deferred redraw coalescing all those calls. Overriding the familiar `drawRect:` is how you gain full control over this stage of the display process in your custom views.

Since each step depends on the one before it, the display pass will trigger a layout pass if any layout changes are pending. Similarly, the layout pass will trigger updating the constraints if the constraint system has pending changes.

It is notable that these three steps are not a one-way street. Constraint-based layout is an iterative process. The layout pass can make changes to the constraints based on the previous layout solution, which again triggers updating the constraints following another layout pass. This can be leveraged to create advanced layouts of custom views, but you can also get stuck in an infinite loop if every call of your custom implementation of `layoutSubviews` results in another layout pass.



## Enabling Custom Views for Auto Layout

### Intrinsic Content Size

The intrinsic content size is **the size a view prefers to have for a specific content it displays**.

To implement an intrinsic content size in a custom view, you have to do two things: 
1. Override `intrinsicContentSize` to return the appropriate size for the content, and 
2. Call `invalidateIntrinsicContentSize` whenever something changes which affects the intrinsic content size. If the view only has an intrinsic size for one dimension, return `UIViewNoIntrinsicMetric`/`NSViewNoIntrinsicMetric` for the other one.

Note that the intrinsic content size must be independent of the view’s frame. For example, it’s not possible to return an intrinsic content size with a specific aspect ratio based on the frame’s height or width.

### Compression Resistance and Content Hugging
Each view has content compression resistance priorities and content hugging priorities assigned for both dimensions. These properties only take effect for views which define an intrinsic content size, otherwise there is no content size defined that could resist compression or be hugged.

Behind the scenes, the intrinsic content size and these priority values get translated into constraints. For a label with an intrinsic content size of `{ 100, 30 }`, horizontal/vertical compression resistance priority of `750`, and horizontal/vertical content hugging priority of `250`, four constraints will be generated.

```
H:[label(<=100@250)]
H:[label(>=100@750)]
V:[label(<=30@250)]
V:[label(>=30@750)]
```

### Frame vs. Alignment Rect

A little bit of background on alignment rects:

> The constraint-based layout system uses alignment rectangles to align views, rather than their frame. This allows custom views to be aligned based on the location of their content while still having a frame that encompasses any ornamentation they need to draw around their content, such as shadows or reflections.

Auto Layout does not operate on views’ frame, but on their alignment rect. This is a powerful concept that decouples a view's layout alignment edges from its visual appearance.

For example, a button in the form of a custom icon that is smaller than the touch target we want to have would normally be difficult to lay out. We would have to know about the dimensions of the artwork displayed within a larger frame and adjust the button’s frame accordingly, so that the icon lines up with other interface elements. The same happens if we want to draw custom ornamentation around the content, like badges, shadows, and reflections.

Using alignment rects we can easily define the rectangle which should be used for layout. In most cases you can just override the `alignmentRectInsets` method, which lets you return edge insets relative to the frame. If you need more control you can override the methods `alignmentRectForFrame:` and `frameForAlignmentRect:`. This can be useful if you want to calculate the alignment rect based on the current frame value instead of just subtracting fixed insets. But you have to make sure that these two methods are inverses of each other.

### Baseline Alignment

If you need a view to have something like a baseline, this can be done by implementing `viewForBaselineLayout`. The bottom edge of the view you return here will be used as baseline. The default implementation simply returns self, while a custom implementation can return any subview. On OS X, you need to override `baselineOffsetFromBottom` instead.



## Taking Control of Layout

### Local Constraints

When composing a custom view out of several subviews, the place to add local constraints is `updateConstraints`. Make sure to invoke `super.updateConstraints` after you've added whatever constraints you need to lay out the subviews. In this method, you are not allowed to invalidate any constraints, because you are already in the first step of the layout process, updating constraints.

If something changes later on that invalidates one of your constraints, you should remove the constraint immediately and call `setNeedsUpdateConstraints`. In fact, that’s the only case where you should have to trigger a constraint update pass.

### Control Layout of Subviews

If you cannot use layout constraints to achieve the desired layout of your subviews, you can go one step further and override `layoutSubviews` on iOS or `layout` on OS X. This way, you’re hooking into the second step of the layout process, when the constraint system has already been solved and the results are being applied to the view.

Call the super class's implementation of `layoutSubviews`/`layout` in the override if you want to use constraints to lay out subviews, otheriwise, you are opting out of Auto Layout for the view tree within the view. From this point on, you can position subviews manually however you like.

Another interesting use case for this is to create a layout-dependent view tree. After Auto Layout has done its first pass and set the frames on your custom view’s subviews, you can inspect the positioning and sizing of these subviews and make changes to the view hierarchy and/or to the constraints. WWDC session [228 – Best Practices for Mastering Auto Layout](https://developer.apple.com/videos/wwdc/2012/?id=228) has a good example of this, where subviews are removed after the first layout pass if they are getting clipped.

You could also decide to change the constraints after the first layout pass. For example, switch from lining up subviews in one row to two rows, if the views are becoming too narrow.



## Intrinsic Content Size of Multi-Line Text

The intrinsic content size of `UILabel` and `NSTextField` is ambiguous for multi-line text. The height of the text depends on the width of the lines, which is yet to be determined when solving the constraints. In order to solve this problem, both classes have a new property called `preferredMaxLayoutWidth`, which specifies the maximum line width for calculating the intrinsic content size.

Since we usually don’t know this value in advance, we need to take a two-step approach to get this right. First we let Auto Layout do its work, and then we use the resulting frame in the layout pass to update the preferred maximum width and trigger layout again.

```swift
override func layoutSubviews() {
    super.layoutSubviews()
    label.preferredMaxLayoutWidth = label.frame.size.width
    super.layoutSubviews()
}
```

The first `layoutSubviews` is necessary for the label to get its frame set, while the second call is necessary to update the layout after the change. If we omit the second call we get an error on making changes in the layout pass which require updating the constraints, but not trigerring the layout again.



This could be done in a label subclass itself,

```swift
class Label: UILabel {
    override func layoutSubviews() {
        self.preferredMaxLayoutWidth = self.frame.size.width
        super.layoutSubviews()
    }
}
```



Or in the view controller level, overriding `viewDidLayoutSubviews`

```swift
override func viewDidLayoutSubviews() {
    super.viewDidLayoutSubviews()
    label.preferredMaxLayoutWidth = label.frame.size.width
    self.view.layoutIfNeeded()
}
```



Lastly, make sure that you don’t have an explicit height constraint on the label that has a higher priority than the label’s content compression resistance priority. Otherwise it will trump the calculated height of the content.



## Animation

There are two fundamentally different strategies when it comes to animations:

1. Animating the constraints themselves
2. Changing the constraints to recalculate the frames and use Core Animation to interpolate between the old and the new position

These are the characteristics of the first approach: 

- Results in a layout that conforms to the constraint system at all times

- Really only a feasible strategy on OS X, and it is limited in what you can animate, since only a constraint's constant can be changed after creating it. On iOS you would have to drive the animation manually, whereas on OS X you can use an animator proxy on the constraint’s constant.

- Slow

And these are for the second:

- You can add constraints, remove constraints, and even use temporary animation constraints. 
- When using Core Animation + Auto Layout, You don't set the views' target frames manually, but instead you modify the constraints and trigger a layout pass to set the frames for you (`layoutIfNeeded`)
- Remember to not touch the views' frame yourself. Once a view is laid out by Auto Layout, you've transferred the responsibility to set its frame to the layout system. 
- Transforms don't always play nice with Auto Layout if they change the view's frame.



## Tricks

- [Applying Different Constraints for Different Devices](http://stackoverflow.com/questions/29179537/set-autolayout-constraints-relative-to-device-size)



#### Reference

[Advanced Auto Layout Toolbox](https://www.objc.io/issues/3-views/advanced-auto-layout-toolbox/)

[More on alignment rects 1](https://useyourloaf.com/blog/auto-layout-and-alignment-rectangles/)

[More on alignment rects 2](https://www.swiftlemma.com/2017/08/alignment-rects-in-auto-layout-views/)