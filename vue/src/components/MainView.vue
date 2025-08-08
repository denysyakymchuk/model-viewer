<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <div class="viewer-container">
      <model-viewer  :src="store.getters.MAIN_MODEL"
                     :skybox-image="store.getters.MAIN_SKY_BOX_IMAGE"
                     :environment-image="store.getters.MAIN_ENV_IMAGE"
                     :shadow-intensity="store.getters.MAIN_MODEL_SHADOW_INTENSITY"
                     :shadow-softness="store.getters.MAIN_MODEL_SHADOW_SOFTNESS"
                     camera-controls
                     touch-action="pan-y"
                     :id="store.getters.MAIN_MODEL"
                      >

        <effect-composer id="customComposer" render-mode="quality" msaa="8">

          <!--   ВСЕ ДЕЛАЕТ ПИКСЕЛЯМИ   -->
          <pixelate-effect v-if="store.getters.MAIN_MODEL_PIXEL"></pixelate-effect>

          <!--   OPACITY     -->
          <color-grade-effect :contrast="store.getters.MAIN_MODEL_CONTRAST" :opacity="store.getters.MAIN_MODEL_OPACITY" :blend-mode="store.getters.MAIN_MODEL_BLENDMODE" :brightness="store.getters.MAIN_MODEL_BRIGHTNESS"></color-grade-effect>

        </effect-composer>

      </model-viewer>
    </div>
  </div>
</template>

<script setup lang="ts">
import '@google/model-viewer';
import '@google/model-viewer-effects';
import {useStore} from "vuex";
import {onMounted} from "vue";
import {EffectPass} from "postprocessing";

const store = useStore();

onMounted(() => {
  const customComposer = document.querySelector('effect-composer#customComposer') as any;
  if (!customComposer) {
    console.error('EffectComposer not found');
    return;
  }
  const noisePass = new EffectPass(undefined, store.getters.MAIN_MODEL_SEPIA_EFFECT,  store.getters.MAIN_MODEL_GRID_EFFECT);
  customComposer.addPass(noisePass);
});
</script>

<style scoped>
.viewer-container {
  width: 100%;
  margin-top: 1%;
  justify-content: center;
}
@font-face {
  font-family: 'Lexend';
  src: url('../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
* {
  font-family: Lexend;
}

model-viewer {
  width: 100%;
  height: 70vh;
  aspect-ratio: 16/9;
  border-radius: 30px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 0;
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
@media only screen and (max-width: 1000px) {
  .viewer-container {
    width: 100vw;

  }

}
</style>