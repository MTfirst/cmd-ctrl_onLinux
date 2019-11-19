# cmd-ctrl_onLinux
This is AutoKey settings files on Linux.
Please reference to [my post Qiita(Japanese IT knowledge website)](https://)

## How To use
1. After installing [AutoKey](https://github.com/autokey/autokey), clone "ctrl-hyper" directry at `~/.config/autokey/data`
2. Open `test.py` and edit variable `regrex` as your favorite terminal name(at 39 lines).
3. Run `test.py`

At #2, if you don't know class name, enter the command below and click your terminal(For example, I click gnome-terminal).
```sh
xprop | grep WM_CLASS
#WM_CLASS(STRING) = "gnome-terminal-server", "Gnome-terminal"
```
If WM_CLASS(STRING) = "x", "y", As a result, `regrex = x.y`  
(For example, `"gnome-terminal-server.Gnome-terminal"`)