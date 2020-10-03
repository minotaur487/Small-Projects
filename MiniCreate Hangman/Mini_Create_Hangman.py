import random
import string
from tkinter import *
from tkinter import ttk, font
from tkinter.ttk import Style

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print( "  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def p_guess(guess, word, show):
    show = list(show)
    if guess in word:
        i = 0
        for x in list(word):
            if guess == x:
                show[i] = guess
            i += 2
        show = ''.join(show)
        return show
    else:
        show = ''.join(show)
        return show


def available_letters():
    l = list(av.get())
    if user_guess.get() in l:
        l.remove(user_guess.get())
        l = ''.join(l)
        av.set(l)
        user_guess.set('')


def click():
    guess = user_guess.get()
    show = p_guess(guess, word, w.get())
    w.set(show)
    x = w.get().split(' ')
    x = ''.join(x)
    if x == word:
        popupmsg()


def popupmsg():
    popup = Tk()
    popup.geometry('250x100+750+250')
    popup.wm_title("Victory")
    poplab = font.Font(family='Comic Sans MS')
    lab = ttk.Label(popup, text="Congrats! You won!", font=poplab)
    lab.pack(pady=10)
    B1 = ttk.Button(popup, text="Okay", command=lambda: [popup.destroy(), root.destroy()])
    B1.pack()
    popup.mainloop()


def character_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:1])


# initialization
wordlist = load_words()
word = choose_word(wordlist)
word_length = len(word)
guesses = 10
show = []
for x in range(word_length):
    show += ['_']
    show += [' ']
show = ''.join(show)

# initialize window
root = Tk()
root.title("Hangman")
# mwindow.resizable(width=False, height=False)
root.geometry('1000x500+500+250')

# frame and window
mf = ttk.Frame(root, borderwidth=0, width=50, height=30, padding=(50, 50, 50, 50))
style = Style()
style.configure("TFrame", background="#333")
style.configure("TLabel", background="#333")

# font
label = (font.Font(family='Comic Sans MS', size=25, weight='bold'))
avlabel = (font.Font(family='Comic Sans MS', size=20, weight='bold'))

# Letters
av = StringVar()
av.set(string.ascii_lowercase)
available_letters_label = ttk.Label(root, text="Available Letters:", font=label, foreground='white')
available_letters_var = ttk.Label(root, textvariable=av, font=avlabel, foreground='white')

# hangman guesses shown
w = StringVar()
w.set(show)
number = ttk.Label(root, text=f'I am thinking of a word that is {word_length} letters long.', font=label,
                   foreground='white')
word_label = ttk.Label(root, textvariable=w, font=label, foreground='white')

# guessing section
user_guess = StringVar()
guess_entry = ttk.Entry(root, textvariable=user_guess, width=50)
user_guess.trace("w", lambda *args: character_limit(user_guess))
guess_button = ttk.Button(root, text='Guess', command=lambda: [click(), available_letters()])

# layout
mf.grid(columnspan=10, rowspan=10, sticky=(N, W, E, S))
available_letters_label.grid(column=0, row=0, sticky=S)
available_letters_var.grid(column=1, row=0, sticky=S)
word_label.grid(columnspan=2, row=1)
number.grid(columnspan=2, row=2)
guess_button.grid(column=0, row=3, sticky=E)
guess_entry.grid(column=1, row=3, sticky=W, padx=20)
# adjusting columns
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

guess_entry.focus()
root.bind('<Return>', lambda a: [click(), available_letters()])

root.mainloop()
