<template>
  <v-card justify-center text-center width="230" outlined style="border-radius:10px;">
    <v-img :src="`${url}`" v-if="(url!=='')&&(url !=='https://image.tmdb.org/t/p/original')">
      <v-container>
        <div class="text-center" style="padding-top:260px;">
          <v-rating
            v-model="rating"
            hover
            color="#ff2f6e"
            background-color="lightgray"
            half-increments
          ></v-rating>
        </div>
      </v-container>
    </v-img>
    <v-img src="/img/avengers_poster.jpg" v-else>
      <v-container>
        <v-card-text justify-center text-center>
          <div class="text-center">{{title}}</div>
        </v-card-text>
        <div class="text-center" style="padding-top:80px;">
          <v-rating
            v-model="rating"
            hover
            color="yellow darken-3"
            background-color="grey darken-1"
            half-increments
          ></v-rating>
        </div>
      </v-container>
    </v-img>
  </v-card>
</template>

<script>
import api from "../../../api";

export default {
  props: {
    id: Number,
    title: String,
    url: String
  },
  data() {
    return {
      rating: 0
    };
  },
  watch: {
    rating: function(newVal, oldVal) {
      this.registerRating();
    }
  },
  methods: {
    async registerRating() {
      this.$store.state.rating.count++;
      console.log("선택된 갯수" + this.$store.state.rating.count);
      const params = {
        id: this.id,
        rating: this.rating
      };
      await api
        .registerRating(params)
        .then(res => {
          if (res.status === 201) {
            alert("평점 등록완료!");
          }
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>
