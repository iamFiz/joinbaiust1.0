<template>
  <v-row justify="center">
    <v-col cols="12" md="10" lg="5">
      <v-card flat>
        <v-card-title v-text="$t('About This Site')"></v-card-title>
        <v-divider> </v-divider>
        <v-card-subtitle class="font-weight-bold  black--text">
          {{ $t("TY_FOR_VISITING") }}</v-card-subtitle
        >

        <v-card-text class="text-justify black--text">{{
          $t("AIBA_TED_COLLAB")
        }}</v-card-text>
        <v-card-text class="font-weight-bold py-0  black--text">
          {{ this.$t("ARMY IBA") }}</v-card-text
        >
        <v-card-text class="text-justify  black--text">
          {{ this.$t("KUBAST_INFO") }}</v-card-text
        >
        <v-card-text
          tag="a"
          href="http://throughedltd.com/"
          style="text-decoration: none"
          target="_blank"
          class="font-weight-bold  black--text"
          v-text="$t('Through ED Limited')"
        ></v-card-text>
        <v-card-text class="text-justify black--text" v-text="$t('TED_INFO')"></v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  metaInfo() {
    return {
      meta: [
        {
          name: "About",
          content: "About the site",
        },
      ],
      scripts: [
        {
          innerHTML: `(function (w, d, s, l, i) {
          w[l] = w[l] || []; w[l].push({
            'gtm.start':
              new Date().getTime(), event: 'gtm.js'
          }); var f = d.getElementsByTagName(s)[0],
            j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : ''; j.async = true; j.src =
              'https://www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
        })(window, document, 'script', 'dataLayer', 'GTM-P4RWXPZ');`,
          vmid: "gtm",
          from: "about",
        },
      ],
    };
  },
};
</script>

<style scoped>

</style>
