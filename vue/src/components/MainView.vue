<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <div class="viewer-container">
      <model-viewer  :src="store.getters.MAIN_MODEL"
                     :skybox-image="store.getters.MAIN_SKY_BOX_IMAGE"
                     :environment-image="store.getters.MAIN_ENV_IMAGE"
                     :shadow-intensity="store.getters.MAIN_MODEL_SHADOW_INTENSITY"
                     :shadow-softness="store.getters.MAIN_MODEL_SHADOW_SOFTNESS"
                     camera-controls
                     touch-action="pan-y"
                     :id="store.getters.MAIN_MODEL"
                      >

        <effect-composer id="customComposer" render-mode="quality" msaa="8">

          <!--   ВСЕ ДЕЛАЕТ ПИКСЕЛЯМИ   -->
          <pixelate-effect v-if="store.getters.MAIN_MODEL_PIXEL"></pixelate-effect>

          <!--   OPACITY     -->
          <color-grade-effect :contrast="store.getters.MAIN_MODEL_CONTRAST" saturation="-1" :opacity="store.getters.MAIN_MODEL_OPACITY" :blend-mode="store.getters.MAIN_MODEL_BLENDMODE" :brightness="store.getters.MAIN_MODEL_BRIGHTNESS"></color-grade-effect>

        </effect-composer>

      </model-viewer>
    </div>

    <!--  BOCZNA PANEL   -->
    <div>
      <MenuComponent />
    </div>
    <!--  BOCZNA PANEL   -->
  </div>
</template>

<script setup lang="ts">
import '@google/model-viewer';
import '@google/model-viewer-effects';
import MenuComponent from './menu/MenuComponent.vue';
import {useStore} from "vuex";

const store = useStore();
</script>

<style scoped>
@font-face {
  font-family: 'Lexend';
  src: url('../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
* {
  font-family: Lexend;
}
.viewer-container {
  width: 100vw;
  margin-top: 1%;
  justify-content: center;
  display: flex;
  position: relative;

}

.btn {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 1000;
  margin-top: 10px;
  margin-right: 10px;
}
model-viewer {
  position: fixed;
  width: 95vw;
  height: 70vh;
  aspect-ratio: 16/9;
  border-radius: 30px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 0;
}

.wd-all {
  width: 270px;
}
.changePointer:hover {
  cursor: pointer;
}
.v-row {
  display: flex;
  flex-wrap: wrap;
  flex: 1 1 auto;
  margin: 0;
}
.color-white {
  color: white
}
model-viewer::part(default-progress-bar) {
  background-color: black; /* Change background color */
  border-radius: 20px;
  height: 8px;
  width: 100%;
}

[data-tooltip] {
  position: relative; /* Относительное позиционирование */
}
[data-tooltip]::after {
  content: attr(data-tooltip); /* Выводим текст */
  position: absolute; /* Абсолютное позиционирование */
  background: #1d1b1b; /* Синий цвет фона */
  color: #fff; /* Цвет текста */
  padding: 0.5em; /* Поля вокруг текста */
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3); /* Параметры тени */
  pointer-events: none; /* Подсказка */
  opacity: 0; /* Подсказка невидима */
  transition-duration: 1s; /* Время появления подсказки */
  right: 2em;
}
[data-tooltip]:hover::after {
  opacity: 1; /* Показываем подсказку */
  right: 2em; /* Положение подсказки */
}
</style>