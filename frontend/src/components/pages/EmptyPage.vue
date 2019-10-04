<template>
  <div>
    <ImgBanner></ImgBanner>
    <v-layout justify-center style="margin-top:-200px;">
      <span id="maintext" class="display-2" style="color:#fff;">SHEEPCHA</span>
    </v-layout>
    <v-bottom-sheet v-model="sheet">
      <v-sheet flat class="text-center" height="100">
        <v-container>
          <v-row style="padding-top:12px;" class="align-center">
            <v-flex xs6 class="align-center justify-center">
              <div class="py-3">
                <span style="color:#f8de7e;">★</span>구독 서비스를 이용하시면 영화 추천 및 다양한 고객 만족서비스를 제공받으실 수 있습니다.
              </div>
            </v-flex>
            <v-flex xs6 text-end>
              <v-btn outlined color="red" @click="subscribe">구독하기</v-btn>
              <v-btn class="mx-5" outlined color="black" @click="sheet = !sheet">close</v-btn>
            </v-flex>
          </v-row>
        </v-container>
      </v-sheet>
    </v-bottom-sheet>
  </div>
</template>

<script>
import ImgBanner from "../base/ImgBanner.vue";
import api from "../../api";
import SubScribePage from "../subscribe/views/SubscribePage";

export default {
  components: {
    SubScribePage,
    ImgBanner
  },
  data: () => ({
    sheet: true
  }),
  created() {
    if (this.$store.state.auth.userInfo.is_subscribe) {
      this.sheet = false;
    } else {
      this.sheet = true;
    }
  },
  methods: {
    subscribe() {
      
    }
  }
};
</script>

<style>
#maintext {
  font-weight: 600;
}
</style>