<template>
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
            :items="filtered"
          ></v-data-table>
        </v-card>
      </v-flex>
    </div>
</template>
<script>
export default {
  name: "HistoryTable",
  props: ['headers', 'dataItems', 'param'],
    data(){
      return {
        search: ''
      }
    },
    computed: {
      filtered(){
        return this.dataItems.filter(item => {
          return item[this.param].toLowerCase().match(this.search.toLowerCase())
        })
      }
    }
}
</script>

