<template>
  <div class="v-container">
    <v-row>
      <v-col>
        <v-row class="d-flex justify-space-around align-center">
          <h1>
            404
          </h1>

          <img src="../../assets/not_found.png" style="width: 30px; height: 30px" alt="not found">

          <h2
              class="justify-end"
              style="opacity: 0.8"
          >
            Page not found
          </h2>
        </v-row>
        <v-row class="d-flex justify-center">
          <v-btn
              color=gray
              @click="GoToHome()"
              stacked
          >
            Go to home
          </v-btn>
        </v-row>
      </v-col>
    </v-row>
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

</style>