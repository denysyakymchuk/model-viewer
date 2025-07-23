<template>
  <div class="app-container">
    <div class="main-content">
      <MainView />
      <VCarousel />
    </div>
    <MenuComponent class="menu-component" />
  </div>
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

<style scoped>
img {
  width: 100%;
}

.app-container {
  display: flex;
  flex-direction: row;
  height: 100vh;
  overflow: hidden;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding: 0 1% 0 1%;
}

.menu-component {
  width: 350px;
  height: 100vh;
  background-color: #f2f2f2;
}

@media only screen and (max-width: 1000px) {
  img {
    width: 100%;
  }

  MainView {
    position: static;
    width: 100%;
    height: 100%;

  }
  .menu-component {
    position: relative;
    width: 0;
    height: 100%;
  }
}
</style>
