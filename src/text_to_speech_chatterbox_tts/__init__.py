import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

print ("Cargando modelo...")

modelo = ChatterboxMultilingualTTS.from_pretrained(
    device="cpu"
)
texto = "Hola bienvenidos a inteligencia artifial generativa, vamos a crear audios,imagenes, texto, y si el pc aguanta videos."
print("Generando audio...")

audio = modelo.generate(
    texto,
    language_id="es",
    exaggeration=0.7,#EMOCIONi
    cfg_weight=0.4,#RITMO, VELOCIDAD DE LA VOZ
    temperature=0.8,#VARIABILIDAD
    repetition_penalty=1.2,
    min_p=0.05,
    top_p=1.0    
)
ta.save(
   "audio.wav",
   audio,
   modelo.sr
)
print("audio guardado.")
texto = "Hola bienvenidos a inteligencia artifial generativa, vamos a crear audios,imagenes, texto, y si el pc aguanta videos."
print("Generando audio...")

audio = modelo.generate(
    texto,
    language_id="es",
    exaggeration=0.7,#EMOCION
    cfg_weight=0.4,#RITMO, VELOCIDAD DE LA VOZ
    temperature=0.8,#VARIABILIDAD
    repetition_penalty=1.2,
    min_p=0.05,
    top_p=1.0    
)
ta.save(
   "audio.wav",
   audio,
   modelo.sr
)
print("audio guardado.")
