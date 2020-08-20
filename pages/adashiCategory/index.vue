<template>
  <v-container>
    <pageTitle title="Categories" />
    <v-row>
          <v-spacer></v-spacer>
          <v-btn class="warning" nuxt link to="/adashiCategory/new">New</v-btn>
          <v-spacer></v-spacer>
      </v-row>
    <v-row>
      <v-col v-for="(category, key) in categories" :key="key" cols="12" sm="4">
        <v-card class="mx-auto" max-width="344" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">Category {{key+1}} : {{ category.name }}</div>
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
            <v-btn class="warning" text nuxt :to="`/coperateSavings/${category.id}`" :disabled="category.maxUsers == category.members">{{category.maxUsers == category.members ? 'Full' : 'Join'}}</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>  
      
    </v-row>
  </v-container>
</template>

<script>
import {mapGetters} from 'vuex'
// import ADASHI_CATEGORIES from '../../gql/adashiCategory/query/categories'
import gql from 'graphql-tag'
export default {
  name: 'Index',
    // apollo: {
    //   adashiCategories: {
    //     query: gql`
    //       query adashiCategories {
    //         Categories {
    //           id
    //           member_size
    //           name
    //           rotation_cumulative_fund
    //           rotation_days
    //           roundup_days
    //           savings
    //         }
    //       }
    //     `,

    //     update: (data) => data,
    //     result({ data }) {
    //       console.log(data)
    //     },
    //   },
    // },
  data(){
    return {
      
    }
  },
  computed: {
    ...mapGetters('categoriesModule', ['categories'])
  }
}
</script>
