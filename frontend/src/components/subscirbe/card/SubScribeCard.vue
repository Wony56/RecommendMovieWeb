<template>
    <v-card justify-center text-center width="230" height="300" outlined style="border-radius:10px;">
        <v-container>
        <v-card-text justify-center text-center >
            <div class="text-center">
            영화 제목
            </div>
        </v-card-text>
        <div class="text-center" style="padding-top:80px;">
            <v-rating
                v-model="rating"
                hover
                color="yellow darken-3"
                background-color="grey darken-1"
                half-increments
            >
            </v-rating>
        </div>
        </v-container>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      rating: 1,
    }),
  }
</script>
