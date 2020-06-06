<template>
  <v-container>
    <v-card class="elevation-12">
      <v-toolbar color="primary" dark flat>
        <v-toolbar-title> Add New Category </v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-form
          ref="form"
          @submit.prevent="addNew"
          v-model="valid"
          lazy-validation
        >
          <v-text-field
            v-model="name"
            :rules="nameRules"
            label="Category Name"
            name="name"
            type="name"
          />

          <v-text-field
            v-model="members"
            :rules="membersRules"
            label="Maximum Members"
            name="members"
            type="number"
          />

          <v-text-field
            v-model="fee"
            :rules="feeRules"
            label="Fee (NGN)"
            name="fee"
            type="number"
          />

          <v-text-field
            v-model="payment"
            :rules="feeRules"
            label="Payment (NGN)"
            name="payment"
            type="number"
          />

          <v-select
            v-model="interval"
            :items="ints"
            label="Select Interval"
            item-value="text"
          ></v-select>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" type="submit">login</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'Index',
  data() {
    return {
      valid: true,
      name: '',
      nameRules: [
        (v) => !!v || 'Category Name name is required',
        (v) =>
          (v && v.length >= 5 && !v.includes(' ')) ||
          'Full Name must be More than 5 characters and should not contain special characters'
      ],
      members: '',
      payment: '',
      membersRules: [(v) => !!v || 'members field is required'],
      fee: '',
      feeRules: [
        (v) => !!v || 'Fee field is required',
        (v) =>
          (v && !v.isNaN && !v.includes(' ')) || 'fee must be a valid number'
      ],
      interval: '',
      ints: [{ text: 'Weekly' }, { text: '2 Weeks' }, { text: 'Monthly' }]
    }
  },
  methods: {
    addNew() {
      // console.log('login')
    }
  }
}
</script>
