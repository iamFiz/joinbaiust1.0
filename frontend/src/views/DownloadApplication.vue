<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8" lg="5">
        <v-alert dense border="left" outlined type="info">
          বিশেষ দ্রষ্টব্য: টেকনিকালি সমস্যার কারণে, আইফোন ব্যবহারকারীদের সাফারি
          ব্রাউজার ব্যবহার করে প্রবেশপত্র সংরক্ষণে সমস্যার সম্মুখীন হচ্ছেন। উক্ত
          সমস্যাটি এড়িয়ে চলতে সাফারি ব্রাউজারের পরিবর্তে অন্য সকল বিকল্প
          ব্রাউজার ব্যবহার করে প্রবেশপত্র ডাউনলোড করার জন্যে অনুরোধ জানানো
          হচ্ছে।
        </v-alert>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12" md="8" lg="5" class="pa-0">
        <v-card-title v-text="$t('Download Admit Card')"></v-card-title>
        <v-divider></v-divider>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="10" md="8" lg="5" class="px-0">
        <!-- <v-card-text class="text-justify">
          ভেন্যু পরিবর্তন করতে ও অন্যান্য সমস্যা সম্পর্কে অবহিত করতে পরীক্ষার
          অন্তত ৪৮ ঘন্টার আগে <a href="/chat/">কথা বলুন</a> অপশনে অনুরোধ
          রাখুন।<br /><br />
          ভর্তি পরীক্ষার প্রবেশপত্র সংগ্রহের তারিখ:  ২ জুন, ২০২৩ (শুক্রবার)
          পরীক্ষার সময়সূচি:<br />
         <ul>
            <li>
              ভর্তি পরীক্ষার প্রবেশপত্র সংগ্রহের তারিখ: জুন, ২০২৩ (প্রথম সপ্তাহ)
            </li>
            <li>মিরপুর সেনানিবাস, ঢাকা: <b>২ জুলাই, ২০২২</b></li>
          </ul> 
        </v-card-text> -->
      </v-col>
    </v-row>
    <v-row class="mt-7">
      <v-row align="center" justify="center">
        <v-col cols="12" md="5">
          <v-card outlined flat class="text-center pa-4">
            <v-text-field
              v-model="application_id"
              :label="$t('Application ID')"
            >
            </v-text-field>
            <!-- TODO: ENABLE ADMIT DOWNLOAD -->
            <v-btn outlined color="primary" @click="download" :loading="loading">
              {{ this.$t("Download") }}
            </v-btn>
          </v-card></v-col
        ></v-row
      >
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "ApplicationDownload",
  metaInfo() {
    return {
      titleTemplate: "%s | Admit Card",

      meta: [
        {
          name: "Download Application",
          content: "Download your application",
        },
      ],
    };
  },
  data() {
    return {
      loading: false,
      application_id: this.$route.query.application_id || "",
    };
  },
  methods: {
    download() {
      this.loading = true;
      this.$axios
        .get(`/application/download/`, {
          params: {
            application_id: this.application_id,
          },
           responseType: "arraybuffer",
        })
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute(
            "download",
            `application-${this.application_id}.pdf`
          );
          document.body.appendChild(link);
          link.click();
        }).finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>

<style></style>
