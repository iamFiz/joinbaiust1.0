<template>
  <v-container>
    <v-row justify="center" v-if="showApplyStepImage">
       <v-col cols="12" md="10" lg="8" xl="5">
        <v-card class="ma-0" flat>
          <v-card-title> আবেদনের ধাপসমূহ</v-card-title>
          <!-- <v-card-title v-text="$t('Admission Circular')"></v-card-title> -->
          <v-divider class="mb-4"></v-divider>
        <v-img
            min-width="100%"
            contain
            :src="image"
            :alt="alt"
            :lazy-src="image"
          >
          </v-img>
       <v-row justify="center">
             <v-col cols="4">
 <v-btn color="primary" dark :href="download_link" class="ma-6" download width="100%">
            {{ this.$t("Download") }} <v-icon right dark>mdi-download</v-icon>
        </v-btn> 
      </v-col>
       </v-row>
      </v-card>
      </v-col>
 

    </v-row>

   <v-row justify="center" class="pa-0 ma-0 mt-10">
      <v-col cols="12" md="10" lg="8" xl="5">
        <v-card class="ma-0" flat>
          <!-- <v-card-title> নোটিশ </v-card-title> -->
         <v-card-title v-text="$t('Admission Circular')"></v-card-title> 
          <v-divider class="mb-4"></v-divider>
          <v-row justify="center">
            <v-col
              >
              <iframe
                src="https://throughltd-my.sharepoint.com/:w:/p/mail/EWVgb0MWJLZOm0JdTFANXRUB8JPVa7wd6v3OEbCSvC6Q-g?rtime=q_991PlJ3Ug"
                width="100%"
                height="840"
                allow="autoplay"
              ></iframe> 
            </v-col>
          </v-row>
           <!-- <v-row justify="center">
            <v-col
              >
              <iframe
                src="https://drive.google.com/file/d/12f2qMQwht-pcWU3WnlZ9lJ8uGAnJbjXf/preview"
                width="100%"
                height="840"
                allow="autoplay"
              ></iframe> 
            </v-col>
          </v-row> -->
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  metaInfo() {
    return {
      titleTemplate: "%s | Circular",
      meta: [
        {
          name: "Circular",
          content: "Check circular",
        },
      ],
    };
  },
  data() {
    return {
      image: "",
      alt: "",
      download_link: "",
      showApplyStepImage: false,
    };
  },
  created() {
    this.$axios.get("circular_banner/active_banner/").then((r) => {
      this.image = r.data.image;
      this.alt = r.data.alt;
      this.download_link = r.data.download_link;
      this.showApplyStepImage = true;
    });
  },
};
</script>

<style></style>
