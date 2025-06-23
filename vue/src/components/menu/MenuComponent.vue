<script lang="ts">
import {computed, defineComponent} from 'vue'
import MobileMenuComponent from "@/components/menu/menus/MobileMenuComponent.vue";
import DesktopMenuComponent from "@/components/menu/menus/DesktopMenuComponent.vue";
import { useWindowSize } from 'vue-window-size';

export default defineComponent({
  name: "MenuComponent",
  components: {
    MobileMenuComponent,
    DesktopMenuComponent
  },
  setup() {
    const { width } = useWindowSize()

    const isDesktop = computed(() => width.value > 1000)

    return {
      isDesktop
    }
  }
})
</script>


<template>
  <div>
    <MobileMenuComponent v-if="!isDesktop" />
    <DesktopMenuComponent v-if="isDesktop" />
  </div>
</template>

<style scoped>

</style>