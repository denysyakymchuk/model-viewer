<template>
  <div>
    <MainView />
    <VCarousel />
  </div>
</template>

<script>
import VCarousel from './components/VCarousel.vue'
import MainView from "@/components/MainView.vue";

export default {
  name: 'App',
  components: {
    VCarousel,
    MainView
  }
}
</script>

<style>
body {
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
