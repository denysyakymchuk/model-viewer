<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <div :id="this.MAIN_MODEL">
      <model-viewer  :src="this.MAIN_MODEL"
                     :skybox-image="this.MAIN_SKY_BOX_IMAGE"
                     :environment-image="this.MAIN_ENV_IMAGE"
                     :shadow-intensity="this.shadowIntensity"
                     :shadow-softness="this.shadowSoftness"
                     camera-controls
                     touch-action="pan-y">

        <effect-composer render-mode="quality" msaa="8">

          <!--   ВСЕ ДЕЛАЕТ ПИКСЕЛЯМИ   -->
          <pixelate-effect v-if="pixar"></pixelate-effect>

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
            max-width="350"
        >
          <template v-slot:activator="{ props }">
            <v-btn
                color="indigo"
                v-bind="props"
            >
              Filters
            </v-btn>
          </template>

          <v-card
              min-width="300"
              color="black"
              :style="{ opacity: this.blockOpacity }"
              style="border-radius: 20px;"
          >
            <v-card>
              <v-tabs
                  align-tabs="left"
                  v-model="tab"
                  bg-color="black"
              >
                <a  @click="this.menu=false" style="cursor: pointer"><v-tab disabled style="opacity: 1"><v-icon color="white" icon="mdi-close" size="x-large"></v-icon></v-tab></a>
                <v-tab value="one">Filters</v-tab>
                <v-tab value="three">Get code</v-tab>
              </v-tabs>

              <v-card-text
                  style="background-color: #0e0e0e">
                <v-window v-model="tab">
                  <v-window-item
                      id="windowFilter"
                      value="one">
                    <div id="filterFrame">
                      <v-row class="color-white">
                        <v-col cols="12">
                          <v-checkbox label="Pixel" v-model="this.pixar"></v-checkbox>
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
                    </div>
                  </v-window-item>

                  <v-window-item
                      value="three"
                      class="color-white"
                      style="text-align: justify"
                  >
                    <div class="d-flex">
                      <v-checkbox label="Environment image" v-model="this.isEnvImage"></v-checkbox>
                      <v-checkbox label="Skybox image" v-model="this.isSkyBoxImage"></v-checkbox>
                    </div>
                    <v-alert
                        class="mb-5"
                        text="The code was copied!"
                        type="success"
                        v-if="this.showIsCopiedLink"
                    >
                    </v-alert>
                    <v-textarea
                        label=""
                        prepend-icon="mdi-content-copy"
                        :value="makeLink()"
                        variant="solo-filled"
                        @click:prepend="this.copyLink()"
                    ></v-textarea>
                  </v-window-item>
                </v-window>
              </v-card-text>
            </v-card>
          </v-card>
        </v-menu>
      </div>
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
      shadowIntensity: 0,
      shadowSoftness: 0,
      isSkyBoxImage: 0,
      blockOpacity: 1,
      isEnvImage: 0,
      brightness: 0,
      activeTab: 1,
      contrast: 0,
      opacity: 1,
      pixar: 0,
      showIsCopiedLink: false,
      message: false,
      menu: false,
      hints: true,
      fav: true,
      tab: null,
      blendMode: 'skip',
    }
  },
  methods: {
    ...mapActions(["GET_MAIN_MODEL"]),
    makeLink() {
      // return `<!--<iframe src="http://localhost/model/${this.MAIN_MODEL_ID}?shadowIntensity=${this.shadowIntensity}&brightness=${this.brightness}&contrast=${this.contrast}&opacity=${this.opacity}&blendMode=${this.blendMode}&blockOpacity=${this.blockOpacity}&pixar=${Number(this.pixar)}&isEnvImage=${Number(this.isEnvImage)}&isSkyBoxImage=${Number(this.isSkyBoxImage)}"></iframe>-->`
      return `<iframe src="http://modelviewer/model/${this.MAIN_MODEL_ID}?shadowIntensity=${this.shadowIntensity}&brightness=${this.brightness}&contrast=${this.contrast}&opacity=${this.opacity}&blendMode=${this.blendMode}&blockOpacity=${this.blockOpacity}&pixar=${Number(this.pixar)}&isEnvImage=${Number(this.isEnvImage)}&isSkyBoxImage=${Number(this.isSkyBoxImage)}"></iframe>`
    },
    copyLink() {
      navigator.clipboard.writeText(this.makeLink());
      this.showIsCopiedLink = true;
    },
  },
  computed: {
    ...mapGetters(["MAIN_MODEL", "MAIN_SKY_BOX_IMAGE", "MAIN_ENV_IMAGE", "MAIN_MODEL_ID"]),
  },
}
</script>

<style scoped>
.btn {
  margin-top: 1%;
  margin-right: 2%;
  position: absolute;
  z-index: 1000;
  top: 0;
  right: 0;
}
model-viewer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  aspect-ratio: 16/9;
  border-radius: 0;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 0;
}

.wd-all {
  width: 270px;
}

.v-row {
  display: flex;
  flex-wrap: wrap;
  flex: 1 1 auto;
  margin: 0;
}
.color-white {
  color: white
}
</style>