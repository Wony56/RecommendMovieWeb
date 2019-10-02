<template>
  <v-container>
    <v-card style="margin-top:100px;" outlined>
      <v-col class="py-0">
        <v-row>
          <v-flex xs4 md4 sm4>
            <v-card flat height="180" class="text-center align-center">Photo</v-card>
          </v-flex>
          <v-flex xs8 md4 sm4 style="padding-left:20px;">
            <v-card-text
              style="background-color:#ff2f6e; color:#fff;"
              class="text-center title font-weight-black py-0"
            >Profile</v-card-text>
            <v-card-text style="padding-top:10px;">
              <p>UserName : {{user.username}}</p>
              <p>Age : {{user.age}}</p>
              <p>Occupation : {{user.occupation}}</p>
            </v-card-text>
          </v-flex>
          <v-flex xs12 md4 sm4>
            <v-card-text>
              <p>Gender : {{user.gender}}</p>
              <p>SubScirbe : {{subscribeInfo}}</p>
              <span>SubScribe term : {{expireDate}}</span>
              <v-btn style="margin-left:10px; margin-top:-5px" text x-small color="#ff2f6e">기간 연장</v-btn>
              <!--<v-btn style="margin-left:10px; margin-top:-5px" text x-small color="#ff2f6e">해지</v-btn>
              <v-btn style="margin-left:10px; margin-top:-5px" text x-small color="#ff2f6e">구독</v-btn>-->
              <v-btn style="margin-top:15px" outlined color="#ff2f6e" block>회원 정보 수정</v-btn>
            </v-card-text>
          </v-flex>
        </v-row>
        <v-row>
          <v-flex xs12>
            <v-card-text
              style="background-color:#ff2f6e; color:#fff;"
              class="text-center py-1"
            >Like Genre</v-card-text>
          </v-flex>
        </v-row>
        <v-row>
          <v-flex xs12>
            <v-card flat height="180"></v-card>
          </v-flex>
        </v-row>
        <v-row>
          <v-flex xs12>
            <v-card-text
              style="background-color:#ff2f6e; color:#fff;"
              class="text-center py-1"
            >Movie</v-card-text>
          </v-flex>
        </v-row>
        <v-row>
          <v-flex xs12>
            <v-card flat height="180"></v-card>
          </v-flex>
        </v-row>
      </v-col>
    </v-card>
  </v-container>
</template>

<script>
import api from "../../../api";
import { mapState } from "vuex";
import MovieListCard from "../../MovieListCard";

export default {
  computed: {
    ...mapState({
      user: state => state.auth.userInfo
    }),
    date() {
      return {
        watchList: []
      };
    },
    subscribeInfo: function() {
      if (this.user.is_subscribe) {
        return "구독";
      } else {
        return "미구독";
      }
    },
    expireDate: function() {
      if (this.user.is_subscribe) {
        return `~ ${this.user.subscribe_expire.substring(0, 10)}`;
      } else {
        return " - ";
      }
    }
  },
  async created() {
    const params = {
      username: this.user.username
    };

    this.watchList = await api
      .watchList(params)
      .then(res => {
        if (res.status === 200) {
          return res.data;
        }
      })
      .catch(err => {
        alert(err);
      });
  }
};
</script>