<template>
  <v-app id="inspire" class="bg">
    <v-main>
      <v-container class="fill-height" fluid>
        <nuxt />
      </v-container>
      <!--      <v-footer absolute class="font-weight-medium" color="transparent">-->
      <!--        <v-col class="text-center white&#45;&#45;text" cols="12">-->
      <!--          {{ new Date().getFullYear() }} — <strong>Corpad</strong>-->
      <!--        </v-col>-->
      <!--      </v-footer>-->
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'Authentication',
}
</script>

<style scoped>
.bg {
  background: #ec9332;
}
</style>
