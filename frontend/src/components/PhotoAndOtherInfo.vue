<template>
  <v-card flat>
    <v-form ref="form">
      <v-card outlined class="pa-4 my-4">
        <v-card-text
          class="text-h5"
          v-text="$t('Personal Information')"
        ></v-card-text>
        <v-divider class="mb-6"></v-divider>
        <v-row class="my-4">
          <v-col cols="12" md="6">
            <v-row justify="center">
              <v-card
                class="my-3"
                outlined
                elevation="0"
                height="202"
                width="202"
              >
                <v-img :src="photo_personal_url" height="100%" contain
                  ><template v-slot:placeholder
                    ><v-row
                      align="center"
                      justify="center"
                      class="fill-height text-center"
                      >Passport size image (300px*300px)
                    </v-row></template
                  ></v-img
                >
              </v-card>
            </v-row>

            <v-file-input
              :rules="photoRules"
              clearable
              accept="image/*"
              show-size
              truncate-length="15"
              v-model="photo_personal"
              @change="loadImage($event, 'photo_personal')"
              :label="$t('Photo')"
            ></v-file-input>
          </v-col>
          <v-col cols="12" md="6">
            <v-row justify="center">
              <v-card
                class="my-3 d-flex align-center"
                outlined
                elevation="0"
                height="202"
                width="202"
              >
                <v-img :src="photo_signature_url" height="80px" width="300px"
                  ><template v-slot:placeholder
                    ><v-row
                      justify="center"
                      align="center"
                      class="fill-height ma-0 text-center"
                      >Image size 80px * 300px
                    </v-row></template
                  ></v-img
                >
              </v-card>
            </v-row>

            <v-file-input
              :rules="photoRules"
              accept="image/*"
              show-size
              clearable
              truncate-length="15"
              v-model="photo_signature"
              @change="loadImage($event, 'photo_signature')"
              :label="$t('Signature')"
            ></v-file-input>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              :rules="requiredRules"
              :label="$t('Birth Place')"
              v-model="birth_place"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-select
              :rules="requiredRules"
              :items="marital_statuses"
              :label="$t('Marital Status')"
              v-model="marital_status"
            ></v-select>
          </v-col>
        </v-row>

        <v-text-field
          :rules="requiredRules"
          :label="$t('Permanent Address')"
          v-model="permanent_address"
        ></v-text-field>
      </v-card>
      <v-card outlined class="pa-4 my-4">
        <v-card-text
          class="text-h5"
          v-text="$t('Educational Qualifications')"
        ></v-card-text>
        <v-divider class="mb-6"></v-divider>
        <v-row justify="center">
          <v-radio-group row v-model="study_level" :label="$t('Study Level')">
            <v-radio
              v-for="(level, index) in study_level_list"
              :key="index"
              :label="$t(`${level.label}`)"
              :value="level.value"
            ></v-radio>
          </v-radio-group> </v-row
        ><v-text-field
          v-if="study_level == 'ssc'"
          :rules="requiredRules"
          v-model="ssc_roll"
          :label="$t('SSC Roll')"
        ></v-text-field>

        <v-row v-if="study_level == 'ssc'">
          <v-col cols="12" md="6">
            <v-select
              :rules="requiredRules"
              :items="board_list"
              v-model="ssc_board"
              :label="$t('SSC Board')"
            ></v-select> </v-col
          ><v-col cols="12" md="6"
            ><v-select
              :rules="requiredRules"
              :items="groups"
              v-model="ssc_group"
              :label="$t('Group')"
            ></v-select>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              type="number"
              max="5"
              min="0"
              :rules="requiredRules"
              v-model="gpa"
              :label="$t('Grade Point')"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-select
              :items="[2018,2019,2020]"
              v-model="passing_year"
              :label="$t('Passing Year')"
              :rules="requiredRules"
              required
            ></v-select>
          </v-col>
        </v-row>
        <v-text-field
          v-model="institution"
          :rules="requiredRules"
          :label="$t('Institution')"
        ></v-text-field>
      </v-card>
      <v-card outlined class="pa-4 my-4">
        <v-card-text
          class="text-h5"
          v-text="$t('Physical Description')"
        ></v-card-text>

        <v-divider class="mb-6"></v-divider>
        <v-text-field
          :rules="requiredRules"
          :label="$t('Identification Mark')"
          v-model="identification_mark"
        ></v-text-field>

        <v-select
          :items="blood_groups"
          :label="$t('Blood Group')"
          :rules="requiredRules"
          v-model="blood_group"
        ></v-select>
      </v-card>
      <v-card outlined class="pa-4 my-4">
        <v-card-text
          class="text-h5"
          v-text="$t('Father\'s Information')"
        ></v-card-text>
        <v-divider class="mb-6"></v-divider>
        <v-text-field
          v-model="name_father"
          :rules="requiredRules"
          :label="$t('Father\'s Name')"
        ></v-text-field>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="work_place_father"
              :label="$t('Work Place')"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="designation_father"
              :label="$t('Designation')"
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              :rules="phoneRules"
              counter="11"
              v-model="phone_father"
              :label="$t('Father\'s Mobile Number')"
            ></v-text-field></v-col
          ><v-col cols="12" md="6">
            <v-text-field
              v-model="national_id_father"
              :label="$t('National ID')"
            ></v-text-field
          ></v-col>
        </v-row>
      </v-card>
      <v-card outlined class="pa-4 my-4">
        <v-card-text
          class="text-h5"
          v-text="$t('Mother\'s Information')"
        ></v-card-text>
        <v-divider class="mb-6"></v-divider>
        <v-text-field
          :rules="requiredRules"
          v-model="name_mother"
          :label="$t('Mother\'s Name')"
        ></v-text-field>
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="work_place_mother"
              :label="$t('Work Place')"
            ></v-text-field></v-col
          ><v-col cols="12" md="6">
            <v-text-field
              v-model="designation_mother"
              :label="$t('Designation')"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              :rules="phoneRules"
              counter="11"
              v-model="phone_mother"
              :label="$t('Mother\'s Mobile Number')"
            ></v-text-field></v-col
          ><v-col cols="12" md="6">
            <v-text-field
              v-model="national_id_mother"
              :label="$t('National ID')"
            ></v-text-field
          ></v-col>
        </v-row>
      </v-card>

      <v-card outlined class="pa-4 my-4">
        <v-card-text
          class="text-h5"
          v-text="$t('Others Information')"
        ></v-card-text>
        <v-divider class="mb-6"></v-divider>
        <v-radio-group
          v-model="has_working_experience"
          row
          :label="$t('Did You Have any Working Experience?')"
        >
          <v-radio :label="$t('Yes')" :value="1"></v-radio>
          <v-radio :label="$t('No')" :value="0"></v-radio>
        </v-radio-group>
        <v-textarea
          :rules="requiredRules"
          v-if="has_working_experience"
          v-model="working_experience_details"
          :label="$t('In Details')"
        >
        </v-textarea>
        <v-select
          :rules="requiredRules"
          :items="source_list"
          v-model="information_source"
          :label="$t('HOW_DID_YOU_GET_THE_INFORMATION')"
        ></v-select>
        <v-text-field
          :rules="requiredRules"
          v-if="information_source == 'others'"
          v-model="information_source_details"
          :label="$t('In Details')"
        ></v-text-field>
      </v-card>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" @click="upload" :loading="loading">{{
          this.$t("SUBMIT")
        }}</v-btn
        ><v-spacer></v-spacer>
      </v-card-actions>
    </v-form>
     <v-snackbar color="green lighten-2" centered v-model="show_snackbar"  >{{ this.$t(snackbar_message) }}
      <template v-slot:action="{ attrs }">
        <v-btn dark text v-bind="attrs" @click="show_snackbar = false">
          {{ $t("Close") }}
        </v-btn>
      </template>
    </v-snackbar>
  </v-card>
