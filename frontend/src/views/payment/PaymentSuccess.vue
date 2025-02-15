<template>
  <v-container fill-height class="my-6">
    <v-row align="center" justify="center">
      <v-col cols="12" md="6">
        <v-card flat class="text-center pa-4" min-height="300">
          <v-icon size="64px" color="primary">mdi-check-decagram</v-icon>
          <v-card-title
            primary-title
            class="justify-center"
            style="word-break: keep-all"
            >আপনার ফি প্রদানের তথ্য সফলভাবে সংরক্ষিত হয়েছে।
          </v-card-title>
          <!-- <p>
            <strong
              >Please complete the payment within 24 hours. Otherwise, the
              application will be invalid</strong
            >
          </p> -->
          <v-card-text
            ><strong>
              ফি প্রদানের তথ্য যাচাই শেষে, সংক্রিয়ভাবে আবেদনকারীর নিবন্ধিত
              মোবাইল ফোন বা ইমেইল এড্রেসে নিশ্চিতকরণ বার্তা পাঠানো হবে। সফলভাবে
              ফি-প্রদান সম্পন্ন হলে, 'ছবি জমা' আপশনে গিয়ে ছবি, স্বাক্ষর ও
              অন্যান্য তথ্য জমা দিন।</strong
            ></v-card-text
          >
          <v-card-text>
            ফি প্রদানের ৪৮ ঘন্টার মধ্যে নিশ্চিতকরণ বার্তা না পেলে, 'কথা বলুন'
            অপশনে চ্যাট রিকোয়েস্ট জমা দিন অথবা অফিসিয়াল হটলাইন নম্বরে যোগাযোগ করুন
          </v-card-text>
          <v-row justify="center">
            <v-col cols="10" md="8" lg="6">
              <v-text-field
                class="centered-input"
                text-align="center"
                v-model="application_id"
                readonly
              >
                <template v-slot:append
                  ><v-btn icon @click="copyText"
                    ><v-icon>mdi-clipboard-multiple-outline</v-icon></v-btn
                  ></template
                ></v-text-field
              >
            </v-col>
          </v-row>
          <v-card-actions>
            <v-spacer> </v-spacer>
            <v-btn color="primary" @click="routeToUpload"
              >ছবি ও স্বাক্ষর জমাকরণ</v-btn
            >
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <!-- <v-card-text
      class="text-justify"
      v-text="$t('CHECK_NEXT_STEPS')"
    ></v-card-text> -->
    <v-snackbar v-model="showCopied" timeout="1000">Copied</v-snackbar>
  </v-container>
</template>

<script>
export default {
  metaInfo() {
    return {
      titleTemplate: "%s | Payment-Success",
      meta: [
        {
          name: "payment-success",
          content: "Payment Success",
        },
      ],
    };
  },
  name: "PaymentSuccess",
  props: ["application_id"],
  data() {
    return { showCopied: false, verified: false };
  },

  mounted() {},
  created() {
    this.$meta().refresh;
    // if (this.$gtm.enabled()) {
    //   window.dataLayer?.push({
    //     event: "custom",
    //     customEventName: "Registration Complete",
    //     // further parameters
    //   });
    // }
  },

  methods: {
    copyText() {
      if (this.application_id !== undefined) {
        navigator.clipboard.writeText(this.application_id);
        this.showCopied = true;
      }
    },
    routeToUpload() {
      this.$router.push({
        name: "UploadPhoto",
        query: { application_id: this.application_id },
      });
    },
  },
};
</script>

<style>
.centered-input input {
  text-align: center;
}
</style>
