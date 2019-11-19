import json
import string

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


            file_python = open(description + '.py', 'w')
            file_python.write(pytxt)
            file_python.close()


            json_data["description"] = description
            json_data["hotkey"]["hotKey"] = hotkey
            json_data["hotkey"]["modifiers"][0] = "<" + modifier + ">"

            file_json = open('.' + description + ".json", 'w')
            json.dump(json_data, file_json, indent=4)

            file_json.close()

    f.close()


if __name__ == "__main__":
    # input your favorite terminal
    regrex = "gnome-terminal-server.Gnome-terminal"
    main(regrex)
