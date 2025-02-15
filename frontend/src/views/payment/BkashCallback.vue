<template>
  <v-container fill-height>
    <v-row justify="center" align="center" class="text-center">
      <v-col v-if="this.$route.query.status === 'success'">
        <v-progress-circular
          indeterminate
          color="primary"
        ></v-progress-circular>
        <h3 class="my-4">Completing the Payment</h3>
      </v-col>
      <v-col v-else>
        <v-card-text v-if="$route.query.status === 'cancel'">
          <h1>Payment Cancelled</h1>
        </v-card-text>
        <v-card-text v-else-if="$route.query.status === 'failed'">
          <h1>Payment Failed</h1>
        </v-card-text>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    loading: false,
  }),
  async mounted() {
    await this.executePayment();
  },
  methods: {
    executePayment() {
      const { status, paymentID } = this.$route.query;
      if (status === "success") {
        this.loading = true;
        this.$axios
          .post("payment/bkash/execute/", {
            payment_id: paymentID,
          })
          .then((res) =>
            this.$router.push({
              name: "PaymentSuccess",
              query: {
                application_id: res.data.payment.application,
              },
            })
          )
          .catch((err) =>
            alert(
              err.response.data.message
                ? err.response.data.message
                : err.message
            )
          )
          .finally(() => {
            this.loading = false;
          });
      }
    },
  },
};
</script>

<style>
</style>