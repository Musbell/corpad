<template>
  <v-container>
    <PageTitle title="Adashi History"></PageTitle>
    <app-table :headers="headers" :items="items"></app-table>
  </v-container>
</template>
<script>
import table from '~/components/DataTable.vue'
export default {
  components: { appTable: table },
  data() {
    return {
      // fetch from async data
      headers: [
        {
          text: 'Date',
          align: 'left',
          value: 'date'
        },
        { text: 'Ammount', value: 'ammount' },
        { text: 'Status', value: 'status' },
        { text: 'Category', value: 'category' },
        { text: 'Payment Method', value: 'method' },
        { text: 'Income Type', value: 'type' }
      ],
      items: [
        {
          date: '05/02/2020',
          ammount: 20000,
          status: 'Completed',
          category: 'Young Millionaires',
          method: 'PayStack',
          type: 'Debit'
        },
        {
          date: '05/03/2020',
          ammount: 20000,
          status: 'Completed',
          category: 'Young Millionaires',
          method: 'PayStack',
          type: 'Debit'
        },
        {
          date: '05/04/2020',
          ammount: 20000,
          status: 'Completed',
          category: 'Young Millionaires',
          method: 'Transfer',
          type: 'Debit'
        },
        {
          date: '05/05/2020',
          ammount: 180000,
          status: 'Completed',
          category: 'Young Millionaires',
          method: 'PayStack',
          type: 'Credit'
        }
      ]
    }
  }
}
</script>
