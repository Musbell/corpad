<template>
  <v-card class="elevation-12">
    <v-toolbar color="primary" dark flat>
      <v-toolbar-title>Create Account</v-toolbar-title>
      <!-- <v-spacer />
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn :href="source" v-on="on" icon large target="_blank">
            <v-icon>mdi-code-tags</v-icon>
          </v-btn>
        </template>
        <span>Source</span>
      </v-tooltip>
      <v-tooltip right>
        <template v-slot:activator="{ on }">
          <v-btn
            v-on="on"
            icon
            large
            href="https://codepen.io/johnjleider/pen/pMvGQO"
            target="_blank"
          >
            <v-icon>mdi-codepen</v-icon>
          </v-btn>
        </template>
        <span>Codepen</span>
      </v-tooltip> -->
    </v-toolbar>
    <v-card-text>
      <v-form
        ref="form"
        @submit.prevent="signup"
        v-model="valid"
        lazy-validation
      >
        <v-text-field
          v-model="name"
          :rules="nameRules"
          label="Full Name"
          name="fullName"
          prepend-icon="mdi-person"
          type="text"
        />

        <v-text-field
          v-model="email"
          :rules="emailRules"
          label="email"
          name="email"
          prepend-icon="mdi-person"
          type="email"
        />

        <v-text-field
          v-model="number"
          :rules="numberRules"
          label="Phone Number"
          name="number"
          prepend-icon="mdi-person"
          type="number"
        />

        <v-text-field
          v-model="password"
          :rules="passwordRules"
          label="Password"
          name="password"
          prepend-icon="mdi-lock"
          type="password"
        />
      </v-form>
    </v-card-text>
    <v-card-actions>
      <nuxt-link to="/signin" class="ml-5">login instead</nuxt-link>
      <v-spacer />
      <v-btn color="primary" type="submit">signup</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'Index',
  layout: 'auth',
  data() {
    return {
      valid: true,
      name: '',
      nameRules: [
        (v) => !!v || 'Full Name name is required',
        (v) =>
          (v && v.length >= 5 && v.includes(' ')) ||
          'Full Name must be More than 5 characters and should not contain special characters'
      ],
      email: '',
      emailRules: [
        (v) => !!v || 'E-mail is required',
        (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid'
      ],
      number: '',
      numberRules: [
        (v) => !!v || 'Phone Number is required',
        (v) =>
          (v && v.length === 11 && !v.includes(' ')) ||
          'Phone Number must be valid'
      ],
      gender: '',
      password: '',
      passwordRules: [
        (v) => !!v || 'Password is required',
        (v) =>
          (v && v.length >= 10 && v.length <= 32) ||
          'password must be between 10-32 characters'
      ]
    }
  },
  methods: {
    signup() {
      // console.log('signup')
    }
  }
}
</script>
