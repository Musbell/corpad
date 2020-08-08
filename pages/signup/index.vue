<template>
  <v-row align="center" justify="center">
    <v-col cols="12" sm="12" md="12">
      <h1 id="logo" class="text-center white--text">Corpad</h1>
    </v-col>
    <v-col cols="12" sm="8" md="4">
      <v-card flat color="transparent" class="pa-2" height="400">
        <v-card-text>
          <v-toolbar flat class="mb-5" color="transparent">
            <v-toolbar-title class="white--text">Signup form</v-toolbar-title>
          </v-toolbar>
          <v-form @submit.prevent="pressed">
            <!--            <v-text-field-->
            <!--              label="username"-->
            <!--              name="username"-->
            <!--              prepend-icon="mdi-account"-->
            <!--              type="text"-->
            <!--              dark-->
            <!--              outlined-->
            <!--              dense-->
            <!--              rounded-->
            <!--            ></v-text-field>-->
            <v-text-field
              v-model="email"
              label="email"
              name="email"
              required
              :rules="emailRules"
              prepend-icon="mdi-account"
              type="text"
              dark
              outlined
              rounded
            ></v-text-field>

            <v-text-field
              id="password"
              v-model="password"
              label="Password"
              name="password"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              :type="showPassword ? 'text' : 'password'"
              hint="At least 8 characters"
              counter
              dark
              outlined
              rounded
              @click:append="showPassword = !showPassword"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-btn
            block
            rounded
            color="white"
            class="orange--text"
            @click="pressed"
            >Submit</v-btn
          >
        </v-card-actions>
        <span class="white--text"
          >Already have an account?
          <v-btn text color="white" nuxt to="/login">Sign in</v-btn></span
        >
      </v-card>
    </v-col>
  </v-row>
</template>
<script>
// eslint-disable-next-line @typescript-eslint/no-unused-vars
import * as firebase from 'firebase/app'
import 'firebase/auth'

export default {
  name: 'Index',
  layout: 'authentication',

  data() {
    return {
      email: '',
      password: '',
      error: '',
      valid: false,
      showPassword: false,
    }
  },
  methods: {
    pressed() {
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
        .then((user) => {
          console.log(user)
          this.$router.push('/profile')
        })
        .catch((error) => {
          this.error = error
        })
    },
  },
}
</script>

<style scoped>
#logo {
  font-family: 'MuseoModerno', cursive;
  font-size: 3em;
}
</style>
