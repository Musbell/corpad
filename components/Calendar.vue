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
          color="orange"
          :events="events"
          :type="type"
          @click:more="viewDay"
          @click:date="viewDay"
          :event-color="getEventColor"
          @click:event="showEvent"
        ></v-calendar>
          
           <v-menu
          v-model="selectedOpen"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
          <v-card
            color="grey lighten-4"
            min-width="350px"
            flat
          >
            <v-toolbar
              :color="selectedEvent.color"
              dark
            >
              <!-- <v-btn icon>
                <v-icon>mdi-pencil</v-icon>
              </v-btn> -->
              <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
              <!-- <v-spacer></v-spacer> -->
              <!-- <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn> -->
            </v-toolbar>
            <v-card-text>
              <!-- <span v-html="selectedEvent.details"></span> -->
              <p class="black--text">Adashi WIthdrawal Turn for Position {{selectedEvent.position }}<br>
                <strong>NGN {{selectedEvent.payment}}</strong>
              </p>
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="secondary"
                @click="selectedOpen = false"
              >
                Cancel
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-sheet>
    </v-col>
  </v-row>
</template>

<script>
import {mapGetters} from 'vuex'
  export default {
    data: () => ({
      focus: '',
      colors: ['red', 'blue', 'green', 'yellow'],
      type: 'month',
      typeToLabel: {
        month: 'Month',
        week: 'Week',
        day: 'Day',
      },
      events: [],
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      // categories: [
      //   {name : "Young Money", Ammount: 10000, payment: 47500, members: 10, interval: '7', start: '2020-08-12', finished: "false"},
      //   {name : "Cash Money", Ammount: 30000, payment: 143500, members: 5, interval: '10', start: '2020-08-20', finished: "false"},
      //   {name : "Ultimate", Ammount: 2000, payment: 275000, members: 15, interval: '10', start: '2020-08-20', finished: "false"},
      // ] 
    }),
    mounted () {
      // this.$refs.calendar.checkChange(),
      this.setEvents()
    },
    computed: {
      ...mapGetters('categoriesModule', ['categories'])
    },
    methods: {
      formatDate(date){
        let d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = ''+  d.getDate(),
        year = d.getFullYear();

        if(month.length < 2){
          month = '0' + month;
        }
        if(day.length < 2){
          day = '0' + day;
        }
        return [year,  month, day].join('-')
      },
      setEvents(){
        let arr = [];
        for(let cat in this.categories){
          for (let i = 0; i< this.categories[cat].members; i++){
            arr.push({
              name: this.categories[cat].name,
              payment: this.categories[cat].payment,
              start: this.formatDate(new Date(new Date(this.categories[cat].start).getTime() + (86400000 * (i+1) * +this.categories[cat].interval))),
              position: i+1,
              color: this.colors[cat]
            })
          }
        }
       return this.events = arr
      },
      getEventColor(event){
        return event.color
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
       showEvent ({ nativeEvent, event }) {
        const open = () => {
          this.selectedEvent = event
          this.selectedElement = nativeEvent.target
          setTimeout(() => this.selectedOpen = true, 10)
        }

        if (this.selectedOpen) {
          this.selectedOpen = false
          setTimeout(open, 10)
        } else {
          open()
        }

        nativeEvent.stopPropagation()
      } 
    }
  }
  // Date and time format : 2020-08-19 00:30
</script>