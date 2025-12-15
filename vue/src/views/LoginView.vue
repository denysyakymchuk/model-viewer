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

      <v-btn value="registration">
        Registration
      </v-btn>
      <v-btn value="home" @click="this.$router.push({name: 'home'})">
        Home
      </v-btn>

    </v-btn-toggle>
    <div>
      <LoginComponent
          v-if="this.option === 'login'"
          @setAnimationDuration="handleAnimationDuration"
          @setInputtingPassword="handleInputtingPassword"
      />
      <RegistrationComponent
          v-if="this.option === 'registration'"
          @setAnimationDuration="handleAnimationDuration"
          @setInputtingPassword="handleInputtingPassword"
      />
    </div>
  </v-col>

  <!--FACE ANIMATION-->
  <!--LEFT FACE-->
  <div class="emoji-faces-container">
    <div class="left-emoji-face-container">
      <div class="left-emoji-face left-face-jump" :style="{'animation-duration': animationDuration + 's'}">
        <div class="left-eyes">
          <div :class="[inputtingPassword ? 'closed-left-eye' : 'eye']"></div>
          <div :class="[inputtingPassword ? 'closed-left-eye' : 'eye']"></div>
        </div>
      </div>
    </div>
    <!--LEFT FACE-->

    <!--RIGHT FACE-->
    <div class="right-emoji-face-container">
      <div class="right-emoji-face right-face-jump" :style="{'animation-duration': animationDuration + 's'}">
        <div class="right-eyes">
          <div :class="[inputtingPassword ? 'closed-right-eye' : 'eye']"></div>
          <div :class="[inputtingPassword ? 'closed-right-eye' : 'eye']"></div>
        </div>
      </div>
    </div>
  </div>
  <!--RIGHT FACE-->
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
      animationDuration: 0,
      inputtingPassword: false,
    }
  },
  components: {
    LoginComponent,
    RegistrationComponent,
  },
  methods: {
    handleAnimationDuration(value) {
      this.animationDuration = value;
    },
    handleInputtingPassword(value) {
      let eyes = document.querySelectorAll('.eye');
      eyes.forEach(eye => {
        eye.style.transform = '';
      })

      this.inputtingPassword = value;
    }
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
