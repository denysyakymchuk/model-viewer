<template>
  <v-sheet class="mx-auto form">
    <v-alert
        style="margin-bottom: 1%"
        v-if="this.error_alert"
        title="Failed login"
        :text="this.error_alert_text"
        type="error"
        variant="outlined"
    ></v-alert>

    <div class="d-flex justify-center align-center">
      <v-progress-circular v-if="isLoaded"  indeterminate color="white" :size="53" :width="4"></v-progress-circular>
    </div>

    <v-form v-if="!isLoaded" ref="form" v-model="this.valid" fast-fail @submit.prevent>
      <v-text-field
          v-model="this.email"
          label="Email"
          :rules="emailRules"
          class="field"
      ></v-text-field>

      <v-text-field
          v-model="this.password"
          label="Password"
          type="password"
          :rules="passwordRules"
          class="field"
      ></v-text-field>

      <v-btn @click="sendCredentials" :disabled="!this.valid" block class="submit-btn mt-2 mb-2">Submit</v-btn>

      <!--Google auth button-->
      <div class="d-flex justify-center align-center">
        <GoogleAuthComponent></GoogleAuthComponent>
      </div>
      <!--Google auth button-->

    </v-form>
  </v-sheet>
</template>


<script>
import {mapActions} from "vuex";
import GoogleAuthComponent from "@/components/GoogleAuthComponent.vue";


export default {
  name: "LoginComponent",
  components: {
    GoogleAuthComponent,
  },
  data() {
    return {
      valid: false,
      isLoaded: false,
      password: '',
      email: '',
      error_alert: false,
      error_alert_text: '',
      emailRules:  [
        value => {
          if (value) return true
          return 'The field can not be empty.'
        },
      ],
      passwordRules: [
        value => {
          if (value) return true
          return 'The field can not be empty.'
        },
      ],
    }
  },
  methods: {
    async sendCredentials() {
      this.isLoaded = true
      try {
        const response = await this.GET_LOGIN({
          email: this.email,
          password: this.password
        })
        if (response === 200) {
          this.$router.push({ name: 'admin' });
        }
      } catch (error) {
        if (error.response && error.response.status === 400) {
          this.error_alert_text = error.response.data.non_field_errors[0] || 'Invalid Credentials';
          this.error_alert = true;
        } else if (error.response && error.response.status === 404) {
          this.error_alert_text = 'The requested resource was not found. Please try again later.';
          this.error_alert = true;
        } else {
          this.error_alert_text = 'An error occurred while trying to log in. Please try again later.';
          this.error_alert = true;
        }
      }
      this.isLoaded = false
    },
    ...mapActions(["GET_LOGIN", "ACTIVATE_ACCOUNT"]),
  },
  async mounted() {
    if (this.$route.params.uid && this.$route.params.token) {
      await this.ACTIVATE_ACCOUNT({
        uid: this.$route.params.uid,
        token: this.$route.params.token
      })
  }
  }
}
</script>

<style scoped>
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
.form[data-v-5c6101e4] {
  background-color: #0e0e0e;
  /*! border-radius: 4px; */
  padding: 16px;
  width: 400px;
  max-width: 100%;
  box-sizing: border-box;
}
.form[data-v-dcfd9078] {
  background-color: #0e0e0e;
  /*! border-radius: 4px; */
  padding: 16px;
  width: 400px;
  max-width: 100%;
  box-sizing: border-box;
}
</style>
