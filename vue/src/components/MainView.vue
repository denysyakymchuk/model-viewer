<template>
  <div>
    <div class="model-viewer-container">
      <model-viewer  :src="this.MAIN_MODEL"
                     :shadow-intensity="this.shadowIntensity"
                     :shadow-softness="this.shadowSoftness"
                     camera-controls
                     touch-action="pan-y">

      <effect-composer  render-mode="quality" msaa="8">

        <!--   ВСЕ ДЕЛАЕТ ПИКСЕЛЯМИ   -->
        <pixelate-effect v-if="pixar"></pixelate-effect>

<!--        <outline-effect color="red"></outline-effect>-->

        <!--   OPACITY     -->
          <color-grade-effect :contrast="this.contrast" saturation="-1" :opacity="this.opacity" :blend-mode="this.blendMode" :brightness="this.brightness"></color-grade-effect>

        </effect-composer>

      </model-viewer>
    </div>

      <!--  BOCZNA PANEL   -->
      <div>
        <div class="btn"
        >
          <v-menu
              v-model="menu"
              :close-on-content-click="false"
              location="center"
              max-width="300"
          >
            <template v-slot:activator="{ props }">
              <v-btn
                  color="indigo"
                  v-bind="props"
              >
                Filters
              </v-btn>
            </template>

            <v-card min-width="300" color="black">
                <v-row>
                  <v-col cols="12">
                    <v-checkbox label="Pixelem" v-model="this.pixar"></v-checkbox>
                  </v-col>

                  <v-col cols="12">
                    <v-slider
                        class="wd-all"
                        v-model="this.brightness"
                        label="Brightness"
                        color="orange"
                        min="-1"
                        max="1"
                        step="0.01"
                        thumb-label="true"></v-slider>
                  </v-col>

                  <v-col cols="12">
                    <v-slider
                        class="wd-all"
                        v-model="this.opacity"
                        label="Opacity"
                        color="orange"
                        min="0"
                        max="1"
                        step="0.01"
                        thumb-label="true"></v-slider>
                  </v-col>

                  <v-col cols="12">
                    <v-slider
                        class="wd-all"
                        v-model="this.contrast"
                        label="Contrast"
                        color="orange"
                        min="0"
                        max="1"
                        step="0.01"
                        thumb-label="true"></v-slider>
                  </v-col>

                  <v-col cols="12">
                    <v-slider
                        v-model="this.shadowSoftness"
                        class="wd-all"
                        label="Shadow softness"
                        color="orange"
                        min="0"
                        max="1"
                        step="0.01"
                        thumb-label="true"></v-slider>
                  </v-col>

                  <v-col cols="12">
                    <v-slider
                        class="wd-all"
                        v-model="this.shadowIntensity"
                        label="Shadow intensity"
                        min="0"
                        max="4"
                        step="0.01"
                        color="orange"
                        thumb-label="true"></v-slider>
                  </v-col>

                  <v-col cols="12">
                    <v-select
                        v-model="this.blendMode"
                        :items="['Default', 'Skip', 'Add', 'Subtract', 'Divide', 'Negation']"
                        variant="primary"
                    ></v-select>
                  </v-col>

                </v-row>
            </v-card>
          </v-menu>
        </div>
      </div>
    <!--  BOCZNA PANEL   -->
  </div>
</template>

<script>
import '@google/model-viewer';
import '@google/model-viewer-effects';
import { mapActions, mapGetters } from "vuex";


export default {
  name: "MainView",
  data() {
    return {
      shadowIntensity: 0,
      shadowSoftness: 0,
      brightness: 0,
      contrast: 0,
      opacity: 0,
      grid: 0,
      blendMode: 'skip',
      message: false,
      pixar: false,
      menu: false,
      hints: true,
      fav: true,
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
@media only screen and (max-width: 672px) {
  model-viewer {
    margin-top: 10%;
    width: 100%; /* Full width of its container */
    height: 100%; /* Full height of its container */
    max-width: none; /* Overrides any max-width set previously */
    aspect-ratio: unset; /* If aspect-ratio is set, unset it for this viewport size */
    position: relative; /* Position set to relative */
  }
}
.btn {
  margin-top: 1%;
  margin-right: 2%;
  position: fixed;
  top: 0;
  right: 0;
}
model-viewer {
  margin-bottom: 60%;
  max-width: 600px;
  width: 100%;
  height: 450px;
  aspect-ratio: 16/9;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-image: url('../assets/bg.png');
  background-size: cover;
}
.wd-all {
  width: 270px;
}

</style>