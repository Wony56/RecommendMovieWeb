<template>
    <v-container fluid pa-0>
        <v-col class="pa-0">
            <v-flex>
                <v-card height="600" class="card_background_color">
                    <v-form ref="form">
                        <v-card-title class="paddingx70 padding_top70 font-weight-bold display-1" style="color:#fff">
                            로그인
                        </v-card-title>
                        <v-text-field
                            height="60"
                            class="paddingx70 padding_top40 label_color rounded"
                            label="아이디"
                            v-model="username"
                            background-color="rgba(128, 128, 128, 0.5)"
                            color="#fff"
                            required
                            dark
                        ></v-text-field>
                        <v-text-field
                            v-model="password"
                            height="60"
                            dark
                            style="margin-top:-20px;"
                            required
                            class="paddingx70 label_color rounded"
                            type='password'
                            label="비밀번호"
                            background-color="rgba(128, 128, 128, 0.5)"
                            color="#fff"
                        ></v-text-field>
                        <div class="paddingx70 padding_top40">
                            <v-btn 
                            style="background-color:#ff2f6e; color:#fff; font-size:17px;"
                            height="55"
                            block
                            @click="onSubmit"
                            >
                                로그인
                            </v-btn>
                        </div>
                        <div class="paddingx70">
                            <v-checkbox dark class="label_color2" v-model="checkbox1" label="로그인 정보 저장"></v-checkbox> 
                        </div>
                        <div class="paddingx70 padding_top90" style="color:gray;">
                            Sheepcha 회원이 아니신가요? <a style="color:#fff; font-size:15px;" @click="createAccount">지금 가입하세요</a>
                        </div>
                    </v-form>
                </v-card>
            </v-flex>
        </v-col>
    </v-container>
</template>

<script>

import api from "../../../api"

export default {
    props:{
        isLogin: {
            type: Boolean,
            required: true
        }
    },
    data() {
        return {
            username: "",
            password: ""
        };
    },
    methods: 
        {
        onSubmit() {
        const params = {
            username: this.username.trim(),
            password: this.password.trim()
        };

        api
            .login(params)
            .then(res => {
            if (res.status === 200) {
                console.log(JSON.stringify(res.data));
                this.$cookie.set("hojin_token", res.data.token, { expires: "30m" });
                this.$router.push("/");
            }
            })
            .catch(err => {
            alert(err);
            });
        },   
        createAccount() {
            this.$emit('update:isLogin', false)
        }
    },
}
</script>

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
    color:#fff;
}

</style>