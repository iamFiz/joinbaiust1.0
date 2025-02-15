<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8" lg="5">
        <v-card flat>
          <v-card-text class="text-h5" v-text="'ফলাফল'"></v-card-text>
          <v-divider></v-divider>
        </v-card> </v-col
    ></v-row>

    <v-row v-if="Object.keys(status).length === 0" justify="center">
      <v-col cols="12" md="8" lg="5">
        <iframe
          src="https://throughltd-my.sharepoint.com/:w:/p/mail/EQjYF_X1ba5Cv2uCZKdEtyoBhHB9EYNow-IQ1AwmuC805A?e=cyTfHK"
          width="100%"
          height="1000"
          allow="autoplay"
        ></iframe>
      </v-col>
    </v-row>
    <!-- <v-row justify="center" class="pa-0 ma-0 mt-10">
      <v-col cols="12" md="10" lg="8" xl="5">
        <v-card class="ma-0" flat>
          <v-card-title> নোটিশ </v-card-title>
         
          <v-divider class="mb-4"></v-divider>
          <v-row justify="center">
            <v-col
              ><iframe
                src=""
                width="100%"
                height="840"
                allow="autoplay"
              ></iframe>
            
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row> -->
  </v-container>
</template>

<script>
export default {
  metaInfo() {
    return {
      titleTemplate: "%s | Result",
      meta: [
        {
          name: "description",
          content: "Check your Result",
        },
      ],
    };
  },
  name: "ApplicationResult",

  data() {
    return {
      applicationId_or_roll: "",
      status: {},
    };
  },
  methods: {
    check() {
      this.$axios
        .get(`/result/individual/${this.applicationId_or_roll.trim()}/`)
        .then((response) => {
          this.status = response.data;
        })
        .catch(() => alert("Could not Find Your Result"));
    },
  },
};
</script>

<style></style>
