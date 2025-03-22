<template>
  <div class="app-container">
    <h1>Suppression d’arrière-plan</h1>
    <ImageUploader />
  </div>
</template>

<script>
import ImageUploader from "./components/ImageUploader.vue";

export default {
  components: {
    ImageUploader,
  },
};
</script>

<style scoped>
/* Appliquer le fond blanc à toute la page */
body, html {
  margin: 0;
  padding: 0;
  background-color: #ffffff; /* Fond blanc pour toute la page */
  color: #333;
  height: 100%;
}

/* Style pour centrer le contenu de la page */
.app-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #ffffff; /* Fond blanc */
  padding: 40px;
  border-radius: 10px;
  width: 100%;
  max-width: 600px;
  transition: all 0.3s ease;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1); /* Ombre subtile pour l'effet de profondeur */
}

.app-container:hover {
  box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.1); /* Ombre plus forte au survol */
}

/* Style du titre */
h1 {
  font-size: 32px;
  font-weight: 600;
  color: #333;
  margin-bottom: 40px;
  letter-spacing: 1px;
  text-transform: uppercase;
}

/* Style global du composant ImageUploader */
.image-upload-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  gap: 20px;
}

/* Style des boutons dans le composant ImageUploader */
.convert-btn, .download-btn {
  background-color: #007bff;
  color: white;
  padding: 12px 25px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.convert-btn:hover, .download-btn:hover {
  background-color: #0056b3;
  transform: translateY(-2px);
}

.convert-btn:disabled, .download-btn:disabled {
  background-color: #ddd;
  cursor: not-allowed;
}

/* Pour les images de prévisualisation */
.preview-image {
  max-width: 300px;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* S'assurer que tout est centré sur la page */
html, body {
  height: 100%;
  margin: 0;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
