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
              <v-btn
                style="margin-left:10px; margin-top:-5px"
                text
                x-small
                color="#ff2f6e"
                @click="subscibe"
              >기간 연장</v-btn>
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
<<<<<<< HEAD
=======
            <template v-for="item in recommendList">
              <template v-for="(value,key) in item">{{key}}:{{value}}</template>
            </template>
>>>>>>> develop
          </v-flex>
        </v-row>
        <v-row class="justify-center text-center">
            <v-flex mx-4 my-1 xs2 v-for="(item,index) in recommendations" :key=index flat height="180">
              <MovieCard 
              :id='recommendations[index].id' 
              :title='recommendations[index].title' 
              :genres_array='recommendations[index].genres_array' 
              :viewCnt='recommendations[index].view_cnt' 
              :timeStamp='recommendations[index].timeStamp' 
              :year='recommendations[index].year' 
              :overview='recommendations[index].overview' 
              :rating='recommendations[index].rrating' 
              :img='recommendations[index].poster_path'
              />
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
        <v-row class="justify-center text-center">
          <v-flex>
              <MovieSeen :movieListCards="watchList" />
          </v-flex>
        </v-row>
      </v-col>
    </v-card>
  </v-container>
</template>

<script>
import api from "../../../api";
import { mapState } from "vuex";
import MovieCard from "../../base/card/MovieCard.vue";
import MovieSeen from "../../MovieSeen.vue";

export default {
  components: {
    MovieCard,
    MovieSeen
  },
  data() {
      return {
        watchList: [],
        recommendList: []
      };
  },
  computed: {
    ...mapState({
      user: state => state.auth.userInfo
    }),
    recommendations: function() {
      return this.recommendList;
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
        return ` ~ ${this.user.subscribe_expire.substring(0, 10)}`;
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
    // SVD
    this.recommendList = await api
<<<<<<< HEAD
    .recommendSVD(params)
    .then(res=> {
      console.log(res.data)
      if(res.status === 200){
        this.$forceUpdate();
        return res.data;
      }
    })
    .catch(err=>{
      alert(err)
    })
    // // KNN 지우지마세요 사용할거에요
    // this.recommendList = await api
    // .recommendKNN(params)
    // .then(res=> {
    //   console.log(res.data)
    //   if(res.status === 200){
    //     this.$forceUpdate();
    //     return res.data;
    //   }
    // })
    // .catch(err=>{
    //   alert(err)
    // })
=======
      .recommendSVD(params)
      .then(res => {
        console.log(res.data);
        if (res.status === 200) {
          return res.data;
        }
      })
      .catch(err => {
        alert(err);
      });
    // KNN
    this.recommendList = await api
      .recommendKNN(params)
      .then(res => {
        console.log(res.data);
        if (res.status === 200) {
          return res.data;
        }
      })
      .catch(err => {
        alert(err);
      });
>>>>>>> develop
  },
  methods: {
    subscibe() {
      api
        .subscribe()
        .then(res => {
          if (res.status === 200) {
            alert("구독 업데이트 완료");
            //사용자 정보 업데이트
            api.getProfile().then(res => {
              if (res.status === 200) {
                this.$store.state.auth.userInfo = res.data;
              }
            });
          }
        })
        .catch(err => {
          alert(err);
        });
    }
  }
};
</script>