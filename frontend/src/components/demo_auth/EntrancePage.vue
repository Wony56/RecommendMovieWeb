<template>
  <div class="hello">
    <v-card max-width="600" class="mx-auto" dark>
      <v-card-title class="text-center justify-center py-6">
        <h1 class="font-weight-bold display-3 basil--text">SHEEPCHA</h1>
      </v-card-title>

      <v-tabs v-model="tab" background-color="transparent" grow>
        <v-tab v-for="item in items" :key="item">{{ item }}</v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab" dark>
        <v-tab-item v-for="item in items" :key="item">
          <v-card flat dark>
            <template v-if="item === '로그인'">
              <v-card-text>
                <v-form ref="form" v-model="valid" lazy-validation>
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
            </template>
            <template v-else>
              <v-card-text>
                <signup-card />
              </v-card-text>
            </template>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </div>
</template>

<script>
import api from "../../api";
import SignUpCard from "./SignUpCard";

export default {
  components: {
    "signup-card": SignUpCard
  },
  data() {
    return {
      tab: null,
      items: ["로그인", "회원가입"],
      valid: true,
      username: "",
      nameRules: [v => !!v || "Username입력은 필수입니다."],
      password: "",
      passwordRules: [
        v => !!v || "패스워드입력은 필수입니다.",
        v => v.length >= 4 || "패스워드의 길이는 4글자 이상이어야 합니다."
      ]
    };
  },
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
            }
          })
          .catch(err => {
            alert(err);
          });
      }
    }
  }
};
</script>

<style scoped>
.hello {
  height: 100%;
  background: #356859;
  background-image: url("https://cdn.onebauer.media/one/media/5d20/5d91/a205/650c/a1d3/d71f/empire-joker-subscriber-cover-crop.jpeg?quality=50&width=1800&ratio=16-9&resizeStyle=aspectfill&format=jpg");
}
.basil {
  background-color: #fffbe6 !important;
}
.basil--text {
  color: white !important;
}
</style>