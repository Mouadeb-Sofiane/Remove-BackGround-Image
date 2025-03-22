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
body, html {
  margin: 0;
  padding: 0;
  background-color: #ffffff; 
  color: #333;
  height: 100%;
}

.app-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #ffffff; 
  padding: 40px;
  border-radius: 10px;
  width: 100%;
  max-width: 600px;
  transition: all 0.3s ease;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1); 
}

.app-container:hover {
  box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.1); 
}

h1 {
  font-size: 32px;
  font-weight: 600;
  color: #333;
  margin-bottom: 40px;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.image-upload-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  gap: 20px;
}

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

.preview-image {
  max-width: 300px;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
