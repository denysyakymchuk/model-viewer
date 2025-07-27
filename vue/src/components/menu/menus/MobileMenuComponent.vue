<script setup lang="ts">
import EffectsModelComponent from "@/components/EffectsModelComponent.vue";
import EmbedCodeMenuComponent from "@/components/EmbedCodeMenuComponent.vue";

import { ref} from "vue";

const tab =  ref('one');
const menu =  ref(false);

</script>

<template>
  <div class="btn"
  >
    <v-menu
        v-model="menu"
        :close-on-content-click="false"
        location="center"
        max-width="350"
    >
      <template v-slot:activator="{ props }">
        <p
            data-tooltip="Menu">
          <img
              height="30"
              width="30"
              v-bind="props"
              class="changePointer"
              src="../../../../public/menu.svg"
          >
        </p>
      </template>

      <v-card
          min-width="300"
          color="black"
          style="border-radius: 20px;"
      >
        <v-card>
          <v-tabs
              align-tabs="left"
              v-model="tab"
              bg-color="black"
          >
            <a  @click="menu=false"
                style="cursor: pointer;
                     width: 70px"
            >
              <v-tab
                  disabled
                  style="opacity: 1"
              >
                <v-icon color="white"
                        size="large"
                >
                  mdi-close
                </v-icon>
              </v-tab>
            </a>
            <v-tab value="one">Filters</v-tab>
            <v-tab value="three">Get code</v-tab>
              <v-tab to="/admin">
                <v-icon color="white" size="large">
                  mdi-login
                </v-icon>
              </v-tab>
          </v-tabs>

          <v-card-text
              style="background-color: #0e0e0e">

            <!--     EFFECTS       -->
            <v-window v-model="tab">
              <v-window-item
                  id="windowFilter"
                  value="one">
                <div id="filterFrame">
                  <EffectsModelComponent />
                </div>
              </v-window-item>
              <!--     EFFECTS       -->

              <!--     EMBED       -->
              <v-window-item
                  value="three"
                  class="color-white"
                  style="text-align: justify"
              >
                <EmbedCodeMenuComponent />
              </v-window-item>
              <!--     EMBED       -->

            </v-window>
          </v-card-text>
        </v-card>
      </v-card>
    </v-menu>
  </div>
</template>

<style scoped>
@font-face {
  font-family: 'Lexend';
  src: url('../../../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
* {
  font-family: Lexend;
}
.btn {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 1000;
  margin-top: 10px;
  margin-right: 10px;
}
</style>