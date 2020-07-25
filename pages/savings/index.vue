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
      <v-tabs-items v-model="model" style="background-color: transparent;">
        <v-tab-item value="tab-1">
          <v-row>
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
        </v-tab-item>
        <v-tab-item value="tab-2">
          bkbbb
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
  }),
}
</script>

<style scoped>
.v-sheet--offset {
  top: -24px;
  position: relative;
}
</style>
