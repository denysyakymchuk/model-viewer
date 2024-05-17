<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <model-viewer  :src="this.MAIN_MODEL_IFRAME"
                   :skybox-image="this.MAIN_MODEL_IFRAME_SBI"
                   :environment-image="this.MAIN_MODEL_IFRAME_EI"
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
</template>

<script>
import '@google/model-viewer'
import '@google/model-viewer-effects'
import { mapActions, mapGetters } from "vuex";

export default {
  name: "MainView",
  data() {
    return {
      env_image: null,
      shadowIntensity: 0,
      shadowSoftness: 0,
      brightness: 0,
      contrast: 0,
      pixar: false,
      opacity: 1,
      blendMode: 'skip',
      blockOpacity: 1,
    }
  },
  computed: {
    ...mapGetters(["MAIN_MODEL_IFRAME", "MAIN_MODEL_IFRAME_SBI", "MAIN_MODEL_IFRAME_EI"])
  },
  methods: {
    ...mapActions(["GET_MAIN_MODEL_IFRAME"]),
  },
  async mounted() {
    await this.GET_MAIN_MODEL_IFRAME(this.$route.params.id)
    this.shadowIntensity = this.$route.query.shadowIntensity;
    this.shadowSoftness = this.$route.query.shadowSoftness;
    this.brightness = this.$route.query.brightness;
    this.contrast = this.$route.query.contrast;
    this.opacity = this.$route.query.opacity;
    this.blendMode = this.$route.query.blendMode;
    this.blockOpacity = this.$route.query.blockOpacity;
    this.pixar = Number(this.$route.query.pixar);
  }
}
</script>
