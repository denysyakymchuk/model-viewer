<script setup lang="ts">
import { VCheckbox } from 'vuetify/components';

import {ref} from "vue";
import {useStore} from "vuex";

const store = useStore();

const showIsCopiedLink =  ref(false);
const isSkyBoxImage =  ref(false);
const isEnvImage =  ref(false);


function makeLink(): string {
  // return `<iframe src="http://localhost/model/${this.MAIN_MODEL_ID}?shadowIntensity=${this.shadowIntensity}&brightness=${thi s.brightness}&contrast=${this.contrast}&opacity=${this.opacity}&blendMode=${this.blendMode}&blockOpacity=${this.blockOpacity}&pixar=${Number(this.pixar)}&isEnvImage=${Number(this.isEnvImage)}&isSkyBoxImage=${Number(this.isSkyBoxImage)}"></iframe>`
  return `<iframe src="https://modelviewer.pl/model/${store.getters.MAIN_MODEL_ID}?grid=${store.getters.MAIN_MODEL_GRID}&sepia=${store.getters.MAIN_MODEL_SEPIA}&shadowIntensity=${store.getters.MAIN_MODEL_SEPIA}&brightness=${store.getters.MAIN_MODEL_BRIGHTNESS}&contrast=${store.getters.MAIN_MODEL_CONTRAST}&opacity=${store.getters.MAIN_MODEL_OPACITY}&blendMode=${store.getters.MAIN_MODEL_BLENDMODE}&blockOpacity=${store.getters.MAIN_MODEL_OPACITY}&pixar=${Number(store.getters.MAIN_MODEL_PIXEL)}&isEnvImage=${Number(isEnvImage.value)}&isSkyBoxImage=${Number(isSkyBoxImage.value)}"></iframe>`
}
function copyLink(): void {
  navigator.clipboard.writeText(makeLink());
  showIsCopiedLink.value = true;
}

</script>

<template>
    <div class="d-flex">
      <VCheckbox label="Environment image" v-model="isEnvImage"></VCheckbox>
      <VCheckbox label="Skybox image" v-model="isSkyBoxImage"></VCheckbox>
    </div>
    <v-alert
        class="mb-5"
        text="The code was copied!"
        type="success"
        v-if="showIsCopiedLink"
    >
    </v-alert>
    <v-textarea
        label=""
        prepend-icon="mdi-content-copy"
        :value="makeLink()"
        variant="solo-filled"
        @click:prepend="copyLink()"
    ></v-textarea>
</template>

<style scoped>
* {
  color: white;
}
</style>