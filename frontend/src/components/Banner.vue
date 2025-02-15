<template>
  <router-link width="0" to="/apply">
    <v-img
      min-width="100vw"
      contain
      :src="image"
      :lazy-src="image"
      :alt="alt"
    />
  </router-link>
</template>

<script>
export default {
  data() {
    return {
      image: "",
      download_url: "",
      alt: "",
    };
  },
  created() {
    this.$axios.get("home_banner/active_banner/").then((r) => {
      this.image = r.data.image;
      this.alt = r.data.alt;
    });
  },
};
</script>

<style></style>
