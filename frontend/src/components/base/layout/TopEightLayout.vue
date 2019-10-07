<template>
  <carousel
    :responsive="{0:{items:1,nav:false},600:{items:3,nav:false},900:{items:8,nav:false}}"
    :loop="true "
    :nav="false"
    :margin="10"
    style="height:130px;"
  >
  <MovieCard :id='recommends[0].id' :title='recommends[0].title' :genres_array='recommends[0].genres_array' :viewCnt='recommends[0].view_cnt' :timeStamp='recommends[0].timeStamp' :year='recommends[0].year' :overview='recommends[0].overview' :rating='recommends[0].average_rating' :img='recommends[0].poster_path'/>
  <MovieCard :id='recommends[1].id' :title='recommends[1].title' :genres_array='recommends[1].genres_array' :viewCnt='recommends[1].view_cnt' :timeStamp='recommends[1].timeStamp' :year='recommends[1].year' :overview='recommends[1].overview' :rating='recommends[1].average_rating' :img='recommends[1].poster_path'/>
  <MovieCard :id='recommends[2].id' :title='recommends[2].title' :genres_array='recommends[2].genres_array' :viewCnt='recommends[2].view_cnt' :timeStamp='recommends[2].timeStamp' :year='recommends[2].year' :overview='recommends[2].overview' :rating='recommends[2].average_rating' :img='recommends[2].poster_path'/>
  <MovieCard :id='recommends[3].id' :title='recommends[3].title' :genres_array='recommends[3].genres_array' :viewCnt='recommends[3].view_cnt' :timeStamp='recommends[3].timeStamp' :year='recommends[3].year' :overview='recommends[3].overview' :rating='recommends[3].average_rating' :img='recommends[3].poster_path'/>
  <MovieCard :id='recommends[4].id' :title='recommends[4].title' :genres_array='recommends[4].genres_array' :viewCnt='recommends[4].view_cnt' :timeStamp='recommends[4].timeStamp' :year='recommends[4].year' :overview='recommends[4].overview' :rating='recommends[4].average_rating' :img='recommends[4].poster_path'/>
  <MovieCard :id='recommends[5].id' :title='recommends[5].title' :genres_array='recommends[5].genres_array' :viewCnt='recommends[5].view_cnt' :timeStamp='recommends[5].timeStamp' :year='recommends[5].year' :overview='recommends[5].overview' :rating='recommends[5].average_rating' :img='recommends[5].poster_path'/>
  <MovieCard :id='recommends[6].id' :title='recommends[6].title' :genres_array='recommends[6].genres_array' :viewCnt='recommends[6].view_cnt' :timeStamp='recommends[6].timeStamp' :year='recommends[6].year' :overview='recommends[6].overview' :rating='recommends[6].average_rating' :img='recommends[6].poster_path'/>
  <MovieCard :id='recommends[7].id' :title='recommends[7].title' :genres_array='recommends[7].genres_array' :viewCnt='recommends[7].view_cnt' :timeStamp='recommends[7].timeStamp' :year='recommends[7].year' :overview='recommends[7].overview' :rating='recommends[7].average_rating' :img='recommends[7].poster_path'/>
  {{recommends}}
    
  </carousel>
</template>
<script>
import MovieCard from "../card/MovieCard.vue";
import carousel from "vue-owl-carousel";
import api from '../../../api';

export default {
  components: {
    carousel,
    MovieCard
  },
  props:{
    movieId:{
      type:Number,
      default :0
    }
  },
  data() {
    return {
      recommends : {}
    };
  },
  created(){
    const params = {
      username: this.user.username
    }
    // api.getSimilarMovie(params).then(res => {
    //   console.log(JSON.stringify(res.data))
    //   this.recommends = res.data;
    // }).catch(err => {
    //   alert(err);
    // })
    // SVD
    this.recommends = api
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
 
  }
};
</script>