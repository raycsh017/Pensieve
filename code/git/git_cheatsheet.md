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



## Formulas

### Creating a branch from your coworker's branch

1. Add the remote path to your coworker's git repo

   `git remote add {remote name} {remote path}`

2. Fetch from the remote repo

   `git fetch {remote name}`

3. Checkout a new branch from your coworker's remote branch

   `git checkout -b {your branch name} {remote name}/{remote branch name}`



### Changing the author

#### Last commit

Run `git commit --amend --author="Author Name <email@address.com>"`

#### Multiple commits

1. Use `git rebase -i {branch name}`, change `pick` to `edit` for the commits you want to change the author name
2. Once the rebase starts, it would pause at the first commit that you marked with `edit`
3. Run `git commit --amend --author="Author Name <email@address.com>"`
4. Run `git rebase --continue` to hit the next commit that you want to edit
5. Repeat the steps 3 and 4