from tkinter import *
from tkinter.ttk import *
from googletrans import Translator

import random
import pandas as pd


translator = Translator()

'''
translation = translator.translate("Ystävä", src='fi', dest='ru')
print(translation.text)
'''

# reading from csv database that was made one time higher and saved
db = pd.read_csv('db_suomen.csv', index_col=0)

'''
# new data for test for the first time(than i added datas with this program)
db.loc[len(db.index)] = ['Kieli', 'Язык']
'''

# Hello from program
print('\nHei! Se on suomen sanasto!\n')

print(db.to_string())

# db.to_csv('db_suomen.csv')


app = Tk()
app.title('SuomenKieli')
app.geometry('311x255')
# app.configure(background='')
index_word = 100000000


# done
def give_word():
    global index_word

    translate_st['text'] = ''

    index_word = random.randint(0, len(db.index) - 1)
    word = db.loc[index_word].iloc[1]
    ind_2 = index_word

    if result['text'] != word:
        result_5['text'] = index_word + 1, '/', len(db)
        result['text'] = word

    else:
        while index_word == ind_2:
            index_word = random.randint(0, len(db.index) - 1)
            word = db.loc[index_word].iloc[1]
            result_5['text'] = index_word + 1, '/', len(db)
            result['text'] = word


# done
def translate():
    if index_word == 100000000:
        translate_st['text'] = "Nothing to translate"
    else:
        word_tr = db.loc[index_word].iloc[0]
        translate_st['text'] = word_tr


# not done
def add_word():

    try:
        new_word = command_text.get()
        list_words = []

        for i in db.word:
            list_words.append(i.lower())

        if new_word.lower() not in list_words:
            translation = translator.translate(new_word, src='fi', dest='ru')
            db.loc[len(db.index)] = [translation.origin.lower(), translation.text.lower()]
            status['text'] = '"' + str(translation.origin) + '"' + ' added'
            result_4['text'] = 'Need To Save Changes'
        else:
            print('Word is already in library')
            status['text'] = 'Word is already in library'
        status_2['text'] = ""

    except:
        print('Something goes wrong')
        status['text'] = 'Something goes wrong'
    command_text.delete(0, 300)


# done
def exit_com():
    quit()


# done
def save_com():
    db.to_csv('db_suomen.csv')

    result_4['text'] = 'Changes Saved'
    result_5['text'] = f'- / {len(db)}'

    status['text'] = ""
    status_2['text'] = ""

    result['text'] = ""
    translate_st['text'] = ""


def translate_word():
    status['text'] = ""
    status_2['text'] = ""
    try:
        translation = translator.translate(command_text.get(), src='fi', dest='ru')
        texxxt = str(translation.origin) + ' - ' + str(translation.text)

        if 40 >= len(texxxt) > 20:
            status['text'] = texxxt[:20]
            status_2['text'] = texxxt[20:]
        elif len(texxxt) > 40:
            status['text'] = 'Too long translate'
        else:
            status['text'] = texxxt

    except:
        print('Something goes wrong')
        status['text'] = 'Something goes wrong'
    command_text.delete(0, 300)


def delete_word():

    list_words = []
    del_word = command_text.get().lower()

    for i in db.word:
        list_words.append(i.lower())

    try:

        if del_word in list_words:

            del_index = db.index[db['word'] == del_word]

            db.drop(labels=del_index, axis=0, inplace=True)
            db.reset_index(drop=True, inplace=True)

            status['text'] = del_word, 'deleted'
            result_4['text'] = 'Need To Save Changes'

        else:
            status['text'] = 'Unexpected word'

        result_5['text'] = f'- / {len(db)}'
        result['text'] = ""
        translate_st['text'] = ""

    except:
        status['text'] = 'Sorry, some error'
    command_text.delete(0, 300)
    result['text'] = 'Tap "Random"'


# all interface

title = Label(
    app,
    text="--- Suomen App ---",
    font='Times 13'

)
title.grid(row=1, column=2)


command_text = Entry(
    app,
    background=''
)
command_text.grid(row=6, column=2)


btn_add = Button(
    app,
    text='Add word',
    command=add_word
)
btn_add.grid(row=8, column=1)

btn_delete = Button(
    app,
    text='Delete word',
    command=delete_word
)
btn_delete.grid(row=9, column=2)
btn_delete.config(width=14)

btn_find = Button(
    app,
    text='Translate',
    command=translate_word
)
btn_find.grid(row=8, column=3)


btn_launch = Button(
    app,
    text='Random',
    command=give_word
)
btn_launch.grid(row=2, column=2)


btn_translate = Button(
    app,
    text='Translate',
    command=translate
)
btn_translate.grid(row=3, column=2)


result = Label(
    app,
    text='Tap "Random"',
    foreground="firebrick",
    font='Times 11'

)
result.grid(row=4, column=2)


translate_st = Label(
    app,
    text='',
    foreground="green",
    font='Times 11'

)
translate_st.grid(row=5, column=2)

status = Label(
    app,
    text='',

)
status.grid(row=7, column=2)

status_2 = Label(
    app,
    text='',

)
status_2.grid(row=8, column=2)


btn_exit = Button(
    app,
    text='Exit',
    command=exit_com
)
btn_exit.grid(row=13, column=1, padx=7)

btn_save = Button(
    app,
    text='Save',
    command=save_com
)
btn_save.grid(row=13, column=3)

result_4 = Label(
    app,
    text='',

)
result_4.grid(row=13, column=2)

space = Label(
    app,
    text='',

)
space.grid(row=12, column=2)

slash = f'- / {len(db)}'

result_5 = Label(
    app,
    text=str(slash),

)
result_5.grid(row=4, column=3)

app.mainloop()
