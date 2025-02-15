<template>
  <v-container class="mt-4">
    <v-row justify="center" class="mb-4">
      <v-col cols="12" lg="9">
        <application-form></application-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ApplicationForm from "../components/ApplicationForm.vue";
// @ is an alias to /src

export default {
  metaInfo() {

    return { titleTemplate: "%s | Apply",
      meta: [ {
          name: "Apply",
          content: "Apply for a application",
        },
        {
          name: "description",
          content: "Apply for a application",
        },
        {
          property: "og:description",
          content: "BAUST Khulna - A Military Governed Business School",
        },
        {
          vmid: "og_title",
          property: "og:title",
          content: "Army IBA | Apply Now | No Application Fees Required",
        },
        {
          property: "og:url",
          content: "https://www.joinarmyiba.com/apply/",
        },
      ],
    };
  },
  name: "Home",
  components: {
    ApplicationForm,
  },

  mounted() {},

  created() {
    this.$meta().refresh;
  },
  data() {
    return {};
  },
};
</script>
