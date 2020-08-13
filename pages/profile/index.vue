<template>
  <v-container fluid grid-list-md text-md-center>
    <v-layout row wrap>
      <v-flex xs12 sm12 md4>
        <v-card outlined class="mt-5 mx-auto" max-width="400">
          <v-sheet
            class="v-sheet--offset mx-auto"
            color="orange lighten-3"
            outlined
            max-width="calc(100% - 32px)"
            elevation="2"
          >
            <v-container>
              <v-avatar size="100">
                <!--                <img-->
                <!--                  src="https://res.cloudinary.com/musbell/image/upload/v1567088793/planta/iihjeofuq2luewvuhxkj.svg"-->
                <!--                  alt="avatar"-->
                <!--                />-->
                <!--                <img :src="$auth.user.picture" alt="avatar" />-->
              </v-avatar>
            </v-container>
          </v-sheet>
          <v-card-text class="pt-0">
            <div class="title font-weight-light mb-2">
              <!--              UserID: {{ user.email }}-->
            </div>
            <div class="subheading font-weight-light grey--text">
              <!--              {{ user.displayName }}-->
            </div>
            <v-divider class="my-2" />
            <v-icon class="mr-2" small>
              mdi-clock
            </v-icon>
            <span class="caption grey--text font-weight-light">Registered</span>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs12 sm12 md8>
        <div>
          <v-card outlined>
            <v-toolbar flat color="white">
              <v-toolbarTitle class="grey--text">
                <v-icon class="grey--text">mdi-account</v-icon> Personal details
              </v-toolbarTitle>
            </v-toolbar>
            <v-divider color="yellow" />
            <v-container>
              <v-card-text>
                <form @submit.prevent="update">
                  <v-text-field
                    data-vv-name="username"
                    prepend-inner-icon="mdi-account"
                    clearable
                    label="username"
                    required
                    outlined
                    shaped
                  />
                  <v-text-field
                    prepend-inner-icon="mdi-email"
                    label="E-mail"
                    clearable
                    required
                    outlined
                    shaped
                    data-vv-name="email"
                  />
                  <v-text-field
                    data-vv-name="first_name"
                    prepend-inner-icon="mdi-account"
                    clearable
                    label="First name"
                    required
                    outlined
                    shaped
                  />
                  <v-text-field
                    data-vv-name="last_name"
                    prepend-inner-icon="mdi-account"
                    clearable
                    label="Last name"
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
                        label="Birthday date"
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
                  <v-btn>Edit</v-btn>
                </form>
              </v-card-text>
            </v-container>
          </v-card>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// eslint-disable-next-line @typescript-eslint/no-unused-vars
import * as firebase from 'firebase/app'
import 'firebase/auth'

export default {
  name: 'Index',

  computed: {
    currentUser(){
      const user = firebase.auth().currentUser
      let uid
      if (user != null) {
        // name = user.displayName
        // email = user.email
        // photoUrl = user.photoURL
        // emailVerified = user.emailVerified
        uid = user.uid
      }
    }
  },

  methods: {},
}
</script>

<style scoped>
.v-sheet--offset {
  top: -24px;
  position: relative;
}
</style>
