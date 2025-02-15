<template>
  <v-container style="margin-top: 0px">
    <v-row justify="center">
      <v-col cols="12" sm="12" md="10" lg="10">
        <v-card flat max-height="fit-content" class="pa-6">
          <v-row justify="center">
            <v-col md="6" sm="12" order="last" order-md="first">
              <v-row
                ><v-card-text
                  class="pl-0 my-5 text-h6 text-lg-h3 text-md-h4 text-justify"
                  >{{ this.$t("BAUST_KHULNA") }}</v-card-text
                >
              </v-row>
              <v-row>
                <v-card-text class="pa-0 text-justify">{{
                  this.$t("KUAST_INFO")
                }}</v-card-text>
              </v-row>
              <v-row class="py-4 mt-5">
                <v-btn
                  dark
                  :color="buttonColor"
                  outlined
                  min-width="100%"
                  href="https://baustkhulna.ac.bd"
                  target="_blank"
                >
                  <template v-slot:default>
                    <v-row justify="start">
                      <span
                        class="px-2"
                        v-text="$t('INSTITUTION PORTAL')"
                      ></span>
                      <v-spacer></v-spacer>
                      <v-icon left>mdi-arrow-right</v-icon>
                    </v-row>
                  </template>
                </v-btn>
              </v-row>
              <v-row class="py-4">
                <v-btn
                  dark
                  :color="buttonColor"
                  outlined
                  min-width="100%"
                  target="_blank"
                  href="http://facebook.com/baustkhulna"
                >
                  <template v-slot:default>
                    <v-row justify="start">
                      <span class="px-2" v-text="$t('CAMPUS LIFE')"></span>
                      <v-spacer></v-spacer>
                      <v-icon left>mdi-arrow-right</v-icon>
                    </v-row>
                  </template>
                </v-btn>
              </v-row>
              <v-row class="py-4">
                <v-btn
                  min-width="100%"
                  dark
                  :color="buttonColor"
                  :to="{ path: '/apply' }"
                >
                  <template v-slot:default>
                    <v-row justify="start">
                      <span class="px-2" v-text="$t('APPLY_BAUST_KHULNA')"></span>
                      <v-spacer></v-spacer>
                      <v-icon left>mdi-arrow-right</v-icon>
                    </v-row>
                  </template>
                </v-btn>
              </v-row>
            </v-col>
            <v-col
              class="px-3"
              order-lg="last"
              order-md="first"
              order="first"
              md="6"
              sm="12"
            >
              <v-img
                height="100%"
                width="100%"
                src="@/assets/baust-img.png"
                lazy-src="@/assets/baust-img.png"
                contain
              >
              </v-img>
            </v-col>
          </v-row>
        </v-card>

        <v-card flat max-height="fit-content" class="pa-6">
          <v-row justify="center">
            <v-col class="pr-5 pl-0" md="6" cols="12">
              <v-img
                height="100%"
                width="100%"
                contain
                src="@/assets/baust-logo.png"
                lazy-src="@/assets/baust-logo.png"
              >
              </v-img>
            </v-col>
            <v-col class="pl-5">
              <v-row
                ><v-card-text
                  class="pl-0 my-5 text-h6 text-lg-h3 text-md-h4"
                  v-text="$t('Bangladesh Army in Education Sector')"
                >
                </v-card-text>
              </v-row>
              <v-row>
                <v-card-text class="text-justify pa-0">
                  {{ this.$t("DESC_SYLHET_LIFE") }}
                </v-card-text>
              </v-row>
              <v-row class="py-4 mt-5">
                <v-btn
                  dark
                  outlined
                  :color="buttonColor"
                  min-width="100%"
                  href="https://www.army.mil.bd/"
                  target="_blank"
                >
                  <template v-slot:default>
                    <v-row justify="start">
                      <span
                        class="px-2"
                        v-text="$t('Bangladesh Army\'s Website')"
                      ></span>
                      <v-spacer></v-spacer>
                      <v-icon left>mdi-arrow-right</v-icon>
                    </v-row>
                  </template>
                </v-btn>
              </v-row>
              <v-row class="py-4">
                <v-btn
                  min-width="100%"
                  dark
                  outlined
                  :color="buttonColor"
                  href="https://bn.m.wikipedia.org/wiki/%E0%A6%AC%E0%A6%BE%E0%A6%82%E0%A6%B2%E0%A6%BE%E0%A6%A6%E0%A7%87%E0%A6%B6%E0%A7%87%E0%A6%B0_%E0%A6%B8%E0%A6%BE%E0%A6%AE%E0%A6%B0%E0%A6%BF%E0%A6%95_%E0%A6%AC%E0%A6%BE%E0%A6%B9%E0%A6%BF%E0%A6%A8%E0%A7%80%E0%A6%B0_%E0%A6%B6%E0%A6%BF%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE_%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A4%E0%A6%BF%E0%A6%B7%E0%A7%8D%E0%A6%A0%E0%A6%BE%E0%A6%A8%E0%A6%B8%E0%A6%AE%E0%A7%82%E0%A6%B9%E0%A7%87%E0%A6%B0_%E0%A6%A4%E0%A6%BE%E0%A6%B2%E0%A6%BF%E0%A6%95%E0%A6%BE"
                  target="_blank"
                >
                  <template v-slot:default>
                    <v-row justify="start">
                      <span
                        class="px-2"
                        v-text="$t('Bangladesh Army\'s Institutions')"
                      ></span>
                      <v-spacer></v-spacer>
                      <v-icon left>mdi-arrow-right</v-icon>
                    </v-row>
                  </template>
                </v-btn>
              </v-row>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <news-letter-form></news-letter-form>
  </v-container>
</template>

<script>
//import Banner from "../components/Banner.vue";

import NewsLetterForm from "../components/NewsLetterForm.vue";
export default {
  components: { NewsLetterForm },
  metaInfo() {
    return {
      meta: [
        {
          name: "Home",
          content: "Portal Home",
        },
        {
          property: "og:description",
          content: "BAUST Khulna - A Military Governed Business School",
        },
        {
          property: "og:title",
          content: "Join Army IBA",
        },
        { property: "og:url", content: "https://baustkhulna.ac.bd" },
      ],
    };
  },
  data() {
    return { buttonColor: "primary" };
  },
  created() {
    this.$meta().refresh;
  },
};
</script>
