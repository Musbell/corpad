<template>
  <div class="d-flex text-center">
    <v-scroll-y-transition mode="out-in">
      <v-card class="pt-6 mx-auto" flat max-width="400">
        <v-card-text>
          <v-avatar size="88">
            <v-img
              src="https://avatars0.githubusercontent.com/u/4477954?s=460&v=4"
              class="mb-6"
            ></v-img>
          </v-avatar>
          <h3 class="headline mb-2">
            Bello Musa
          </h3>
          <div class="blue--text mb-2">musbell007@gmail.com</div>
          <div class="blue--text subheading font-weight-bold">
            musbell
          </div>
        </v-card-text>
        <v-divider></v-divider>
        <v-row class="text-left" tag="v-card-text">
          <v-col class="text-right mr-4 mb-2" tag="strong" cols="5"
            >Company:</v-col
          >
          <v-col>Planta</v-col>
          <v-col class="text-right mr-4 mb-2" tag="strong" cols="5"
            >Website:</v-col
          >
          <v-col>
            <a href="https://github.com/musbell" target="_blank">Github page</a>
          </v-col>
          <v-col class="text-right mr-4 mb-2" tag="strong" cols="5"
            >Phone:</v-col
          >
          <v-col>+2348066131053</v-col>
        </v-row>
      </v-card>
    </v-scroll-y-transition>
  </div>
</template>

<script>
export default {
  name: 'Index'
}
</script>

<style scoped></style>
