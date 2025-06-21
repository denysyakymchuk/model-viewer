<script lang="ts">
import {defineComponent} from 'vue'
import MobileMenuComponent from "@/components/menu/menus/MobileMenuComponent.vue";
import DesktopMenuComponent from "@/components/menu/menus/DesktopMenuComponent.vue";
import { VueScreenSizeMixin } from 'vue-screen-size';

export default defineComponent({
  name: "MenuComponent",
  components: {
    MobileMenuComponent,
    DesktopMenuComponent
  },
  mixins: [VueScreenSizeMixin],
  data() {
    return {
      isDesktop: true,
    }
  },
  methods: {
    //Check size of screen. Need for change a menu from mobile to desktop
    changeSizeOfScreen() {
      this.isDesktop = this.$vssWidth >= 1000;
    }
  },
  watch: {
    $vssWidth() {
      this.changeSizeOfScreen()
    }
  },
  mounted() {
    this.changeSizeOfScreen()
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