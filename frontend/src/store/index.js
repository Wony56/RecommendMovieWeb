import Vue from 'vue'
import Vuex from 'vuex'
import data from './modules/data'
import auth from './modules/auth'
import dialog from './modules/dialog'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        data,
        auth,
        dialog
    },
    state: {
        header: ""
    }
})