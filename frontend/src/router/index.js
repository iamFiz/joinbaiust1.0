import Vue from "vue";
import VueMeta from "vue-meta";
import VueRouter from "vue-router";
Vue.use(VueRouter);
Vue.use(VueMeta);
const routes = [
  {
    path: "/",
    name: "AIBA",
    component: () =>
      import(/* webpackChunkName: "home" */ "../views/AboutAIBA.vue"),
  },
  {
    path: "/apply",
    name: "Apply",
    component: () =>
      import(/* webpackChunkName: "apply" */ "../views/Apply.vue"),
    // meta: { gtm: "Apply Now" },
  },
  {
    path: "/success",
    name: "Success",
    component: () =>
      import(/* webpackChunkName: "success" */ "../views/Success.vue"),
    // meta: { gtm: "Registration Complete" },
  },
  {
    path: "/paymentsuccess",
    name: "PaymentSuccess",
    component: () =>
      import(
        /* webpackChunkName: "paymnet-success" */ "../views/payment/PaymentSuccess.vue"
      ),
    props: (route) => ({ application_id: route.query.application_id }),
  },
  {
    path: "/pay",
    name: "Pay",

    component: () => import(/* webpackChunkName: "pay" */ "../views/Pay.vue"),
  },
  {
    path: "/download",
    name: "Download",

    component: () =>
      import(
        /* webpackChunkName: "download" */ "../views/DownloadApplication.vue"
      ),
  },
  {
    path: "/status",
    name: "Status",
    component: () =>
      import(/* webpackChunkName: "status" */ "../views/CheckStatus.vue"),
  },
  {
    path: "/circular",
    name: "Circular",
    component: () =>
      import(/* webpackChunkName: "circular" */ "../views/Circular.vue"),
  },
  {
    path: "/chat/",
    name: "Chat",

    component: () => import(/* webpackChunkName: "chat" */ "../views/Chat.vue"),
  },
  {
    path: "/about/",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/find_application",
    name: "Find Application",
    component: () =>
      import(/* webpackChunkName: "find" */ "../views/FindApplication.vue"),
  },
  {
    path: "/contact",
    name: "Contact",
    component: () =>
      import(/* webpackChunkName: "contact" */ "../views/ContactUs.vue"),
  },
  {
    path: "/privacy-policy",
    name: "Privacy Policy",
    component: () =>
      import(
        /* webpackChunkName: "privacy-policy" */ "../views/PrivacyPolicy.vue"
      ),
  },
  {
    path: "/legal",
    name: "Legal",
    component: () =>
      import(/* webpackChunkName: "legal" */ "../views/Legal.vue"),
  },
  {
    path: "/upload",
    name: "UploadPhoto",
    component: () =>
      import(
        /* webpackChunkName: "photo-collection" */ "../views/PhotoCollection.vue"
      ),
    props: (route) => ({ ...route.query }),
  },
  {
    path: "/result",
    name: "Result",
    component: () =>
      import(/* webpackChunkName: "photo-collection" */ "../views/Result.vue"),
  },
  {
    path: "/payment/bkash",
    name: "BkashCallback",
    component: () =>
      import(
        /* webpackChunkName: "bkash-callback" */ "../views/payment/BkashCallback.vue"
      ),
    props: (route) => ({ ...route.query }),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    return { el: "main" };
  },
});

export default router;
