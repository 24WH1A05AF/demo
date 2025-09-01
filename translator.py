import tkinter as tk
from tkinter import ttk
import requests

API_URL = 'http://127.0.0.1:5000/translate'

LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'hi': 'Hindi',
    'zh-cn': 'Chinese',
    'ar': 'Arabic',
    'ru': 'Russian',
    'ja': 'Japanese',
    'pt': 'Portuguese',
}

def translate_text():
    src_lang = src_lang_var.get()
    dest_lang = dest_lang_var.get()
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter text to translate.")
        return
    try:
        response = requests.post(API_URL, json={
            'text': text,
            'src': src_lang,
            'dest': dest_lang
        })
        if response.status_code == 200:
            translated = response.json().get('translated_text', '')
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, translated)
        else:
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, "Translation failed.")
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {e}")

root = tk.Tk()
root.title("Language Translator App")

src_lang_var = tk.StringVar(value='en')
dest_lang_var = tk.StringVar(value='es')

frame = ttk.Frame(root, padding=10)
frame.pack(fill='both', expand=True)

# Source Language
src_label = ttk.Label(frame, text="Source Language:")
src_label.grid(row=0, column=0, sticky='w')
src_lang_menu = ttk.Combobox(frame, textvariable=src_lang_var, values=list(LANGUAGES.keys()))
src_lang_menu.grid(row=0, column=1)

# Target Language
dest_label = ttk.Label(frame, text="Target Language:")
dest_label.grid(row=1, column=0, sticky='w')
dest_lang_menu = ttk.Combobox(frame, textvariable=dest_lang_var, values=list(LANGUAGES.keys()))
dest_lang_menu.grid(row=1, column=1)

# Input Text
input_label = ttk.Label(frame, text="Enter text to translate:")
input_label.grid(row=2, column=0, sticky='w')
input_text = tk.Text(frame, height=5, width=40)
input_text.grid(row=3, column=0, columnspan=2)

# Translate Button
translate_btn = ttk.Button(frame, text="Translate", command=translate_text)
translate_btn.grid(row=4, column=0, columnspan=2)

# Output Text
output_label = ttk.Label(frame, text="Translated text:")
output_label.grid(row=5, column=0, sticky='w')
output_text = tk.Text(frame, height=5, width=40)
output_text.grid(row=6, column=0, columnspan=2)

root.mainloop()
