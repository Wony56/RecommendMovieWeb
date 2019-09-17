import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import store from './store'
import api from './api'
import carousel from 'vue-owl-carousel'
import VueParticles from 'vue-particles'
import VueCookies from 'vue-cookies'
import Vuelidate from 'vuelidate'

Vue.use(VueCookies)
Vue.use(VueParticles)
Vue.use(Vuelidate)

Vue.config.productionTip = false

api.onAuthUser().then(res => {
    if(res.status === 200){
        if(res.data){
            store.state.auth.userInfo = res.data;
            VueCookies.set('user', res.data.username, "30min");
        }else{
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
}).catch(err=>{
    alert(err);
})
