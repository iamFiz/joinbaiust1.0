import Vue from "vue";
import Vuetify from "vuetify/lib/framework";
//  {
//   VApp,
//   VBtn,
//   VCol,
//   VRow,
//   VImg,
//   VFooter,
//   VCard,
// }

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#1d9b59",
      },
    },
  },
  icons: {
    iconfont: "mdi",
    values: {
      hamburger_aligned: {
        component: () => import("@/components/icons/HamburgerAligned.vue"),
      },
      payment: {
        component: () => import("@/components/icons/Payment.vue"),
      },
      download: {
        component: () => import("@/components/icons/Download.vue"),
      },
      chat: {
        component: () => import("@/components/icons/Chat.vue"),
      },
      find: {
        component: () => import("@/components/icons/Find.vue"),
      },
      circular: {
        component: () => import("@/components/icons/Circular.vue"),
      },
      status: {
        component: () => import("@/components/icons/Status.vue"),
      },
      apply: {
        component: () => import("@/components/icons/Apply.vue"),
      },
      language: {
        component: () => import("@/components/icons/Language.vue"),
      },
      home: {
        component: () => import("@/components/icons/Home.vue"),
      },
      nagad: {
        component: () => import("@/components/icons/Nagad.vue"),
      },
      uploadPhoto: {
        component: () => import("@/components/icons/UploadPhoto.vue"),
      },
      report: {
        component: () => import("@/components/icons/Report.vue"),
      },
      bkash: {
        component: () => import("@/components/icons/Bkash.vue"),
      },
    },
  },
});
