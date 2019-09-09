<template>
  <v-container grid-list-md>
    <v-layout justify-center wrap>
      <v-flex xs12 sm8 md8>
        <v-card outlined>
          <v-layout column>
            <v-flex xs8 sm8 md8>
              <v-layout row wrap>
                <v-flex xs12 sm5 md5 align-center justify-center text-xs-center>
                  <span>포스터자리</span>
                </v-flex>
                <v-flex xs12 sm7 md7>
                  <v-card flat>
                    <v-card-text class="filledcolor headline">{{movie.title}}</v-card-text>
                    <v-card-text>장르 : {{genresStr}}</v-card-text>
                    <v-card-text>별점 : {{movie.average_rating}}</v-card-text>
                    <v-card-text>조회수 : {{movie.view_cnt}}</v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex xs12 sm12 md12>
              <v-card flat>
                <v-card-text class="filledcolor headline">영화 본 회원</v-card-text>
              </v-card>
              <v-card flat>
                <v-btn
                  text
                  v-for="(user,i) in movie.rating_set"
                  :key="i"
                  :to="`/user/detail/${user.user-1}`"
                >User{{user.user-1}}</v-btn>
              </v-card>
            </v-flex>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      movie: {
        genres_array: []
      }
    };
  },
  computed: {
    genresStr: function() {
      return this.movie.genres_array.join(" / ");
    }
  },
  methods: {},
  mounted() {
    var params = {
      id: this.$route.query.id
    };
    const apiUrl = "/api";
    axios
      .get(`${apiUrl}/movies/`, {
        params
      })
      .then(res => {
        this.movie = res.data[0];
        console.log(this.movie);
      });
  }
};
</script>

<style>
.filledcolor {
  background-color: #f5f5f5;
  color: #fff;
  text-align: center;
}
</style>