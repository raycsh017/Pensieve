# iOS: Layout

## The Layout Process
Auto Layout introduces two additional steps to the process before views can be displayed: 
1. Updating constraints
2. Laying out views

Each step is dependent on the one before; display depends on layout, and layout depends on updating constraints.

### Updating Constraints
This happens bottom-up, **from subview to superview** and prepares the information needed for the layout pass to actually set the views’ frame. You can trigger this pass by calling `setNeedsUpdateConstraints`. Any changes you make to the system of constraints itself will automatically trigger this. However, it is useful to notify Auto Layout about changes in custom views that could affect the layout. Speaking of custom views, you can override `updateConstraints` to add the local constraints needed for your view in this phase.

### Laying out Views
This happens top-down, from superview to subview. This layout pass actually applies the solution of the constraint system to the views by setting their frames (on OS X) or their center and bounds (on iOS). You can trigger this pass by calling `setNeedsLayout`, which does not actually go ahead and apply the layout immediately, but takes note of your request for later. This way you don’t have to worry about calling it too often, since all the layout requests will be coalesced into one layout pass.

To force the system to update the layout of a view tree immediately, you can call `layoutIfNeeded`/`layoutSubtreeIfNeeded` (on iOS and OS X respectively). This can be helpful if your next steps rely on the views’ frame being up to date. In your custom views you can override `layoutSubviews`/`layout` to gain full control over the layout pass.

### Display
Finally, the display pass renders the views to screen and is independent of whether you’re using Auto Layout or not. It operates top-down and can be triggered by calling `setNeedsDisplay`, which results in a deferred redraw coalescing all those calls. Overriding the familiar `drawRect:` is how you gain full control over this stage of the display process in your custom views.

Since each step depends on the one before it, the display pass will trigger a layout pass if any layout changes are pending. Similarly, the layout pass will trigger updating the constraints if the constraint system has pending changes.

It is notable that constraint-based layout is an iterative process. Each step triggers another.

## Tricks
- [Applying Different Constraints for Different Devices](http://stackoverflow.com/questions/29179537/set-autolayout-constraints-relative-to-device-size)

## Reference
[Advanced Auto Layout Toolbox](https://www.objc.io/issues/3-views/advanced-auto-layout-toolbox/)