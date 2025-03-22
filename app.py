from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware  # Importer CORSMiddleware
from rembg import remove
from PIL import Image
import io

app = FastAPI()

# Ajouter le middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permet les requêtes venant de localhost:5173
    allow_credentials=True,
    allow_methods=["*"],  # Permet toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Permet tous les en-têtes
)

@app.post("/remove-bg/")
async def remove_bg(file: UploadFile = File(...)):
    print(f"Fichier reçu : {file.filename}")  # ➜ Ajoute ce log
    try:
        image = Image.open(io.BytesIO(await file.read()))
        output = remove(image)
        img_byte_arr = io.BytesIO()
        output.save(img_byte_arr, format='PNG')
        print("Image traitée avec succès")  # ➜ Log après traitement
        return Response(content=img_byte_arr.getvalue(), media_type="image/png")
    except Exception as e:
        print(f"Erreur : {e}")  # ➜ Affiche l’erreur si ça plante

# Démarrer l'API
# uvicorn app:app --reload
