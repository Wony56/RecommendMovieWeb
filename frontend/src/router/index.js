import Vue from 'vue'
import VueRouter from 'vue-router'
import EmptyPage from '../components/pages/EmptyPage'
import MovieSearchPage from '../components/pages/MovieSearchPage'
import MovieDetailPage from '../components/pages/MovieDetailPage'
import UserDetailPage from '../components/pages/UserDetailPage'
import AdminPage from '../components/pages/AdminPage'

import store from '../store'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: EmptyPage, name: 'home' },
        { path: '/movies/search', component: MovieSearchPage, name: 'movie-search' },
        { path: '/movies/detail', component: MovieDetailPage, name: 'movie-detail' },
        { path: '/user/detail/:id', component: UserDetailPage, name: 'user-detail' },
        { path: '/admin', component: AdminPage, name: 'admin', meta: { requiresAuth: true } },
    ],
    scrollBehavior() {
        return { x: 0, y: 0 }
    },
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
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