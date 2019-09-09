<!-- 영화 검색 페이지 -->
<template>
    <v-container grid-list-md style="margin-top:60px; background-color:#fff;">
      <v-layout justify-center wrap>
        <v-flex xs12>
          <MovieList :movie-list-cards="movieList" />
        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex"; 
import MovieList from "../MovieList.vue";
import TopEight from '../base/layout/TopEightLayout.vue';
export default {
  components: {
    TopEight,
    MovieList,
  },
  data: () => ({}),
  computed: {
    ...mapState({
      movieList: state => state.data.movieSearchList
    })
  },
  created() {
    console.log(this.$store.state.Header);
  },
  methods: mapActions("data", ["searchMovies"])
};
</script>
