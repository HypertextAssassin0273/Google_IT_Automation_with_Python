## 0:10 - 0:16
It's a good idea to always synchronize your branches before starting any work on your own.

## 0:25 - 0:33
Another common practice is to try and avoid having very large changes that modify a lot of different things.

## 0:38 - 0:49
For example, if you are renaming a variable for clarity reasons, you don't want to have code that adds new functionality in the same commit. It's better if you split it into different commits.

## 1:02 - 1:07
when working on a big change, it makes sense to have a separate feature branch.

## 1:13 - 1:29
To make the final merge of the feature branch easier, it makes sense to regularly merge changes made on the master branch back onto the feature branch. This way, we won't end up with a huge number of merge conflicts when the final merge time comes around.

## 1:31 - 1:42
If you need to maintain more than one version of a project at the same time, it's common practice to have the latest version of the project in the master branch and a stable version of the project on a separate branch.

## 2:05 - 2:12
Rebasing can help a lot with identifying bugs, but use it with caution. Whenever we do a rebase, we're rewriting the history of our branch.

## 2:13 - 2:17 - 2:22
The old commits get replaced with new commits, and they'll have completely different hash sums.

## 2:31 - 2:42
So as a general rule, you shouldn't rebase changes that have been pushed to remote repos. The Git server will automatically reject pushes that attempt to rewrite the history of the branch.

## 2:51 - 3:05
In our feature branch example, we rebased the branch. Merged it to the master and then deleted the old one. That way, we didn't push the rebase changes to the refactor branch, only to the master branch that hadn't seen those changes before.
