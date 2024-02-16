<template>
  <div class="container">
  <div>
    <h1>
      404
    </h1>
    <h2>
      Page not found
    </h2>
  </div>
  <div class="ml-16">
    <v-btn @click="GoToHome()" stacked>
      Go to home
    </v-btn>
  </div>
  </div>
</template>

<script>
export default {
  name: "NotFoundView",
  methods: {
    GoToHome() {
      this.$router.push({name: 'home'});
    },
  }
}
</script>

<style scoped>
h1{
  font-size: 100px;
}
.container {
  position: fixed;
  top: 50%;
  left: 50%;
  width: 40%;
  height: 40%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  transform: translate(-50%, -50%);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-image: url('../../assets/bg.png');
  background-size: cover;
}
</style>