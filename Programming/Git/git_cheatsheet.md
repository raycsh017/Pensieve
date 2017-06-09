# Git: Let's git it

## `git stash`
Saves your local modifications to a new stash and rolls them back to HEAD

### `git stash list`
Lists the stashes you currently have

ex. `stash@{0}` is the latest stash you saved, `stash@{1}` would be the second latest stash you saved, so on.

### `git stash show`
Shows the changes recorded in the stash as a diff between the stashed state and its original parent. With `-p` flag, it shows more detailed version of diff.

### `git stash pop`
Removes a single stashed state from the stash list and applies it on top of the current working tree state.
