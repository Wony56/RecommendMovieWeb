<template>
  <v-form ref="form">
    <v-layout column>
      <v-flex xs12>
        <v-combobox
          v-model="select"
          :items="items"
          label="영화 장르"
          multiple
          chips
          color="black"
          item-color="black"
        ></v-combobox>
      </v-flex>
      <v-flex xs>
        <v-text-field v-model="title" color="black" label="영화 제목" />
      </v-flex>
      <v-flex xs12>
        <div style="padding-top:10px;">성별우선순위</div>
        <v-btn-toggle v-model="gender">
          <v-btn gender value="M">남성</v-btn>
          <v-btn gender value="F">여성</v-btn>
        </v-btn-toggle>
        <div style="padding-top:10px;">연령별우선순위</div>
        <v-btn-toggle v-model="age">
          <v-btn age value="1">18세 이하</v-btn>
          <v-btn age value="18">18~24세</v-btn>
          <v-btn age value="25">25~34세</v-btn>
          <v-btn age value="35">35~44세</v-btn>
          <v-btn age value="45">45~49세</v-btn>
          <v-btn age value="50">50~55세</v-btn>
          <v-btn age value="56">56세 이상</v-btn>
        </v-btn-toggle>
        <v-btn outlined color="black" block @click="onSubmit">Search</v-btn>
      </v-flex>
    </v-layout>
  </v-form>
</template>


<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
    gender: "",
    text: "",
    title: "",
    genre: "",
    select: "",
    items: [
      "Action",
      "Crime",
      "Thriller",
      "Animation",
      "Children's",
      "Comedy",
      "Adventure",
      "Fantasy",
      "Romance",
      "Drama",
      "Horror",
      "Sci-Fi",
      "Musical",
      "War",
      "Mystery",
      "Documentary"
    ]
  }),
  methods: {
    onSubmit: function() {
      var genres = "";
      for (var i = 0; i < this.select.length; i++) {
        genres += this.select[i] + ",";
      }
      if (this.text == undefined) {
        this.text = "";
      }
      const params = {
        title: this.title,
        genre: genres,
        sort: this.text,
        occupation: "academic/educator",
        gender: this.gender,
        age: "25"
      };
      console.log(this.text);
      this.submit(params);
    }
  }
};
</script>