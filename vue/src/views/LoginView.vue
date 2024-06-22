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

    <v-form ref="form" v-model="this.valid" fast-fail @submit.prevent>
      <v-text-field
          v-model="this.username"
          label="Username"
          :rules="usernameRules"
          class="field"
      ></v-text-field>

      <v-text-field
          v-model="this.password"
          label="Password"
          type="password"
          :rules="passwordRules"
          class="field"
      ></v-text-field>

      <v-btn @click="sendCredentials" :disabled="!this.valid" block class="submit-btn mt-2">Submit</v-btn>
    </v-form>
  </v-sheet>
</template>


<script>
import {mapActions} from "vuex";

export default {
  name: "LoginView",
  data() {
    return {
      valid: false,
      password: '',
      username: '',
      error_alert: false,
      error_alert_text: '',
      usernameRules:  [
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
      try {
        const response = await this.GET_LOGIN({
          username: this.username,
          password: this.password
        });

        if (response === 200) {
          this.$router.push({ name: 'admin' });
        }
      } catch (error) {
        if (error.response && error.response.status === 400) {
          this.error_alert_text = error.response.data.non_field_errors[0] || 'Invalid Credentials';
          this.error_alert = true;
        } else if (error.response && error.response.status === 404) {
          this.error_alert_text = 'The requested resource was not found.';
          this.error_alert = true;
        } else {
          this.error_alert_text = 'An error occurred while trying to log in. Please try again later.';
          this.error_alert = true;
        }
      }},
    ...mapActions(["GET_LOGIN"]),
  },
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
</style>
