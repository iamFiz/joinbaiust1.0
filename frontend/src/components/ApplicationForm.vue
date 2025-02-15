<template>
  <v-row justify="center">
    <v-col cols="12" md="10" lg="8">
      <v-card class="pa-0" flat color="white">
        <v-card-text style="word-break: keep-all; color: black"
          class="text-center font-weight-bold text-xl-h4 text-md-h5">{{ $t("site_title") }}
        </v-card-text>
        <v-card-text style="word-break: keep-all; color: black"
          class="text-center font-weight-bold text-xl-h5 text-md-h6">
          {{ $t("site_subtitle") }}</v-card-text>

        <v-form ref="form">

          <v-card elevation="0" outlined class="pa-4 my-2">
            <v-row>
              <v-col>
                <v-select :items="[{
                  text: $t('UNDERGRADUATE_PROGRAM_1'), value: 'BBA1'
                },
                {
                  text: $t('UNDERGRADUATE_PROGRAM_2'), value: 'BBA2'
                },
                {
                  text: $t('UNDERGRADUATE_PROGRAM_3'), value: 'BBA3'
                },
                {
                  text: $t('UNDERGRADUATE_PROGRAM_4'), value: 'BBA4'
                },
                {
                  text: $t('UNDERGRADUATE_PROGRAM_5'), value: 'BBA5'
                },
                {
                  text: $t('UNDERGRADUATE_PROGRAM_6'), value: 'BBA6', disabled: true 
                },
                {
                  text: $t('UNDERGRADUATE_PROGRAM_7'), value: 'BBA7', disabled: true 
                }]" v-model="programme" label="APPLICATION_PROGRAM"></v-select>
              </v-col>
            </v-row>
            <v-card-text style="color: black" class="ma-0 pa-0 font-weight-bold">{{ $t("Details about Applicant:")
            }}</v-card-text>
            <v-row>
              <v-col cols="12" md="6"><v-select :items="venues" v-model="venue" item-text="label" item-value="value"
                  required :label="$t('Applying Venue')" :rules="requiredRules">
                </v-select></v-col>
              <v-col cols="12" md="6">
                <v-select row v-model="quota" :items="quota_list" item-text="label" item-value="value"
                  :label="$t('Quota')">
                </v-select>
              </v-col>
            </v-row>

            <v-text-field v-model="name" placeholder="Tanvir Mahtab" :rules="requiredRules" required
              :label="$t('Full Name')">
            </v-text-field>
            <!-- <v-file-input
                                                    v-model="photo"
                                                    :rules="requiredRules"
                                                    label="Photo"
                                                  ></v-file-input> -->
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field v-model="phone" placeholder="01797925566" type="tel" counter="11" :rules="phoneRules"
                  :label="$t('Mobile Number for SMS')">
                </v-text-field></v-col>
              <v-col cols="12" md="6">
                <v-text-field v-model="guardians_phone" placeholder="01797925566" type="tel" counter="11"
                  :rules="[...phoneRules,
                    (v) => v!== phone || $t('Guardian’s phone number cannot be the same as the applicant’s phone number')
              ]" :label="$t('Guardian’s Phone Number')">
                </v-text-field>
              </v-col>
            </v-row>
            <v-text-field v-model="email" placeholder="team@joinarmyiba.com" :rules="emailRules"
              :label="$t('Email')"></v-text-field>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field :label="$t('Date of Birth')" v-model="date_of_birth" type="date"
                  :rules="ageRules"></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-select :items="gender_list" v-model="gender" item-text="label" item-value="value" :label="$t('Gender')"
                  required :rules="requiredRules">
                </v-select>
              </v-col>
              <!-- <v-col cols="12" md="6">
                                                        <v-text-field
                                                          v-model="nationality"
                                                          label="Nationality"
                                                          placeholder="Bangladeshi"
                                                          :rules="requiredRules"
                                                        ></v-text-field>
                                                      </v-col> -->
            </v-row>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field v-model="address"
                  placeholder="House: 37 (Ventura Capital), Road: 11, Gulshan, Dhaka 1213, BD"
                  :rules="presentAddressRules" :label="$t('Present Address')">
                </v-text-field></v-col>
              <v-col cols="12" md="6">
                <v-select v-model="district" placeholder="Dhaka" :items="district_list" item-text="label"
                  item-value="value" :rules="requiredRules" :label="$t('District')"></v-select></v-col>
            </v-row>
          </v-card>
          <v-card elevation="0" outlined class="pa-4 my-2">
            <v-row justify="center">
              <v-radio-group row v-model="study_level" :label="$t('Study Level')">
                <v-radio v-for="(level, index) in study_level_list" :key="index" :label="$t(`${level.label}`)"
                  :value="level.value"></v-radio>
              </v-radio-group>
            </v-row>

            <v-row v-if="study_level == 'hsc'">
              <v-col cols="12" md="6">
                <v-text-field v-model="hsc_roll" :rules="requiredRules" placeholder="12345678901234"
                  :label="$t('HSC/Alim Roll')"></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field v-model="hsc_reg_no" :label="$t('HSC/Alim Registration No.')" placeholder="12345678901234"
                  :rules="requiredRules"></v-text-field>
              </v-col>
            </v-row>

            <v-row v-if="study_level == 'hsc'">
              <v-col cols="12" md="6">
                <v-select :items="board_list" item-text="label" item-value="value" v-model="hsc_board" placeholder="Dhaka"
                  :rules="requiredRules" :label="$t('HSC/Alim Board')"></v-select>
              </v-col>
              <v-col cols="12" md="6">
                <v-select :items="hsc_groups" v-model="hsc_group" :rules="requiredRules" :label="$t('HSC/Alim Group')"
                  item-text="label" item-value="value" required></v-select>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field v-model="gpa" type="number" max="5" placeholder="2.5" min="0" step="0.01"
                  :rules="study_level == 'hsc' ? hscGPARules : ALevelGPARules" :label="$t('Grade Point')"></v-text-field>
              </v-col>

              <v-col cols="12" md="6">
                <v-select :items="passing_year_choices" v-model="passing_year" :label="$t('Passing Year')"
                  :rules="requiredRules" required></v-select>
              </v-col>
            </v-row>

            <v-text-field v-model="institution" placeholder="Mastermind School" :rules="requiredRules"
              :label="$t('Institution')"></v-text-field>
            <v-select :rules="requiredRules" :items="source_list" v-model="information_source"
              :label="$t('HOW_DID_YOU_GET_THE_INFORMATION')"></v-select>
          </v-card>
        </v-form>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn :loading="loading" type="submit" color="primary" width="200px" @click="submit">{{ this.$t("GO_TO_NEXT_STEP")
          }}</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      loading: false,

      form: "",
      menu: "",
      name: null,
      //photo: null,
      phone: null,
      email: null,
      date_of_birth: null,
      gender: null,
      nationality: null,
      district: null,
      address: "",
      hsc_roll: null,
      hsc_reg_no: null,
      gpa: null,
      hsc_board: null,
      hsc_group: null,
      passing_year: null,
      study_level: "hsc",
      institution: null,
      guardians_phone: null,
      quota: "general",
      programme: "BBA",
      // father_name: "",
      // father_phone: "",
      // father_occupation: "",
      // mother_name: "",
      // mother_phone: "",
      // mother_occupation: "",
      venue: null,
      information_source: '',
      study_level_list: [
        { label: "HSC/Alim", value: "hsc" },
        { label: "A Level", value: "a_level" },
      ],

      passing_year_choices: [2021, 2022, 2023, 2024, 2025],
      education_boards: ["Dhaka"],
      cantonments: [
        // "Mymensing Cantonment",
        "Dhaka",
        "Khulna",
        "Barisal",
        // "Mirpur Cantonment",
        // "Postogola Cantonment",
        // "Savar Cantonment",
        // "Ghatail Cantonment",
        // "Rajendrapur Cantonment",
        // "Bogra Cantonment",
        // "Jahangirabad Cantonment",
        // "Rangpur Cantonment",
        // "Sayedpur Cantonment",
        // "Kholahati Cantonment",
        // "Qadirabad Cantonment",
        // "Sylhet",
        // "Jalalabad Cantonment",
        // "Rajshahi Cantonment",
        // "Jahanabad Cantonment",
        // "Jessore Cantonment",
        // "Comilla Cantonment",
        // "Chittagong Cantonment",
        // "Alikadam Cantonment",
        // "Ramu Cantonment",
        // "Bandarban Cantonment",
        // "Khagrachhari Cantonment",
        // "Rangamati Cantonment",
        // "Dighinala Cantonment",
        // "Kaptai Cantonment",
      ],
      districts: [
        "Dhaka",
        "Faridpur",
        "Gazipur",
        "Gopalganj",
        "Jamalpur",
        "Kishoreganj",
        "Madaripur",
        "Manikganj",
        "Munshiganj",
        "Mymensingh",
        "Narayanganj",
        "Narsingdi",
        "Netrokona",
        "Rajbari",
        "Shariatpur",
        "Sherpur",
        "Tangail",
        "Bogra",
        "Joypurhat",
        "Naogaon",
        "Natore",
        "Nawabganj",
        "Pabna",
        "Rajshahi",
        "Sirajganj",
        "Dinajpur",
        "Gaibandha",
        "Kurigram",
        "Lalmonirhat",
        "Nilphamari",
        "Panchagarh",
        "Rangpur",
        "Thakurgaon",
        "Barguna",
        "Barisal",
        "Bhola",
        "Jhalokati",
        "Patuakhali",
        "Pirojpur",
        "Bandarban",
        "Brahmanbaria",
        "Chandpur",
        "Chittagong",
        "Comilla",
        "Cox's Bazar",
        "Feni",
        "Khagrachari",
        "Lakshmipur",
        "Noakhali",
        "Rangamati",
        "Habiganj",
        "Maulvibazar",
        "Sunamganj",
        "Sylhet",
        "Bagerhat",
        "Chuadanga",
        "Jessore",
        "Jhenaidah",
        "Khulna",
        "Kushtia",
        "Magura",
        "Meherpur",
        "Narail",
        "Satkhira",
      ],
    };
  },
  computed: {
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
          text: this.$t("BAUST_STUDENTS"),
          value: "aiba_current_students",
        },
        {
          text: this.$t("Bkash"),
          value: "bkash",
        },
        { text: this.$t("Others"), value: "others" },
      ];
    },
    district_list: function () {
      return this.districts.map((district) => ({
        label: this.$t(`${district}`),
        value: district,
      }));
    },
    gender_list: function () {
      return [
        { label: this.$t("Male"), value: "male" },
        { label: this.$t("Female"), value: "female" },
        { label: this.$t("Other"), value: "other" },
      ];
    },
    venues: function () {
      return this.cantonments.map((cantonment) => ({
        label: this.$t(cantonment),
        value: cantonment,
      }));
    },
    hsc_groups: function () {
      return [
        { label: this.$t("Science"), value: "science" },
        { label: this.$t("Commerce"), value: "commerce" },
        { label: this.$t("Arts"), value: "arts" },
      ];
    },
    quota_list: function () {
      return [
        { value: "general", label: this.$t("General") },
        { value: "tribal", label: this.$t("Tribal") },
        // {
        //   value: "armed_forces_officer",
        //   label: this.$t("Armed Forces Officer"),
        // },
        {
          value: "armed_force_personnel",
          label: this.$t("Armed Forces Personnel"),
        },
        {
          value: "freedom_fighter",
          label: this.$t("Freedom Fighter"),
        },
      ];
    },
    requiredRules: function () {
      return [(v) => !!v || this.$t("This field is required")];
    },
    emailRules: function () {
      return [
        (v) => !!v || this.$t("E-mail is required"),
        (v) =>
          /.+@.+\..+/.test(v) || this.$t("Please enter a valid email address"),
      ];
    },
    phoneRules: function () {
      return [
        (v) => !!v || this.$t("Phone is required"),
        (v) => /^\d{11}$/.test(v) || this.$t("Phone must be 11 digits"),
      ];
    },
    ageRules: function () {
      return [
        (v) => !!v || this.$t("Date of Birth is required"),
        (v) =>
          (14 <= new Date().getFullYear() - new Date(v).getFullYear() &&
            new Date().getFullYear() - new Date(v).getFullYear() <= 25) ||
          this.$t("Age must be between 14 and 25"),
      ];
    },
    presentAddressRules: function () {
      return [
        (v) => !!v || this.$t("Present Address is required"),
        (v) =>
          v.length >= 5 ||
          this.$t("Present Address must be at least 5 characters"),
      ];
    },
    hscGPARules: function () {
      return [
        (v) => !!v || this.$t("GPA is required"),
        (v) => (v >= 0 && v <= 5) || this.$t("GPA must be between 0 and 5"),
      ];
    },
    ALevelGPARules: function () {
      return [
        (v) => !!v || this.$t("GPA is required"),
        (v) => (v >= 0 && v <= 4) || this.$t("GPA must be between 0 and 4"),
      ];
    },
    board_list: function () {
      return [
        { label: this.$t("Dhaka"), value: "dhaka" },
        { label: this.$t("Comilla"), value: "comilla" },
        { label: this.$t("Barisal"), value: "barisal" },
        { label: this.$t("Chittagong"), value: "chittagong" },
        { label: this.$t("Jessore"), value: "jessore" },
        { label: this.$t("Dinajpur"), value: "dinajpur" },
        { label: this.$t("Gazipur"), value: "gazipur" },
        { label: this.$t("Mymensingh"), value: "mymensingh" },
        { label: this.$t("Sylhet"), value: "sylhet" },
        { label: this.$t("Rajshahi"), value: "rajshahi" },
        { label: this.$t("Madrasah"), value: "madrasah" },
      ];
    },
  },
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        this.loading = true;
        const {
          name,
          // photo,
          phone,
          email,
          date_of_birth,
          gender,
          //nationality,
          hsc_roll,
          hsc_reg_no,
          gpa,
          hsc_board,
          hsc_group,
          passing_year,
          study_level,
          institution,
          address,
          district,
          quota,
          guardians_phone,
          // father_name,
          // father_phone,
          // father_occupation,
          // mother_name,
          // mother_phone,
          // mother_occupation,
          venue,
          information_source, programme
        } = this;
        var data = {
          name,
          //photo,
          phone,
          email,
          date_of_birth,
          gender,
          guardians_phone,
          //nationality,
          gpa,
          passing_year,
          study_level,
          address,
          district,
          quota,
          // father_name,
          // father_phone,
          // father_occupation,
          // mother_name,
          // mother_phone,
          // mother_occupation,
          venue,
          institution,
          information_source, programme
        };
        study_level == "hsc" &&
          (data = { ...data, hsc_board, hsc_group, hsc_roll, hsc_reg_no });

        const formData = new FormData();
        Object.keys(data).forEach((key) =>
          data[key] == null ? delete data[key] : formData.append(key, data[key])
        );

        this.$axios
          .post("/application", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          })
          .then((response) => {
            this.loading = false;
            // window.location.href =
            //   "/success?application_id=" + response.data.id;
            this.$router.push({
              name: "Success",
              query: { application_id: response.data.id },
            });
          })
          .catch((err) => {
            this.loading = false;
            if (err.response.status === 400) {
              if(err.response.data['non_field_errors'][0]==="You have already registered.")
                alert(this.$t("You have already registered."));
              else
                alert("Something went wrong. Please try again later.\n"+
                +"Error: "+err.response.data);
            } else {
              alert(this.$t("Something went wrong. Please try again later."));
            }
            // this.$router.push({
            //   name: "Error",
            //   params: { application_id: err.response.data.id },
            // });
          });
      }
    },
  },
};
</script>

<style>
/* .v-card__title,
h4 {
  color: #a1b57d;
} */
</style>
