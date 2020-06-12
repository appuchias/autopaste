import keyboard, pyperclip, os

fn = input("Type the filename:\n> ")

path = os.path.join("D:\Pablo\Documentos\PastedTxts", fn)

with open(path, "a") as a:
    while True:
        if keyboard.read_key() == "esc":
            raise SystemExit

        copy = pyperclip.waitForNewPaste()
        a.write(copy + "\n")
        print(copy)
