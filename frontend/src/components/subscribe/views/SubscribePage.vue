<template>
  <v-container fluid>
    <v-col>
      <div class="text-center justify-center headline">선호하는 영화를 선택 해주세요</div>
      <br />
      <div class="text-right">
        <v-btn outlined style="margin-right:10px" color="#ff2f6e" @click="gotomain">건너뛰기</v-btn>
        <v-btn
          v-if="$store.state.rating.count === 10"
          outlined
          color="#ff2f6e"
          @click="subscribe"
        >구독하기</v-btn>
      </div>
      <br />
      <v-row>
        <v-progress-linear v-model="select" height="25" reactive color="#ff2f6e" rounded>
          <strong>{{ Math.ceil(select) }}%</strong>
        </v-progress-linear>
      </v-row>
      <v-row class="justify-center my-5 mx-0">
        <template v-for="(movie, key) in movieList">
          <v-flex xs6 sm3 md2 my-1 mx-3 :key="key">
            <SubScribeCard :id="movie.id" :title="movie.title" :url="movie.poster_path" />
          </v-flex>
        </template>
      </v-row>
    </v-col>
  </v-container>
</template>

<script>
import SubScribeCard from "../card/SubScribeCard";
import api from "../../../api";

export default {
  data: () => ({
    select: 80,
    movieList: []
  }),
  components: {
    SubScribeCard
  },
  async created() {
    this.movieList = await api
      .searchMovies()
      .then(res => {
        if (res.status === 200) {
          return res.data;
        }
      })
      .catch(err => {
        console.log(err);
      });

    this.movieList.sort(() => {
      return Math.random() - Math.random();
    });

    this.movieList = this.movieList.slice(0, 30);
  },
  methods: {
    gotomain() {
      this.$router.push("home");
    },
    subscribe() {
      api
        .subscribe()
        .then(res => {
          if (res.status === 200) {
            alert("구독신청완료!");
            api
              .getProfile()
              .then(res => {
                if (res.status === 200) {
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
    }
  }
};
</script>
