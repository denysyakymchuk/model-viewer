<template>
  <div>
    <carousel :items-to-show="3">

      <slide v-for="slide in MODELS" :key="slide.path">
        <model-viewer @click="setMainModel(slide.path)" :src="slide.path"></model-viewer>
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
import { mapActions, mapGetters } from "vuex";


import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';

export default {
  name: 'VCarousel',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  data() {
    return {
      baseModel: 0,
    };
  },
  methods: {
    setMainModel(path) {
      this.GET_MAIN_MODEL(path)
    },
    ...mapActions(["GET_MODELS", "GET_MAIN_MODEL"]),
  },
  computed: {
    ...mapGetters(["MODELS"]),
  },
  async mounted() {
    await this.GET_MODELS()
    this.GET_MAIN_MODEL(this.MODELS[0].path)
  }
}
</script>

<style scoped>

</style>
