<template>
  <v-hover v-slot:default="{hover}">
    <v-card flat>
      <v-img :src="`${img}`">
        <!-- 이위에이미지 -->
        <v-expand-transition>
          <div
            v-if="hover"
            class="transition-fast-in-fast-out"
            style="height: 100%; background-color:#000; opacity:0.7; color:#fff;"
          >
            <v-col justify-center text-xs-center>
              <div
                style="font-size:10px; text-align:center;"
                class="text-xs-center justify-center"
              >{{title}}</div>
              <div style="text-align:center">
                <v-rating
                  small
                  :value="rating"
                  color="#ff2f6e"
                  background-color="white"
                  half-increments
                  dense
                  readonly
                  class="justify-center my-2"
                />
              </div>
              <v-row class="justify-center my-2" style="color:#fff;">
                <span style="font-size:12px;">rating : {{ rating.toFixed(1) }}</span>
              </v-row>
              <v-row class="justify-center my-2" style="color:#fff;">
                <span style="font-size:12px;">viewer : {{ viewCnt }}</span>
              </v-row>
            </v-col>
          </div>
        </v-expand-transition>
      </v-img>
    </v-card>
  </v-hover>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      dialog: false
    };
  },
  props: {
    id: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ""
    },
    genres: {
      type: Array,
      default: () => new Array()
    },
    img: {
      type: String,
      default: ""
    },
    rating: {
      type: Number,
      default: 0.0
    },
    viewCnt: {
      type: Number,
      default: 0
    },
    overview: {
      type: String,
      default: ""
    },
    year: {
      type: Number,
      default: 0
    },
    rating_set: {},
    i: {
      type: Number,
      default: 0
    },
    movieListCards: {
      type: Array,
      default: () => new Array()
    }
  },
  mounted() {
    this.searchedList = this.movieListCards.slice();
  },
  computed: {
    genresStr: function() {
      return this.genres.join(" / ");
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
