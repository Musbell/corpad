<template>
  <v-container>
    <v-card-text>
      <form @submit.prevent="update">
        <v-text-field
          data-vv-name="username"
          prepend-inner-icon="mdi-account"
          readonly
          clearable
          label="userId"
          required
          outlined
          shaped
        />
        <v-text-field
          data-vv-name="amount"
          prepend-inner-icon="mdi-cash"
          readonly
          clearable
          label="Amount"
          required
          outlined
          shaped
        />
        <v-text-field
          data-vv-name="category"
          prepend-inner-icon="mdi-bank"
          readonly
          clearable
          label="Category"
          required
          outlined
          shaped
        />

        <v-menu
          ref="menu"
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          full-width
          min-width="290px"
        >
          <template v-slot:activator="{ on }">
            <v-text-field
              data-vv-name="date_of_birth"
              clearable
              prepend-inner-icon="mdi-calendar"
              label="Date"
              outlined
              shaped
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            ref="picker"
            :max="new Date().toISOString().substr(0, 10)"
            min="1950-01-01"
          ></v-date-picker>
        </v-menu>
        <!--/Date Picker-->

        <v-text-field
          clearable
          prepend-inner-icon="mdi-phone"
          label="phone"
          required
          outlined
          shaped
        />
        <v-btn>Pay</v-btn>
      </form>
    </v-card-text>
  </v-container>
</template>

<script>
export default {
  name: 'Cash',
  data: () => ({}),
}
</script>

<style scoped>
.form {
  display: flex;
}
</style>
