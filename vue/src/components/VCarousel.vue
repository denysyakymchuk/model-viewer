<template>
  <div class="pos">
    <carousel :items-to-show="4">

      <slide v-for="slide in MODELS" :key="slide.path" class="slide">
        <model-viewer class="ww" @click="setMainModel(slide.path)" :src="slide.path"></model-viewer>
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
@media only screen and (max-width: 672px) {
  .ww {
    height: 150px;
  }
}
model-viewer {
  width: 100%; /* Занимает всю ширину слайда */
  height: 100%;
  background-image: url('../assets/bg.png');
}
.slide {
  height: 250px; /* Задайте нужную высоту для слайдов */
  margin: 1%;
}

.pos {
  width: 100%; /* Занимает всю ширину экрана */
  max-width: 1400px; /* Максимальная ширина карусели */
  margin: auto;
  position: fixed;
  bottom: 5%; /* Позиционирует карусель в самом низу экрана */
  left: 50%;
  transform: translateX(-50%); /* Центрирование по горизонтали */
  z-index: 1000;
}
</style>
