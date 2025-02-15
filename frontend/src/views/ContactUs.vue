<template>
  <v-row class="ma-0" justify="center">
    <v-col cols="12" md="10" lg="5">
      <v-card flat>
        <v-card-title v-text="$t('Contact Us')"></v-card-title>
        <v-divider></v-divider>
        <v-card-text
          class="font-weight-bold text--h4 pb-2"
          v-text="$t('Campus:')"
        >
        </v-card-text>
        <v-card-text
          class="py-0 my-0"
          v-text="$t('Shiromoni, Fultala, close to Jahanabad Cantonment, Khanjahan Ali, Khulna 9204, Bangladesh')"
        >
        </v-card-text>
        <v-card-text
          class="font-weight-bold text--h4 mt-4 pb-2"
          v-text="$t('Phone:')"
        ></v-card-text>
        <v-card-text
          class="py-0"
          v-text="`${$t('Office:')} ${$t('+88 02 996642777')}`"
        ></v-card-text>

        <!-- <v-card-text
          class="font-weight-bold text--h4 mt-4 pb-2"
          v-text="$t('Email:')"
        ></v-card-text>
        <v-card-text
          tag="a"
          class="py-0"
          href="mailto:armyiba@applykoro.com"
          v-text="'armyiba@applykoro.com'"
        ></v-card-text> -->
        <v-card-text
          class="font-weight-bold text--h4 mt-4 pb-2"
          v-text="$t('Media Personals:')"
        ></v-card-text>
        <v-card-text
          tag="a"
          href="mailto:armyibasylhet@throughedltd.com"
          v-text="'armyibasylhet@throughedltd.com'"
        ></v-card-text>
        <v-card-text
          class="font-weight-bold text--h4 mt-4 pb-2"
          v-text="$t('Website:')"
        ></v-card-text>
        <v-card-text
          class="py-0"
          target="_blank"
          tag="a"
          href="https://baustkhulna.ac.bd"
          v-text="'baustkhulna.ac.bd'"
        ></v-card-text>
        <v-card-text
          class="font-weight-bold text--h4"
          v-text="$t('Follow us on:')"
        ></v-card-text>
        <v-btn
          class="mx-3"
          icon
          link
          href="https://www.facebook.com/baustkhulna"
          target="_blank"
          ><v-icon x-large color="blue">mdi-facebook</v-icon></v-btn
        >
        <v-btn
          class="mx-3"
          icon
          target="_blank"
          link
          href="https://www.x.com/baustkhulna "
          ><v-icon x-large color="blue lighten-2">mdi-twitter</v-icon></v-btn
        >
        <v-btn
          class="mx-3"
          icon
          link
          target="_blank"
          href="https://www.instagram.com/baustkhulna"
          ><v-icon x-large color="red lighten-2">mdi-instagram</v-icon></v-btn
        >
      </v-card><br>

      <v-card-text
              class="py-0 my-0"
              v-text="$t('ApplyingNext is a one-stop application platform that enables individuals to apply to educational institutions and companies effortlessly. By connecting applicants with registered institutions, we simplify the application process, making opportunities more accessible for everyone.')"
      ></v-card-text>
      <br>
      <v-card-text
  class="py-0 my-0"
  v-text="$t('baustkhulna.applyingnext.com is a joint initiative of Bangladesh Army University of Science and Technology Khulna, and Applying Next. The website has been launched to assist students in applying for admission to the university\'s entrance exam in a hassle-free, simple, and seamless manner.')"
></v-card-text>
<br>
<v-card-text
  class="py-0 my-0"
  v-text="$t('Applying Next is a one-stop application platform that enables individuals to apply to educational institutions and companies effortlessly. By connecting applicants with registered institutions, we simplify the application process, making opportunities more accessible for everyone.')"
></v-card-text>
<br>
<v-card-text
  class="py-0 my-0"
  v-text="$t('Bangladesh Army University of Science and Technology, Khulna (BAUST Khulna), a military institution, operates under the supervision of the Bangladesh Army. It was established to promote academic excellence and leadership, the university is temporarily located near Jahanabad Cantonment in Khulna District.')"
></v-card-text>

    </v-col>
    
  </v-row>

</template>



<script>
export default {
  metaInfo() {
    return {
      meta: [
        {
          name: "Contact us",
          content: "contact with us",
        },
      ],
    };
  },
};
</script>

<style scoped>
* {
  color: rgba(0, 0, 0, 0.89) !important;
}
</style>
