# 🦍 Gorila IA System - Video Generator

Generador de videos promocionales con voz de IA usando ElevenLabs API y MoviePy.

## 📋 Requisitos

- Python 3.8+
- API Key de [ElevenLabs](https://elevenlabs.io/)
- Un archivo de video base (MP4)

## 🚀 Inicio rápido

### 1. Clonar el repositorio

```bash
git clone https://github.com/mglrte1986/my-python-new-proyect-1.git
cd my-python-new-proyect-1
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar API Key

**Linux/macOS:**
```bash
export ELEVENLABS_API_KEY="tu-api-key-aqui"
```

**Windows (PowerShell):**
```powershell
$env:ELEVENLABS_API_KEY="tu-api-key-aqui"
```

**Windows (Permanente):**
```bash
setx ELEVENLABS_API_KEY "tu-api-key-aqui"
```

O crear `.env`:
```bash
cp .env.example .env
# Editar .env y agregar tu API key
```

### 4. Crear carpeta de assets

```bash
mkdir assets
```

Coloca tu video base en `assets/fondo_playa.mp4`

### 5. Actualizar configuración

Editar `config_gorila.json`:

```json
{
  "api_key": "TU_API_KEY_AQUI",
  "voice_id": "TU_VOICE_ID_AQUI",
  "video_base": "assets/fondo_playa.mp4",
  "texto": "Tu texto aquí",
  "titulo": "Tu título",
  "salida": "gorila_promocional.mp4"
}
```

## ▶️ Ejecutar

```bash
python main.py
```

Se abrirá una ventana GUI con un botón para generar el video.

## 📁 Estructura

```
.
├── main.py                      # Script principal
├── config_gorila.json           # Configuración
├── requirements.txt             # Dependencias
├── .env.example                 # Variables de entorno
├── .gitignore                   # Archivos a ignorar
├── README.md                    # Este archivo
└── assets/
    └── fondo_playa.mp4          # Video base (agregar)
```

## 🔑 Obtener Voice ID

1. Ir a [ElevenLabs](https://elevenlabs.io/)
2. Inicia sesión en tu cuenta
3. Ve a Voice Lab
4. Selecciona una voz
5. Copia el ID de voz

## ⚙️ Configuración de ElevenLabs

```json
{
  "stability": 0.45,           // Consistencia (0-1)
  "similarity_boost": 0.85,    // Similitud (0-1)
  "style": "épico",            // Estilo de voz
  "use_speaker_boost": true    // Mejorar calidad
}
```

## 🎬 Opciones de video

- **Codec**: libx264 (H.264)
- **Audio**: AAC
- **Texto**: Arial-Bold, 70px, blanco, abajo
- **Duración**: Igual a la del video base

## 🔒 Seguridad

- **NUNCA** hagas commit de tu API key
- Usa `.env` para credenciales locales
- El archivo `.env` está en `.gitignore`

## 📞 Solución de problemas

### Error: "No se encontró config_gorila.json"
- Verifica que el archivo existe en el mismo directorio

### Error: "Debes configurar ELEVENLABS_API_KEY"
```bash
export ELEVENLABS_API_KEY="tu-api-key"
```

### Error: "Video no encontrado"
- Crea la carpeta `assets/`
- Coloca tu video MP4 en `assets/fondo_playa.mp4`
- Verifica la ruta en `config_gorila.json`

---

**Hecho con ❤️ por mglrte1986**  
**🦍 Gorila IA System**