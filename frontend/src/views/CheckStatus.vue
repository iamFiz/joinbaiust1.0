<template>
  <v-container>
    <v-row justify="center" class="pa-0">
      <v-col cols="12" lg="5" md="8" class="pa-0">
        <v-card-title v-text="$t('Application Status')"></v-card-title>
        <v-divider></v-divider>
      </v-col>
    </v-row>
    <v-row v-if="status.application" justify="center" class="pa-0">
      <v-col cols="12" md="8" lg="6" class="pa-0">
        <v-card outlined flat class="text-justify my-4">
          <v-card-text
            class="text-center text-h6"
            v-if="status.application"
            v-text="$t('THANKS_FOR_SEARCHING')"
          ></v-card-text>
          <v-card-text class="text-h6" v-if="status.application"
            >{{ this.$t("Application ID") }}:
            <span
              class="text-h6 font-weight-bold"
              v-html="status.application"
            ></span
          ></v-card-text>
          <v-card-text class="text-h6" v-if="status.status == 'under_review'"
            >{{ this.$t("Payment Status") }}:
            <span v-if="status.payment_verified === true">
              {{ $t("Payment Verified") }}
            </span>
            <span v-else-if="status.payment_verified === false">
              {{ $t("Payment Not Verified") }}
            </span>
            <span v-else>
              {{ $t("Payment Under Review") }}
            </span>
          </v-card-text>
          <v-card-text v-if="status.status_text" class="text-h6"
            >{{ this.$t("Application Status") }}:

            <span
              :class="`font-weight-bold' ${
                status.status_text == 'Approved'
                  ? 'green--text text--lighten-1'
                  : 'red--text text--lighten-1'
              }`"
              v-html="status.status_text"
            ></span>
          </v-card-text>
          <v-card-text
            v-if="status.message"
            class="text-h6"
            v-html="`${$t('Message')}: ${status.message}`"
          ></v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row v-else justify="center">
      <v-col cols="12" md="8" lg="5">
        <v-card outlined flat class="text-center pa-4">
          <v-card-subtitle
            class="font-weight-bold text-subtitle-1"
            v-text="$t('APPLICATION_STATUS_TEXT')"
          ></v-card-subtitle>
          <v-text-field
            class="centered-input"
            text-align="center"
            v-model="application_id"
            :label="$t('Application ID')"
          >
          </v-text-field
          ><v-btn color="primary" @click="check">
            {{ this.$t("Check") }}
          </v-btn>
        </v-card></v-col
      >
    </v-row>
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
  name: "ApplicationDownload",

  data() {
    return {
      application_id: this.$route.params.application_id || "",
      status: {},
    };
  },
  methods: {
    check() {
      this.$axios
        .get(`/status/${this.application_id.trim()}/`)
        .then((response) => {
          this.status = response.data;
        })
        .catch((err) => alert(err.response.data.message));
    },
  },
};
</script>

<style></style>
