import tkinter
from tkinter import filedialog
import webbrowser

# Определение функции для выбора файла через диалоговое окно
def file_select():
    filename = filedialog.askopenfilename(
                                          initialdir="/",                   # Устанавливаем начальную директорию,
                                          title="Выберите файл",            # Заголовок диалогового окна
                                          filetypes=(                       # Список доступных типов файлов для выбора
                                              ('Текстовый файл', '.txt'),   # Тип: текстовые файлы с расширением .txt
                                              ('Все файлы', '*')))          # Тип: все файлы (с любым расширением)
    if filename:  # Если файл выбран, то обновляем текст
        text_widget.delete(1.0, tkinter.END)  # Очистить текущее содержимое Text
        link_text = f'Файл: {filename}'  # Текст с путем к файлу
        text_widget.insert(tkinter.END, link_text)  # Вставить путь в Text
        text_widget.tag_add("hyperlink", "1.0", tkinter.END)  # Добавляем тег для ссылки
        text_widget.tag_configure("hyperlink", foreground="blue", underline=True)  # Настройка внешнего вида ссылки
        text_widget.tag_bind("hyperlink", "<Button-1>", lambda e: open_file(filename))  # Привязка события клика

# Открытие файла по клику на ссылку
def open_file(filename):
    webbrowser.open(f'file:///{filename}')  # Открыть файл через веб-браузер или по умолчанию

# Создание главного окна приложения
window = tkinter.Tk()

# Настройка параметров главного окна
window.title('Проводник')                           # Имя окна
window.geometry('350x150')                          # Размеры окна
window.configure(bg='lightgray')                    # Цвет фона
window.resizable(False, False)                      # Запрет изменения размера окна

# Создание текстового виджета с полосой прокрутки
text_widget = tkinter.Text(window,
                           height=5, width=50,       # Устанавливаем размер Text
                           wrap=tkinter.WORD,        # Перенос слов на новую строку
                           bg='lightgray',           # Цвет фона
                           fg='black',               # Цвет текста
                           padx=5, pady=5)           # Добавляем отступы внутри Text

# Создание полосы прокрутки
scrollbar = tkinter.Scrollbar(window, command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

# Размещение виджетов в окне
text_widget.grid(row=1, column=1, sticky='w')
scrollbar.grid(row=1, column=2, sticky='ns')

# Создание кнопки для выбора файла
button_select = tkinter.Button(window,
                               width=15, height=1,          # Размеры кнопки
                               text='Выбрать файл',         # Текст на кнопке
                               background='silver',         # Цвет фона кнопки
                               foreground='black',          # Цвет текста кнопки
                               command=file_select)         # При нажатии на кнопку будет вызываться функция file_select

# Размещение кнопки в окне
button_select.grid(column=1,                # Устанавливаем расположение кнопки в 1-й колонке
                   row=2,                   # Устанавливаем расположение кнопки в 2-й строке
                   pady=5)                  # Добавляем отступ по вертикали (в пикселях)

# Запуск главного цикла приложения
window.mainloop()
