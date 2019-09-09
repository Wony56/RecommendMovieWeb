const state = {
    userInfo: null
}

const getters = {
    loggedIn(state) {
        if (state.userInfo) {
            return true;
        } else {
            return false;
        }
    }
}

export default {
    state,
    getters
}