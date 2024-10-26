<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <div class="viewer-container">
      <model-viewer  :src="store.getters.MAIN_MODEL"
                     :skybox-image="store.getters.MAIN_SKY_BOX_IMAGE"
                     :environment-image="store.getters.MAIN_ENV_IMAGE"
                     :shadow-intensity="shadowIntensity"
                     :shadow-softness="shadowSoftness"
                     camera-controls
                     touch-action="pan-y"
                     :id="store.getters.MAIN_MODEL"
                      >

        <effect-composer id="customComposer" render-mode="quality" msaa="8">

          <!--   ВСЕ ДЕЛАЕТ ПИКСЕЛЯМИ   -->
          <pixelate-effect v-if="pixar"></pixelate-effect>

          <!--   OPACITY     -->
          <color-grade-effect :contrast="contrast" saturation="-1" :opacity="opacity" :blend-mode="blendMode" :brightness="brightness"></color-grade-effect>

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
              :style="{ opacity: blockOpacity }"
              style="border-radius: 20px;"
          >
            <v-card>
              <v-tabs
                  align-tabs="left"
                  v-model="tab"
                  bg-color="black"
              >
                <a  @click="menu=false"
                    style="cursor: pointer;
                     width: 70px"
                >
                  <v-tab
                      disabled
                      style="opacity: 1"
                  >
                    <v-icon color="white"
                            size="x-large"
                    >
                      mdi-close
                    </v-icon>
                  </v-tab>
                </a>
                <v-tab value="one">Filters</v-tab>
                <v-tab value="three">Get code</v-tab>
                <a  style="cursor: pointer;
                    width: 30px"
                    @click="goToLogin()"
                >
                  <v-tab style="opacity: 1"
                  >
                    <v-icon color="white" size="x-large">
                      mdi-login
                    </v-icon>

                  </v-tab>
                </a>
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
                          <VCheckbox label="Pixel" v-model="pixar"></VCheckbox>
                        </v-col>

                        <v-col cols="12">
                          <v-slider
                              class="wd-all"
                              v-model="brightness"
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
                              v-model="opacity"
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
                              v-model="contrast"
                              label="Contrast"
                              color="orange"
                              min="0"
                              max="1"
                              step="0.01"
                              thumb-label="true"></v-slider>
                        </v-col>

                        <v-col cols="12">
                          <v-slider
                              class="wd-all"
                              v-model="grid"
                              :update="changeGrid()"
                              label="Grid"
                              color="orange"
                              min="0"
                              max="2"
                              step="0.01"
                              thumb-label="true"></v-slider>
                        </v-col>

                        <v-col cols="12">
                          <v-slider
                              class="wd-all"
                              v-model="sepia"
                              :update="changeSepia()"
                              label="Sepia"
                              color="orange"
                              min="0"
                              max="5"
                              step="0.01"
                              thumb-label="true"></v-slider>
                        </v-col>

                        <v-col cols="12">
                          <v-slider
                              v-model="shadowSoftness"
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
                              v-model="shadowIntensity"
                              label="Shadow intensity"
                              min="0"
                              max="4"
                              step="0.01"
                              color="orange"
                              thumb-label="true"></v-slider>
                        </v-col>

                        <v-col cols="12">
                          <v-select
                              v-model="blendMode"
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
                      <VCheckbox label="Environment image" v-model="isEnvImage"></VCheckbox>
                      <VCheckbox label="Skybox image" v-model="isSkyBoxImage"></VCheckbox>
                    </div>
                    <v-alert
                        class="mb-5"
                        text="The code was copied!"
                        type="success"
                        v-if="showIsCopiedLink"
                    >
                    </v-alert>
                    <v-textarea
                        label=""
                        prepend-icon="mdi-content-copy"
                        :value="makeLink()"
                        variant="solo-filled"
                        @click:prepend="copyLink()"
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

