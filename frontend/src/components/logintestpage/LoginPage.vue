<template>
  <v-container>
    <v-layout row class="text-xs-center">
      <v-flex xs3 style="background-image: url('http://cdn.wallpapersafari.com/7/86/gqiGH7.jpg')">
        <v-card height="500px"></v-card>
      </v-flex>
      <v-flex xs4 class="grey lighten-4">
        <v-container style="position: relative;top: 13%;" class="text-xs-center">
          <v-card flat>
            <v-card-title primary-title>
              <h4>Login</h4>
            </v-card-title>
            <v-form>
              <v-text-field prepend-icon="person" v-model="username" label="Username"></v-text-field>
              <v-text-field prepend-icon="lock" v-model="password" label="Password" type="password"></v-text-field>
              <v-card-actions>
                <v-btn primary large block @click="onSubmit">Login</v-btn>
              </v-card-actions>
            </v-form>
          </v-card>
        </v-container>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import api from "../../api";

export default {
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    onSubmit() {
      const params = {
        username: this.username.trim(),
        password: this.password.trim()
      };

      api
        .login(params)
        .then(res => {
          if (res.status === 200) {
            console.log(JSON.stringify(res.data));
            this.$cookie.set("hojin_token", res.data.token, { expires: "30m" });
            this.$router.push("/");
          }
        })
        .catch(err => {
          alert(err);
        });
    }
  }
};
</script>