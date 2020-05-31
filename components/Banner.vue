<template>
  <v-container>
    <v-card flat>
      <v-row align="center" justify="center">
        <v-col cols="12" md="6">
          <v-container>
            <h1 class="display-2 mb-4">
              The Smart Farm Management Software
            </h1>
            <p class="body-1">
              A one stop place for farm management, crop productions, finance,
              resource management, pest monitoring and detection, weather
              forecast, aggregation and lots more.
            </p>
            <div class="my-2">
              <a
                href="https://demo.planta.ng"
                style="text-decoration: none"
                target="_blank"
              >
                <v-btn x-large color="#CF4D24" dark depressed tile
                  >Sign up for free</v-btn
                >
              </a>
            </div>
          </v-container>
        </v-col>
        <v-col cols="12" md="6">
          <iframe width="600" height="400" src="https://www.youtube.com/embed/L8W1tbEVyOM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'Banner'
}
</script>

<style scoped>

</style>
