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
      <app-table :headers="headers" :items="desserts"></app-table>
    </v-card>
  </div>
</template>

<script>
import table from '~/components/DataTable.vue'
export default {
  components: { appTable: table },
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
      (v) => v.length <= 10 || 'Name must be less than 10 characters'
    ],
    email: '',
    emailRules: [
      (v) => !!v || 'E-mail is required',
      (v) => /.+@.+/.test(v) || 'E-mail must be valid'
    ],
    headers: [
      {
        text: 'Date',
        align: 'left',
        sortable: false,
        value: 'date'
      },
      { text: 'Ammount', value: 'ammount' },
      { text: 'Status', value: 'status' },
      { text: 'Borrower', value: 'borrower' },
      { text: 'Close Date', value: 'close' },
      { text: 'Loan Type', value: 'type' }
    ],
    desserts: [
      {
        date: '12/06/2020',
        ammount: 20000,
        status: 'New',
        borrower: 'Bello Musa',
        close: '12/12/2020',
        type: 'term'
      },
      {
        date: '12/06/2020',
        ammount: 20000,
        status: 'New',
        borrower: 'Bello Musa',
        close: '12/12/2020',
        type: 'term'
      },
      {
        date: '12/06/2020',
        ammount: 20000,
        status: 'New',
        borrower: 'Bello Musa',
        close: '12/12/2020',
        type: 'term'
      },
      {
        date: '12/06/2020',
        ammount: 20000,
        status: 'New',
        borrower: 'Bello Musa',
        close: '12/12/2020',
        type: 'term'
      },
      {
        date: '12/06/2020',
        ammount: 20000,
        status: 'New',
        borrower: 'Bello Musa',
        close: '12/12/2020',
        type: 'term'
      },
      {
        date: '12/06/2020',
        ammount: 20000,
        status: 'New',
        borrower: 'Bello Musa',
        close: '12/12/2020',
        type: 'term'
      },
      {
        date: '12/06/2020',
        ammount: 20000,
        status: 'New',
        borrower: 'Bello Musa',
        close: '12/12/2020',
        type: 'term'
      },
      {
        date: '12/06/2020',
        ammount: 20000,
        status: 'New',
        borrower: 'Bello Musa',
        close: '12/12/2020',
        type: 'term'
      },
      {
        date: '12/06/2020',
        ammount: 20000,
        status: 'New',
        borrower: 'Bello Musa',
        close: '12/12/2020',
        type: 'term'
      },
      {
        date: '12/06/2020',
        ammount: 20000,
        status: 'New',
        borrower: 'Bello Musa',
        close: '12/12/2020',
        type: 'term'
      }
    ]
  })
}
</script>

<style scoped></style>
