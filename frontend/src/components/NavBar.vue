<template>
  <v-container>
    <v-navigation-drawer
      width="100vw"
      floating
      app
      v-model="dialog"
      v-if="$vuetify.breakpoint.smAndDown"
      ><phone-nav-menu
        :items="menuItems"
        @closeDialog="closeDialog"
      ></phone-nav-menu
    ></v-navigation-drawer>
    <v-app-bar
      flat
      :height="$vuetify.breakpoint.smAndDown ? '150px' : '180px'"
      color="white"
      class="d-flex justify-center align-center pa-2"
    >
      <v-app-bar-nav-icon
        @click.stop="dialog = !dialog"
        v-if="$vuetify.breakpoint.smAndDown"
      >
        <template v-slot:default>
          <v-icon>$vuetify.icons.hamburger_aligned </v-icon></template
        >
      </v-app-bar-nav-icon>

      <v-img
        max-width="80vw"
        max-height="60%"
        contain
        src="@/assets/baust.jpeg"
        lazy-src="@/assets/baust.jpeg"
        style="cursor: pointer"
        @click="toHome"
      ></v-img>
    </v-app-bar>
    <v-row>
      <v-app-bar class="pa-4 mb-15" color="transparent" flat>
        <v-row align="center" justify="center">
          <v-toolbar-items>
            <v-btn
              text
              plain
              :ripple="false"
              retain-focus-on-click
              v-for="item in menuItems"
              :key="item.title"
              :to="item.path"
              :class="`flexcol  ${
                $route.path == item.path ? 'active_custom' : ''
              } ${item.show_on_xs ? '' : 'hidden-xs-only'}`"
              :style="{
                'text-transform': 'None',
                'font-weight': 700,
              }"
            >
              <v-icon v-html="`$vuetify.icons.${item.icon}`"> </v-icon>
              <div>{{ item.title }}</div>
            </v-btn>

            <v-menu top v-if="$vuetify.breakpoint.mdAndUp">
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  v-bind="attrs"
                  text
                  v-on="on"
                  plain
                  :ripple="false"
                  offset-y
                  retain-focus-on-click
                  class="flexcol"
                  :style="{
                    'text-transform': 'None',
                    'font-weight': 700,
                  }"
                >
                  <v-icon>$vuetify.icons.language</v-icon>
                  {{ $t("Language") }}
                </v-btn>
              </template>
              <v-list>
                <v-list-item
                  v-for="(item, index) in langs"
                  :key="index"
                  @click="saveLocale(item.value)"
                >
                  {{ item.label }}
                </v-list-item>
              
              </v-list>
            </v-menu>
          </v-toolbar-items>
        </v-row>
      </v-app-bar>
    </v-row>
  </v-container>
</template>

<script>
export default {
  components: { PhoneNavMenu: () => import("./PhoneNavMenu.vue") },

  data() {
    return {
      dialog: false,
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
      appTitle: "Join Army IBA",
      sidebar: false,

      mounted: false,
    };
  },
  computed: {
    menuItems: function () {
      return [
        // { title: "Army IBA", path: "/army-iba" },
        { title: this.$t("Home"), path: "/", icon: "home" },
        {
          title: this.$t("Apply"),
          path: "/apply",
          icon: "apply",
           show_on_xs: true,
        },
        {
          title: this.$t("Circular"),
           path: "/circular",
           icon: "circular",
            show_on_xs: true,
         },
        {
          title: this.$t("Payment"),
          path: "/pay",
          icon: "payment",
          show_on_xs: true,
        },
        {
          title: this.$t("Upload Photo"),
          path: "/upload",
          icon: "uploadPhoto",
          show_on_xs: false,
        },
        // {
        //   title: this.$t("Admit Card"),
        //   path: "/download",
        //   icon: "download",
        //   show_on_xs: true,
        // },
        // {
        //   title: this.$t("Result"),
        //   path: "/result",
        //   icon: "report",
        //   show_on_xs: true,
        // },
        {
          title: this.$t("Status"),
          path: "/status",
          icon: "status",
          show_on_xs: true,
        },

        {
          title: this.$t("Find"),
          path: "/find_application",
          icon: "find",
        },

        {
          title: this.$t("Chat"),
          path: "/chat",
          icon: "chat",
        },
        // { title: "About us", path: "/about-us" },
      ];
    },
  },

  methods: {
    toHome() {
      if (this.$route.path != "/") {
        this.$router.push("/");
      }
    },
    saveLocale(val) {
      this.$root.$i18n.locale = val;
      localStorage.setItem("lang", val);
    },
    closeDialog() {
      this.dialog = false;
    },
  },
};
</script>

<style>
:root {
  --btn_color: #1d9b59;
}
.active_custom {
  color: var(--btn_color) !important;
}
.flexcol .v-btn__content {
  flex-direction: column;
  gap: 2px;
}
.flexcol .v-btn__content:hover {
  color: var(--btn_color) !important;
}
.icon-tabler {
  /* fill: currentColor; */
  stroke: currentColor;
}
</style>
