<template>
  <div class="hello">
    <v-card max-width="600" class="mx-auto" dark>
      <v-card-title class="text-center justify-center py-6">
        <h1 class="font-weight-bold display-3 basil--text">SHEEPCHA</h1>
      </v-card-title>

      <v-tabs v-model="tab" background-color="transparent" grow>
        <v-tab v-for="item in items" :key="item">{{ item }}</v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab" dark>
        <v-tab-item v-for="item in items" :key="item">
          <v-card flat dark>
            <template v-if="item === '로그인'">
              <v-card-text>
                <signin-card />
              </v-card-text>
            </template>
            <template v-else>
              <v-card-text>
                <signup-card />
              </v-card-text>
            </template>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </div>
</template>

<script>
import SignInCard from "./SignInCard";
import SignUpCard from "./SignUpCard";

export default {
  components: {
    "signin-card": SignInCard,
    "signup-card": SignUpCard
  },
  data: () => ({
    tab: null,
    items: ["로그인", "회원가입"]
  })
};
</script>

<style scoped>
.hello {
  height: 100%;
  background: #356859;
  background-image: url("https://cdn.onebauer.media/one/media/5d20/5d91/a205/650c/a1d3/d71f/empire-joker-subscriber-cover-crop.jpeg?quality=50&width=1800&ratio=16-9&resizeStyle=aspectfill&format=jpg");
}
.basil {
  background-color: #fffbe6 !important;
}
.basil--text {
  color: white !important;
}
</style>