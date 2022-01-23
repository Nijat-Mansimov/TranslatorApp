from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob

root = Tk()
root.title("Google Translator")
root.geometry("900x400")

def translate_now():
	global language
	try:
		text_ = text1.get(1.0, END)
		# c2 = combo1.get()
		c3 = combo2.get()
		if(text_):
			words = textblob.TextBlob(text_)
			lan = words.detect_language()
			for i,j in language.items():
				if(j == c3.lower()):
					lan_ = i
			words = words.translate(from_lang=lan, to=str(lan_))
			text2.delete(1.0, END)
			text2.insert(END, words)

	except Exception as e:
		messagebox.showerror("googletrans", "please try again")

image_icon = PhotoImage(file="translate_logo.png")
root.iconphoto(False, image_icon)

language = googletrans.LANGUAGES
values= list(language.values())
languageV = []
for i in values:
	languageV.append(i.capitalize())

combo1 = ttk.Combobox(root, values=languageV, font="verdana 8 italic", state="r")
combo1.place(x=110, y=20)
combo1.set("Azerbaijani")

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=400, height=210)

text1 = Text(f, font= "Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=390, height=200)

combo2 = ttk.Combobox(root, values=languageV,font="Verdana 8 italic", state="r")
combo2.place(x=600, y=20)
combo2.set("Select language")

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=490, y=118, width=400, height=210)

text2 = Text(f1, font= "Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=390, height=200)

translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd=5,bg="red", fg="white", width=20, command=translate_now)
translate.place(x=330, y=340)

root.configure(bg="yellow")
root.mainloop()