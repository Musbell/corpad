<template>
  <div>
    <welcome-slider />
    <v-container>
      <v-subheader class="title">Join our available categories now</v-subheader>
      <v-row dense>
        <v-col v-for="(item, i) in items" :key="i" cols="12" sm="4">
          <v-hover v-slot:default="{ hover }">
            <v-card :elevation="hover ? 12 : 2" :color="item.color" dark>
              <div class="d-flex flex-no-wrap justify-space-between">
                <div>
                  <v-card-title
                    v-text="item.title"
                    class="headline"
                  ></v-card-title>

                  <v-card-subtitle v-text="item.artist"></v-card-subtitle>
                  <v-card-subtitle v-text="item.members"></v-card-subtitle>
                </div>

                <v-avatar class="ma-3" size="125" tile>
                  <v-img :src="item.src"></v-img>
                </v-avatar>
              </div>
              <v-card-actions>
                <v-btn nuxt to="game" color="primary" dark>Join Now</v-btn>
              </v-card-actions>
            </v-card>
          </v-hover>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import WelcomeSlider from '../components/welcomeSlider'
export default {
  name: 'Index',
  components: { WelcomeSlider },
  data: () => ({
    items: [
      {
        color: '#1F7087',
        src:
          'https://buzznigeria.com/wp-content/uploads/2013/11/naira1000-e1433411934680-640x449.jpg',
        title: 'Group 1',
        artist: ' ₦10,000',
        members: '20 members'
      },
      {
        color: '#952175',
        src:
          'https://risenetworks.org/wp-content/uploads/2014/11/naira-notes1.jpg',
        title: 'Group 2',
        artist: '#20,000',
        members: '20 members'
      },
      {
        color: '#1F7087',
        src:
          'https://media.gettyimages.com/photos/cropped-hand-of-person-holding-paper-currency-picture-id1188415524?s=612x612',
        title: 'Group 3',
        artist: '₦30,000',
        members: '20 members'
      }
    ]
  })
}
</script>

<style scoped></style>
