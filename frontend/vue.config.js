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
  assetsDir: "static"
}