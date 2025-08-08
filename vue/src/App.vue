<template>
  <div>
    <component :is="layout">
      <router-view />
    </component>
  </div>
</template>

<script>
import AdminLayout from "@/layout/AdminLayout.vue";
import MainLayout from "@/layout/MainLayout.vue";

export default {
  name: 'App',
  computed: {
    layout() {
      return this.$route.meta.layout === 'admin' ? AdminLayout : MainLayout;
    },
    components: {
      AdminLayout,
      MainLayout,
    }
  }
}
</script>
