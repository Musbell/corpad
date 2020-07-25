<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      color="#FF9800"
      dark
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="clipped" fixed app flat>
      <v-app-bar-nav-icon color="gray" @click.stop="drawer = !drawer" />
      <!--      <v-btn @click.stop="miniVariant = !miniVariant" icon>-->
      <!--        <v-icon>mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon>-->
      <!--      </v-btn>-->
      <!--      <v-btn @click.stop="clipped = !clipped" icon>-->
      <!--        <v-icon>mdi-application</v-icon>-->
      <!--      </v-btn>-->
      <!--      <v-btn @click.stop="fixed = !fixed" icon>-->
      <!--        <v-icon>mdi-minus</v-icon>-->
      <!--      </v-btn>-->
      <v-toolbar-title>
        <v-img
          src="https://res.cloudinary.com/musbell/image/upload/v1580986143/CORPAP3_btmvyg.png"
          max-width="200"
        />
      </v-toolbar-title>
      <v-spacer />
      <v-btn icon @click.stop="rightDrawer = !rightDrawer">
        <v-icon color="grey">mdi-power-off</v-icon>
      </v-btn>
    </v-app-bar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <v-navigation-drawer v-model="rightDrawer" :right="right" temporary fixed>
      <v-list>
        <v-list-item @click.native="right = !right">
          <v-list-item-action>
            <v-icon light color="white">
              mdi-repeat
            </v-icon>
          </v-list-item-action>
          <v-list-item-title>Switch drawer (click me)</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <!--    <v-footer :fixed="fixed" app>-->
    <!--      <span>&copy; 2019</span>-->
    <!--    </v-footer>-->
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/',
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Profile',
          to: '/profile',
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Savings',
          to: '/savings',
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Loan',
          to: '/loan',
        },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Corpad',
    }
  },
}
</script>
