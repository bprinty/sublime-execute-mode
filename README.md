sublime-execute-mode
======

Wouldn't you love to use vim execute mode in sublime? Well now you can! 


Status
------
Still in pre-alpha development. This section will be removed when the package is ready for widespread use.


Installation
-----------
This project isn't yet hosted on package control, so it has to be installed manually (for now). To install this package, clone the repository:

```bash
git clone git@github.com:bprinty/sublime-execute-mode.git
```

into your sublime ```Packages/``` folder.


Use
---

After highlighting a selection of text, use super+shift+e (OSX) or ctrl+shift+e (Linux, Windows) to open up the command console, where you can then type any shell command that reads from stdin. For instance, to remove all non-foo variables in the following block:

```bash
foo = 'foo'
bar = 'bar'
baz = 'baz'
```

Open the command console and type:

```bash
grep 'foo'
```

Or, to replace all instances of foo in the command above to foobar, open the command console and type:

```bash
sed 's/foo/foobar/g'
```

Questions/Feedback
------------------

Submit an issue or comment in the GitHub issue tracker.
