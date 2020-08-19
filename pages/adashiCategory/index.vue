<template>
  <v-container>
    <v-row>
      <v-col v-for="(category, key) in categories" :key="key" cols="12" sm="4">
        <v-card class="mx-auto" max-width="344" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">Category {{ category.name }}</div>
              <v-list-item-title class="headline mb-1"
                >₦{{category.ammount}}</v-list-item-title
              >
              <v-list-item-subtitle>{{category.members}} members</v-list-item-subtitle>
              <v-list-item-subtitle>Max Users: {{category.maxUsers}}</v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-avatar
              tile
              size="80"
              color="grey"
            ></v-list-item-avatar>
          </v-list-item>

          <v-card-actions>
            <v-btn class="success" text nuxt to="/coperateSavings" :disabled="category.maxUsers == category.members">{{category.maxUsers == category.members ? 'Full' : 'Join'}}</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import ADASHI_CATEGORIES from '../../gql/adashiCategory/query/categories'
import gql from 'graphql-tag'
export default {
  name: 'Index',
  apollo: {
    adashiCategories: {
      query: gql`
        query adashiCategories {
          Categories {
            id
            member_size
            name
            rotation_cumulative_fund
            rotation_days
            roundup_days
            savings
          }
        }
      `,

      update: (data) => data,
      result({ data }) {
        console.log(data)
      },
    },
  },
  data(){
    return {
      categories: [
        {name : "Young Money", ammount: 10000, payment: 47500, members: 10, interval: '7', start: '2020-08-12', finished: "false", maxUsers: 10},
        {name : "Cash Money", ammount: 30000, payment: 143500, members: 5, interval: '10', start: '2020-08-20', finished: "false", maxUsers: 10},
        {name : "Ultimate", ammount: 2000, payment: 275000, members: 15, interval: '10', start: '2020-08-20', finished: "false", maxUsers: 20},
      ] 
    }
  }
}
</script>
