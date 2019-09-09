<template>
  <v-card style="border-radius:20px;">
    <v-card-text style="font-size:30px; text-align:center; color:#ff2f6e;">Sign Up</v-card-text>
    <v-card-text>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="name"
          color="#ff2f6e"
          :counter="10"
          :rules="nameRules"
          label="이름을 입력해주세요"
          required
        ></v-text-field>

        <v-text-field v-model="password" color="#ff2f6e" label="비밀번호를 입력해주세요" required></v-text-field>

        <v-select v-model="occupation" :items="items" color="#ff2f6e" label="직업을 선택해주세요" required></v-select>

        <v-text-field v-model="age" color="#ff2f6e" label="나이를 입력해주세요" required></v-text-field>
        <v-radio-group v-model="gender" row>
          <v-radio label="남" color="#ff2f6e" value="M"></v-radio>
          <v-radio label="여" color="#ff2f6e" value="W"></v-radio>
        </v-radio-group>
        <v-checkbox
          v-model="checkbox"
          :rules="[v => !!v || 'You must agree to continue!']"
          label="동의하십니까?"
          color="#ff2f6e"
          required
        ></v-checkbox>

        <v-btn
          :disabled="!valid"
          color="#ff2f6e"
          rounded
          outlined
          class="mr-4"
          @click="signup({name, password, gender, age, occupation})"
          row
          justify-start
        >SIGN UP</v-btn>

        <v-btn rounded outlined color="blue" class="mr-4" @click="reset" row justify-start>Reset</v-btn>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data: () => ({
    valid: true,
    name: "",
    nameRules: [
      v => !!v || "Name is required",
      v => (v && v.length <= 10) || "Name must be less than 10 characters"
    ],
    select: null,
    items: [
      "other",
      "academic/educator",
      "artist",
      "clerical/admin",
      "college/grad student",
      "customer service",
      "doctor/health care",
      "executive/managerial",
      "farmer",
      "homemaker",
      "K-12 student",
      "lawyer",
      "programmer",
      "retired",
      "sales/marketing",
      "scientist",
      "self-employed",
      "technician/engineer",
      "tradesman/craftsman",
      "unemployed",
      "writer"
    ],
    checkbox: false
  }),

methods: {
    ...mapActions("data", ["signup"])
  ,
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>