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

const showIsCopiedLink =  ref(false);
const isSkyBoxImage =  ref(false);
const isEnvImage =  ref(false);


const tab =  ref('one');
const menu =  ref(false);

// Initialize PostProcessing effects
let gridEffect: PostProcessing.GridEffect | null = null;
let sepiaEffect: PostProcessing.SepiaEffect | null = null;

function makeLink(): string {
  // return `<iframe src="http://localhost/model/${this.MAIN_MODEL_ID}?shadowIntensity=${this.shadowIntensity}&brightness=${this.brightness}&contrast=${this.contrast}&opacity=${this.opacity}&blendMode=${this.blendMode}&blockOpacity=${this.blockOpacity}&pixar=${Number(this.pixar)}&isEnvImage=${Number(this.isEnvImage)}&isSkyBoxImage=${Number(this.isSkyBoxImage)}"></iframe>`
  return `<iframe src="https://modelviewer.pl/model/${store.getters.MAIN_MODEL_ID}?grid=${store.getters.MAIN_MODEL_GRID}&sepia=${store.getters.MAIN_MODEL_SEPIA}&shadowIntensity=${store.getters.MAIN_MODEL_SEPIA}&brightness=${store.getters.MAIN_MODEL_BRIGHTNESS}&contrast=${store.getters.MAIN_MODEL_CONTRAST}&opacity=${store.getters.MAIN_MODEL_OPACITY}&blendMode=${store.getters.MAIN_MODEL_BLENDMODE}&blockOpacity=${store.getters.MAIN_MODEL_OPACITY}&pixar=${Number(store.getters.MAIN_MODEL_PIXEL)}&isEnvImage=${Number(1)}&isSkyBoxImage=${Number(1)}"></iframe>`
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
  sepiaEffect.setIntensity(store.getters.MAIN_MODEL_SEPIA);
  customComposer.queueRender()

}

function changeGrid(): void {
  if (!gridEffect) {
    console.error('GridEffect is not initialized');
    return;
  }

  gridEffect.scale = store.getters.MAIN_MODEL_GRID;

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

<template>
  <div class="btn"
  >
    <v-menu
        v-model="menu"
        :close-on-content-click="false"
        location="center"
        max-width="350"
    >
      <template v-slot:activator="{ props }">
        <p
            data-tooltip="Menu">
          <img
              height="30"
              width="30"
              v-bind="props"
              class="changePointer"
              src="../../../../public/menu.svg"
          >
        </p>
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
                      <VCheckbox label="Pixel"
                                 :model-value="store.getters.MAIN_MODEL_PIXEL"
                                 @update:modelValue="value => store.commit('MAIN_MODEL_PIXEL', value)"
                      ></VCheckbox>
                    </v-col>

                    <v-col cols="12">
                      <v-slider
                          class="wd-all"
                          :model-value="store.getters.MAIN_MODEL_BRIGHTNESS"
                          @update:modelValue="value => store.commit('MAIN_MODEL_BRIGHTNESS', value)"
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
                          :model-value="store.getters.MAIN_MODEL_OPACITY"
                          @update:modelValue="value => store.commit('MAIN_MODEL_OPACITY', value)"
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
                          :model-value="store.getters.MAIN_MODEL_CONTRAST"
                          @update:modelValue="value => store.commit('MAIN_MODEL_CONTRAST', value)"
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
                          :model-value="store.getters.MAIN_MODEL_GRID"
                          @update:modelValue="value => store.commit('MAIN_MODEL_GRID', value)"
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
                          :model-value="store.getters.MAIN_MODEL_SEPIA"
                          @update:modelValue="value => store.commit('MAIN_MODEL_SEPIA', value)"
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
                          class="wd-all"
                          :model-value="store.getters.MAIN_MODEL_SHADOW_SOFTNESS"
                          @update:modelValue="value => store.commit('MAIN_MODEL_SHADOW_SOFTNESS', value)"
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
                          :model-value="store.getters.MAIN_MODEL_SHADOW_INTENSITY"
                          @update:modelValue="value => store.commit('MAIN_MODEL_SHADOW_INTENSITY', value)"
                          label="Shadow intensity"
                          min="0"
                          max="4"
                          step="0.01"
                          color="orange"
                          thumb-label="true"></v-slider>
                    </v-col>

                    <v-col cols="12">
                      <v-select
                          :model-value="store.getters.MAIN_MODEL_BLENDMODE"
                          @update:modelValue="value => store.commit('MAIN_MODEL_BLENDMODE', value)"
                          :items="['DEFAULT', 'SKIP', 'ADD', 'DIVIDE', 'NEGATION', 'SET', 'AVERAGE', 'COLOR', 'COLOR_BURN', 'COLOR_DODGE', 'DARKEN', 'DIFFERENCE', 'DST', 'NORMAL', 'SUBTRACT']"
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
                  <VCheckbox label="Environment image" :value="isEnvImage" @change="isEnvImage = !isEnvImage"></VCheckbox>
                  <VCheckbox label="Skybox image" :value="isSkyBoxImage" @change="isSkyBoxImage = !isSkyBoxImage"></VCheckbox>
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
</template>

<style scoped>
@font-face {
  font-family: 'Lexend';
  src: url('../../../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
* {
  font-family: Lexend;
}
.viewer-container {
  width: 100vw;
  margin-top: 1%;
  justify-content: center;
  display: flex;
  position: relative;

}

.btn {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 1000;
  margin-top: 10px;
  margin-right: 10px;
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
.changePointer:hover {
  cursor: pointer;
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
  background-color: black;
  border-radius: 20px;
  height: 8px;
  width: 100%;
}

[data-tooltip] {
  position: relative;
}
[data-tooltip]::after {
  content: attr(data-tooltip);
  position: absolute;
  background: #1d1b1b;
  color: #fff;
  padding: 0.5em;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
  pointer-events: none;
  opacity: 0;
  transition-duration: 1s;
  right: 2em;
}
[data-tooltip]:hover::after {
  opacity: 1;
  right: 2em;
}
</style>