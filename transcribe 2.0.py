import tkinter as tk
from tkinter import filedialog
from googletrans import Translator
import openai
import os
from httpx import Timeout

# Establecer la variable de entorno GOOGLE_APPLICATION_CREDENTIALS
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\get\flowing-access-382006-ae5a242457d5.json'


from googletrans import Translator

# Crear objeto de traducción de Google Translate
translator = Translator(service_urls=['translate.google.com'], timeout=15, proxies=None)


# Configurar OpenAI API key
openai.api_key = "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"

# Modelo e idioma para la transcripción de OpenAI
model = "whisper-1"
language = "es"

# Inicializar variable de transcripción
transcript = ""

# Función para transcribir audio usando OpenAI
def transcribe_audio():
    global transcript
    # Abra la ventana de selección de archivos para seleccionar el archivo de audio
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3;*.wav")])
    if file_path:
        # Transcribir audio usando OpenAI
        with open(file_path, "rb") as f:
            result = openai.Audio.transcribe(model, f, language=language)
            transcript = result['text']
        # Mostrar la transcripción en el cuadro de texto
        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END, transcript)

            

# Función para traducir la transcripción al francés
def translate_to_french(transcript):
    traductor = Traductor(service_urls=['translate.google.com'], tiempo de espera=Tiempo de espera(15.0), proxies=Ninguno)
    texto_traducido = traductor.translate(transcript, src='es', dest='fr').text
    return texto_traducido
# Función para traducir la transcripción al alemán
def translate_to_german(text_box):
    text = text_box.get(1.0, tk.END)
    translator = Translator(service_urls=['translate.google.com'], timeout=Timeout(15.0), proxies=None)
    translated_text = translator.translate(text, src='es', dest='ru').text
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, translated_text)

# Función para traducir la transcripción al italiano
def translate_to_italian(text_box):
    text = text_box.get(1.0, tk.END)
    translator = Translator(service_urls=['translate.google.com'], timeout=Timeout(15.0), proxies=None)
    translated_text = translator.translate(text, src='es', dest='it').text
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, translated_text)

# Función para traducir la transcripción al inglés
def translate_to_english(text_box):
    text = text_box.get(1.0, tk.END)
    translator = Translator(service_urls=['translate.google.com'], timeout=Timeout(15.0), proxies=None)
    translated_text = translator.translate(text, src='es', dest='en').text
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, translated_text)

# Crea la ventana
root = tk.Tk()
root.title("Transcriptor de audio")
root.geometry("400x400")

# Crea el marco
frame = tk.Frame(root, bg="#444654", padx=10, pady=10)
frame.pack(expand=True, fill="both")

# Crear el botón de selección de archivos
select_file_button = tk.Button(frame, text="Seleccionar archivo", command=transcribe_audio, bg="#888787", fg="#000000", activebackground="#353741", activeforeground="#ffffff", padx=10, pady=5)
select_file_button.pack(pady=10)

# Crear los botones de idiomas
translate_frame = tk.Frame(frame, bg="#444654", padx=10, pady=10)
translate_frame.pack(side=tk.TOP, pady=10)

french_button = tk.Button(translate_frame, text="Francés", command=lambda: translate_to_french(text_box), bg="#888787", fg="#000000", activebackground="#353741", activeforeground="#ffffff", padx=10, pady=5)
french_button.pack(side=tk.LEFT, padx=3)

german_button = tk.Button(translate_frame, text="Alemán", command=lambda: translate_to_german(text_box), bg="#888787", fg="#000000", activebackground="#353741", activeforeground="#ffffff", padx=10, pady=5)
german_button.pack(side=tk.LEFT, padx=3)

italian_button = tk.Button(translate_frame, text="Italiano", command=lambda: translate_to_italian(text_box), bg="#888787", fg="#000000", activebackground="#353741", activeforeground="#ffffff", padx=10, pady=5)
italian_button.pack(side=tk.LEFT, padx=3)

english_button = tk.Button(translate_frame, text="Inglés", command=lambda: translate_to_english(text_box), bg="#888787", fg="#000000", activebackground="#353741", activeforeground="#ffffff", padx=10, pady=5)
english_button.pack(side=tk.LEFT, padx=3)

# Cree el cuadro de texto para mostrar la transcripción y las traducciones
text_box = tk.Text(frame, height=8, width=40, bg="#444654", fg="#ffffff", font=("Arial", 12))
text_box.pack(expand=True, fill=tk.BOTH)

# Ejecutar la aplicación
root.mainloop()
