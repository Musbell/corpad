<template>
  <v-row class="fill-height">
    <v-col>
      <v-sheet height="64">
        <v-toolbar flat color="white">
          <v-btn outlined class="mr-4" color="grey darken-2" @click="setToday">
            Today
          </v-btn>
          <v-btn fab text small color="grey darken-2" @click="prev" >
            <v-icon small>mdi-chevron-left</v-icon>
          </v-btn>
          <v-btn fab text small color="grey darken-2" @click="next">
            <v-icon small>mdi-chevron-right</v-icon>
          </v-btn>
          <v-toolbar-title v-if="$refs.calendar">
            {{ $refs.calendar.title }}
          </v-toolbar-title>
          <v-spacer></v-spacer>
          <v-menu bottom right>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                outlined
                color="grey darken-2"
                v-bind="attrs"
                v-on="on"
              >
                <span>{{ typeToLabel[type] }}</span>
                <v-icon right>mdi-menu-down</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item @click="type = 'day'">
                <v-list-item-title>Day</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'week'">
                <v-list-item-title>Week</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'month'">
                <v-list-item-title>Month</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-toolbar>
      </v-sheet>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          :events="events"
          :type="type"
          @change="getEvents"
          @click:more="viewDay"
          @click:date="viewDay"
        ></v-calendar>
        
          <!-- @change="updateRange" -->
          <!-- @click:event="showEvent" -->
          <!-- :event-color="getEventColor" -->
      </v-sheet>
      {{events}}
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data: () => ({
      focus: '',
      type: 'month',
      typeToLabel: {
        month: 'Month',
        week: 'Week',
        day: 'Day',
      },
      events: [
        { "name": "Payment", "start": "2020-08-19 00:30",  "color": "blue"},
      ],
      categories: [
        {name : "Young Money", Ammount: 10000, interval: '10', positions: {1: 'Musbell', 2: "Kamal", 3: "Marshall"}, rounds: 3, start: '', finish: ''},
        {name : "Young Billionaires", Ammount: 30000, interval: '70', positions: {1: 'Seth', 2: "Keith", 3: "Melissa", 4: "Michelle"}, rounds: 4, start: '', finish: ''
        }
      ] 
      //learn how to convert time into days to set auto interval for dates close to end of the month
    }),
    mounted () {
      this.$refs.calendar.checkChange()
    },
    methods: {
      getEvents(){
        //fetch events from the database
        // console.log(this.focus, this.type)
      },
      viewDay ({ date }) {
        this.focus = date
        this.type = 'day'
      },
      setToday () {
        this.focus = ''
      },
      prev () {
        this.$refs.calendar.prev()
      },
      next () {
        this.$refs.calendar.next()
      },
      
    },
  }
  // Date and time format : 2020-08-19 00:30
</script>