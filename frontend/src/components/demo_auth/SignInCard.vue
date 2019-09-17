<template>
  <div>
    <v-card class="mx-auto" flat>
      <v-card-title class="title font-weight-regular justify-space-between">
        <span>Sign-In</span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="valid">
          <v-text-field v-model="username" :rules="nameRules" label="Username" required></v-text-field>
          <v-text-field
            v-model="password"
            type="password"
            :rules="passwordRules"
            label="Password"
            required
          ></v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn block text color="success" class="mr-4" @click="login">로그인</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import api from "../../api";

export default {
  data: () => ({
    valid: true,
    username: "",
    nameRules: [v => !!v || "Username입력은 필수입니다."],
    password: "",
    passwordRules: [
      v => !!v || "패스워드입력은 필수입니다.",
      v => v.length >= 4 || "패스워드의 길이는 4글자 이상이어야 합니다."
    ]
  }),
  methods: {
    login() {
      const params = {
        username: this.username,
        password: this.password
      };

      if (this.$refs.form.validate()) {
        api
          .login(params)
          .then(res => {
            if (res.status === 200) {
              this.$store.state.auth.userInfo = res.data;
              this.$cookies.set("user", res.data.username, "30min");

              this.$router.replace("/");
            }
          })
          .catch(err => {
            if (err.response.status === 401) {
              const message = err.response.data;
              alert(message);
            }
          });
      }
    }
  }
};
</script>