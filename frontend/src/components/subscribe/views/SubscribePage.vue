<template>
    <v-container fluid>
        <v-col>
            <div class="text-center justify-center headline"> 선호하는 영화를 선택 해주세요 </div>
            <br>
            <div class="text-right">
                <v-btn outlined color="#ff2f6e">건너뛰기</v-btn>
            </div>
            <br>
            <v-row>
                <v-progress-linear
                v-model="select"
                height="25"
                reactive
                color="#ff2f6e"
                rounded
                >
                <strong>{{ Math.ceil(select) }}%</strong>
                </v-progress-linear>
            </v-row>
            <v-row class="justify-center my-5 mx-0">
                <v-flex xs6 sm3 md2 my-1>
                    <SubScribeCard/>
                </v-flex>
                <v-flex xs6 sm3 md2 my-1>
                    <SubScribeCard/>
                </v-flex>
                <v-flex xs6 sm3 md2 my-1>
                    <SubScribeCard/>
                </v-flex>
                <v-flex xs6 sm3 md2 my-1>
                    <SubScribeCard/>
                </v-flex>
                <v-flex xs6 sm3 md2 my-1>
                    <SubScribeCard/>
                </v-flex>
                <v-flex xs6 sm3 md2 my-1>
                    <SubScribeCard/>
                </v-flex>
                <v-flex xs6 sm3 md2 my-1>
                    <SubScribeCard/>
                </v-flex>
                <v-flex xs6 sm3 md2 my-1>
                    <SubScribeCard/>
                </v-flex>
                <v-flex xs6 sm3 md2 my-1>
                    <SubScribeCard/>
                </v-flex>
                <v-flex xs6 sm3 md2 my-1>
                    <SubScribeCard/>
                </v-flex>
                <v-flex xs6 sm3 md2 my-1>
                    <SubScribeCard/>
                </v-flex>
                <v-flex xs6 sm3 md2 my-1>
                    <SubScribeCard/>
                </v-flex>
            </v-row>
        </v-col>
    </v-container>
</template>

<script>
import SubScribeCard from '../card/SubScribeCard'

export default {
    data: () => ({
      select:80,
    }),
    components:{
        SubScribeCard
    },
}
</script>