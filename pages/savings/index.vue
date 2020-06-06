<template>
  <v-row>
    <v-col cols="12">
      <v-tabs
        v-model="model"
        centered
        slider-color="orange"
        color="orange"
        right
        background-color="transparent"
      >
        <v-tab href="#tab-1"> Personal</v-tab>
        <v-tab href="#tab-2"> Coperate</v-tab>
      </v-tabs>
      <v-tabs-items v-model="model" style="background-color: transparent">
        <v-tab-item value="tab-1">
          <v-row v-if="savings">
            <v-col v-for="(s, i) in 2" :key="i" cols="12" sm="6">
              <v-card class="mt-4 mx-auto" max-width="400">
                <v-sheet
                  class="v-sheet--offset mx-auto"
                  color="#F9A825"
                  elevation="12"
                  max-width="calc(100% - 32px)"
                >
                  <v-sparkline
                    :labels="labels"
                    :value="value"
                    color="white"
                    line-width="2"
                    padding="16"
                  ></v-sparkline>
                </v-sheet>

                <v-card-text class="pt-0">
                  <div class="title font-weight-light mb-2">
                    My weekly savings
                  </div>
                  <div class="subheading font-weight-light grey--text">
                    Last Campaign Performance
                  </div>
                  <v-divider class="my-2"></v-divider>
                  <v-icon class="mr-2" small>
                    mdi-clock
                  </v-icon>
                  <span class="caption grey--text font-weight-light"
                    >last registration 26 minutes ago</span
                  >
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
          <div v-else>
            <p>You havent made any savings yet.</p>
            <nuxt-link to="/payments">Start saving now</nuxt-link>
          </div>
          <v-row v-if="savings">
            <v-btn class="primary" nuxt to="/savings/history">History</v-btn>
            <v-spacer></v-spacer>
            <v-btn class="primary" nuxt to="/payments/withdraw">Withdraw</v-btn>
            <v-spacer></v-spacer>
            <v-btn class="primary" nuxt to="/payments">make Payment</v-btn>
          </v-row>
        </v-tab-item>
        <v-tab-item value="tab-2">
          <v-card v-if="corporate">
            <v-card-title>My Adashi</v-card-title>
            <v-card-text>
              <p>Category Name: Young Millionaires</p>
              <p>Monthly Fee: NGN 30000</p>
              <p>Monthly Payment: Paid</p>
              <p>Position: 02</p>
              <p>Payment Interval: Monthly</p>
              <p>Payment Recieved: Yes</p>
              <p>Payment Rounds Left: 9</p>
              <v-row>
                <v-btn class="primary" nuxt to="/adashiCategory/history"
                  >History</v-btn
                >
                <v-spacer></v-spacer>
                <v-btn class="primary" nuxt to="/payments">make Payment</v-btn>
              </v-row>
            </v-card-text>
          </v-card>
          <div v-else>
            <p>You dont belong to any Adashi Category.</p>
            <nuxt-link to="/adashiCategory">Join a category</nuxt-link>
          </div>
        </v-tab-item>
      </v-tabs-items>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'Index',
  data: () => ({
    labels: ['12am', '3am', '6am', '9am', '12pm', '3pm', '6pm', '9pm'],
    value: [200, 675, 410, 390, 310, 460, 250, 240],
    model: 'tab-2',
    corporate: true,
    savings: true
  })
}
</script>

<style scoped>
.v-sheet--offset {
  top: -24px;
  position: relative;
}
</style>
