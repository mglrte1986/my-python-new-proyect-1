import os
import json
import requests
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip

def generar_video():
    try:
        # Cargar configuración
        with open("config_gorila.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        API_KEY = os.getenv("ELEVENLABS_API_KEY", config["api_key"])
        VOICE_ID = config["voice_id"]
        video_base_path = config["video_base"]
        texto_gorila = config["texto"]

        # 1. Generar voz con ElevenLabs
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": API_KEY
        }
        data = {
            "text": texto_gorila,
            "voice_settings": {
                "stability": 0.45,
                "similarity_boost": 0.85,
                "style": "épico",
                "use_speaker_boost": True
            }
        }

        response = requests.post(url, headers=headers, json=data)
        voz_path = "voz_gorila.mp3"
        with open(voz_path, "wb") as f:
            f.write(response.content)

        # 2. Crear video con MoviePy
        video_base = VideoFileClip(video_base_path)
        audio_gorila = AudioFileClip(voz_path)

        texto = TextClip(config["titulo"], fontsize=70, color="white", font="Arial-Bold")
        texto = texto.set_position(("center", "bottom")).set_duration(video_base.duration)

        video_final = CompositeVideoClip([video_base, texto])
        video_final = video_final.set_audio(audio_gorila)

        # 3. Exportar resultado
        output_path = config["salida"]
        video_final.write_videofile(output_path, codec="libx264", audio_codec="aac")

        messagebox.showinfo("Éxito", f"Video generado: {output_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def iniciar_app():
    root = tk.Tk()
    root.title("Gorila IA System - Motor de Video")
    root.geometry("400x200")

    label = tk.Label(root, text="Generador de Video del Gorila IA System", font=("Arial", 12))
    label.pack(pady=20)

    boton_generar = tk.Button(root, text="Generar Video", command=generar_video, font=("Arial", 12))
    boton_generar.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    iniciar_app()