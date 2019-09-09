import Vue from 'vue'
import VueCookie from 'vue-cookie'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import store from './store'
import api from './api'
import carousel from 'vue-owl-carousel'
import VueParticles from 'vue-particles'
Vue.use(VueParticles)
const TOKEN = 'hojin_token';

Vue.config.productionTip = false

Vue.use(VueCookie)

const tokenFromCookie = document.cookie.match('(^|;) ?' + TOKEN + '=([^;]*)(;|$)');

const token = tokenFromCookie ? tokenFromCookie[2] : '';

api.onAuthUser(token).then(res => {
    if (res.status === 200) {
        if (res.data) {
            store.state.auth.userInfo = res.data;
        } else {
            store.state.auth.userInfo = null;
        }

        new Vue({
            carousel,
            vuetify,
            router,
            store,
            render: h => h(App)
        }).$mount('#app')
    }
}).catch(err => {
    alert(err);
})