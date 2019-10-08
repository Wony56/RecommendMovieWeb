<template>
  <v-container>
    <v-layout row class="justify-center text-center">
      <v-flex mx-4 my-1 xs2 v-for="(card) in movieListCardsSliced" :key="card.id"  flat height="180">
        <MovieCard 
          :id='card.id' 
          :title='card.title' 
          :genres_array='card.genres_array' 
          :viewCnt='card.view_cnt' 
          :timeStamp='card.timeStamp' 
          :year='card.year' 
          :overview='card.overview' 
          :rating='card.rrating' 
          :img='card.poster_path'
        />
      </v-flex>

      <v-pagination
        v-if="maxPages > 1"
        v-model="page"
        :length="maxPages"
        :total-visible="11"
        dark
        color="#ff2f6e"
        background-color="#ff2f6e"
        circle
      />
    </v-layout>
  </v-container>
</template>

<script>
import MovieCard from "./base/card/MovieCard.vue";

export default {
  components: {
    MovieCard
  },
  props: {
    movieListCards: {
      type: Array,
      default: () => new Array()
    }
  },
  data: () => ({
    cardsPerPage: 10,
    page: 1,
    text: "",
    searchedList: [],
    tempList: [],
    value: "",
    lists: {
      
    }
  }),
  mounted() {
    this.searchedList = this.movieListCards.slice();
  },
  computed: {
    // pagination related variables
    movieListEmpty: function() {
      return this.movieListCards.length === 0;
    },
    maxPages: function() {
      return Math.floor(
        (this.searchedList.length + this.cardsPerPage - 1) / this.cardsPerPage
      );
    },
    movieListCardsSliced: function() {
      return this.searchedList.slice(
        this.cardsPerPage * (this.page - 1),
        this.cardsPerPage * this.page
      );
    }
  },

  watch: {
    movieListCards() {
      this.searchedList = this.movieListCards.slice();
      console.log(this.searchedList);
      this.tempList = this.searchedList;
    },
  },
  methods: {
    
  }
};
</script>