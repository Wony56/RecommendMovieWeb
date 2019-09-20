
<template>
<!-- 테블릿 , PC -->
    <v-container
    v-if="$vuetify.breakpoint.smAndUp"
    class="fill-height"
    id="background_img"
    fluid
    pa-0
    > 
    <v-col>
        <v-img src="../../../../public/img/logo/logo.png" width="250"></v-img>
        <v-row  
        align="center"
        justify="center"
        >
            <v-flex xs12 sm6 md5 >
                <LoginCard v-if="isLogin" :isLogin.sync="isLogin" @update:isLogin="val => isLogin = val"/>
                <AccountCard v-else :isLogin.sync="isLogin" @update:isLogin="val => isLogin = val"/>
            </v-flex>
        </v-row>
    </v-col>
    </v-container>
<!--모바일-->
    <v-container
    v-else
    class="fill-height "
    fluid
    style="background-color:#000;"
    pa-0
    > 
    <v-col >
        <v-img src="../../../../public/img/logo/logo.png" width="250"></v-img>
        <v-row  
        align="center"
        justify="center"
        >
            <v-flex xs12 sm6 md5 >
                <LoginCard v-if="isLogin" :isLogin.sync="isLogin" @update:isLogin="val => isLogin = val"/>
                <AccountCard v-else :isLogin.sync="isLogin" @update:isLogin="val => isLogin = val"/>
            </v-flex>
        </v-row>
    </v-col>
    </v-container>
</template>

<script>
import LoginCard from '../login/LoginCard.vue';
import AccountCard from '../account/AccountCard.vue';

export default {
    components:{
        LoginCard,
        AccountCard
    },
    data(){
        return{
            isLogin: true
        }
    }
}
</script>

<style scoped>
#background_img{
    background: url("../../../../public/img/background/enterance.jpg") no-repeat;
}

</style>