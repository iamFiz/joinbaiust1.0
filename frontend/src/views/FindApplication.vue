<template>
  <v-container>
    <v-row justify="center" class="mb-1">
      <v-col cols="12" md="8" lg="5" class="pa-0">
        <v-card-title v-text="$t('Find Application ID')"></v-card-title>
        <v-divider></v-divider>
      </v-col>
    </v-row>
    <v-row justify="center" class="mt-0">
      <v-col cols="12" md="5">
        <v-card
          outlined
          v-if="!Object.keys(application).length == 0"
          flat
          class="text-center pa-4"
        >
          <v-card-text class="text-h4"
            >{{ this.$t("Application ID") }}:
            {{ this.application.id }}</v-card-text
          >
        </v-card>
        <v-card outlined v-else flat class="text-center pa-4">
          <v-card-text
            class="font-weight-bold text-justify px-0"
            v-text="$t('FORGOTTEN_AID')"
          ></v-card-text>

          <v-text-field v-model="phone_no" :label="$t('Phone Number')">
          </v-text-field>
          <v-text-field
            v-model="date_of_birth"
            type="date"
            :label="$t('Date of Birth')"
          >
          </v-text-field>
          <v-btn @click="getApplicationId" color="primary">{{
            this.$t("SUBMIT")
          }}</v-btn>
        </v-card></v-col
      ></v-row
    ></v-container
  >
</template>

<script>
export default {
  name: "ApplicationDownload",
  metaInfo() {
    return {
      titleTemplate: "%s | Find",
      meta: [
        {
          name: "Find",
          content: "Find your application",
        },
      ],
    };
  },
  data() {
    return {
      phone_no: "",
      date_of_birth: "",
      application: {},
    };
  },
  methods: {
    getApplicationId() {
      this.$axios
        .get("/application/find/", {
          params: {
            phone: this.phone_no,
            date_of_birth: this.date_of_birth,
          },
        })
        .then((res) => (this.application = res.data))
        .catch((err) => {
          if (err.response.status === 404) {
            alert(err.response.message);
          } else {
            alert(err);
          }
        });
    },
  },
};
</script>

<style></style>
