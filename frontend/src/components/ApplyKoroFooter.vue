<template>
  <v-footer padless color="grey lighten-5" min-height="10vh">
    <v-card flat tile min-width="100%" class="pa-4" color="transparent">
      <v-card-title>{{ this.$t("BAUST_KHULNA") }}</v-card-title>
      <v-divider></v-divider>
      <v-row no-gutters justify="space-between">
        <v-col cols="12" md="6">
          <v-card-text>
            © {{ `${new Date().getFullYear()}  ${this.$t("FOOTER_TEXT")}` }}
          </v-card-text>
        </v-col>

        <v-col cols="12" md="6">
          <v-row justify-md="end" justify="start" class="ma-2">
            <v-btn
              :style="style"
              text
              class="px-2"
              v-for="link in quick_links"
              :key="link.name"
              :to="link.to"
            >
              <span>{{ link.name }} </span>
            </v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  data() {
    return {
      style: {
        "text-transform": "None",
      },
    };
  },
  computed: {
    quick_links() {
      return [
        {
          name: this.$t("Contact Us"),
          to: "/contact",
        },
        {
          name: this.$t("About This Site"),
          to: "/about",
        },
        {
          name: this.$t("Legal"),
          to: "/legal",
        },
        {
          name: this.$t("Privacy Policy"),
          to: "/privacy-policy",
        },
      ];
    },
  },
};
</script>

<style></style>
