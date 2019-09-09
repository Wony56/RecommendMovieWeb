<template>
  <div>
    <ImgBanner></ImgBanner>
    <v-layout justify-center style="margin-top:-200px;">
      <span id="maintext" class="display-2" style="color:#fff;">SHEEPCHA</span>
    </v-layout>
    <v-container px-5 style="margin-top:108px;">
      <v-layout justify-center>
        <v-flex xs12 sm9 md5></v-flex>
      </v-layout>
      <v-layout justfiy-center>
        <v-flex xs12 sm9 md5></v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import SearchForm from "../base/forms/SearchForm.vue";
import ImgBanner from "../base/ImgBanner.vue";
export default {
  components: {
    SearchForm,
    ImgBanner
  }
};
</script>

<style>
#maintext {
  font-weight: 600;
}
</style>