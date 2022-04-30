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

Need to add a comma to the end of the line above it ("argv.json").

---

## Wanted to use SHH with VS CODE on Manjaro.

### Had problems

**01 MAR 22**


Generating an SSH key for use with Github.

Terminal Window:

> ssh-keygen -o -t rsa -C "email@domain.com"

asks for location for the file.  default is /home/chuck/.ssh/id_rsa

it says it doesn't exist when trying to cd into this dir. but accepted defaults.

Turns out it put the public & private keys in my home directory.

> cat ssh-github-jobian.pub

Prints out the key contents so you can copy and paste into github.

Still not working for VS Code.

___

**02 MAR 22**

Installed this: 

> sudo pacman -S x11-ssh-askpass                                          

then:

> cd /usr/lib/ssh/ssh-askpass 

> cd: not a directory: /usr/lib/ssh/ssh-askpass

*sigh*
___

> eval ssh-agent -s
```
SSH_AUTH_SOCK=/tmp/ssh-XXXXXXjK7mqK/agent.37618; export SSH_AUTH_SOCK;
SSH_AGENT_PID=37619; export SSH_AGENT_PID;
echo Agent pid 37619;
```
___

Still not working

Restart

___

Still not working
___

**03 MAR 22**

```
Git: git@github.com: Permission denied(publickey)
```
> eval $(ssh-agent -s)

> ssh-add ~/.ssh/ssh-github-jobian

> Agent pid 2542
```
Git: git@github.com: Permission denied(publickey)
```

can't kill pid so . .

> ssh-add -l 

> Could not open a connection to your authentication agent.

installed sshpass

In terminal:

> ssh-add ~/.ssh/ssh-github-jobian

> Could not open a connection to your authentication agent.

"ssh-agent"
```
SSH_AUTH_SOCK=/tmp/ssh-XXXXXXxzfPfT/agent.4818; export SSH_AUTH_SOCK;
SSH_AGENT_PID=4819; export SSH_AGENT_PID;
echo Agent pid 4819;
```
> eval $(ssh-agent)

> Agent pid 4857

> ssh-add ~/.ssh/ssh-github-jobian

> Identity added: /home/chuck/.ssh/ssh-github-jobian (ops@infil.org)

## YAY!

ssh-add -L  < - NOW WORKS

Now in VS CODE =
```
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.
```

*sigh*
___

### Recreating the SSH key - maybe having a non-default name is bad.

 > ssh-add -D

 > All identities removed.

 > ssh-keygen -o -t rsa -C "email@domain.com"

 ACCEPTED THE DEFAULT NAME id_rsa

 Copied ssh keys from my HOME dir to the .ssh directory (again)

> cd .ssh

> cat id_rsa.pub

copy and paste to github

In terminal:

> ssh-add ~/.ssh/id_rsa

Identity added: /home/chuck/.ssh/id_rsa (email@domain.com)

```
Git: Host key verification failed.

fatal: Could not read from remote repository.
```

*sigh*
___

> ssh -T git@gitlab.com

no worky-worky

restart

___

[Tried tips at this link](https://stackoverflow.com/questions/13363553/git-error-host-key-verification-failed-when-connecting-to-remote-repository)

Shows the key in the known_hosts file

> ssh-keyscan rsa github.com 

Removes the key from the known_hosts file

> ssh-keygen -R github.com

Adds the key back into the known_hosts file.
> ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts 

IN VS CODE / CODE - OSS

## Add the github with SSH < -- PULLS OK!!!!!

## COMMIT & PUSH OK!!!!!

# VICTORY!
___
Test commit from Fedora workstation


>ssh -T git@gitlab.com   

```
git@gitlab.com: Permission denied (publickey,keyboard-interactive).
```

*sigh*

```
virtualenv venv
```

```
source venv/bin/activate
```