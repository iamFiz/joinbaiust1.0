<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="11" md="8" lg="5" class="px-0">
        <v-card-title v-text="$t('Talk to Us')"></v-card-title>
        <v-divider></v-divider>
      </v-col>
    </v-row>

    <v-card flat>
      <v-row justify="center">
        <v-col cols="11" lg="5" md="8">
          <v-card-text
            class="text-subtitle-1 font-weight-bold text-justify pa-0 mt-6"
            v-html="$t('CHAT_OPEN_INSTRUCTION')"
          ></v-card-text>
          <v-form ref="form" class="py-8">
            <v-text-field
              :rules="[rules.required]"
              :label="$t('Name')"
              v-model="name"
            ></v-text-field>
            <v-text-field
              :rules="[rules.required, rules.email]"
              :label="$t('Email')"
              v-model="email"
            ></v-text-field>
            <v-text-field
              :rules="[rules.required]"
              :label="$t('Area')"
              v-model="area"
            ></v-text-field>
            <v-text-field
              :rules="[rules.required]"
              :label="$t('Phone')"
              v-model="phone"
            ></v-text-field>
             <v-text-field
              :label="$t('Application ID')"
              v-model="application_id"
            ></v-text-field>
            <v-select :items="problemTypes" v-model="problem_type" :label="$t('Problem Type')">

            </v-select>
            <!-- <v-text-field :label="$t('Country')" v-model="country"></v-text-field> -->
            <v-textarea
              :rules="[rules.required]"
              :label="$t('Message')"
              v-model="message"
            ></v-textarea
            ><v-card-actions
              ><v-spacer> </v-spacer>
              <!-- TODO: Update Button -->
              <v-btn @click="submit" color="primary">{{
                this.$t("SUBMIT")
              }}</v-btn
              ><v-spacer> </v-spacer>
            </v-card-actions> </v-form
          ><v-card-text
            class="text-center font-weight-bold text-subtitle-1"
            v-text="$t('CHAT_FORM_RESPONSE_48')"
          ></v-card-text
          ><v-card-text
            class="text-center font-weight-bold text-subtitle-1 my-0 py-0"
            v-text="$t('IMMEDIATE_CONTACT')"
          >
          </v-card-text
        ></v-col>
      </v-row> </v-card
  ></v-container>
</template>

<script>
export default {
  metaInfo() {
    return {
          titleTemplate: "%s | Chat",
      meta: [
        {
          name: "Chat",
          content: "Do chat",
        },
      ],
      scripts: [
        {
          innerHTML: `(function (w, d, s, l, i) {
          w[l] = w[l] || []; w[l].push({
            'gtm.start':
              new Date().getTime(), event: 'gtm.js'
          }); var f = d.getElementsByTagName(s)[0],
            j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : ''; j.async = true; j.src =
              'https://www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
        })(window, document, 'script', 'dataLayer', 'GTM-P4RWXPZ');`,
          vmid: "gtm",
          from: "chat",
        },
      ],
    };
  },
  data() {
    return {
      name: "",
      email: "",
      phone: "",
      country: "",
      message: "",
      area: "",
      application_id: "",
      problem_type: "",
    };
  },
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        this.$axios
          .post("/chat/", {
            name: this.name,
            email: this.email,
            phone: this.phone,
            area: this.area,
            // country: this.country,
            message: this.message,
            application_id: this.application_id,
            problem_type: this.problem_type,
          })
          .then(() => {
            alert(this.$t("Submitted Successfully"));
            this.name = "";
            this.email = "";
            this.phone = "";
            this.area = "";
            // this.country = "";
            this.message = "";
            this.application_id = "";
            this.problem_type = "";
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
  computed: {
    problemTypes(){
       return [
          {text: 'ওয়েবসাইট', value: 'website'},
          {text: 'আবেদন সংক্রান্ত', value: 'during_application'},
          {text: 'বিজ্ঞপ্তি', value: 'circular'},
          {text: 'ফি-প্রদান', value: 'payment'},
          {text: 'ছবি জমা', value: 'photo_upload'},
          {text: 'পেমেন্ট উইন্ডো ওপেন', value: 'open_payment_window'},
          {text: 'অন্যান্য', value: 'others'},
       ]
    },

    rules() {
      return {
        required: (value) => !!value || "Required.",
        counter: (value) => value.length <= 20 || "Max 20 characters",
        email: (value) => {
          const pattern =
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || "Invalid e-mail.";
        },
      };
    },
  },
};
</script>

<style></style>
