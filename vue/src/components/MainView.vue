<template>
  <div style="display: flex">
    <div>
      <model-viewer id="blendViewer"  :src="this.MAIN_MODEL" shadow-intensity="1" camera-controls touch-action="pan-y">
        <!--   ВСЕ ДЕЛАЕТ ПИКСЕЛЯМИ   -->
      <effect-composer v-if="pixar">
        <pixelate-effect></pixelate-effect>
      </effect-composer>
        <!--   ВСЕ ДЕЛАЕТ ПИКСЕЛЯМИ   -->
      </model-viewer>
    </div>
      <!--  BOCZNA PANEL   -->
      <div class="sidePanelSetting">
            <label>Pikselem<input type="checkbox" v-model="pixar"/></label>
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
      pixar: false
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
model-viewer {
  margin-left: 50%;
  margin-top: 10%;
  width: 300px;
  height: 300px;
  transform: translate(-50%, -50%);
}
.sidePanelSetting {
  right: 0;
}
</style>