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
      <v-badge color="error" overlap class="mr4">
        <template slot="badge">
          6
        </template>
        <v-icon color="grey">mdi-bell</v-icon> </v-badge
      ><br />
      <v-icon color="red">mdi-power</v-icon>

      <v-avatar>
        <v-img
          height="40"
          width="40"
          src="https://thumbnails.yayimages.com/1600/b/1ff/b1ff916.jpg"
        ></v-img>
      </v-avatar>

      <v-btn icon @click.stop="rightDrawer = !rightDrawer">
        <v-icon color="grey">mdi-power-off</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
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
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-home',
          title: 'Welcome',
          to: '/',
        },
        {
          icon: 'mdi-view-dashboard',
          title: 'Dashboard',
          to: '/dashboard',
        },
        {
          icon: 'mdi-account-cash',
          title: 'Profile',
          to: '/profile',
        },
        {
          icon: 'mdi-bank',
          title: 'Savings',
          to: '/savings',
        },
        {
          icon: 'mdi-package  ',
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
