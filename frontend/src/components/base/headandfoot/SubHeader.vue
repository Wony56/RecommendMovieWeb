<template>
  <v-app-bar id="bars_id" flat fixed height="75" outlined>
    <v-layout justify-start v-if="$vuetify.breakpoint.mdAndUp">
      <v-toolbar-title style="margin-top:-5px;">
        <router-link to="/" style="color:#ff2f6e; text-decoration:none;">
          <span style="font-weight:800;">SHEEPCHA</span>
        </router-link>
      </v-toolbar-title>
    </v-layout>
    <v-layout justify-start v-if="$vuetify.breakpoint.mdAndDown">
     <router-link to="/" style="color:#ff2f6e; text-decoration:none;">
        <v-icon color="#ff2f6e">mdi-home</v-icon>
     </router-link>
    </v-layout>
    <v-layout justify-center mx-5>
      <v-text-field
        style="margin-top:30px;"
        prepend-inner-icon="mdi-magnify"
        flat
        color="#ff2f6e"
        v-model="search"
        background-color="#f5f6f6"
        round
        id="search_form2"
        solo
        @keyup.13="searchByEnter"
        placeholder="작품 제목, 배우, 감독을 검색해보세요."
      ></v-text-field>
    </v-layout>
    <v-layout justify-end v-if="$vuetify.breakpoint.mdAndUp">

      <template v-if="loggedIn">
        <v-btn text color="#ff2f6e" style="margin-right:15px;" @click="profile">프로필</v-btn>
        <v-btn text color="#ff2f6e" style="margin-right:15px;" @click="logout">로그아웃</v-btn>
      </template>
    </v-layout>
    <v-layout justify-end v-if="$vuetify.breakpoint.mdAndDown">
      <v-btn v-if="loggedIn" text fab @click="profile">
        <v-icon  color="#ff2f6e">mdi-account-circle-outline</v-icon>
      </v-btn>
      <v-btn v-if="loggedIn" text color="#ff2f6e" fab @click="logout">
        <v-icon>mdi-logout-variant</v-icon>
      </v-btn>
    </v-layout>
  </v-app-bar>
</template>

<script>
import { mapState, mapActions, mapGetters } from "vuex";
import api from "../../../api";

export default {
  components: {},
  data() {
    return {
      loading: false,
      items: [],
      search: null,
      select: null
    };
  },
  computed: {
    ...mapState({
      user: state => state.auth.userInfo
    }),
    ...mapGetters(["loggedIn"])
  },
  methods: {
    ...mapActions("data", ["searchMovies"]),
    searchByEnter() {
      this.$router.push("/movies/search");
      this.$store.state.search=this.search;
      const params = {
        title: this.search
      };

      this.searchMovies(params);
    },
    logout() {
      api
        .logout()
        .then(res => {
          if (res.status === 200) {
            alert(this.user.username + "님 로그아웃하셨습니다.");
            this.$cookies.remove("user");
            this.$store.state.auth.userInfo = null;
            this.$router.push("/entrance");
          }
        })
        .catch(err => {
          alert(err);
        });
    },
    profile() {
      this.$router.push(`/user/detail/${this.user.username}`);
    }
  }
};
</script>

<style >
#search_form2::placeholder {
  font-weight: 500;
  color: lightgray;
}
#bars_id {
  border-bottom: 1px solid lightgray;
}
</style>