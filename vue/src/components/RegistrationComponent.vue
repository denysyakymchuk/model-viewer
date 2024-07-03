<template>
  <v-sheet class="mx-auto form">
    <v-alert
        style="margin-bottom: 1%"
        v-if="error_alert"
        :title="this.title_error"
        :text="this.text_error"
        :type="this.error_type"
        variant="outlined"
    ></v-alert>

    <v-form ref="form" v-model="valid" @submit.prevent="sendData">
      <v-text-field
          v-model="username"
          label="Username"
          :rules="usernameRules"
          class="field"
      ></v-text-field>

      <v-text-field
          v-model="email"
          label="Gmail"
          type="email"
          :rules="gmailRules"
          class="field"
      ></v-text-field>

      <v-text-field
          v-model="password"
          label="Password"
          type="password"
          :rules="passwordRules"
          class="field"
      ></v-text-field>

      <v-btn @click="this.sendData()" :disabled="!valid" block class="submit-btn mt-2">Submit</v-btn>
    </v-form>
  </v-sheet>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "RegistrationComponent",
  data() {
    return {
      title_error: 'Failed registration new user',
      text_error: '',
      error_type: 'error',
      error_alert: false,
      valid: false,
      password: '',
      username: '',
      email: '',
      usernameRules: [
        value => !!value || 'The field cannot be empty.',
      ],
      passwordRules: [
        value => !!value || 'The field cannot be empty.',
      ],
      gmailRules: [
        value => !!value || 'The field cannot be empty.',
      ],
    }
  },
  methods: {
    async sendData() {
      try {
        await this.REGISTRATION_NEW_USER({
          username: this.username,
          password: this.password,
          email: this.email
        });
        this.title_error = 'The user was created successfully.';
        this.text_error = 'Check your email address.';
        this.error_type = 'success'
        this.error_alert = true;
        this.valid = false //disabled button, that user can not send request again
      } catch (error) {
        this.text_error = error.response.data.username || error.response.data.email || error.response.data.password;
        this.error_alert = true;
      }
    },
    ...mapActions(["REGISTRATION_NEW_USER"]),
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
