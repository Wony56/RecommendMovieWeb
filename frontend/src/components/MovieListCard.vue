<template>
  <v-hover v-slot:default="{hover}">
    <v-card id="hoverScale">
      <v-img :src="`${img}`" v-if="(img!=='')&&(img!=='https://image.tmdb.org/t/p/original')">
        <!-- <v-img src="/img/avengers_poster.jpg"> -->
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
                class="text-xs-center justify-center my-5"
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
                <span style="font-size:12px;">rating : {{ rating.toFixed(2) }}</span>
              </v-row>
              <v-row class="justify-center my-2" style="color:#fff;">
                <span style="font-size:12px;">viewer : {{ viewCnt }}</span>
              </v-row>
              <v-btn
                small
                color="#ff2f6e"
                class="my-5"
                outlined
                block
                @click.stop="dialog = true"
                @click="godetail(id)"
              >detail</v-btn>
            </v-col>
          </div>
        </v-expand-transition>
        <v-dialog v-model="dialog" max-width="1100">
          <v-card rounded color="black">
            <v-row class="mx-0">
              <v-flex xs12 sm4 md4>
                <v-img :src="`${img}`">
                  <!-- 이위에이미지 -->
                </v-img>
              </v-flex>
              <v-flex xs12 sm8 md8>
                <div
                  class="display-2 mx-7 my-4"
                  style="font-weight:300; font-size:35px; color:#fff;"
                >{{title}}</div>
                <div class="mx-7 mx-3" style="color:lightgray">{{ genresStr }}</div>
                <div class="mx-7 mx-3" style="color:lightgray">{{ year }}</div>
                <!-- 날짜 -->
                <div class="mx-7">
                  <v-rating
                    large
                    :value="rating"
                    color="#ff2f6e"
                    background-color="white"
                    half-increments
                    dense
                    readonly
                    class="justify-center my-2"
                  />
                </div>
                <div class="mx-7" style="line-height: 1.3em; color:gray;">{{overview}}</div>
                <!-- 이위에 영화내용 -->
                <div class="mx-7" style="color:white;">
                  조회수 :
                  <span style=" margin-left:10px; color:#ff2f6e">{{ viewCnt }}</span>
                  평점 :
                  <span
                    style=" margin-left:10px; color:#ff2f6e "
                  >{{ rating.toFixed(1) }}</span>
                </div>
                <div class="mx-7 my-4" style="background-color:#2e2e2e">
                <!-- <v-flex>
                    <v-btn
                      text
                      color="#fff"
                      v-for="(user,i) in rating_set"
                      :key="i"
                      :to="`/user/detail/${user.user-1}`"
                    >User{{user.user-1}}</v-btn>
                  
                </v-flex> -->
                </div>
                <div>
                  <!-- <TopEight :movieId='id'/> -->
                </div>
              </v-flex>
            </v-row>
          </v-card>
        </v-dialog>
      </v-img>
      <v-img src="/img/avengers_poster.jpg" v-else>
        <v-expand-transition>
          <div
            v-if="hover"
            class="transition-fast-in-fast-out"
            style="height: 100%; background-color:#000; opacity:0.7; color:#fff;"
          >
            <v-col justify-center text-xs-center>
              <div
                style="font-size:10px; text-align:center;"
                class="text-xs-center justify-center my-5"
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
                <span style="font-size:12px;">rating : {{ rating.toFixed(2) }}</span>
              </v-row>
              <v-row class="justify-center my-2" style="color:#fff;">
                <span style="font-size:12px;">viewer : {{ viewCnt }}</span>
              </v-row>
              <v-btn
                small
                color="#ff2f6e"
                class="my-5"
                outlined
                block
                @click.stop="dialog = true"
              >detail</v-btn>
            </v-col>
          </div>
        </v-expand-transition>
        <v-dialog v-model="dialog" max-width="1100">
          <v-card rounded color="black">
            <v-row class="mx-0">
              <v-flex xs12 sm4 md4>
                <v-img src="/img/avengers_poster.jpg">
                  <!-- 이위에이미지 -->
                </v-img>
              </v-flex>
              <v-flex xs12 sm8 md8>
                <div
                  class="display-2 mx-7 my-4"
                  style="font-weight:300; font-size:35px; color:#fff;"
                >{{title}}</div>
                <div class="mx-7 mx-3" style="color:lightgray">{{ genresStr }}</div>
                <div class="mx-7 mx-3" style="color:lightgray">{{ year }}</div>
                <!-- 날짜 -->
                <div class="mx-7">
                  <v-rating
                    large
                    :value="rating"
                    color="#ff2f6e"
                    background-color="white"
                    half-increments
                    dense
                    readonly
                    class="justify-center my-2"
                  />
                </div>
                <div class="mx-7" style="line-height: 1.3em; color:gray;">{{overview}}</div>
                <!-- 이위에 영화내용 -->
                <div class="mx-7" style="color:gray;">
                  <v-icon style="color:gray;">mdi-eye</v-icon>
                  <span style=" margin-left:10px; color:#ff2f6e">{{ viewCnt }}</span>
                  <v-icon style="color:gray; margin-left:10px;">mdi-star</v-icon>
                  <span style=" margin-left:10px; color:#ff2f6e ">{{ rating.toFixed(1) }}</span>
                </div>
                <!-- <div>
                  <v-card flat>
                    <v-btn
                      text
                      v-for="(user,i) in rating_set"
                      :key="i"
                      :to="`/user/detail/${user.user-1}`"
                    >User{{user.user-1}}</v-btn>
                  </v-card>
                </div> -->
                <div>
                  <!-- <TopEight/> -->
                </div>
              </v-flex>
            </v-row>
          </v-card>
        </v-dialog>
      </v-img>
    </v-card>
  </v-hover>
</template>

<script>
import axios from "axios";
import TopEight from "../components/base/layout/TopEightLayout.vue"
export default {
  data() {
    return {
      dialog: false
    };
  },
  components: {
    TopEight
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
    rating_set:{
     
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
    godetail(id) {
      // console.log(this.movieListCards,id,idx)
      this.$emit("update:view-cnt", this.viewCnt+1);
      // this.movieListCards[idx]['viewCnt']++ 
      var params = {
        id : this.id
      }
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

<style>
#hoverScale {
  -webkit-transition: all 200ms ease-in;
  -webkit-transform: scale(1);
  -ms-transition: all 200ms ease-in;
  -ms-transform: scale(1);
  -moz-transition: all 200ms ease-in;
  -moz-transform: scale(1);
  transition: all 200ms ease-in;
  transform: scale(1);
}
#hoverScale:hover {
  z-index: 2;
  -webkit-transition: all 200ms ease-in;
  -webkit-transform: scale(1.3);
  -ms-transition: all 200ms ease-in;
  -ms-transform: scale(1.3);
  -moz-transition: all 200ms ease-in;
  -moz-transform: scale(1.3);
  transition: all 200ms ease-in;
  transform: scale(1.3);
}
</style>