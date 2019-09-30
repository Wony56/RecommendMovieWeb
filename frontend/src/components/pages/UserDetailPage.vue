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
              <v-card-text>나이 : {{user.age}}세</v-card-text>
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
      <v-card flat>
        <v-card-text class="text-center">본 영화</v-card-text>
        <v-divider></v-divider>
        <v-container>
          <v-row>
            <template v-if="watchList.length !== 0">
              <v-flex xs6 sm3 md2 v-for="(card) in movieListCardsSliced" :key="card.id" pa-2>
                <MovieListCard
                  :id="card.id"
                  :img="card.img"
                  :title="card.title"
                  :genres="card.genres"
                  :rating="card.rating"
                  :view-cnt.sync="card.viewCnt"
                  :overview="card.overview"
                  :year="card.year"
                  :rating_set="card.rating_set"
                  :movieListCards="movieListCards"
                />
              </v-flex>
            </template>
            <template v-else>아직 본 영화가 없습니다.</template>
          </v-row>
        </v-container>
      </v-card>
    </v-layout>
  </v-card>
</template>

<script>
import api from "../../api";
import { mapState } from "vuex";
import MovieListCard from "../MovieListCard";

export default {
  component: {
    MovieListCard
  },
  data() {
    return {
      hover: false,
      watchList: []
    };
  },
  computed: {
    ...mapState({
      user: state => state.auth.userInfo
    })
  },
  async created() {
    const params = {
      username: this.user.username
    };

    this.watchList = await api
      .watchList(params)
      .then(res => {
        if (res.status === 200) {
          return res.data;
        }
      })
      .catch(err => {
        alert(err);
      });
  }
};
</script>