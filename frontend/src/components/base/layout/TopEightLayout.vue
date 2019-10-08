<template>
  
  <div v-if='recommends.length !=0'>
    <carousel
    :responsive="{0:{items:1,nav:false},600:{items:3,nav:false},900:{items:5,nav:false}}"
    :loop="true "
    :nav="false"
    :margin="10"
    >
      <MovieCard  v-for="(card) in recommends" :key="card.id"
      :id='card.id'
      :title='card.title' 
      :genres_array='card.genres_array' 
      :viewCnt='card.view_cnt' 
      :timeStamp='card.timeStamp' 
      :year='card.year' 
      :overview='card.overview' 
      :rating='card.rrating' 
      :img='card.poster_path'/>
       </carousel>
  </div>
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
      recommends : []
    };
  },
  async created(){
    const params = {
      movieId: this.movieId
    }
    console.log(this.movieId)
    // const params = {
    //   username: this.user.username
    // }
    await api.getSimilarMovie(params).then(res => {
      // console.log(JSON.stringify(res.data))
      this.recommends = res.data;
      console.log(res.data)
    }).catch(err => {
      alert(err);
    })
    // SVD
    // this.recommends = api
    // .recommendSVD(params)
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
 
  }
};
</script>