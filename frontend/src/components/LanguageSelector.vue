<template>
  <v-select
    :items="langs"
    item-text="label"
    item-value="value"
    v-model="$root.$i18n.locale"
    @change="saveLocale"
    prepend-icon="$vuetify.icons.language"
    :style="{ 'max-width': max_width }"
  >
  </v-select>
</template>

<script>
export default {
  name: "LanguageSelector",
  props: ["max_width"],
  data() {
    return {
      langs: [
        {
          label: "বাংলা",
          value: "bn",
          img: "@/assets/bangla.png",
        },
        {
          label: "English",
          value: "en",
        },
      ],
    };
  },
  methods: {
    saveLocale(val) {
      localStorage.setItem("lang", val);
    },
  },
};
</script>

<style></style>