<script setup lang="ts">
import '@google/model-viewer';
import '@google/model-viewer-effects';
import { VCheckbox } from 'vuetify/components';


import {onMounted, ref} from "vue";
import {useStore} from "vuex";
import {useRouter} from "vue-router";
import * as PostProcessing from "postprocessing";


const store = useStore();
const router = useRouter();

const shadowIntensity =  ref(0);
const shadowSoftness =  ref(0);
const isSkyBoxImage =  ref(0);
const isEnvImage =  ref(0);
const brightness =  ref(0);
const contrast =  ref(0);
const opacity =  ref(1);
const pixar =  ref(0);
const grid =  ref(0);
const sepia =  ref(0);
const showIsCopiedLink =  ref(false);
const menu =  ref(false);
const tab =  ref('one');
const blendMode =  ref('skip');

// Initialize PostProcessing effects
let gridEffect: PostProcessing.GridEffect | null = null;
let sepiaEffect: PostProcessing.SepiaEffect | null = null;

function makeLink(): string {
  // return `<iframe src="http://localhost/model/${this.MAIN_MODEL_ID}?shadowIntensity=${this.shadowIntensity}&brightness=${this.brightness}&contrast=${this.contrast}&opacity=${this.opacity}&blendMode=${this.blendMode}&blockOpacity=${this.blockOpacity}&pixar=${Number(this.pixar)}&isEnvImage=${Number(this.isEnvImage)}&isSkyBoxImage=${Number(this.isSkyBoxImage)}"></iframe>`
  return `<iframe src="https://modelviewer.pl/model/${store.getters.MAIN_MODEL_ID}?grid=${grid.value}&sepia=${sepia.value}&shadowIntensity=${shadowIntensity.value}&brightness=${brightness.value}&contrast=${contrast.value}&opacity=${opacity.value}&blendMode=${blendMode.value}&blockOpacity=${opacity.value}&pixar=${Number(pixar)}&isEnvImage=${Number(isEnvImage.value)}&isSkyBoxImage=${Number(isSkyBoxImage.value)}"></iframe>`
}
function copyLink(): void {
  navigator.clipboard.writeText(makeLink());
  showIsCopiedLink.value = true;
}
function goToLogin(): void {
  router.push({ name: "login" });
}

function changeSepia(): void {
  const customComposer = document.querySelector('effect-composer#customComposer') as any;
  sepiaEffect.setIntensity(sepia.value)
  customComposer.queueRender()

}

function changeGrid(): void {
  if (!gridEffect) {
    console.error('GridEffect is not initialized');
    return;
  }

  gridEffect.scale = grid.value;

  const customComposer = document.querySelector('effect-composer#customComposer') as any;
  if (!customComposer) {
    console.error('EffectComposer not found');
    return;
  }

  customComposer.queueRender();
}

// Setup PostProcessing on mount
onMounted(() => {
  const customComposer = document.querySelector('effect-composer#customComposer') as any;
  if (!customComposer) {
    console.error('EffectComposer not found');
    return;
  }

  gridEffect = new PostProcessing.GridEffect({scale: 0});
  sepiaEffect = new PostProcessing.SepiaEffect();
  sepiaEffect.intensity = 0;
  const noisePass = new PostProcessing.EffectPass(undefined, gridEffect, sepiaEffect);
  customComposer.addPass(noisePass);
});
</script>

<style scoped>
@font-face {
  font-family: 'Lexend';
  src: url('../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
* {
  font-family: Lexend;
}
.viewer-container {
  height: 100vh;
  width: 100vw;
  margin-top: 1%;
  justify-content: center;
  display: flex;
  position: relative;

}

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
  width: 95vw;
  height: 70vh;
  aspect-ratio: 16/9;
  border-radius: 30px;
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
model-viewer::part(default-progress-bar) {
  background-color: black; /* Change background color */
  border-radius: 20px;
  height: 8px;
  width: 100%;
}
</style>