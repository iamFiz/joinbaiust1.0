<template>
  <v-container>
    <v-row justify="center" class="pa-0">
      <v-col cols="12" lg="6" md="10" class="pa-0">
        <v-card-title
          v-text="$t('Photo and Signature Collection')"
        ></v-card-title>
        <v-divider></v-divider>
      </v-col>
    </v-row>
    <v-row justify="center" v-if="!payment_completed">
      <v-col cols="12" md="8" lg="6">
        <v-card outlined flat class="text-center pa-4">
          <v-card-subtitle
            class="font-weight-bold text-justify"
            v-text="$t('PROCEED_ON_PAYMENT')"
          ></v-card-subtitle>
          <v-text-field
            class="centered-input"
            text-align="center"
            v-model="application"
            :label="$t('Application ID')"
          >
          </v-text-field>
          <v-btn color="primary" @click="check">
            {{ this.$t("Proceed") }}
          </v-btn>
        </v-card></v-col
      >
    </v-row>
    <!-- v-else-if="payment_completed" -->
    <v-row justify="center" v-else>
      <v-col cols="12" md="8" lg="6">
        <photo-and-other-info
          :application_id="application.trim()"
        ></photo-and-other-info>
      </v-col>
    </v-row>
    <v-snackbar color="red lighten-2" centered v-model="show_error_snackbar"
      >{{ this.$t(err_msg) }}
      <template v-slot:action="{ attrs }">
        <v-btn dark text v-bind="attrs" @click="toPayment">
          {{ $t("Payment") }}
        </v-btn>

        <v-btn dark text v-bind="attrs" @click="show_error_snackbar = false">
          {{ $t("Close") }}
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
import PhotoAndOtherInfo from "../components/PhotoAndOtherInfo.vue";
export default {
  components: { PhotoAndOtherInfo },
  props: ["application_id"],
  metaInfo() {
    return {
      titleTemplate: "%s | Photo Upload",
    };
  },
  data() {
    return {
      payment_completed: false,
      show_error_snackbar: false,
      err_code: "",
      err_msg: "",
      application: this.application_id,
    };
  },
  created() {
    this.$meta.refresh;
  },
  methods: {
    toPayment() {
      window.location.href = "/pay";
    },
    check() {
      if (this.application) {
        this.$axios
          .get("/payment/find/", {
            params: {
              application_id: this.application.trim(),
            },
          })
          .then(() => (this.payment_completed = true))
          .catch((err) => {
            this.err_code = err.response.status;
            this.err_msg = err.response.data.message;
            this.show_error_snackbar = true;
          });
      }
    },
  },
};
</script>

<style></style>