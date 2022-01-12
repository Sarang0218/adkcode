from tkinter import *
from tkinter import simpledialog, filedialog
from os import system
from tkinter import font
from time import sleep
from tkinter import colorchooser
from os import system, name
import re
from time import sleep

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')


    else:
        _ = system('clear')


clear()
carrot = "{"
carrot2 = "}"
print("AdkCode 0.1.4 - CLI")




def main(choice = "Normal"):


    print("AdkCode 0.1.4 - UI SETUP....")
    sleep(1)
    root = Tk("")
    root.title("adkCode 0.1.4")

    text=Text(root)
    text.grid()





    def key(event):
        text.tag_remove('found', '1.0', END)
        text.tag_remove('foundin', '1.0', END)
        text.tag_remove('foundfun', '1.0', END)
        text.tag_remove('yellow', '1.0', END)


        def highlight_regex(regex, tag):
            length = IntVar()
            start = 1.0
            idx = text.search(regex, start, stopindex=END, regexp=1, count=length)
            while idx:
                end = f"{idx}+{length.get()}c"
                text.tag_add(tag, idx, end)
                start = end
                idx = text.search(regex, start, stopindex=END, regexp=1, count=length)


        highlight_regex(r"[#][a][p][e][^a-zA-Z]", "utility")
        highlight_regex(r"[#][m][a][x][-][m][e][m][o][r][y][^a-zA-Z]", "utility")
        highlight_regex(r"[c][l][a][s][s][ ]", "keyword")
        highlight_regex(r"[f][u][n][c][t][^a-zA-Z]", "keyword")
        highlight_regex(r"[\'][^\']*[\']", "string")
        highlight_regex(r"[\"][^\']*[\"]", "string")
        highlight_regex(r"(\d)+[.]?(\d)*", "number")
        highlight_regex(r"[^ \t\n\r\f\v]*[(]", "number")
        text.tag_config('number', foreground="blue")
        text.tag_config('string', foreground="green")
        text.tag_config('keyword', foreground="red")
        text.tag_config('utility', foreground="brown")


        #find("#ape", "yellow")
        #find("#max-memory", "yellow")


    root.bind_all('<Key>', key)


    if choice == "server":

        text.insert(INSERT, f'\n#include server\n')
        text.insert(INSERT, f"render_file('index.html')\n")
        text.insert(INSERT, f"errorhandler(404, 'error.html')\n")
        text.insert(INSERT, f"run_server()\n")
    def run():
        global text
        t = text.get("1.0", "end-1c")





    def text_color():
    	# Pick a color
    	my_color = colorchooser.askcolor()[1]
    	if my_color:
    		# Create our font
    		color_font = font.Font(text, text.cget("font"))

    		# Configure a tag
    		text.tag_configure("colored", font=color_font, foreground=my_color)

    		# Define Current tags
    		current_tags = text.tag_names("sel.first")

    		# If statment to see if tag has been set
    		if "colored" in current_tags:
    			text.tag_remove("colored", "sel.first", "sel.last")
    		else:
    			text.tag_add("colored", "sel.first", "sel.last")

    def addText():
        textfieldkey = simpledialog.askstring(title="Insert A Text Object", prompt="Title:")
        text.insert(INSERT, f'\ntextlabel("{textfieldkey}")')
    def addButton():
        buttonkey = simpledialog.askstring(title="Insert A Button Object", prompt="Title:")
        callFunc = simpledialog.askstring(title="Insert A Button Object", prompt="Function On Press")
        text.insert(INSERT, f'\nbutton("{buttonkey}", {callFunc}())')
    def addIf():
        ifstate = simpledialog.askstring(title="If Statement", prompt="Condition")
        res = simpledialog.askstring(title="Result", prompt="On True:")
        text.insert(INSERT, f'\nif {ifstate} {carrot}\n')
        text.insert(INSERT, f'  {res}\n')
        text.insert(INSERT, f'{carrot2}\n')

    def addRepeat():
        iterationVar = simpledialog.askstring(title="Iteration Variable", prompt="Name: ")

        repeat = simpledialog.askstring(title="Repeat", prompt="Cycles: ")
        stuff = simpledialog.askstring(title="Code", prompt="Statement: ")
        text.insert(INSERT, f'\n{iterationVar} = 0 while {iterationVar} < {int(repeat) + 1} {carrot}\n')
        text.insert(INSERT, f'  {stuff}\n')
        text.insert(INSERT, f'{carrot2}\n')
    def addInclude():
        file = simpledialog.askstring(title="Include Statement", prompt="Include:")
        text.insert(INSERT, f'\n#include {file}')

    def saveas():

        t = text.get("1.0", "end-1c")
        savelocation=filedialog.asksaveasfilename()
        file1=open(savelocation, "w+")
        file1.write(t)
        file1.close()
    buttonframe = Frame(root)
    langframe = Frame(root)
    widgetframe = Frame(root)
    functionsframe = Frame(root)

    button7=Button(buttonframe, text="Colorify(Clarification)", command=text_color)
    button6=Button(langframe, text="Repeat(Custom)", command=addRepeat)
    button5=Button(langframe, text="Include Statement", command=addInclude)
    button4=Button(langframe, text="If Statement", command=addIf)
    button=Button(widgetframe, text="Label", command=addText)
    button3=Button(widgetframe, text="Button", command=addButton)
    button1=Button(functionsframe, text="Save", command=saveas)
    button2=Button(functionsframe, text="Run", command=run)

    c=Label(root, text="Language", font=("Helvetica", 30))
    c.grid()
    langframe.grid()
    button5.grid(row=0, column=0)
    button6.grid(row=0, column=1)
    button4.grid(row=0, column=2)
    a=Label(root, text="Widgets", font=("Helvetica", 30))
    a.grid()
    widgetframe.grid()
    button.grid(row=0, column=3)
    button3.grid(row=0, column=4)
    b=Label(root, text="Functions", font=("Helvetica", 30))
    b.grid()
    functionsframe.grid()
    button1.grid(row=0, column=5)
    button2.grid(row=0, column=6)



while True:
    choice = input(">>> ")
    cmd = choice.split()
    try:
        if cmd[0].lower() == "ui" and len(cmd) == 1:
            print("Close the UI window if you want to continue the CLI...")
            main()
            clear()
            print("AdkCode 0.1.4 - CLI")
        elif cmd[0].lower() == "ui" and len(cmd) > 1:
            if cmd[1] == "server":
                main("server")
                clear()
                print("AdkCode 0.1.4 - CLI")
        elif cmd[0].lower() == "clear":
            clear()
            print("AdkCode 0.1.4 - CLI")

        elif cmd[0].lower() == "clear":
            clear()
            print("AdkCode 0.1.4 - CLI")



    except:
        continue
