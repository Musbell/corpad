<template>
  <v-carousel height="300">
    <v-carousel-item
      v-for="(item, i) in items"
      :key="i"
      :src="item.src"
      reverse-transition="fade-transition"
      transition="fade-transition"
    ></v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  name: 'WelcomeSlider',
  data() {
    return {
      items: [
        {
          src:
            'https://media.gettyimages.com/vectors/banking-finance-banner-and-icons-vector-id629162108'
        },
        {
          src:
            'https://cdn5.f-cdn.com/contestentries/61278/10210881/53084decebd97_thumb900.jpg'
        },
        {
          src:
            'https://www.postermywall.com/assets/images/open-graph-default.jpg'
        }
      ]
    }
  }
}
</script>

<style scoped></style>
