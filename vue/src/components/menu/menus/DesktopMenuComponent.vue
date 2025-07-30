<script lang="ts" xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
import {defineComponent, ref} from 'vue'
import EffectsModelComponent from "@/components/EffectsModelComponent.vue";
import EmbedCodeMenuComponent from "@/components/EmbedCodeMenuComponent.vue";
import FilterMenuComponent from "@/components/FilterMenuComponent.vue";

export default defineComponent({
  name: "DesktopMenuComponent",
  components: {
    EffectsModelComponent,
    EmbedCodeMenuComponent,
    FilterMenuComponent,
  },
  data() {
    return {
      tab: ref('null')
    }
  }
})
</script>

<template>
  <v-card
      color="grey-darken-4"
      style="height: 100%; border-radius: 0">
    <v-tabs
        v-model="tab"
        align-tabs="center"
        color="white"
        fixed-tabs="true"
    >
      <v-tab :value="1" base-color="white"  style="width: 60px;">Effects</v-tab>
      <v-tab :value="2" base-color="white"  style="width: 60px;">Embed</v-tab>
      <v-tab :value="3" base-color="white"  style="width: 60px;">Filters</v-tab>
      <v-tab :value="4" base-color="white" size="small" to="/admin">
        <v-icon color="white" size="x-large">
          mdi-login
        </v-icon>
      </v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item
          :value="1"
      >
        <v-container fluid>
          <v-row>
            <v-col>
              <EffectsModelComponent />
            </v-col>
          </v-row>
        </v-container>
      </v-tabs-window-item>
      <v-tabs-window-item
          :value="2"
      >
        <v-container fluid>
          <v-row>
            <v-col>
              <EmbedCodeMenuComponent/>
            </v-col>
          </v-row>
        </v-container>
      </v-tabs-window-item>
      <v-tabs-window-item
          :value="3"
      >
        <v-container fluid>
          <v-row>
            <v-col>
              <FilterMenuComponent />
            </v-col>
          </v-row>
        </v-container>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
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
  color: black;
}
</style>