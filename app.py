import tkinter as tk
from tkinter import messagebox
import pyperclip  # Модуль для работы с буфером обмена

# Алфавит А1–Я33 с Ё
alphabet = [chr(code) for code in range(ord('А'), ord('А') + 32)]
alphabet.insert(6, 'Ё')

letter_to_number = {letter: str(i + 1).zfill(2) for i, letter in enumerate(alphabet)}
number_to_letter = {str(i + 1).zfill(2): letter for i, letter in enumerate(alphabet)}

def encrypt(message):
    result = []
    message = message.upper()
    for char in message:
        if char in letter_to_number:
            result.append(letter_to_number[char])
        elif char == ' ':
            result.append(' ')
        else:
            result.append(char)
    return '-'.join(result)

def decrypt(code):
    result = []
    parts = code.strip().split()
    for part in parts:
        if part == '-':
            result.append('')
        elif part == " ":
            result.append(" ") 
        elif part in number_to_letter:
            result.append(number_to_letter[part])
        else:
            result.append('?')
    return ''.join(result)

# GUI
root = tk.Tk()
root.title("Шифр А1–Я33")

# Ввод
tk.Label(root, text="Введите сообщение или шифр:").pack()
input_text = tk.Text(root, height=3, width=40)
input_text.pack()

# Обработчики
def handle_encrypt():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showinfo("Ошибка", "Введите сообщение.")
        return
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypt(text))

def handle_decrypt():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showinfo("Ошибка", "Введите шифр.")
        return
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypt(text))

def copy_to_clipboard():
    result = output_text.get("1.0", tk.END).strip()
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        messagebox.showinfo("Готово", "Результат скопирован в буфер обмена!")
    else:
        messagebox.showinfo("Пусто", "Сначала зашифруйте или расшифруйте текст.")

def paste_from_clipboard():
    try:
        clipboard_text = pyperclip.paste()  # Получаем текст из буфера обмена
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, clipboard_text)
    except Exception as e:
        messagebox.showinfo("Ошибка", "Не удалось вставить текст из буфера обмена.")

# Кнопки
tk.Button(root, text="Зашифровать", command=handle_encrypt).pack(pady=5)
tk.Button(root, text="Расшифровать", command=handle_decrypt).pack()
tk.Button(root, text="Скопировать результат", command=copy_to_clipboard).pack(pady=5)
tk.Button(root, text="Вставить из буфера обмена", command=paste_from_clipboard).pack(pady=5)

# Вывод
tk.Label(root, text="Результат:").pack()
output_text = tk.Text(root, height=3, width=40, bg="#f0f0f0")
output_text.pack()

# Запуск
root.mainloop()