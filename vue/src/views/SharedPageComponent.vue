<template>
  <div>
    <model-viewer  :src="store.getters.MAIN_MODEL_IFRAME"
                   :skybox-image="isSkyBoxImage ? store.getters.MAIN_MODEL_IFRAME_SBI : ''"
                   :environment-image="isEnvImage ? store.getters.MAIN_MODEL_IFRAME_EI : ''"
                   :shadow-intensity="shadowIntensity"
                   :shadow-softness="shadowSoftness"
                   camera-controls
                   touch-action="pan-y">

      <effect-composer id="customComposer" render-mode="quality" msaa="8">

        <!--   ВСЕ ДЕЛАЕТ ПИКСЕЛЯМИ   -->
        <pixelate-effect v-if="pixar"></pixelate-effect>

        <!--   OPACITY     -->
        <color-grade-effect :contrast="contrast" saturation="-1" :opacity="opacity" :blend-mode="blendMode" :brightness="brightness"></color-grade-effect>

      </effect-composer>

    </model-viewer>
  </div>
</template>

<script setup lang="ts">
import '@google/model-viewer'
import '@google/model-viewer-effects'
import * as PostProcessing from "postprocessing";


import {onMounted, ref} from "vue";
import {useStore} from "vuex";
import {useRoute} from "vue-router";


const store = useStore();
const route = useRoute();

// Initialize PostProcessing effects
let gridEffect: PostProcessing.GridEffect | null = null;
let sepiaEffect: PostProcessing.SepiaEffect | null = null;


const  shadowIntensity = ref( 0);
const  shadowSoftness = ref( 0);
const  blockOpacity = ref( 1);
const  brightness = ref( 0);
const  contrast = ref( 0);
const  opacity = ref( 1);
const  grid = ref( 0);
const  sepia = ref( 0);
const  blendMode = ref( 'skip');
const  pixar = ref( 0);
const  isSkyBoxImage = ref( 0);
// const  env_image = ref( 0);
const isEnvImage = ref( 0);

onMounted(async () => {
  await store.dispatch('GET_MAIN_MODEL_IFRAME', route.params.id)
  shadowIntensity.value = Number(route.query.shadowIntensity);
  shadowSoftness.value = Number(route.query.shadowSoftness);
  brightness.value = Number(route.query.brightness);
  contrast.value = Number(route.query.contrast);
  opacity.value = Number(route.query.opacity);
  grid.value = Number(route.query.grid);
  sepia.value = Number(route.query.sepia);
  blendMode.value = String(route.query.blendMode);
  blockOpacity.value = Number(route.query.blockOpacity);
  pixar.value = Number(route.query.pixar);
  isEnvImage.value = Number(route.query.isEnvImage);
  isSkyBoxImage.value = Number(route.query.isSkyBoxImage);

  const customComposer = document.querySelector('effect-composer#customComposer') as any;
  if (!customComposer) {
    console.error('EffectComposer not found');
    return;
  }

  gridEffect = new PostProcessing.GridEffect({scale: grid.value});
  sepiaEffect = new PostProcessing.SepiaEffect();
  sepiaEffect.intensity = sepia.value;

  const noisePass = new PostProcessing.EffectPass(undefined, gridEffect, sepiaEffect);
  customComposer.addPass(noisePass);
})

</script>
