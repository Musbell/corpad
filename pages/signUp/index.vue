<template>
  <v-card class="elevation-12">
    <v-toolbar color="primary" dark flat>
      <v-toolbar-title>Create Account</v-toolbar-title>
      <v-spacer />
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
      </v-tooltip>
    </v-toolbar>
    <v-card-text>
      <v-form @submit.prevent="signup">
        <v-text-field
          v-model="name"
          label="Full Name"
          name="fullName"
          prepend-icon="mdi-person"
          type="text"
        />

        <v-text-field
          v-model="email"
          label="email"
          name="email"
          prepend-icon="mdi-person"
          type="email"
        />

        <v-text-field
          v-model="number"
          label="Phone Number"
          name="number"
          prepend-icon="mdi-person"
          type="number"
        />

        <v-text-field
          v-model="password"
          label="Password"
          name="password"
          prepend-icon="mdi-lock"
          type="password"
        />
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer />
      <v-btn color="primary" type="submit">signup</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'Index',
  layout: 'auth',
  props: {
    source: String
  },
  data() {
    return {
      name: '',
      email: '',
      number: '',
      gender: '',
      password: ''
    }
  },
  methods: {
    signup() {
      console.log('signup')
    }
  }
}
</script>
