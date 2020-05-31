<template>
  <v-app>
    <div id="app-bar">
      <v-app-bar color="white" dense>
        <v-toolbar-title>
          <v-img
            max-width="150"
            src="https://res.cloudinary.com/musbell/image/upload/v1580986143/CORPAP3_btmvyg.png"
          />
        </v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn text small color="blue">
          Go to console
        </v-btn>

        <v-btn text small color="blue">
          Sign in
        </v-btn>
      </v-app-bar>
    </div>
    <v-content>
      <nuxt />
    </v-content>
    <v-footer
      padless
    >
      <v-card
        flat
        tile
        color="white"
        class="text-center"
      >
        <v-card-text>
          <v-btn
            v-for="icon in icons"
            :key="icon"
            class="mx-4"
            icon
          >
            <v-icon size="24px">{{ icon }}</v-icon>
          </v-btn>
        </v-card-text>

        <v-card-text class="pt-0">
          Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum. Praesent ut risus eget metus luctus accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum tempor vel ut orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text>
          {{ new Date().getFullYear() }} — <strong>Corpad</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      count: 0,
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
    }
  }
}
</script>
