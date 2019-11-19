# cmd-ctrl_onLinux
This is AutoKey settings files on Linux.
Please reference to [my article(Qiita: Japanese IT knowledge website)](https://qiita.com/MTfirst/items/61bc6b8d3da9742b4130)

## How To use
1. Install [AutoKey](https://github.com/autokey/autokey).
2. Open `./create-script/create-script.py` and edit variable `regrex` as your favorite terminal name(at 39 line).
3. Run `create-script.py`
4. copy "ctrl-hyper" directry at `~/.config/autokey/data`

At #2, if you don't know class name, change At 45 line As
```python
if 0:
```
and run `create-script.py` and click your terminal.
