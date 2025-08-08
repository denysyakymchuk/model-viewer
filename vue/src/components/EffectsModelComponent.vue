<script setup lang="ts">
import '@google/model-viewer';
import '@google/model-viewer-effects';

import {useStore} from "vuex";

const store = useStore();


function changeSepia(value: number): void {
  store.commit('MAIN_MODEL_SEPIA_EFFECT', value);

  const customComposer = document.querySelector('effect-composer#customComposer') as any;
  if (customComposer) {
    customComposer.queueRender();
  }
}

function changeGrid(value: number): void {
  store.commit('MAIN_MODEL_GRID_EFFECT', value);

  const customComposer = document.querySelector('effect-composer#customComposer') as any;
  if (customComposer) {
    customComposer.queueRender();
  }
}
</script>

<template>
  <div id="filterFrame">
    <v-row>
    <!--   PIXEL   -->
      <v-col cols="12">
        <VCheckbox
            label="Pixel"
            class="color-white"
                   :model-value="store.getters.MAIN_MODEL_PIXEL"
                   @update:modelValue="value => store.commit('MAIN_MODEL_PIXEL', value)"
        ></VCheckbox>
      </v-col>
      <!--   PIXEL   -->

      <!--   BRIGHTNESS…   -->
      <v-col cols="12">
        <v-slider
            class="wd-all"
            :model-value="store.getters.MAIN_MODEL_BRIGHTNESS"
            @update:modelValue="value => store.commit('MAIN_MODEL_BRIGHTNESS', value)"
            label="Brightness"
            color="orange"
            min="0"
            max="1"
            step="0.01"
            thumb-label="true"></v-slider>
      </v-col>
      <!--   BRIGHTNESS   -->

      <!--   OPACITY   -->
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
      <!--   OPACITY   -->

      <!--   CONTRAST   -->
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
      <!--   CONTRAST   -->

      <!--   GRID   -->
      <v-col cols="12">
      <v-slider
          class="wd-all"
          :model-value="store.getters.MAIN_MODEL_GRID"
          @update:modelValue="value => { store.commit('MAIN_MODEL_GRID', value); changeGrid(value); }"
          label="Grid"
          color="orange"
          min="0"
          max="2"
          step="0.01"
          thumb-label="true"
      />
      </v-col>
      <!--   GRID   -->

      <!--   SEPIA   -->
      <v-col cols="12">
      <v-slider
          class="wd-all"
          :model-value="store.getters.MAIN_MODEL_SEPIA"
          @update:modelValue="value => { store.commit('MAIN_MODEL_SEPIA', value); changeSepia(value); }"
          label="Sepia"
          color="orange"
          min="0"
          max="5"
          step="0.01"
          thumb-label="true"
      />
      </v-col>
      <!--   SEPIA   -->

      <!--   SOFTNESS   -->
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
      <!--   SOFTNESS   -->

      <!--   INTENSITY   -->
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
      <!--   INTENSITY   -->

      <!--   BLENDMODE   -->
      <v-col cols="12">
        <v-select
            :model-value="store.getters.MAIN_MODEL_BLENDMODE"
            @update:modelValue="value => store.commit('MAIN_MODEL_BLENDMODE', value)"
            :items="['DEFAULT', 'SKIP', 'ADD', 'DIVIDE', 'NEGATION', 'SET', 'AVERAGE', 'COLOR', 'COLOR_BURN', 'COLOR_DODGE', 'DARKEN', 'DIFFERENCE', 'DST', 'NORMAL', 'SUBTRACT']"
            variant="primary"
        ></v-select>
      </v-col>
      <!--   BLENDMODE   -->

    </v-row>
  </div>
</template>

<style scoped>
@font-face {
  font-family: 'Lexend';
  src: url('../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
* {
  font-family: Lexend;
  color: white;
}

.wd-all {
  width: 270px;
}
.color-white {
  color: white;
}

.v-row {
  display: flex;
  flex-wrap: wrap;
  flex: 1 1 auto;
  margin: 0;
}
</style>