<template>
  <div class="hello">
    <carousel :items-to-show="1.5">
      <slide v-for="slide in 10" :key="slide">
        <model-viewer src="free__bread_pack_cs2.glb" shadow-intensity="1" camera-controls touch-action="pan-y"></model-viewer>
      </slide>

      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
  </div>
</template>


<script>
import '@google/model-viewer'
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';

export default {
  name: 'VCarousel',
  props: {
    msg: String
  },
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
