<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <div>
      <model-viewer  :src="this.MAIN_MODEL_IFRAME"
                     :skybox-image="this.MAIN_MODEL_IFRAME_SBI"
                     :environment-image="this.MAIN_MODEL_IFRAME_EI"
                     camera-controls
                     touch-action="pan-y">


      </model-viewer>
    </div>
  </div>
</template>

<script>
import '@google/model-viewer'
import '@google/model-viewer-effects'
import { mapActions, mapGetters } from "vuex";

export default {
  name: "MainView",
  computed: {
    ...mapGetters(["MAIN_MODEL_IFRAME", "MAIN_MODEL_IFRAME_SBI", "MAIN_MODEL_IFRAME_EI"])
  },
  methods: {
    ...mapActions(["GET_MAIN_MODEL_IFRAME"]),
  },
  async mounted() {
    await this.GET_MAIN_MODEL_IFRAME(this.$route.params.id)
  }
}
</script>

<style scoped>

</style>