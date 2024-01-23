<template>
  <div>
    <div>
      <model-viewer  :src="this.MAIN_MODEL" shadow-intensity="1" camera-controls touch-action="pan-y">
        <!--   ВСЕ ДЕЛАЕТ ПИКСЕЛЯМИ   -->
      <effect-composer v-if="pixar">
        <pixelate-effect></pixelate-effect>
      </effect-composer>
        <!--   ВСЕ ДЕЛАЕТ ПИКСЕЛЯМИ   -->

        <!--   OPACITY     -->
        <effect-composer render-mode="quality" msaa="8">
          <color-grade-effect :contrast="this.contrast" saturation="-1" :opacity="this.opacity" :blend-mode="this.blendMode"></color-grade-effect>
        </effect-composer>
        <!--   OPACITY     -->

        <!--   COLOR GRADING     -->
<!--        <effect-composer render-mode="quality" msaa="8">-->
<!--          <bloom-effect></bloom-effect>-->
<!--          <color-grade-effect></color-grade-effect>-->
<!--        </effect-composer>-->
        <!--   COLOR GRADING     -->

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
              <div class="controls">
                <label>Opacity<input  v-model="this.opacity" type="range" min="0" max="1" step="0.01"></label>
                <label>Contrast<input  v-model="this.contrast" type="range" min="0" max="1" step="0.01"></label>


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
      blendMode: 'default',

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
model-viewer {
  margin-left: 50%;
  margin-top: 10%;
  width: 300px;
  height: 300px;
  transform: translate(-50%, -50%);
}
.sidePanelSetting {
  position: absolute;
  right: 20px; /* або будь-яке інше значення, щоб змістити вправо */
  top: 20px;
}
</style>