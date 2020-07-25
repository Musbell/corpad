<template>
  <div>
    <v-card flat>
      <v-container>
        <v-row>
          <v-col cols="12" sm="4">
            <div class="grey--text">Status</div>
            <div class="title red--text">New</div>
          </v-col>
          <v-col cols="12" sm="4">
            <div class="grey--text">Borrower</div>
            <div class="title">Bello Musa</div>
          </v-col>
          <v-col cols="12" sm="4">
            <div class="grey--text">Close date</div>
            <div class="title">02/02/2020</div>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" sm="4">
            <div class="grey--text">Loan type</div>
            <div class="title">Term/Perm</div>
          </v-col>
          <v-col cols="12" sm="4">
            <div class="display-1 green--text">N10,000</div>
          </v-col>
          <v-col cols="12" sm="4">
            <div class="grey--text">Completed tarsk</div>
            <v-progress-linear v-model="knowledge" height="25" reactive>
              <strong>{{ Math.ceil(knowledge) }}%</strong>
            </v-progress-linear>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
    <v-card flat class="mt-5">
      <v-container>
        <v-subheader>Current Loan Detail</v-subheader>
        <v-form v-model="valid">
          <v-container>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="firstname"
                  :rules="nameRules"
                  :counter="10"
                  label="Request amount"
                  placeholder="N10,000"
                  required
                  outlined
                  disabled
                  dense
                ></v-text-field>
              </v-col>

              <v-col cols="12" md="6">
                <v-text-field
                  v-model="email"
                  :rules="emailRules"
                  label="Amorization Term"
                  placeholder="360 Months"
                  required
                  outlined
                  disabled
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="firstname"
                  :rules="nameRules"
                  :counter="10"
                  label="Loan amount"
                  placeholder="N20,000"
                  required
                  outlined
                  dense
                  disabled
                ></v-text-field>
              </v-col>

              <v-col cols="12" md="6">
                <v-text-field
                  v-model="email"
                  :rules="emailRules"
                  label="Maturity Term"
                  placeholder="120 Months"
                  required
                  outlined
                  disabled
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="firstname"
                  :rules="nameRules"
                  :counter="10"
                  label="Rate"
                  placeholder="2.9"
                  required
                  outlined
                  dense
                  disabled
                ></v-text-field>
              </v-col>

              <v-col cols="12" md="6">
                <v-text-field
                  v-model="email"
                  :rules="emailRules"
                  label="Interest on"
                  placeholder="Approved amount"
                  required
                  outlined
                  dense
                  disabled
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model="firstname"
                  :rules="nameRules"
                  :counter="10"
                  label="Monthly payment"
                  placeholder="Principal & Interest"
                  required
                  outlined
                  dense
                  disabled
                ></v-text-field>
              </v-col>

              <v-col cols="12" md="6">
                <v-text-field
                  v-model="email"
                  :rules="emailRules"
                  label="Points"
                  placeholder="2.9"
                  required
                  outlined
                  dense
                  disabled
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-container>
    </v-card>
    <v-card flat class="mt-5">
      <v-subheader>Previous Loans</v-subheader>
      <v-data-table
        :headers="headers"
        :items="desserts"
        :items-per-page="5"
        class="elevation-1"
      ></v-data-table>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'Index',
  data: () => ({
    skill: 20,
    knowledge: 33,
    power: 78,
    valid: false,
    firstname: '',
    lastname: '',
    nameRules: [
      (v) => !!v || 'Name is required',
      (v) => v.length <= 10 || 'Name must be less than 10 characters',
    ],
    email: '',
    emailRules: [
      (v) => !!v || 'E-mail is required',
      (v) => /.+@.+/.test(v) || 'E-mail must be valid',
    ],
    headers: [
      {
        text: 'Dessert (100g serving)',
        align: 'left',
        sortable: false,
        value: 'name',
      },
      { text: 'Calories', value: 'calories' },
      { text: 'Fat (g)', value: 'fat' },
      { text: 'Carbs (g)', value: 'carbs' },
      { text: 'Protein (g)', value: 'protein' },
      { text: 'Iron (%)', value: 'iron' },
    ],
    desserts: [
      {
        name: 'Frozen Yogurt',
        calories: 159,
        fat: 6.0,
        carbs: 24,
        protein: 4.0,
        iron: '1%',
      },
      {
        name: 'Ice cream sandwich',
        calories: 237,
        fat: 9.0,
        carbs: 37,
        protein: 4.3,
        iron: '1%',
      },
      {
        name: 'Eclair',
        calories: 262,
        fat: 16.0,
        carbs: 23,
        protein: 6.0,
        iron: '7%',
      },
      {
        name: 'Cupcake',
        calories: 305,
        fat: 3.7,
        carbs: 67,
        protein: 4.3,
        iron: '8%',
      },
      {
        name: 'Gingerbread',
        calories: 356,
        fat: 16.0,
        carbs: 49,
        protein: 3.9,
        iron: '16%',
      },
      {
        name: 'Jelly bean',
        calories: 375,
        fat: 0.0,
        carbs: 94,
        protein: 0.0,
        iron: '0%',
      },
      {
        name: 'Lollipop',
        calories: 392,
        fat: 0.2,
        carbs: 98,
        protein: 0,
        iron: '2%',
      },
      {
        name: 'Honeycomb',
        calories: 408,
        fat: 3.2,
        carbs: 87,
        protein: 6.5,
        iron: '45%',
      },
      {
        name: 'Donut',
        calories: 452,
        fat: 25.0,
        carbs: 51,
        protein: 4.9,
        iron: '22%',
      },
      {
        name: 'KitKat',
        calories: 518,
        fat: 26.0,
        carbs: 65,
        protein: 7,
        iron: '6%',
      },
    ],
  }),
}
</script>
