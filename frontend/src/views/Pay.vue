<template>
  <v-row align="center" justify="center">
    <v-col cols="12" md="10" lg="5">
      <v-card flat class="text-center" min-height="300">
        <v-card-title v-text="$t('Make Payment')"></v-card-title>
        <v-divider></v-divider>
        <v-card-text class="text-justify" v-html="$t('PAYMENT_INSTRUCTION')"></v-card-text>

        <v-row justify="center">
          <v-radio-group row v-model="payment_option">
            <v-radio v-for="(p, i) in payment_options" :key="i" :value="p.value">
              <template v-slot:label>
                <v-card-text class="font-weight-bold px-0 py-1" v-text="p.label"></v-card-text>
              </template>
            </v-radio>
          </v-radio-group>
        </v-row>

        <v-card v-if="payment_option" flat outlined class="pa-4 mt-0">
          <v-card-text class="font-weight-bold" v-text="$t('Select Payment Method')"></v-card-text>

          <v-btn-toggle v-model="selected_payment_method" class="pa-8" color="primary">
            <v-btn outlined class="pa-8" value="bkash">
              <v-icon size="120" v-html="`$vuetify.icons.bkash`"></v-icon>
            </v-btn>
          </v-btn-toggle>

          <!-- Show the bKash instructions when bKash is selected -->
          <v-card v-if="selected_payment_method === 'bkash'" outlined class="pa-6 mt-4">
            <v-card-text class="text-justify black--text">
              <b>বিকাশে ম্যানুয়াল প্রসেসে *247# ডায়েল করে পেমেন্ট করার নিয়ম:</b>
              <br /><br />
              ১। *২৪৭# ডায়াল করে বিকাশ মোবাইল মেন্যুতে যান<br />
              ২। “পেমেন্ট” সিলেক্ট করুন<br />
              ৩। মার্চেন্ট বিকাশ একাউন্ট নাম্বার: 01769564531 দিন<br />
              ৪। ভর্তি পরীক্ষার অংশগ্রহণ নিশ্চিতকরণ ফি: 700 দিন<br />
              ৫। রেফারেন্সে আপনার আবেদনের আইডি দিন<br />
              ৬। কাউন্টার নম্বর ‘0’ দিন<br />
              ৭। আপনার পিন দিন<br />
              ৮। আপনি বিকাশ থেকে একটি কনফার্মেশন মেসেজ পাবেন।<br />
              ৯। জয়েন আর্মি আইবিএ ডটকম ওয়েবসাইটের ‘ফি প্রদান’ অপশনে গিয়ে ‘আবেদন আইডি’ ও ‘ট্রানজেকশন আইডি’ লিখে জমা দিন।
            </v-card-text>

            <v-form ref="form">
              <v-text-field v-model="application_id" :label="$t('Application ID')" :rules="requiredRules"></v-text-field>
              <v-text-field v-model="transaction_id" :label="$t('Transaction ID')" :rules="traxIDRules"></v-text-field>
            </v-form>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" @click="pay">{{ this.$t("SUBMIT") }}</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-card>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      application_id: "",
      transaction_id: "",
      payment_option: "",
      selected_payment_method: "",
    };
  },
  computed: {
    payment_options() {
      return [
        { label: this.$t("Manual Payment"), value: "offline" },
        { label: this.$t("App Payment"), value: "app" },
      ];
    },
    requiredRules() {
      return [(v) => !!v || this.$t("This field is required")];
    },
    traxIDRules() {
      return [
        (v) => !!v || this.$t("This field is required"),
        (v) => v !== this.application_id || this.$t("APPIID_TRAXID_NOT_ALLOWED"),
      ];
    },
  },
  methods: {
    pay() {
      if (this.$refs.form.validate()) {
        alert("Payment Submitted!");
      }
    },
  },
};
</script>

<style>
/* Customize styles if needed */
</style>
