module.exports = {
  publicPath: '/',
  devServer: {
    proxy: {
      '^/api/': {
        target: 'http://localhost:8000/api/',
      },
      '/static/posters': {
        target: 'http://localhost:8000/',
      },
    }
  },
  outputDir: "./dist/",
  assetsDir: "static",
  
  async fetchPhrases() {
    const response = await this.$http.get('/api/phrases/')
    return response.body.data
  }
}