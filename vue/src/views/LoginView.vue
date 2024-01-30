<template>
<div>
  <div class="container">
    <h2>Login</h2>
    <form>
      <div class="form-group">
        <label for="username">Username:</label>
        <input v-model="username" type="text" id="username" name="username" required>
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input v-model="password" type="password" id="password" name="password" required>
      </div>
      <input @click="sendCredentials" type="button" class="btn" value="Login">
    </form>
  </div>
</div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "LoginView",
  data() {
    return {
      password: '',
      username: '',
    }
  },
  methods: {
    async sendCredentials() {
      try {
        await this.GET_LOGIN({
          username: this.username,
          password: this.password
        });
        this.$nextTick(() => {
          this.$router.push('/');
        })
      } catch (error) {
        console.log(error)
      }
    },
    ...mapActions(["GET_LOGIN"]),
  },
}
</script>

<style scoped>
.container {
  width: 300px;
  margin: 0 auto;
  padding: 20px;
  background-color: #201f1f;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  color: white;
}

.form-group {
  margin-bottom: 15px;
  margin-right: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.btn {
  width: 100%;
  padding: 10px;
  background-color: #444;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn:hover {
  background-color: #666;
}
</style>