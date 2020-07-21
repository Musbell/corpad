<template>
  <v-container>
    <login-form :submit-form="loginUser" />
  </v-container>
</template>

<script>
import loginForm from '~/components/Authentication/loginForm'
export default {
  name: 'Index',
  components: {
    loginForm,
  },
  layout: 'authentication',

  methods: {
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    async loginUser(userInfo) {
      // eslint-disable-next-line @typescript-eslint/no-unused-vars
      await this.$auth.loginWith('auth0', {
        data: this.userInfo,
      })
      this.$router.push('/')
      // alert('You just logged in!')
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
