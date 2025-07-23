<script lang="ts">
import {defineComponent} from 'vue'
import VCarousel from '@/components/VCarousel.vue'

export default defineComponent({
  name: "DesktopMenuComponent",
  components: {
    VCarousel,
  }
})
</script>

<template>
    <v-card
        style="height: 100%;
        border-radius: 0;
        padding: 0 2% 0 2%;
        "
        color="black"
        subtitle="Menu"
        variant="flat">
        <div>
          <v-expansion-panels class="my-4" variant="accordion">
            <v-expansion-panel>
              <template v-slot:title>
                Filters
              </template>

              <template v-slot:text>
                <VCarousel/>
                <MyComponent />
              </template>
            </v-expansion-panel>
          </v-expansion-panels>
        </div>
    </v-card>
</template>

<style scoped>

</style>