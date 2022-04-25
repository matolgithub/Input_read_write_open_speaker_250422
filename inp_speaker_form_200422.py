import datetime
from tkinter import *
from tkinter import Tk
from tkinter import simpledialog
from tkinter import messagebox
from speaker import speaker


def sim_dial_form():
    speaker('Меня зовут Клава, я сестра Алисы! И так, начнём.')
    ask_1 = 'Введите число.'
    speaker(ask_1)
    sdf_1 = simpledialog.askinteger('Ввод числа', f'{ask_1}: ', parent=window)
    answer_1 = 'Ваши числовые данные'
    speaker(f'{answer_1} {sdf_1}')
    messagebox.showinfo('Результат ввода', f'{answer_1}: {sdf_1}.')
    write_inp_file(num_id=sdf_1)
    return sdf_1

def quit_form():
    speaker('Так и быть, мы закончили!')
    window.quit()

def write_inp_file(num_id, file_name='input_fl.txt'):
    dtn = datetime.datetime.now()
    with open(file_name, 'w', encoding='utf-8') as new_file:
        sp_fd_1 = f'Вы записали в файл данные, {num_id}'
        speaker(sp_fd_1)
        new_file.write(f'{sp_fd_1}, которые были введены: {dtn}.')
        sp_fd_2 = f'Файл: {file_name} - только что был создан!'
        speaker(sp_fd_2)
    messagebox.showinfo('Создание файла.', sp_fd_2)
    read_inp_file(file_name='input_fl.txt')

def read_inp_file(file_name='input_fl.txt'):
    sp_fd_3 = f'Вы хотите открыть файл: {file_name}?'
    speaker(sp_fd_3)
    ask_form_1 = messagebox.askquestion('Форма открытия и просмотра файла.', sp_fd_3)
    if ask_form_1 == 'yes':
        sp_fd_4 = f'Отлично, сейчас мы откроем для Вас данные из файла: {file_name}. Вот эти данные.'
        speaker(sp_fd_4)
        with open(file_name, 'r', encoding='utf-8') as open_file:
            open_file_text = open_file.read()
            messagebox.showinfo('Открытый текст из файла:', f'{open_file_text}')
    else:
        sp_fd_5 = 'Ясно, тогда мы ничего не делаем!'
        speaker(sp_fd_5)
        messagebox.showinfo('Отказ', sp_fd_5)


window = Tk()
window['bg'] = 'grey10'
window.geometry('400x100+200+200')
window.title('Input form with speaker.')
lbl_1 = Label(window, text='Input form, read, write, open file, with speaker help.', padx=10, pady=10,
              fg='white', bg='grey10')
lbl_1.grid(row=1, column=1)
btn_1 = Button(text='Start', command=sim_dial_form)
btn_1.grid(row=3, column=2, padx=10, pady=10, sticky=E)
btn_2 = Button(text='Quit', command=quit_form)
btn_2.grid(row=3, column=3, padx=10, pady=10, sticky=E)
window.mainloop()
