<template>
  <v-container fill-height class="my-6">
    <v-row align="center" justify="center">
      <v-col cols="12" md="6">
        <v-card v-if="verified" flat class="text-center pa-4" min-height="300">
          <v-icon size="64px" color="primary">mdi-check-decagram</v-icon>
          <v-card-title
            primary-title
            class="justify-center"
            style="word-break: keep-all"
            v-text="$t('APPLICATION_SUBMITTED_SUCCESSFULLY')"
          >
          </v-card-title>
          <!-- <p>
            <strong
              >Please complete the payment within 24 hours. Otherwise, the
              application will be invalid</strong
            >
          </p> -->
          <v-card-text
            ><strong v-text="$t('PLEASE_SAVE_APPLICATION_ID')"></strong
          ></v-card-text>
             <v-card-text>
            <br/><br/>
            আবেদনকারীকে 'সাতশত টাকা' ফি প্রদান করে ভর্তি পরীক্ষার অংশগ্রহণ নিশ্চিত করতে হবে। ফি পরিশোধ করতে 'ফি প্রদান' বাটনে ক্লিক করুন।  </v-card-text> 
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
            <v-btn color="primary" @click="routeToPayment">Pay Now</v-btn>
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
      titleTemplate: "%s | Status",
      meta: [
        {
          name: "description",
          content: "Check your application status",
        },
      ],
    };
  },
  name: "Success",
  // props: ["application_id"],
  data() {
    return { showCopied: false, verified: false, application_id: "" };
  },

  mounted() {},
  created() {
    this.$meta().refresh;
    this.$axios.get(`/status/${this.$route.query.application_id}/`).then(
      (response) => {
        this.application_id = response.data.application;
        this.verified = true;
      },
      (error) => {
        console.log(error);
      }
    );
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
    routeToPayment() {
      window.location.href = `/pay?application_id=${this.application_id}`;
    },
  },
};
</script>

<style>
.centered-input input {
  text-align: center;
}
</style>