</template>

<script>
export default {
  props: ["application_id"],
  data() {
    return {
      loading: false,
      form: "",
      birth_place: "",
      marital_status: "",
      permanent_address: "",
      identification_mark: "",
      blood_group: "",
      name_father: "",
      designation_father: "",
      work_place_father: "",
      national_id_father: "",
      phone_father: "",
      name_mother: "",
      designation_mother: "",
      work_place_mother: "",
      national_id_mother: "",
      phone_mother: "",
      ssc_roll: "",
      ssc_board: "",
      ssc_group: "",
      photo_personal: null,
      photo_signature: null,
      photo_personal_url: "",
      photo_signature_url: "",
      information_source: "",
      gpa: "",
      passing_year: "",
      institution: "",
      study_level: "ssc",
      has_working_experience: 0,
      working_experience_details: "",
      information_source_details: "",
      show_snackbar: false,
      snackbar_message: "",
    };
  },

  methods: {
    loadImage(e, type) {
      if (!this[type]) return (this[type + "_url"] = "");
      return (this[type + "_url"] = URL.createObjectURL(this[type]));
    },

    upload() {
      if (this.$refs.form.validate()) {
        this.loading = true;
        const {
          birth_place,
          marital_status,
          permanent_address,
          identification_mark,
          blood_group,
          name_father,
          designation_father,
          work_place_father,
          national_id_father,
          phone_father,
          name_mother,
          designation_mother,
          work_place_mother,
          national_id_mother,
          phone_mother,
          passing_year,
          institution,
          ssc_roll,
          ssc_board,
          ssc_group,
          photo_personal,
          photo_signature,
          information_source,
          study_level,
          has_working_experience,
          information_source_details,
          working_experience_details,
          gpa,
        } = this;
        var data = {
          passing_year,
          institution,
          information_source,
          birth_place,
          marital_status,
          permanent_address,
          identification_mark,
          blood_group,
          name_father,
          designation_father,
          work_place_father,
          national_id_father,
          phone_father,
          name_mother,
          designation_mother,
          work_place_mother,
          national_id_mother,
          phone_mother,
          gpa,

          photo_personal,
          photo_signature,
          study_level,
          has_working_experience,
        };

        const formData = new FormData();
        if (study_level === "ssc") {
          data = {
            ...data,
            ssc_roll,
            ssc_board,
            ssc_group,
          };
        }

        if (has_working_experience) {
          formData.append(
            "working_experience_details",
            working_experience_details
          );
        }
        if (information_source == "others") {
          formData.append(
            "information_source_details",
            information_source_details
          );
        }
        formData.append("application", this.application_id);
        for (var key in data) {
          if (data[key] !== "") {
            formData.append(key, data[key]);
          }
        }

        this.$axios
          .post("/extra_information/", formData)
          .then(() => {
            this.show_snackbar=true
            this.snackbar_message="আপনার ছবি, স্বাক্ষর ও অন্যান্য তথ্য সফলভাবে জমা হয়েছে। পরীক্ষার প্রবেশপত্র পাবার জন্যে আর্মি আইবিএ কতৃপক্ষের মেসেজের জন্যে অপেক্ষা করুন।"
            this.loading = false;
          })
          .catch((error) => {
            alert(error.response.data);
            this.loading = false;
          });
      }
    },
  },

  computed: {
    blood_groups() {
      return ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"].map((item) => {
        return { text: this.$t(item), value: item };
      });
    },

    marital_statuses() {
      return [
        { text: this.$t("Single"), value: "single" },
        { text: this.$t("Married"), value: "married" },
        { text: this.$t("Divorced"), value: "divorced" },
        { text: this.$t("Widowed"), value: "widowed" },
      ];
    },
    groups: function () {
      return [
        { text: this.$t("Science"), value: "science" },
        { text: this.$t("Commerce"), value: "commerce" },
        { text: this.$t("Arts"), value: "arts" },
      ];
    },
    board_list: function () {
      return [
        { text: this.$t("Dhaka"), value: "dhaka" },
        { text: this.$t("Comilla"), value: "comilla" },
        { text: this.$t("Barisal"), value: "barisal" },
        { text: this.$t("Chittagong"), value: "chittagong" },
        { text: this.$t("Jessore"), value: "jessore" },
        { text: this.$t("Dinajpur"), value: "dinajpur" },
        { text: this.$t("Gazipur"), value: "gazipur" },
        { text: this.$t("Mymensingh"), value: "mymensingh" },
        { text: this.$t("Sylhet"), value: "sylhet" },
        { text: this.$t("Rajshahi"), value: "rajshahi" },
        { text: this.$t("Madrasah"), value: "madrasah" },
      ];
    },
    source_list() {
      return [
        { text: this.$t("Newspaper"), value: "newspaper" },
        { text: this.$t("Google Search"), value: "google_search" },
        { text: this.$t("Facebook Group"), value: "facebook_group" },
        { text: this.$t("Facebook Page"), value: "facebook_page" },
        { text: this.$t("Friends"), value: "friends" },
        { text: this.$t("Television"), value: "television" },
        { text: this.$t("Relatives"), value: "relatives" },
        {
          text: this.$t("BAUST Khulna Current Students"),
          value: "aiba_current_students",
        },
        { text: this.$t("Others"), value: "others" },
      ];
    },

    study_level_list() {
      return [
        { label: "SSC", value: "ssc" },
        { label: "O Level", value: "o_level" },
      ];
    },
    requiredRules: function () {
      return [(v) => !!v || this.$t("This field is required")];
    },

    phoneRules: function () {
      return [
        (v) => !v || /^\d{11}$/.test(v) || this.$t("Phone must be 11 digits"),
      ];
    },
    photoRules: function () {
      return [
        (v) => !!v || this.$t("This field is required"),
        (v) =>
          !v || v.size < 1000000 || this.$t("Photo size must be less than 1MB"),
      ];
    },
  },
};
</script>

<style>
</style>