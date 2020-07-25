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
          <v-form>
            <v-text-field
              label="username"
              name="username"
              prepend-icon="mdi-account"
              type="text"
              dark
              outlined
              dense
              rounded
            ></v-text-field>
            <v-text-field
              label="email"
              name="email"
              prepend-icon="mdi-email"
              type="text"
              dark
              outlined
              rounded
              dense
            ></v-text-field>

            <v-text-field
              id="password"
              label="Password"
              name="password"
              prepend-icon="mdi-lock"
              type="password"
              dark
              outlined
              rounded
              dense
            ></v-text-field>
            <v-text-field
              id="confirmPassword"
              label="Password"
              name="confirmPassword"
              prepend-icon="mdi-lock"
              type="password"
              dark
              outlined
              rounded
              dense
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-btn block rounded color="white" class="orange--text">Login</v-btn>
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
export default {
  name: 'Index',
  layout: 'authentication',
}
</script>

<style scoped>
#logo {
  font-family: 'MuseoModerno', cursive;
  font-size: 3em;
}
</style>
