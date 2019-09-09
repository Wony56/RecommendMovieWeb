<template>
<v-form ref="form">
          <v-autocomplete
            id="search_form"
            label="Components"
            :items="components"
            elevation-14
            solo
            prepend-inner-icon="mdi-magnify"
            placeholder="작품 제목, 배우, 감독을 검색해보세요."
            color="#ff2f6e"
            @keyup.enter="searchMovie"
          >
          </v-autocomplete>
 </v-form>   
</template>
<style>
#search_form::placeholder{
font-weight: 600;
}
</style>
<script>
export default {
  data () {
      return {
        components: [
          'Autocompletes', 'Comboboxes', 'Forms', 'Inputs', 'Overflow Buttons', 'Selects', 'Selection Controls', 'Sliders', 'Textareas', 'Text Fields',
        ],
      }
    },
  methods: {
    searchMovie(e){
      e.preventDefault();
      this.$router.push('/movies/search')
    }
  },
   
}
</script>