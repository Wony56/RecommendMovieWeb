<template>
  <v-card style="border-radius:20px;">
    <v-card-text
      style="font-size:30px; text-align:center; background-color:#ff2f6e; color:#fff;"
    >Sign In</v-card-text>
    <v-card-text class="ma-0">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="username"
          color="#ff2f6e"
          :counter="10"
          :rules="nameRules"
          label="이름을 입력해주세요"
          required
        ></v-text-field>

        <v-text-field v-model="password" color="#ff2f6e" label="비밀번호를 입력해주세요" required></v-text-field>

        <v-btn
          block
          color="#ff2f6e"
          rounded
          outlined
          class="mr-4"
          @click="onSubmit"
          row
          justify-start
        >LOGIN</v-btn>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
import api from "../../../api";
export default {
  data: () => ({
    valid: true,
    username: "",
    password: "",
    nameRules: [
      v => !!v || "Name is required",
      v => (v && v.length <= 10) || "Name must be less than 10 characters"
    ]
  }),

  methods: {
    reset() {
      this.$refs.form.reset();
    },
    onSubmit() {
      const params = {
        username: this.username.trim(),
        password: this.password.trim()
      };

      api
        .login(params)
        .then(res => {
          if (res.status === 200) {
            this.$store.state.auth.userInfo = res.data;
            this.$cookie.set("hojin_token", res.data.token, { expires: "30m" });
            this.$store.state.dialog.signinDialog = false;
            alert(res.data.name + "님 로그인하셨습니다.");
          }
        })
        .catch(err => {
          alert(err);
        });
    }
  }
};
</script>