<template>
  <div class="pos">
    <carousel
        @slide-start="handleSlideStart"
        :items-to-show="4"
    >
      <slide
          v-for="(slide, index) in MODELS"
          :key="slide.path"
          class="slide"
      >
        <model-viewer class="ww"
                      @click="setMainModel(slide.path, slide.path_skybox_image, slide.path_env_image, slide.id, index);"
                      :src="slide.path"
                      :skybox-image="slide.path_skybox_image"
                      :environment-image="slide.path_env_image">
        </model-viewer>
      </slide>

      <template #addons>
        <div>
          {{ this.MAIN_MODEL_INDEX + 1 }}
          of
          {{ this.MODELS.length }}
        </div>
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
    setMainModel(path, skyBoxImage, envImage, id, mainModelIndex) {
      const baseModel = {
        path: path,
        id: id,
        skyBoxImage: skyBoxImage,
        envImage: envImage,
        mainModelIndex: mainModelIndex,
      };
      this.GET_MAIN_MODEL(baseModel);
    },
    handleSlideStart(data) {
      if (data.slidesCount - data.currentSlideIndex === 4 && this.NEXT_PAGE){
        this.GET_EXTEND_MODELS()
      }
    },
    ...mapActions(["GET_ACTIVE_MODELS", "GET_MAIN_MODEL", "GET_EXTEND_MODELS"]),
  },
  computed: {
    ...mapGetters(["MODELS", "NEXT_PAGE", "MAIN_MODEL_INDEX"]),
  },
  async mounted() {
    await this.GET_ACTIVE_MODELS();

    const baseModel = {
      path: this.MODELS[0].path,
      id: this.MODELS[0].id,
      skyBoxImage: this.MODELS[0].path_skybox_image,
      envImage: this.MODELS[0].path_env_image,
      mainModelIndex: 0
    };
    await this.GET_MAIN_MODEL(baseModel);
  }
};
</script>

<style scoped>
* {
  font-family: Lexend;
}

@font-face {
  font-family: 'Lexend';
  src: url('../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}

model-viewer {
  width: 100%;
  height: 100%;
  border-radius: 20px;
}

.slide {
  height: 180px;
  width: 150px;
  margin: 1%;
}

.pos {
  width: 100%;
  max-width: 100%;
  margin: auto;
  position: relative;
  bottom: 0;
  left: 0;
  transform: none;
  z-index: 1;
}

@media only screen and (max-width: 1000px) {
  .pos {
    position: fixed;
    bottom: 3%;
    left: 50%;
    transform: translateX(-50%);
    width: 100%;
    max-width: 1800px;
    z-index: 1000;
  }

  .ww {
    height: 100px;
  }
}
@media only screen and (max-width: 672px) {
  .ww {
    height: 100px;
  }
  .pos {
    bottom: 1%;
  }
}
</style>
