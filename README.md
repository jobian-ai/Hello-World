# Hello-World
Code that I am sharing, with the entire world.

## So far, this is just some code written while doing a tutorial

## VS CODE virtual environment:

- Hold SHIFT & Right click on Scripts directory
- Select "Copy Path"
- paste into terminal window at bottom of screen.
- add "activate.bat" or "dactivate.bat"
___
## Problem with CODE - OSS (VS Code) on Manjaro

Error with Jupyter notebooks like this one:
[StackOverflow](https://stackoverflow.com/questions/71106136/jupyter-extension-for-vscode-on-linux-throws-error-when-doing-anything-jupyter-r/71245496)

I followed the intructions (It's CTL+SHIFT+P not CTL+ALT+P) > *Preference: Configure Runtime*

and added this to the "argv.json" file
>
```
{
// Stuff deleted
	// Hellow World!
	"enable-proposed-api": ["ms-toolsai.jupyter"]
}
```

Need to add a comma to the end of the line above it.
