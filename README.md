# cmd-ctrl_onLinux
This is AutoKey settings files on Linux.
Please reference to [my post Qiita(Japanese IT knowledge website)](https://)

## How To use
1. Install [AutoKey](https://github.com/autokey/autokey).
2. Open `./create-script/create-script.py` and edit variable `regrex` as your favorite terminal name(at 39 lines).
3. Run `create-script.py`
4. copy "ctrl-hyper" directry at `~/.config/autokey/data`

At #2, if you don't know class name, enter the command below and click your terminal(For example, I click gnome-terminal).
```sh
xprop | grep WM_CLASS
#WM_CLASS(STRING) = "gnome-terminal-server", "Gnome-terminal"
```
If WM_CLASS(STRING) = "x", "y", As a result, `regrex = x.y`  
(For example, `"gnome-terminal-server.Gnome-terminal"`)
