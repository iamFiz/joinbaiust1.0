<template>
  <v-app>
    <nav-bar></nav-bar>
    <!-- <v-app-bar app color="#1575aa" dark>
      <v-btn text to="/">
        <v-img width="38" src="@/assets/logo.png" class="ma-2"></v-img>
        <span class="hidden-sm-and-down">BAUST Khulna Admission</span>
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn :to="{ name: 'Pay' }" text class="pa-2">
        <span>{{ $t("Payment") }}</span>
      </v-btn>
      <v-btn class="pa-2" :to="{ name: 'DownloadApplication' }" text>
        <span>{{ $t("Check Status") }}</span>
      </v-btn>
    </v-app-bar> -->

    <banner v-if="$route.path === '/'"></banner>

    <v-main>
      <router-view />
    </v-main>

    <apply-koro-footer></apply-koro-footer>
  </v-app>
</template>

<script>
import ApplyKoroFooter from "./components/ApplyKoroFooter.vue";

import NavBar from "./components/NavBar.vue";
export default {
  components: {
    ApplyKoroFooter,
    NavBar,
    Banner: () => import("./components/Banner.vue"),
  },
  name: "App",
  metaInfo: {
    title: "BAUST Khulna Admission",
    titleTemplate: "%s",
  },
  data: () => ({
    langs: ["bn", "en"],
    isVisible: true,
  }),
  methods: {
    scrollHandler(e) {
      console.log(e);
      this.isVisible = e.target.scrollTop > 100 ? false : true;
    },
  },
};
</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto+Slab&display=swap");
* {
  font-family: "Roboto Slab";
  font-display: swap;
}
.lower-right {
  position: fixed;
  bottom: 0;
  right: 0;
  z-index: 5;
}
</style>
