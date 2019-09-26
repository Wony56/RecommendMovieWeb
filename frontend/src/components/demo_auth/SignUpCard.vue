<template>
  <div>
    <v-card class="mx-auto" flat dark>
      <v-card-title class="title font-weight-regular justify-space-between">
        <span>{{ currentTitle }}</span>
      </v-card-title>

      <v-window v-model="step">
        <v-window-item :value="1">
          <v-card-text>
            <v-container>
              <v-row justify="center">
                <v-col cols="10">
                  <v-form ref="usernameForm" v-model="usernameValid">
                    <v-text-field v-model="username" :rules="nameRules" label="Username"></v-text-field>
                    <span
                      class="caption grey--text text--darken-1"
                    >This is the username. you will use to login to your account</span>
                  </v-form>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="2">
          <v-card-text>
            <v-container>
              <v-row justify="center">
                <v-col cols="10">
                  <v-form ref="pwdForm" v-model="passwordValid">
                    <v-text-field
                      v-model="password"
                      :rules="passwordRules"
                      label="Password"
                      type="password"
                    ></v-text-field>
                    <v-text-field
                      v-model="re_password"
                      :rules="rePasswordRules"
                      label="Confirm Password"
                      type="password"
                    ></v-text-field>
                    <span
                      class="caption grey--text text--darken-1"
                    >Please enter a password for your account</span>
                  </v-form>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="3">
          <v-card-text>
            <v-container>
              <v-form ref="infoForm" v-model="ageValid">
                <v-row justify="center">
                  <v-col cols="12" sm="6">
                    <div>Gender</div>
                    <v-col cols="12">
                      <v-radio-group v-model="gender" row>
                        <v-radio label="Man" value="M"></v-radio>
                        <v-radio label="Woman" value="W"></v-radio>
                      </v-radio-group>
                    </v-col>
                    <div>Age</div>
                    <v-col cols="5">
                      <v-text-field
                        class="age-input"
                        v-model="age"
                        placeholder="ex) 20"
                        type="number"
                        :rules="ageRules"
                        suffix="세"
                      ></v-text-field>
                    </v-col>
                  </v-col>
                </v-row>
              </v-form>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="4">
          <v-card-text>
            <v-container>
              <v-row justify="center">
                <v-col cols="12" sm="6">
                  <v-col cols="12">
                    <v-combobox v-model="occupation" :items="items" label="Occupation"></v-combobox>
                  </v-col>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="5">
          <v-card-text>
            <div>구독을 하시면 영화 추천서비스를 이용하실 수 있습니다.</div>
            <div>구독하시겠습니까?</div>
            <v-container>
              <v-row justify="end">
                <v-col cols="12" sm="6">
                  <v-row justify="end">
                    <v-btn color="red" @click="agreeSubscribe">구독하기</v-btn>
                    <v-btn @click="passSubscibe">건너띄기</v-btn>
                  </v-row>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>
      </v-window>

      <v-divider></v-divider>

      <v-card-actions>
        <v-btn :disabled="step === 1" text @click="step--">Back</v-btn>
        <div class="flex-grow-1"></div>
        <v-btn :disabled="step === 5" v-if="step !== 5" color="primary" depressed @click="next">Next</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import api from "../../api";

export default {
  data() {
    return {
      usernameValid: true,
      passwordValid: true,
      ageValid: false,
      step: 1,
      username: "",
      password: "",
      re_password: "",
      gender: "M",
      age: "",
      nameRules: [v => !!v || "Username 입력은 필수입니다."],
      passwordRules: [
        v => !!v || "패스워드 입력은 필수입니다.",
        v => v.length >= 4 || "패스워드의 길이는 4글자 이상이어야 합니다."
      ],
      rePasswordRules: [
        v => !!v || "패스워드 확인이 필요합니다.",
        v => v === this.password || "패스워드가 일치하지 않습니다."
      ],
      ageRules: [v => !!v || "나이 입력은 필수입니다."],
      occupation: "academic/educator",
      isSubscribe: false,
      items: [
        "academic/educator",
        "artist",
        "clerical/admin",
        "college/grad student",
        "customer service",
        "doctor/health care",
        "executive/managerial",
        "farmer",
        "homemaker",
        "K-12 student",
        "lawyer",
        "programmer",
        "retired",
        "sales/marketing",
        "scientist",
        "self-employed",
        "technician/engineer",
        "tradesman/craftsman",
        "unemployed",
        "writer",
        "other"
      ]
    };
  },

  computed: {
    currentTitle() {
      switch (this.step) {
        case 1:
          return "Sign-up";
        case 2:
          return "Create a password";
        case 3:
          return "Gender & Age";
        case 4:
          return "Occupation";
        case 5:
          return "Subscribe";
        default:
          return "Account created";
      }
    }
  },
  methods: {
    next() {
      if (this.step === 1) {
        //사용자 중복 체크
        if (this.$refs.usernameForm.validate()) {
          const params = {
            username: this.username
          };
          api
            .checkDuplicate(params)
            .then(res => {
              if (res.status === 200) {
                this.step++;
              }
            })
            .catch(err => {
              if (err.response.status === 400) {
                const message = err.response.data;
                alert(message);
              }
            });
        }
      } else if (this.step === 2) {
        if (this.$refs.pwdForm.validate()) {
          this.step++;
        }
      } else if (this.step === 3) {
        if (this.$refs.infoForm.validate()) {
          this.step++;
        }
      } else {
        this.step++;
      }
    },
    signup() {
      const params = {
        username: this.username,
        password: this.password,
        gender: this.gender,
        age: parseInt(this.age),
        occupation: this.occupation,
        is_subscribe: this.isSubscribe
      };

      api
        .signup(params)
        .then(res => {
          if (res.status === 201) {
            alert("회원이 되신 것을 축하드립니다.");

            const user = {
              username: this.username,
              password: this.password
            };

            api
              .login(user)
              .then(res => {
                if (res.status === 200) {
                  this.$store.state.auth.userInfo = res.data;
                  this.$cookies.set("user", res.data.username, "30min");

                  this.$router.push("/");
                }
              })
              .catch(err => {
                alert(err);
              });
          }
        })
        .catch(err => {
          alert(err);
        });
    },

    agreeSubscribe() {
      this.isSubscribe = true;

      this.signup();
    },

    passSubscibe() {
      this.isSubscribe = false;

      this.signup();
    }
  }
};
</script>

<style scoped>
.age-input {
  text-align: right;
}
</style>