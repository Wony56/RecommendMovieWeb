import Vue from 'vue'
import VueRouter from 'vue-router'
import EmptyPage from '../components/pages/EmptyPage'
import MovieSearchPage from '../components/pages/MovieSearchPage'
import MovieDetailPage from '../components/pages/MovieDetailPage'
import UserDetailPage from '../components/pages/UserDetailPage'
import AdminPage from '../components/pages/AdminPage'

import EntrancePage from '../components/auth/views/LandingPage'

import store from '../store'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '*', redirect: '/' },
        { path: '/', component: EmptyPage, name: 'home' },
        { path: '/movies/search', component: MovieSearchPage, name: 'movie-search', meta: { requiresLogin: true } },
        { path: '/movies/detail', component: MovieDetailPage, name: 'movie-detail', meta: { requiresLogin: true } },
        { path: '/user/detail/:id', component: UserDetailPage, name: 'user-detail', meta: { requiresLogin: true } },
        { path: '/admin', component: AdminPage, name: 'admin', meta: { requiresAuth: true } },
        { path: '/entrance', component: EntrancePage, name: 'entrance' }
    ],
    scrollBehavior() {
        return { x: 0, y: 0 }
    },
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresLogin)) {
        // if (!store.getters.loggedIn) {
        //     next('/entrance');
        // } else {
        //     next();
        // }
        next();
    } else if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!store.getters.loggedIn || !store.state.auth.userInfo.is_staff) {
            alert("관리자권한이 없습니다...")
            next('/');
        } else {
            next();
        }
    } else {
        next();
    }
})

export default router