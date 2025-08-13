<template>
  <v-autocomplete
      v-model="selectedOwners"
      @blur="updateListOfModels()"
      chips
      bg-color="white"
      label="Owners"
      :items="store.getters.OWNER_LIST"
      multiple
      append-inner-icon="mdi mdi-account-tie">
  </v-autocomplete>

  <div class="d-flex justify-center">
    <v-date-input
        bg-color="white"
        @blur="updateListOfModels()"
        v-model="dateRangeFilter"
        label="Select range"
        input-format="yyyy-mm-dd"
        max-width="368"
        multiple="range"
        prepend-icon=""
        append-inner-icon="mdi-calendar-month"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { shallowRef } from 'vue'
import {VDateInput} from "vuetify/labs/components";


const store = useStore()
const selectedOwners = ref([])
const dateRangeFilter = shallowRef(null)

async function updateListOfModels() {
  if (selectedOwners.value !== store.getters.OWNER_LIST) {
      await store.dispatch('GET_ACTIVE_MODELS', { owners: preparedOwners(), ...preparedTime()})
      await store.dispatch('GET_MAIN_MODEL', {
        path: store.getters?.MODELS[0]?.path ? store.getters.MODELS[0].path : store.getters.MAIN_MODEL,
        id: store.getters?.MODELS[0]?.id ? store.getters.MODELS[0]?.id : store.getters.MAIN_MODEL_ID,
        skyBoxImage: store.getters?.MODELS[0]?.path_skybox_image ? store.getters.MODELS[0].path_skybox_image : store.getters.MAIN_SKY_BOX_IMAGE,
        envImage: store.getters?.MODELS[0]?.path_env_image ? store.getters.MODELS[0].path_env_image : store.getters.MAIN_ENV_IMAGE,
        mainModelIndex: 0
      })
  }
}

function preparedOwners() {
  return selectedOwners.value.toString().replace(/\[|\]/g, "");
}

function preparedTime() {
  const start = dateRangeFilter.value.at(0)
  const end = dateRangeFilter.value.at(-1)
  return {created_after: formatDate(start), created_before: formatDate(end)}
}

function formatDate(date) {
  if (!date) return ''
  const d = new Date(date)
  const year = d.getFullYear()
  const month = String(d.getMonth() + 1).padStart(2, '0')
  const day = String(d.getDate()).padStart(2, '0')
  return `${year}-${month}-${day}`
}


</script>
