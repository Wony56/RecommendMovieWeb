<template>
<!-- 아디 패스워드 패스워드검증  성별 (남,여) 나이 직업 구독하기 건너뛰기-->
    <v-container fluid pa-0>
        <v-col class="pa-0">
            <v-flex>
                <v-card height="700" class="card_background_color">
                    <v-form>
                        <v-card-title class="paddingx70 padding_top70 font-weight-bold display-1" style="color:#fff">
                            회원가입
                        </v-card-title>
                        <v-text-field
                            height="60"
                            class="paddingx70 padding_top40 label_color rounded"
                            label="아이디"
                            dark
                            background-color="rgba(128, 128, 128, 0.5)"
                            required
                        ></v-text-field>
                        <v-text-field
                            height="60"
                            style="margin-top:-20px;"
                            required
                            dark
                            class="paddingx70 label_color rounded"
                            type='password'
                            label="비밀번호"
                            background-color="rgba(128, 128, 128, 0.5)"
                            color="#fff"
                        ></v-text-field>
                        <v-text-field
                            height="60"
                            style="margin-top:-20px;"
                            required
                            dark
                            class="paddingx70 label_color rounded"
                            type='password'
                            label="비밀번호 확인"
                            background-color="rgba(128, 128, 128, 0.5)"
                            color="#fff"
                        ></v-text-field>
                        <v-row class="paddingx70" style="margin-top:-20px; margin-left:0px;">
                            <v-flex xs5 justify-start>
                                <v-text-field
                                    height="60"
                                    required
                                    dark
                                    class="label_color rounded"
                                    label="나이"
                                    background-color="rgba(128, 128, 128, 0.5)"
                                    color="#fff"
                                ></v-text-field>
                            </v-flex>
                            <v-flex class="justify-center align-center">
                                <v-radio-group class="justify-center align-center" v-model="row" row>
                                    <v-radio class="justify-center align-center" dark label="남" value="radio-1"></v-radio>
                                    <v-radio class="justify-center align-center" dark label="여" value="radio-2"></v-radio>
                                </v-radio-group>
                            </v-flex>
                        </v-row>
                        <v-select
                            label="직업"
                            height="60"
                            required
                            style="margin-top:-20px;"
                            class="paddingx70 label_color rounded"
                            background-color="rgba(128, 128, 128, 0.5)"
                            color="#fff"
                            dark
                        ></v-select>
                        <div class="paddingx70 padding_top20">
                            <v-btn 
                            style="background-color:#ff2f6e; color:#fff; font-size:17px;"
                            height="55"
                            block
                            >
                                회원가입
                            </v-btn>
                        </div>
                      
                        <div class="paddingx70 padding_top20" style="color:gray;">
                            이미 회원이신가요? <a style="color:#fff; font-size:15px;" @click="createAccount">지금 로그인하세요</a>
                        </div>
                    </v-form>
                </v-card>
            </v-flex>
        </v-col>
    </v-container>
</template>

<style scoped>
.card_background_color
{
    background-color:rgba(0,0,0,0.8);
}

.padding_top20
{
    padding-top:20px;
}
.padding_top40
{
    padding-top:30px;
}
.padding_top50
{
    padding-top:50px;
}
.padding_top70
{
    padding-top:70px;
}
.padding_top90
{
    padding-top:90px;
}
.paddingx30
{
    padding-left:30px;
    padding-right:30px;
}
.paddingx50
{
    padding-left:50px;
    padding-right:50px;
}
.paddingx70
{
    padding-left:70px;
    padding-right:70px;
}
.paddingx90
{
    padding-left:90px;
    padding-right:90px;
}

.label_color >>> label {
    color:gray;
    padding-left:15px;
}
.label_color2 >>> label {
    color:gray;
    font-size:15px;
}
.label_color >>> input {
    padding-left:15px;
    font-size:20px;
}

</style>