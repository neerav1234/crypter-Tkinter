from tkinter import *
import base64

root = Tk()
root.geometry('500x300')
root.title("data Encode and Decode")

Label(root, text='ENCODER-DECODER', font='algerian 20 bold').pack()
Label(root, text="-by w3ath3ringR0ck1", font='times 16').pack(side=BOTTOM)

text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


def Encode(key, msg):
    enc = []

    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(msg[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def Decode(key, msg):
    dec = []
    msg = base64.urlsafe_b64decode(msg).decode()

    for i in range(len(msg)):
        key_c = key[i % len(key)]
        dec.append(chr((ord(msg[i]) - ord(key_c) + 256) % 256))

    return "".join(dec)


def setMode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), text.get()))
    else:
        Result.set("Invalid Mode!")


def Exit():
    root.destroy()


def Reset():
    text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


Label(root, font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
Entry(root, font='arial 10', textvariable=text,
      bg='ghost white').place(x=290, y=60)

Label(root, font='arial 12 bold', text='KEY').place(x=60, y=90)
Entry(root, font='arial 10', textvariable=private_key,
      bg='ghost white').place(x=290, y=90)

Label(root, font='arial 12 bold',
      text='MODE(e-encode, d-decode)').place(x=60, y=120)
Entry(root, font='arial 10', textvariable=mode,
      bg='ghost white').place(x=290, y=120)
Entry(root, font='arial 10 bold', textvariable=Result,
      bg='ghost white').place(x=290, y=150)

Button(root, font='arial 10 bold', text='RESULT', padx=2,
       bg='LightGray', command=setMode).place(x=60, y=150)

Button(root, font='arial 10 bold', text='RESET', width=6,
       command=Reset, bg='LimeGreen', padx=2).place(x=80, y=190)

Button(root, font='arial 10 bold', text='EXIT', width=6, command=Exit,
       bg='OrangeRed', padx=2, pady=2).place(x=180, y=190)

root.mainloop()
