<template>
  <v-col
      class="py-2"
      cols="12"
  >
    <v-btn-toggle
        v-model="option"
        color="black"
        rounded="1"
        group
    >
      <v-btn value="login">
        Login
      </v-btn>

      <v-btn value="registartion">
        Registartion
      </v-btn>
      <v-btn value="home" @click="this.$router.push({name: 'home'})">
        Home
      </v-btn>

    </v-btn-toggle>
    <div>
      <LoginComponent v-if="this.option === 'login'" />
      <RegistrationComponent v-if="this.option === 'registartion'" />
    </div>
  </v-col>

  <!--FACE ANIMATION-->
  <div class="emoji-face-container">
    <div class="emoji-face">
      <div class="eyes">
        <div class="eye"></div>
        <div class="eye"></div>
      </div>
    </div>
  </div>
  <!--FACE ANIMATION-->

</template>


<script>
import LoginComponent from "@/components/LoginComponent.vue";
import RegistrationComponent from "@/components/RegistrationComponent.vue";
import {eyeball} from "@/utils/eyes-animation/animation.js"

export default {
  name: "LoginView",
  data() {
    return {
      option: 'login',
      icon: 'justify',
      toggle_none: null,
      toggle_one: 0,
      toggle_exclusive: 2,
      toggle_multiple: [0, 1, 2],
      valid: false,
    }
  },
  components: {
    LoginComponent,
    RegistrationComponent,
  },
  mounted() {
    document.body.addEventListener('mousemove', eyeball);
  },
  beforeUnmount() {
    document.body.removeEventListener('mousemove', eyeball);
  }
}
</script>

<style scoped>

@import '@/utils/eyes-animation/eyes.css';

@font-face {
  font-family: 'Lexend';
  src: url('../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf') format('truetype');
  font-weight: normal; /* or a specific weight */
  font-style: normal; /* or italic */
}
* {
  font-family: Lexend;
}
.form {
  background-color: #0e0e0e;
  border-radius: 4px;
  padding: 16px;
  width: 400px;
  max-width: 100%;
  box-sizing: border-box;
}

.field {
  background-color: #0e0e0e;
  border: none;
  color: #DDD;
}

.field::placeholder {
  color: #BBB;
}

.field .v-label {
  color: #BBB;
}

.submit-btn {
  background-color: #666;
  color: #FFF;
}

.submit-btn:hover {
  background-color: #777;
}
</style>
