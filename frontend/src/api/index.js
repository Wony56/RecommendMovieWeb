import axios from 'axios'

const apiUrl = '/api'

export default {
  signup(params){
    return axios.post(`${apiUrl}/auth/signup/`,{
      params,
    })
  },
  searchMovies(params) {
    return axios.get(`${apiUrl}/movies/`, {
      params,
    })
  },
  getAllProfiles(){
    return axios.get(`${apiUrl}/users/all/`)
  },
  saveEditedUser(params){
    return axios.post(`${apiUrl}/users/edit/`, {
      params
    })
  },
  saveEditedMovie(params){
    return axios.post(`${apiUrl}/movies/edit/`, {
      params
    })
  },
  deleteUser(params){
    return axios.delete(`${apiUrl}/users/delete/`, {
      params
    })
  },
  deleteMovie(params){
    return axios.delete(`${apiUrl}/movies/delete/`, {
      params
    })
  },
  login(params){
    return axios.post(`${apiUrl}/auth/login/`, {
      params
    })
  },
  logout(){
    return axios.get(`${apiUrl}/auth/logout/`)
  },
  onAuthUser(){
    return axios.get(`${apiUrl}/auth/on/`);
  },
  getSimilarMovie(params){
    return axios.get(`${apiUrl}/cluster/getClusterMovie/`, {
      params
    })
  },
  checkDuplicate(params){
    return axios.post(`${apiUrl}/auth/duplicate/`, {
      params
    })
  },
  subscribe(){
    return axios.get(`${apiUrl}/auth/subscribe/`);
  },
  getProfile(){
    return axios.get(`${apiUrl}/auth/detail/`);
  },
  watchList(params){
    return axios.get(`${apiUrl}/movies/watch-list/`, {
      params
    })
  },
  recommendSVD(params){
    return axios.get(`${apiUrl}/recommend/svd/`,{
      params,
    })
  },
  recommendKNN(params){
    return axios.get(`${apiUrl}/recommend/knn_age_view/get/`,{
      params,
    })
  },
  registerRating(params){
    return axios.post(`${apiUrl}/movies/register-rating/`, {
      params
    })
  }
}