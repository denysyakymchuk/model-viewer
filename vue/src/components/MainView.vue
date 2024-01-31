<template>
  <div class="container">
    <div class="model-viewer-container">
      <model-viewer  :src="this.MAIN_MODEL"
                     :shadow-intensity="this.shadowIntensity"
                     :shadow-softness="this.shadowSoftness"
                     camera-controls
                     touch-action="pan-y">

      <effect-composer render-mode="quality" msaa="8">

        <!--   ВСЕ ДЕЛАЕТ ПИКСЕЛЯМИ   -->
        <pixelate-effect v-if="pixar"></pixelate-effect>

        <!--   OPACITY     -->
          <color-grade-effect :contrast="this.contrast" saturation="-1" :opacity="this.opacity" :blend-mode="this.blendMode"></color-grade-effect>

        </effect-composer>

      </model-viewer>
    </div>

      <!--  BOCZNA PANEL   -->
      <div class="sidePanelSetting">
        <fieldset>
          <legend>Pixel</legend>
            <label>Pikselem<input type="checkbox" v-model="pixar"/></label>
        </fieldset>

            <fieldset>
              <legend>Opacity</legend>
              <label>Opacity<input  v-model="this.opacity" type="range" min="0" max="1" step="0.01"></label>
            </fieldset>

            <fieldset>
              <legend>Contrast</legend>
                  <label>Contrast<input  v-model="this.contrast" type="range" min="0" max="1" step="0.01"></label>
            </fieldset>

              <fieldset>
                <legend>Blend Mode:</legend>
                <div>
                  <label for="blend-mode">Blend Mode:</label>
                  <select id="blend-mode" v-model="this.blendMode">
                    <option value="default">Default</option>
                    <option value="skip">Skip</option>
                    <option value="add">Add</option>
                    <option value="subtract">Subtract</option>
                    <option value="divide">Divide</option>
                    <option value="negation">Negation</option>
                  </select>
                </div>
              </fieldset>


        <fieldset>
          <legend>Shadow intensity</legend>
          <label>Shadow intensity<input  v-model="this.shadowIntensity" type="range" min="0" max="2" step="0.01"></label>
        </fieldset>

        <fieldset>
          <legend>Shadow softness</legend>
          <label>Shadow softness<input  v-model="this.shadowSoftness" type="range" min="0" max="1" step="0.01"></label>
        </fieldset>

      </div>
    <!--  BOCZNA PANEL   -->
  </div>
</template>

<script>
import '@google/model-viewer'
import '@google/model-viewer-effects'
import { mapActions, mapGetters } from "vuex";


export default {
  name: "MainView",
  data() {
    return {
      pixar: false,
      contrast: 0,
      opacity: 1,
      shadowIntensity: 0,
      shadowSoftness: 0,
      blendMode: 'skip',
    }
  },
  methods: {
    ...mapActions(["GET_MAIN_MODEL"]),
  },
  computed: {
    ...mapGetters(["MAIN_MODEL"]),
  },
}
</script>

<style scoped>
@media only screen and (max-width: 600px) {
  .model-viewer-container {
    margin-left: auto;
    margin-right: auto;
    width: 80%;
    height: auto;
  }
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

model-viewer {
  margin-bottom: 60%;
  max-width: 600px;
  width: 100%;
  height: 450px;
  aspect-ratio: 16/9;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-image: url('../assets/bg.png'); /* Consider using a higher resolution background */
  background-size: cover;
}

.sidePanelSetting {
  background-color: #2C2C2C; /* Slightly lighter for better contrast */
  color: white;
  font-family: "Cantarell Light", sans-serif;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  position: fixed;
  right: 20px;
  top: 20px;
  width: 270px;
}

input[type="range"] {
  width: 100%;
}

/* Additional styles */
button, select {
  background-color: #333;
  color: white;
  border: none;
  padding: 10px 15px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
}

button:hover, select:hover {
  background-color: #444;
}
fieldset {
  padding: 2px;
  padding-left: 5px;
}
</style>