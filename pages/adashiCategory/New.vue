<template>
  <v-container>
    <pageTitle title="New Category" />

  <v-layout row>
    <v-flex xs12 sm8 offset-sm2>
      <form @submit.prevent="addNew">
        <!-- <v-card class="pa-3 mt-3" > -->
          <v-layout row mt-5>
            <v-flex xs12>
              <v-text-field
              label="Category Name"
              v-model="cred.name"
              class="mx-5"
              required
              type="text"
              outlined
              rounded
              ></v-text-field> 
            </v-flex>

            <v-flex xs12>
              <v-text-field
              label="Maximum Users"
              v-model="cred.maxUsers"
              class="mx-5"
              required
              type="number"
              outlined
              rounded
              ></v-text-field> 
            </v-flex>

            <v-flex xs12>
              <v-text-field
              label="Ammount"
              v-model="cred.ammount"
              class="mx-5"
              required
              type="number"
              outlined
              rounded
              ></v-text-field> 
            </v-flex>
            <v-flex xs12>
              <v-text-field
              label="Payment Interval"
              v-model="cred.interval"
              class="mx-5"
              required
              type="number"
              outlined
              rounded
              ></v-text-field> 
            </v-flex>

            <v-flex xs12>
              <v-text-field
              label="Start Date"
              v-model="cred.start"
              class="mx-5"
              required
              type="date"
              outlined
              rounded
              ></v-text-field> 
            </v-flex>

            <v-flex xs12>
              <v-textarea
              label="Description"
              v-model="cred.description"
              class="mx-5"
              required
              type="text"
              outlined
              rounded
              ></v-textarea> 
            </v-flex>

            <v-flex xs12>
              <v-btn
              class="mx-5 warning white--text"
              required
              type="submit"
              outlined
              rounded
              >submit</v-btn> 
            </v-flex>
          </v-layout>
        <!-- </v-card> -->
      </form>  
    </v-flex>  
  </v-layout>    
  </v-container>
</template>
<script>
export default {
  data(){
    return {
      cred: {
        name: "",
        maxUsers: "",
        ammount: "",
        interval: "",
        start: "",
        description: ""
      }
    }
  },
  methods: {
    addNew(){
      console.log(this.cred)
    }
  }
}
</script>
