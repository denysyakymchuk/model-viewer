<template>
  <div class="pos">
    <carousel
        @slide-start="handleSlideStart"
        :items-to-show="3.5"
    >
      <slide
          v-for="slide in MODELS"
          :key="slide.path"
          class="slide"
      >
        <model-viewer class="ww"
                      @click="setMainModel(slide.path, slide.path_skybox_image, slide.path_env_image, slide.id);"
                      :src="slide.path">
        </model-viewer>
      </slide>

      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
  </div>
</template>

<script>
import '@google/model-viewer';
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
  data(){
    return {
      page_number: 1
    }
  },
  methods: {
    setMainModel(path, skyBoxImage, envImage, id) {
      this.GET_MAIN_MODEL({ path, skyBoxImage, envImage, id });
    },
    handleSlideStart(data) {
      if (data.slidesCount - data.currentSlideIndex === 3 && this.NEXT_PAGE){
        this.GET_EXTEND_MODELS()
      }
    },
    ...mapActions(["GET_ACTIVE_MODELS", "GET_MAIN_MODEL", "GET_EXTEND_MODELS"]),
  },
  computed: {
    ...mapGetters(["MODELS", "NEXT_PAGE"]),
  },
  async mounted() {
    await this.GET_ACTIVE_MODELS();

    const baseModel = {
      path: this.MODELS[0].path,
      id: this.MODELS[0].id,
      skyBoxImage: this.MODELS[0].path_skybox_image,
      envImage: this.MODELS[0].path_env_image
    };
    await this.GET_MAIN_MODEL(baseModel);
  }
};
</script>

<style scoped>
@media only screen and (max-width: 672px) {
  .ww {
    height: 150px;
  }
}

model-viewer {
  width: 100%;
  height: 100%;
}

.slide {
  height: 150px;
  width: 150px;
  margin: 1%;
}

.pos {
  width: 100%;
  max-width: 1400px;
  margin: auto;
  position: fixed;
  bottom: 5%;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
}
</style>
