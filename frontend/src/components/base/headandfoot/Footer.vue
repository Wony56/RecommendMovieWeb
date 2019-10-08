<template>
  <v-footer light padless color="#fff" style="border-top: 1px solid lightgray;">
    <v-layout px-5 justify-center>
      <v-flex xs12 sm9 md5>
        <v-card flat tile>
          <v-card-title>
            <v-layout justify-start>
              <span class="body-2">
                지금까지
                <span style="color:#ffa136;">★ 개의 평가가</span>쌓였어요.
              </span>
            </v-layout>
            <v-layout justify-end>
              <v-btn x-small class="mx-1" icon outlined color="#3b5988">
                <v-icon fab>mdi-facebook-box</v-icon>
              </v-btn>
              <v-btn x-small class="mx-1" icon outlined color="#00acee">
                <v-icon fab>mdi-twitter</v-icon>
              </v-btn>
              <v-btn x-small class="mx-1" icon outlined color="#05d686">
                <v-icon fab>mdi-blogger</v-icon>
              </v-btn>
            </v-layout>
          </v-card-title>

          <v-card-actions class="justify-center">
            @ {{ new Date().getFullYear() }} —
            <strong>SHEEPCHA</strong>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-footer>
</template>

