<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout justify-end>
      <v-btn-toggle v-model="text">
        <v-btn text outlined color="#ff2f6e" value="searchbyviewcount">조회수</v-btn>
        <v-btn text outlined color="#ff2f6e" value="searchbyrating">평점</v-btn>
        <v-btn text outlined color="#ff2f6e" value="searchbygender">성별</v-btn>
        <v-btn text outlined color="#ff2f6e" value="searchbyoccupation">직업별</v-btn>
        <v-btn text outlined color="#ff2f6e" value="searchbyage">연령별</v-btn>
      </v-btn-toggle>
      <v-select v-model="value" :items="lists[text]"></v-select>
    </v-layout>
    <v-layout row wrap>
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
import MovieListCard from "./MovieListCard";
import axios from "axios";

export default {
  components: {
    MovieListCard
  },
  props: {
    movieListCards: {
      type: Array,
      default: () => new Array()
    }
  },
  data: () => ({
    cardsPerPage: 12,
    page: 1,
    text: "",
    searchedList: [],
    tempList: [],
    value: "",
    lists: {
      searchbyviewcount: ["많은순", "적은순"],
      searchbyrating: ["높은순", "낮은순"],
      searchbygender: ["남성", "여성"],
      searchbyoccupation: [
        "필터 없음",
        "other",
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
        "writer"
      ],
      searchbyage: [
        "필터 없음",
        "18세 이하",
        "18~24세",
        "25~34세",
        "35~44세",
        "45~49세",
        "50~55세",
        "56세 이상"
      ]
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
      // console.log(this.movieListCards.slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page))
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
    value() {
      console.log("정렬");
      console.log(this.value);

      if (this.value === "많은순") {
        this.searchedList = this.searchedList.sort(function(a, b) {
          return a.viewCnt > b.viewCnt ? -1 : 1;
        });
        this.page = 1;
      } else if (this.value === "적은순") {
        this.searchedList = this.searchedList.sort(function(a, b) {
          return a.viewCnt < b.viewCnt ? -1 : 1;
        });
        this.page = 1;
      } else if (this.value === "높은순") {
        this.searchedList = this.searchedList.sort(function(a, b) {
          return a.rating > b.rating ? -1 : 1;
        });
        this.page = 1;
      } else if (this.value === "낮은순") {
        this.searchedList = this.searchedList.sort(function(a, b) {
          return a.rating < b.rating ? -1 : 1;
        });
        this.page = 1;
      } else if (this.value === "남성") {
        this.searchedList = this.searchedList.sort(function(a, b) {
          return a.mcount > b.mcount ? -1 : 1;
        });
        this.page = 1;
      } else if (this.value === "여성") {
        this.searchedList = this.searchedList.sort(function(a, b) {
          return a.mcount < b.mcount ? -1 : 1;
        });
        this.page = 1;
      } else if (this.value === "필터 없음") {
        this.searchedList = this.tempList;

        this.page = 1;
      } else if (this.value === "other") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "other";
        });
        this.page = 1;
      } else if (this.value === "academic/educator") {
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "academic/educator";
        });
        this.page = 1;
      } else if (this.value === "artist") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "artist";
        });
        this.page = 1;
      } else if (this.value === "clerical/admin") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "clerical/admin";
        });
        this.page = 1;
      } else if (this.value === "college/grad student") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "college/grad student";
        });
        this.page = 1;
      } else if (this.value === "customer service") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "customer service";
        });
        this.page = 1;
      } else if (this.value === "doctor/health care") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "doctor/health care";
        });
        this.page = 1;
      } else if (this.value === "executive/managerial") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "executive/managerial";
        });
        this.page = 1;
      } else if (this.value === "farmer") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "farmer";
        });
        this.page = 1;
      } else if (this.value === "homemaker") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "homemaker";
        });
        this.page = 1;
      } else if (this.value === "K-12 student") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "K-12 student";
        });
        this.page = 1;
      } else if (this.value === "lawyer") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "lawyer";
        });
        this.page = 1;
      } else if (this.value === "programmer") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "programmer";
        });
        this.page = 1;
      } else if (this.value === "retired") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "retired";
        });
        this.page = 1;
      } else if (this.value === "sales/marketing") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "sales/marketing";
        });
        this.page = 1;
      } else if (this.value === "scientist") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "scientist";
        });
        this.page = 1;
      } else if (this.value === "self-employed") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "self-employed";
        });
        this.page = 1;
      } else if (this.value === "technician/engineer") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "technician/engineer";
        });
        this.page = 1;
      } else if (this.value === "tradesman/craftsman") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "tradesman/craftsman";
        });
        this.page = 1;
      } else if (this.value === "unemployed") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "unemployed";
        });
        this.page = 1;
      } else if (this.value === "writer") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.count == "writer";
        });
        this.page = 1;
      } else if (this.value === "18세 이하") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.agecount == "1";
        });
        this.page = 1;
      } else if (this.value === "18~24세") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.agecount == "18";
        });
        this.page = 1;
      } else if (this.value === "25~34세") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.agecount == "25";
        });
        this.page = 1;
      } else if (this.value === "35~44세") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.agecount == "35";
        });
        this.page = 1;
      } else if (this.value === "45~49세") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.agecount == "45";
        });
        this.page = 1;
      } else if (this.value === "50~55세") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.agecount == "50";
        });
        this.page = 1;
      } else if (this.value === "56세 이상") {
        this.searchedList = this.tempList;
        this.searchedList = this.searchedList.filter(function(a) {
          return a.agecount == "56";
        });
        this.page = 1;
      } else {
        this.searchedList = this.movieListCards.slice();
        this.page = 1;
      }
    }
  },
  methods: {
    godetail(id, idx) {
      // console.log(this.movieListCards,id,idx)
      this.movieListCards[idx]["viewCnt"]++;
      var params = {
        id: this.movieListCards[idx]["id"],
        view_cnt: this.movieListCards[idx]["viewCnt"]
      };
      // console.log(params)
      const apiUrl = "/api";
      axios
        .get(`${apiUrl}/update_view_cnt/`, {
          params
        })
        .then(() => {});
    }
  }
};
</script>