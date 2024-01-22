<template>
  <div>
    <model-viewer :src="this.MAIN_MODEL" shadow-intensity="1" camera-controls touch-action="pan-y"></model-viewer>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "MainView",
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
</style>