<template>
  <v-card min-width="100%" flat>
    <v-row class="my-5">
      <v-col>
        <v-form lazy-validation ref="form">
          <v-card-text
            class="text-center text-h5 font-weight-bold"
            v-text="$t('GET_UPDATE_FROM_BUAST_KHULNA')"
          ></v-card-text>
          <v-row class="px-5" justify="center">
            <v-col cols="12" sm="4" md="3">
              <v-text-field
                v-model="name"
                :rules="[rules.required]"
                :label="$t('Name')"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="4" md="3">
              <v-select
                :label="$t('Occupation')"
                :items="occupation_set"
                v-model="occupation"
                :rules="[rules.required]"
                item-text="label"
                item-value="value"
              ></v-select>
            </v-col>
          </v-row>
          <v-row class="px-5" justify="center">
            <v-col cols="12" sm="4" md="3">
              <vue-tel-input-vuetify
                defaultCountry="bd"
                :rules="[rules.required, rules.numeric]"
                v-model="phone"
                :label="$t('Mobile')"
                :placeholder="$t('Enter your Mobile Number')"
              ></vue-tel-input-vuetify>
            </v-col>
            <v-col cols="12" sm="4" md="3">
              <v-text-field
                :rules="[rules.required, rules.email]"
                v-model="email"
                :label="$t('Email')"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row justify="center" class="pa-3">
            <v-btn color="primary" dark @click="submit"
              >{{ this.$t("SUBMIT") }}
            </v-btn>
          </v-row>
        </v-form>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      name: null,
      email: null,
      occupation: null,
      phone: "",
    };
  },
  computed: {
    rules() {
      return {
        required: (value) => !!value || "Required.",
        counter: (value) => value.length <= 20 || "Max 20 characters",
        email: (value) => {
          const pattern =
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || "Invalid e-mail.";
        },
        numeric: (value) =>
          /^\d+$/.test(value) || "Only numbers are allowed.",
      };
    },
    occupation_set: function () {
      return [
        {
          label: this.$t("Student"),
          value: "student",
        },
        {
          label: this.$t("Teacher"),
          value: "teacher",
        },
        {
          label: this.$t("Guardian"),
          value: "guardian",
        },
      ];
    },
  },
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        this.$axios
          .post("subscribers/", {
            name: this.name,
            occupation: this.occupation,
            phone: this.phone,
            email: this.email,
          })
          .then(() => {
            alert("Subscribed Successfully");
          })
          .catch((err) => {
            this.loading = false;
            if (err.response.status === 400) {
              alert(this.$t("You have already registered."));
            } else {
              alert(this.$t("Something went wrong from our site."));
            }
          });
      }
    },
  },
};
</script>

<style></style>
