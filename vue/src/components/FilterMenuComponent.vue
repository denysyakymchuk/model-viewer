<template>
  <v-autocomplete
      v-model="selectedOwners"
      @blur="updateOwners()"
      chips
      bg-color="white"
      label="Owners"
      :items="store.getters.OWNER_LIST"
      multiple
  >
    <template #append>
      <v-icon color="white" size="x-large" icon="mdi mdi-account-tie"></v-icon>
    </template>
  </v-autocomplete>
</template>

<script setup>
import { ref } from 'vue'
import { useStore } from 'vuex'

const store = useStore()
const selectedOwners = ref([])

async function updateOwners() {
  if (selectedOwners.value !== store.getters.OWNER_LIST) {
      await store.dispatch('GET_ACTIVE_MODELS', selectedOwners.value.toString().replace(/\[|\]/g, ""))
      await store.dispatch('GET_MAIN_MODEL', {
        path: store.getters.MODELS[0].path,
        id: store.getters.MODELS[0].id,
        skyBoxImage: store.getters.MODELS[0].path_skybox_image,
        envImage: store.getters.MODELS[0].path_env_image,
        mainModelIndex: 0
      })
  }
}
</script>
