<template>
    <!--  COMPONENTS  -->
      <MainView />
      <MenuComponent />
      <VCarousel />
</template>

<script>
import VCarousel from '../components/VCarousel.vue';
import MainView from "@/components/MainView.vue";
import MenuComponent from "@/components/menu/MenuComponent.vue";

export default {
  name: 'App',
  components: {
    VCarousel,
    MainView,
    MenuComponent,
  },
}
</script>

<style>
img {
  width: 100%;
}

MainView {
  width: 100%;
  height: 100%;
}

@media only screen and (max-width: 672px) {
  .panelImage {
    width: 80px;
    height: 900px;
  }
  .panelImageR {
    width: 60px;
    height: 950px;
  }
}
</style>
