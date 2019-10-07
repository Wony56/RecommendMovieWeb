<template>
  <v-card justify-center text-center width="230" outlined style="border-radius:10px;">
    <v-img :src="`${url}`" v-if="(url!=='')&&(url !=='https://image.tmdb.org/t/p/original')">
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
            @click="registerRating"
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
            @click="registerRating"
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
  data: () => ({
    rating: 0
  }),
  methods: {
    registerRating() {
      const params = {
        id: this.id,
        rating: this.rating
      };

      api
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
