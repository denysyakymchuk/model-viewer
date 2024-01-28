<template>
  <div>
    <!--  LEFT PANEL  -->
    <div class="openLeft"  @animationend="onAnimationEnd('left')">
      <img src="./assets/panel-left.png">
    </div>

      <!--  RIGHT PANEL  -->
    <div class="openRight" @animationend="onAnimationEnd('right')">
      <img src="./assets/panel-right.png">
    </div>

      <!--  COMPONENTS  -->
    <div>
      <MainView v-if="allAnimationsDone" />
      <VCarousel v-if="allAnimationsDone" />
    </div>

    <!--  BOTTOM PANEL  -->
    <div class="openBottom"  @animationend="onAnimationEnd('bottom')">
      <img src="./assets/panel-bottom.png">
    </div>
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
  },
  data() {
    return {
      animationLeftDone: false,
      animationRightDone: false,
      animationBottomDone: false,
      };
    },
  computed: {
    allAnimationsDone() {
      return this.animationLeftDone && this.animationRightDone && this.animationBottomDone;
    }
  },
  methods: {
    // Dopiero jak wszystkie wartosci beda `true` wtedy zaczynaja ladowac sie 3d modele
    onAnimationEnd(position) {
      if (position === 'left') {
        this.animationLeftDone = true;
      } else if (position === 'right') {
        this.animationRightDone = true;
      } else if (position === 'bottom') {
        this.animationBottomDone = true;
      }
    }
  }
}
</script>

<style>
body {
  background-image: url("./assets/background2.webp");
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
/*Animowana lewa panel*/
.openLeft {
  top: 0;
  left: -200px;
  position: fixed;
  animation: slideLeft 2s ease-in-out forwards;
}

@keyframes slideLeft {
  from {
    left: -200px;
  }
  to {
    left: 0px;
  }
}

/*Animowana prawa panel*/
.openRight {
  top: 0;
  right: -200px; /* Начальное положение за пределами экрана */
  position: fixed;
  animation: slideRight 2s ease-in-out forwards;
}

@keyframes slideRight {
  from {
    right: -200px;
  }
  to {
    right: 0px;
  }
}

/*Animowana dolna panel*/
.openBottom {
  left: 0;
  bottom: -200px; /* Начальное положение за пределами экрана */
  position: fixed;
  animation: slideUp 2s ease-in-out forwards;
}

@keyframes slideUp {
  from {
    bottom: -200px;
  }
  to {
    bottom: -10px;
  }
}

</style>
