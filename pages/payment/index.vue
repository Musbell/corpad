<template>
  <div>
    <h1>Payment</h1>
    <v-container>
      <v-row>
        <v-col class="d-flex" cols="12" sm="6">
          <v-select
            v-model="component"
            :on-change="Toggle"
            :items="items"
            label=" SELECT
          PAYMENT
          METHOD"
            outlined
            shaped
          >
          </v-select>
        </v-col>
      </v-row>
      <v-card-actions class="justify-center">
        <flutterwave
          :is-production="isProduction"
          :name="customer.name"
          :email="customer.email"
          :amount="5000"
          :reference="reference"
          :flw-key="flwKey"
          :callback="callback"
          :close="close"
          :currency="currency"
          :country="country"
          :custom_title="customizations.title"
          :custom_logo="customizations.logo"
          :payment_method="paymentMethod"
        />
      </v-card-actions>
    </v-container>
    <v-flex> <component :is="component" /></v-flex>
  </div>
</template>

<script>
import Cash from '~/components/Cash'
import BankTransfer from '~/components/BankTransfer'
import CardPayment from '~/components/CardPayment'


import axios from 'axios'
const flwKey = process.env.VUE_APP_FLUTTERWAVE_TEST_KEY
export default {
  name: 'Index',
  components: {
    CardPayment,
    BankTransfer,
    Cash,
    // Flutterwave,
  },

  data: () => ({
    items: ['CardPayment', 'Cash', 'BankTransfer'],
    component: '',
    carResponse: [],
    isProduction: false,
    flwKey,
    amount: '',
    currency: 'NGN',
    country: 'NG',
    customer: {
      name: 'Kamal Yahaya',
      email: 'kamal@gmail.com',
    },
    customizations: {
      title: 'Corpad',
      description: 'Payment for adashi',
    },
    paymentMethod: '',
    computed: {
      reference() {
        let text = ''
        const possible =
          'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        for (let i = 0; i < 10; i++)
          text += possible.charAt(Math.floor(Math.random() * possible.length))
        return text
      },
    },
  }),

  methods: {
    Toggle() {
      if (this.items === 'Cash') {
        this.component = Cash
      } else if (this.items === 'BankTransfer') {
        this.component = BankTransfer
      } else {
        this.component = CardPayment
      }
    },
  },
}
</script>

<style scoped>
.h1 {
  text-justify: auto;
}
</style>
