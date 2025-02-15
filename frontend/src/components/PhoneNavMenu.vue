<template>
  <v-card flat>
    <v-toolbar height="200px" flat c>
      <v-img
        max-width="200px"
        contain
        src="@/assets/armyiba.webp"
        lazy-src="@/assets/armyiba.webp"
      ></v-img>
      <v-spacer></v-spacer>
      <v-btn icon @click="$emit('closeDialog')"
        ><v-icon>mdi-close</v-icon></v-btn
      >
    </v-toolbar>
    <v-row justify="center">
      <language-selector max_width="130px"></language-selector>
    </v-row>

    <v-row justify="center" align="center" class="pa-3">
      <v-col v-for="item in items" :key="item.title" cols="6">
        <v-card
          link
          :to="item.path"
          width="100%"
          height="70px"
          @click="dialog = false"
          class="pa-2 d-flex align-center justify-center text-center"
        >
          <v-icon class="ml-3" v-html="`$vuetify.icons.${item.icon}`"></v-icon>
          <v-card-text class="ma-0 pl-2">{{ item.title }}</v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import LanguageSelector from "./LanguageSelector.vue";
export default {
  emits: ["closeDialog"],
  props: ["items"],
  components: { LanguageSelector },
};
</script>

<style></style>
