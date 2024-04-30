<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <div>
      <model-viewer  :src="this.model"
                     :skybox-image="this.MAIN_SKY_BOX_IMAGE"
                     :environment-image="this.MAIN_ENV_IMAGE"
                     camera-controls
                     touch-action="pan-y">


      </model-viewer>
    </div>
  </div>
</template>

<script>
import '@google/model-viewer'
import '@google/model-viewer-effects'
import { mapActions } from "vuex";


export default {
  name: "MainView",
  data() {
    return {
      model: null,
    }
  },
  methods: {
    ...mapActions(["GET_MAIN_MODEL_REQUEST"]),
  },
  async mounted() {
    this.model = await this.GET_MAIN_MODEL_REQUEST(this.$route.params.id)
  }
}
</script>

<style scoped>

</style>