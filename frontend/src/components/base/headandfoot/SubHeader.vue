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
      <v-btn text color="#ff2f6e">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
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
      <template v-if="!loggedIn">
        <v-btn
          text
          color="#ff2f6e"
          style="margin-right:15px;"
          @click.stop="$store.state.dialog.signinDialog = true"
        >로그인</v-btn>
        <v-btn
          outlined
          color="#ff2f6e"
          style="margin-right:15px;"
          @click.stop="signupdialog = true"
        >회원가입</v-btn>
      </template>
      <template v-else>
        <v-btn text color="#ff2f6e" style="margin-right:15px;" @click="logout">로그아웃</v-btn>
      </template>
    </v-layout>
    <v-layout justify-end v-if="$vuetify.breakpoint.mdAndDown">
      <v-btn  v-if="!loggedIn" text color="#ff2f6e" fab @click.stop="$store.state.dialog.signinDialog = true">
        <v-icon>mdi-login-variant</v-icon>
      </v-btn>
       <v-btn v-else text color="#ff2f6e" fab @click="logout"><v-icon>mdi-logout-variant</v-icon></v-btn>
      <v-btn text color="#ff2f6e" fab @click.stop="signupdialog = true">
        <v-icon>mdi-account-plus</v-icon>
      </v-btn>
    </v-layout>
    <v-dialog v-model="signupdialog" max-width="400">
      <SignUpPanel />
    </v-dialog>
    <v-dialog v-model="$store.state.dialog.signinDialog" max-width="400">
      <SingInPanel />
    </v-dialog>
  </v-app-bar>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import SignUpPanel from "../login/SignUpPanel.vue";
import SingInPanel from "../login/SignInPanel.vue";
export default {
  components: {
    SignUpPanel,
    SingInPanel
  },
  data() {
    return {
      signindialog: false,
      signupdialog: false,
      loading: false,
      items: [],
      search: null,
      select: null
    };
  },
  computed: mapGetters(["loggedIn"]),
  methods: {
    ...mapActions("data", ["searchMovies"]),
    searchByEnter() {
      this.$router.push("/movies/search");

      const params = {
        title: this.search
      };

      this.searchMovies(params);
    },
    logout() {
      alert(this.$store.state.auth.userInfo.name + "님 로그아웃하셨습니다.");
      this.$cookie.delete("hojin_token");
      this.$store.state.auth.userInfo = null;
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