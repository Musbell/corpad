<template>
  <v-container>
    <PageTitle title="Payments"></PageTitle>
    <v-card>
      <v-form
        ref="form"
        @submit.prevent="makePayment"
        v-model="valid"
        lazy-validation
        class="pa-2"
      >
        <v-select
          v-model="purpose"
          :items="purposeItems"
          label="Select Purpose of Payment"
          item-value="text"
        ></v-select>

        <v-select
          v-model="method"
          :items="paymentItems"
          label="Select Method of Payment"
          item-value="text"
        ></v-select>

        <v-text-field
          v-model="ammount"
          :rules="ammountRules"
          label="Ammount (NGN)"
          name="ammount"
          type="number"
        />
        <!-- <v-text-field
          v-model="password"
          :rules="passwordRules"
          label="Password"
          name="password"
          prepend-icon="mdi-lock"
          type="password"
        /> -->
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" type="submit">Proceed</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      valid: true,
      purpose: '',
      method: '',
      ammount: '',
      purposeItems: [{ text: 'Adashi' }, { text: 'Savings' }],
      paymentItems: [
        { text: 'Paystack' },
        { text: 'Transfer' },
        { text: 'Cash' }
      ],
      ammountRules: [
        (v) => !!v || 'Ammount field is required',
        (v) =>
          (v && !v.isNaN && !v.includes(' ')) ||
          'Ammount must be a valid number'
      ]
    }
  },
  methods: {
    makePayment() {
      // make payment in vuex
    }
  }
}
</script>
