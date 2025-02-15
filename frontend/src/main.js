import Vue from "vue";
import "./plugins/axios";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import i18n from "./i18n";
import VueMeta from "vue-meta";
import "vuetify/dist/vuetify.min.css";
import VueTelInputVuetify from "vue-tel-input-vuetify/lib";
import VueGtm from "@gtm-support/vue2-gtm";
Vue.config.productionTip = false;
Vue.use(VueTelInputVuetify, {
  vuetify,
});

Vue.use(VueMeta);

Vue.use(VueGtm, {
  id: "GTM-P4RWXPZ", // Your GTM single container ID, array of container ids ['GTM-xxxxxx', 'GTM-yyyyyy'] or array of objects [{id: 'GTM-xxxxxx', queryParams: { gtm_auth: 'abc123', gtm_preview: 'env-4', gtm_cookies_win: 'x'}}, {id: 'GTM-yyyyyy', queryParams: {gtm_auth: 'abc234', gtm_preview: 'env-5', gtm_cookies_win: 'x'}}], // Your GTM single container ID or array of container ids ['GTM-xxxxxx', 'GTM-yyyyyy']
  queryParams: {
    // Add URL query string when loading gtm.js with GTM ID (required when using custom environments)
    gtm_auth: "jjFQJTPxtzISo9cchB5b5Q",
    gtm_preview: "env-4",
    gtm_cookies_win: "x",
  },
  defer: false, // Script can be set to `defer` to speed up page load at the cost of less accurate results (in case visitor leaves before script is loaded, which is unlikely but possible). Defaults to false, so the script is loaded `async` by default
  compatibility: false, // Will add `async` and `defer` to the script tag to not block requests for old browsers that do not support `async`
  nonce: "2726c7f26c", // Will add `nonce` to the script tag
  enabled: true, // defaults to true. Plugin can be disabled by setting this to false for Ex: enabled: !!GDPR_Cookie (optional)
  debug: false, // Whether or not display console logs debugs (optional)
  loadScript: true, // Whether or not to load the GTM Script (Helpful if you are including GTM manually, but need the dataLayer functionality in your components) (optional)
  vueRouter: router, // Pass the router instance to automatically sync with router (optional)
  // Don't trigger events for specified router names (optional)
 // trackOnNextTick: false, // Whether or not call trackView in Vue.nextTick
});

new Vue({
  router,
  vuetify,
  i18n,
  render: (h) => h(App),
}).$mount("#app");

i18n.locale = localStorage.getItem("lang") || "bn";
