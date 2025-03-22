<template>
  <div class="container">
    <h2>Ajouter une image</h2>
    <input type="file" @change="onFileSelect" accept="image/*" class="file-input" />
    
    <!-- Erreur si quelque chose ne va pas -->
    <div v-if="errorMessage" class="error-message">
      <p>{{ errorMessage }}</p>
    </div>

    <!-- Prévisualisation des images -->
    <div v-if="originalImageUrl" class="image-preview">
      <div>
        <p>Image originale :</p>
        <img :src="originalImageUrl" class="preview-image" />
      </div>
      <div v-if="processedImageUrl">
        <p>Image sans arrière-plan :</p>
        <img :src="processedImageUrl" class="preview-image" />
      </div>
    </div>

    <!-- Bouton pour supprimer l'arrière-plan -->
    <button @click="removeBackground" :disabled="!originalImageUrl" class="convert-btn">
      Supprimer l'arrière-plan
    </button>

    <!-- Bouton de téléchargement après traitement -->
    <button 
      v-if="processedImageUrl" 
      @click="downloadImage" 
      class="download-btn">
      Télécharger l'image sans fond
    </button>

    <!-- Indicateur de chargement -->
    <div v-if="isLoading" class="loading-spinner">
      <div class="spinner"></div>
      <p>Chargement...</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      originalImageUrl: null,  // Stocke l'image sélectionnée
      selectedFile: null,      // Stocke le fichier sélectionné
      processedImageUrl: null, // Stocke l'image sans fond
      isLoading: false,        // Indicateur de chargement
      errorMessage: null,      // Message d'erreur si quelque chose se passe mal
    };
  },
  methods: {
    onFileSelect(event) {
      const file = event.target.files[0];
      if (!file) return;
      
      this.selectedFile = file;
      this.originalImageUrl = URL.createObjectURL(file);
      this.processedImageUrl = null; // Réinitialise l'image traitée
      this.errorMessage = null;  // Réinitialise le message d'erreur
    },
    
    async removeBackground() {
      if (!this.selectedFile) {
        console.error("Aucun fichier sélectionné !");
        return;
      }

      this.isLoading = true;  // Afficher l'indicateur de chargement

      const formData = new FormData();
      formData.append("file", this.selectedFile);

      try {
        // Appel API pour traiter l'image
        const response = await axios.post("http://localhost:8000/remove-bg/", formData, {
          responseType: "blob",
        });

        this.processedImageUrl = URL.createObjectURL(response.data);
        this.errorMessage = null; // Réinitialise l'erreur
      } catch (error) {
        console.error("Erreur de traitement :", error);
        this.errorMessage = "Une erreur est survenue lors de la suppression de l'arrière-plan.";
      } finally {
        this.isLoading = false;  // Masquer l'indicateur de chargement
      }
    },

    // Méthode pour télécharger l'image sans fond
    downloadImage() {
      if (this.processedImageUrl) {
        const a = document.createElement("a");
        a.href = this.processedImageUrl;
        a.download = "image_sans_fond.png";  // Nom du fichier de téléchargement
        a.click();
      }
    }
  }
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  padding: 20px;
  color: black;
}

.file-input {
  padding: 10px;
  border: 1px solid black;
  border-radius: 5px;
  cursor: pointer;
}

.image-preview {
  display: flex;
  gap: 20px;
  justify-content: center;
  align-items: center;
}

.preview-image {
  width: 250px;
  height: auto;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
}

.convert-btn {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}

.convert-btn:disabled {
  background-color: gray;
  cursor: not-allowed;
}

.convert-btn:hover:not(:disabled) {
  background-color: #0056b3;
}

.download-btn {
  background-color: #28a745;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}

.download-btn:hover {
  background-color: #218838;
}

.error-message {
  color: red;
  font-weight: bold;
  margin-top: 15px;
}

.loading-spinner {
  margin-top: 15px;
  text-align: center;
  color: #007bff;
  font-weight: bold;
}

.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #007bff;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
