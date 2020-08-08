<template>
  <v-container>
    <h1>Pay with Debit/Credit Card</h1>

    <div class="flw mt4">
      <v-btn class="button" @click="makePayment">
        Pay Now
      </v-btn>
    </div>
  </v-container>
</template>

<script>
export default {
  name: 'CardPayment',
  props: {
    isProduction: {
      type: Boolean,
      required: false,
      default: false, // set to true if you are going live
    },
    email: {
      type: String,
      required: true,
    },
    amount: {
      type: Number,
      required: true,
      default: 0,
    },
    flwKey: {
      type: String,
      required: true,
    },
    callback: {
      type: Function,
      required: true,
      default: () => {
        console.log('Payment made, verify payment')
      },
    },
    close: {
      type: Function,
      required: true,
      default: () => {},
    },
    currency: {
      type: String,
      default: 'NGN',
    },
    country: {
      type: String,
      default: 'NG',
    },
    customTitle: {
      type: String,
      default: '',
    },
    customLogo: {
      type: String,
      default: '',
    },
    reference: {
      type: String,
      required: true,
    },
    paymentMethod: {
      type: String,
      default: 'card,mobilemoney,ussd',
    },
  },
  created() {
    const script = document.createElement('script')
    script.src = !this.isProduction
      ? 'https://ravemodal-dev.herokuapp.com/v3.js'
      : 'https://checkout.flutterwave.com/v3.js'
    document.getElementsByTagName('head')[0].appendChild(script)
  },
  methods: {
    makePayment() {
      window.FlutterwaveCheckout({
        public_key: this.flwKey,
        tx_ref: this.reference,
        amount: this.amount,
        currency: this.currency,
        payment_options: this.payment_method,
        customer: {
          name: this.name,
          email: this.email,
        },
        callback: (response) => this.callback(response),
        customizations: {
          title: this.custom_title,
          description: 'Payment for Adashi',
          logo: this.custom_logo,
        },
      })
    },
  },
}
</script>

<style scoped>
.h1 {
  text-align: justify;
}
.button {
  background-color: greenyellow;
  color: green;
  width: 100px;
  height: 40px;
  font-weight: 800;
  border-radius: 5px;
  opacity: 0.9;
  transition: 0.5s;
}
.button:hover {
  opacity: 1;
}
</style>
