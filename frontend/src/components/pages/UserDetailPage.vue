<template>
          <v-card flat outlined :elevation="hover ? 10 : 0">
            <v-layout row justify-center>
              <v-flex xs12 md5 sm5>
                <v-card flat>
                  <v-card-text>사진자리</v-card-text>
                </v-card>
              </v-flex>

              <v-flex xs12 md7 sm7>
                <v-card flat>
                  <v-layout>
                    <v-flex xs12 sm12 md12>
                      <v-card-title headline>회원정보</v-card-title>
                    </v-flex>
                  </v-layout>
                  <v-divider></v-divider>
                  <v-layout row>
                    <v-flex xs6 md6 sm6>
                      <v-card-text>이름 : {{user.username}}</v-card-text>
                    </v-flex>
                    <v-flex>
                      <v-card-text>성별 : {{user.gender}}</v-card-text>
                    </v-flex>
                  </v-layout>
                  <v-layout row>
                    <v-flex xs6 md6 sm6>
                      <v-card-text>나이 : {{user.age}}</v-card-text>
                    </v-flex>
                    <v-flex>
                      <v-card-text>직업 : {{user.occupation}}</v-card-text>
                    </v-flex>
                  </v-layout>
                </v-card>
              </v-flex>
            </v-layout>
            <v-divider></v-divider>
            <v-layout justify-center>
              <v-flex xs12 md12 sm12>
                <v-card flat>
                  <v-card-text>본 영화</v-card-text>
                  <v-divider></v-divider>
                  <v-card-text v-for="(r,i) in user.ratings" :key="i">{{r.movie_name}}</v-card-text>
                </v-card>
              </v-flex>
            </v-layout>
          </v-card>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      user: {}
    };
  },
  computed: {},
  mounted() {
    var params = {
      id: this.$route.params.id
    };
    const apiUrl = "/api";
    axios
      .get(`${apiUrl}/auth/detail/`, {
        params
      })
      .then(res => {
        this.user = res.data;
        console.log(this.user);
      });
  }
};
</script>