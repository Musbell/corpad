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

  <HistoryTable :headers="headers" :dataItems="desserts" param="category"/>
    
  </v-container>
</template>

<script>
import HistoryTable from '~/components/HistoryTable'
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
    HistoryTable
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
        text: 'Category',
        align: 'start',
        filterable: false,
        value: 'category',
      },
      { text: 'Ammount', value: 'ammount' },
      { text: 'Type', value: 'type'},
      { text: 'Date', value: 'date' },
      { text: 'Payment Method', value: 'method' },
      { text: 'Completed', value: 'completed' },
      { text: 'Status', value: 'status' },
    ],
    desserts: [
      {
        category: 'Young Millionaires',
        ammount: 10000,
        type: 'Debit',
        date: '12/08/2020',
        method: 'Card',
        completed: 'True',
        status: 'Verified',
      },
      {
        category: 'Young Millionaires',
        ammount: 10000,
        type: 'Debit',
        date: '12/09/2020',
        method: 'Card',
        completed: 'True',
        status: 'Verified',
      },
      {
        category: 'Ultimate',
        ammount: 10000,
        type: 'Debit',
        date: '12/10/2020',
        method: 'Card',
        completed: 'True',
        status: 'Verified',
      },
      {
        category: 'Super Money',
        ammount: 10000,
        type: 'Debit',
        date: '12/11/2020',
        method: 'Card',
        completed: 'True',
        status: 'Pending',
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
