<template>
  <div>
    <model-viewer src="free__bread_pack_cs2.glb" shadow-intensity="1" camera-controls touch-action="pan-y"></model-viewer>
  </div>
</template>

<script>
export default {
  name: "MainView"
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