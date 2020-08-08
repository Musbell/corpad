<template>
  <v-container>
    <v-row>
      <v-col md-4>
        <v-flex>
          <v-card id="row2" class="mt-4 mx-auto">
            <v-list-item three-line>
              <v-list-item-content>
                <div class="overline mb-4"><strong>ADASHI</strong></div>
                <v-list-item-title class="headline mb-1"
                  >HEADLINE</v-list-item-title
                >
                <v-list-item-subtitle>
                  <div class="my-2">
                    <v-btn small color="success" href="/payment"
                      >Make Payment
                      <v-icon color="white">mdi-cash</v-icon>
                    </v-btn>
                  </div>
                </v-list-item-subtitle>
              </v-list-item-content>

              <v-list-item-avatar tile size="80" color="grey">
                <v-img
                  height="80"
                  width="80"
                  src="https://thumbnails.yayimages.com/1600/b/1ff/b1ff916.jpg"
                ></v-img>
              </v-list-item-avatar>
            </v-list-item>
          </v-card>
        </v-flex>
      </v-col>

      <v-col id="row2" md-4>
        <v-flex>
          <v-card id="row2" class="mt-4 mx-auto">
            <v-list-item three-line>
              <v-list-item-content>
                <div class="overline mb-4"><strong>SAVINGS</strong></div>
                <v-list-item-title class="headline mb-1"
                  >Balance: NGN 65,000</v-list-item-title
                >
                <v-list-item-subtitle
                  >Greyhound divisely hello coldly
                  fonwderfully</v-list-item-subtitle
                >
              </v-list-item-content>

              <v-list-item-avatar tile size="80" color="grey">
                <v-img
                  height="80"
                  width="80"
                  src="https://img.favpng.com/18/23/20/computer-icons-money-finance-investment-icon-png-favpng-q0uz31DcV9FSyx7aCKL1mxj2X.jpg"
                ></v-img>
              </v-list-item-avatar>
            </v-list-item>
          </v-card>
        </v-flex>
      </v-col>
      <v-col id="row3" md-4>
        <v-flex>
          <v-card id="row3" class="mt-4 mx-auto">
            <v-list-item three-line>
              <v-list-item-content>
                <div class="overline mb-4">CREDITS</div>
                <v-list-item-title class="headline mb-1"
                  >On-credit commodity</v-list-item-title
                >
                <v-list-item-subtitle
                  >Greyhound divisely hello coldly
                  fonwderfully</v-list-item-subtitle
                >
              </v-list-item-content>

              <v-list-item-avatar tile size="80" color="grey">
                <v-img
                  height="80"
                  width="80"
                  src="https://cdn4.iconfinder.com/data/icons/types-of-investment-filloutline/64/lending-investment-loan-return-profit-512.png"
                ></v-img>
              </v-list-item-avatar>
            </v-list-item>
          </v-card>
        </v-flex>
      </v-col>
    </v-row>
    <br />
    <section>
      <v-row>
        <v-col md-6>
          <!--          <charts />-->
          <v-card class="pt-0,">
            <v-layout justify-center>
              <v-progress-circular
                :rotate="360"
                :size="250"
                :width="25"
                :value="75"
                color="teal"
                align="center"
              >
                <h1>{{ valu }}</h1>
              </v-progress-circular>
            </v-layout>
          </v-card>
        </v-col>
        <v-col md-6>
          <v-card>
            <v-layout justify-center>
              <v-progress-circular
                :rotate="360"
                :size="250"
                :width="25"
                :value="80"
                color="green"
                align="center"
              >
                <h1>{{ valu }}</h1>
              </v-progress-circular>
            </v-layout>
          </v-card>
        </v-col>
      </v-row>
    </section>

    <br />
    <v-divider></v-divider>
    <div class="mt8">
      <v-card>
<!--        <v-layout justify-center>-->
          <h2 class="adashiHead">Adashi Calender</h2>

          <adashi-calender />
<!--        </v-layout>-->
      </v-card>
    </div>

    <div class="mt4">
      <v-flex class="mt4">
        <v-card>
          <v-card-title>
            <h3 class="mt4">Adashi History</h3>
            <v-text-field
              v-model="search"
              append-icon="search"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="desserts"
            :search="search"
          ></v-data-table>
        </v-card>
      </v-flex>
    </div>
  </v-container>
</template>

<script>
import charts from '~/components/charts'
import AdashiCalender from '~/components/adashiCalender'
// import gql from 'graphql-tag'
export default {
  // apollo: {
  //   Categories: gql`
  //     query getCategories {
  //       Categories {
  //         member_size
  //         name
  //         rotation_cumulative_fund
  //         rotation_days
  //         roundup_days
  //         savings
  //       }
  //     }
  //   `,
  //   update: (data) => data,
  //   result({ data }) {
  //     console.log(data)
  //   },
  // },
  components: {
    AdashiCalender,
    charts,
  },
  data: () => ({
    labels: ['12am', '3am', '6am', '9am', '12pm', '3pm', '6pm', '9pm'],
    value: [200, 675, 410, 390, 310, 460, 250, 240],
    valu: 45,
    tab: null,
    text:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    search: '',
    headers: [
      {
        text: 'Dessert (100g serving)',
        align: 'start',
        filterable: false,
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

<style>
.v-sheet--offset {
  top: -24px;
  position: relative;
}
.userName {
  text-align: right;
  margin-top: initial;
}

.v-progress-circular {
  margin: 1rem;
}
#row1 {
  margin: 5px;
  height: 150px;
  background-color: greenyellow;
  border-radius: 5px;
  box-shadow: #7f828b;
}
#row2 {
  margin: 5px;
  height: 150px;
  background-color: white;
  border-radius: 5px;
  box-shadow: #7f828b;
}
#row3 {
  margin: 5px;
  height: 150px;
  background-color: white;
  border-radius: 5px;
  box-shadow: #7f828b;
  border: 2px;
}
.adashiHead {
  margin: 20px;
}
</style>
