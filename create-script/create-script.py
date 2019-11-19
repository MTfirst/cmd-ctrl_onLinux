import json
import string
import subprocess
import re

def main(regrex):
    f = open("sample.json", "r")
    json_data = json.load(f)

    json_data["filter"]["regrex"] = regrex

    hotkeys = string.ascii_lowercase[:26]
    modifiers = ['ctrl', 'hyper']
    sends = ['<ctrl>+<shift>', '<ctrl>']

    for hotkey in hotkeys:
        for modifier, send in zip(modifiers, sends):
            description = modifier + "-" + hotkey
            pytxt = "keyboard.send_keys(\"" + send + "+" + hotkey + "\")"


            file_python = open('../ctrl-hyper/' + description + '.py', 'w')
            file_python.write(pytxt)
            file_python.close()


            json_data["description"] = description
            json_data["hotkey"]["hotKey"] = hotkey
            json_data["hotkey"]["modifiers"][0] = "<" + modifier + ">"

            file_json = open('../ctrl-hyper/.' + description + ".json", 'w')
            json.dump(json_data, file_json, indent=4)

            file_json.close()

    f.close()


if __name__ == "__main__":
    # input your favorite terminal


    # 1: manually input
    # 2: auto-detected
    if 1:
        regrex = "gnome-terminal-server.Gnome-terminal"
    else :
        print("Click your Terminal Window")
        cmd = "xprop | grep WM_CLASS"
        regrex_str = subprocess.check_output(cmd, shell=True, encoding='utf-8')
        regrex_list = re.findall('\".*\"', regrex_str)[0].split(',')
        regrex = regrex_list[0].strip('\"') + '.' + regrex_list[1].strip(' ').strip('\"')
   
   
    print(regrex) 
    main(regrex)
