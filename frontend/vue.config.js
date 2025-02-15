module.exports = {
  // outputDir: "dist",
  // outputDir: "/var/www/joinarmyiba/",
  assetsDir: "static",
  transpileDependencies: ["vuetify", "vue-tel-input-vuetify"],
  filenameHashing: false,
  runtimeCompiler: true,
  devServer: {
    writeToDisk: true,
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        ws: true,
        changeOrigin: true,
      },
    },
  },
  productionSourceMap: false,

  // chainWebpack: (config) => {
  //   config.plugins.delete("html");
  //   config.plugins.delete("preload");
  //   config.plugins.delete("prefetch");
  // },
  pluginOptions: {
    i18n: {
      locale: "bn",
      fallbackLocale: "en",
      localeDir: "locales",
      enableInSFC: false,
      enableBridge: false,
    },
  },
};
