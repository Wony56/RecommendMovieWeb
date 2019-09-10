<template>
  <v-app>
    <Header v-if="loggedIn" />
    <v-content style="background-color:#fff">
      <router-view />
    </v-content>
    <Footer v-if="loggedIn" />
  </v-app>
</template>

<script>
import router from "./router";
import Footer from "./components/base/headandfoot/Footer.vue";
import Header from "./components/base/headandfoot/SubHeader.vue";
import { mapGetters } from "vuex";

export default {
  components: {
    Footer,
    Header
  },
  data: () => ({
    drawer: null,
    choices: [
      {
        icon: "mdi-movie",
        text: "영화 검색",
        path: "movie-search"
      }
    ]
  }),
  computed: mapGetters(["loggedIn"]),
  methods: {
    goTo: function(path) {
      router.push({ name: path });
    }
  }
};
</script>

<style>
* {
  font-family: "Noto Sans KR", sans-serif;
}
</style>