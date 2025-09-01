"""
Language Translator Application

This Python script provides a simple GUI for translating text between languages using an API.
It demonstrates Python programming, Tkinter GUI development, and API integration.

Features:
- Input text in one language and translate to another
- Select source and target languages
- Real-time translation using an API
- User-friendly interface

Author: [Your Name]
Date: August 30, 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "https://libretranslate.de/translate"  # Public translation API

def translate_text():
    src_lang = src_lang_var.get()
    dest_lang = dest_lang_var.get()
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return
    payload = {
        "q": text,
        "source": src_lang,
        "target": dest_lang,
        "format": "text"
    }
    try:
        response = requests.post(API_URL, data=payload)
        response.raise_for_status()
        translated = response.json()["translatedText"]
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

root = tk.Tk()
root.title("Language Translator App")

languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Russian": "ru",
    "Chinese": "zh",
    "Arabic": "ar",
    "Hindi": "hi"
}

src_lang_var = tk.StringVar(value="en")
dest_lang_var = tk.StringVar(value="es")

ttk.Label(root, text="Source Language:").pack(pady=2)
src_lang_menu = ttk.Combobox(root, textvariable=src_lang_var, values=list(languages.values()))
src_lang_menu.pack(pady=2)

ttk.Label(root, text="Target Language:").pack(pady=2)
dest_lang_menu = ttk.Combobox(root, textvariable=dest_lang_var, values=list(languages.values()))
dest_lang_menu.pack(pady=2)

ttk.Label(root, text="Enter text to translate:").pack(pady=2)
input_text = tk.Text(root, height=5, width=50)
input_text.pack(pady=2)

ttk.Button(root, text="Translate", command=translate_text).pack(pady=5)

ttk.Label(root, text="Translated text:").pack(pady=2)
output_text = tk.Text(root, height=5, width=50)
output_text.pack(pady=2)

root.mainloop()