<template>
  <v-container>
    <PageTitle title="Adashi Category"></PageTitle>
    <v-row>
      <v-col v-for="(item, key) in categories" :key="key" cols="12" sm="4">
        <v-card class="mx-auto" max-width="344" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">{{ item.name }}</div>
              <v-list-item-title class="headline mb-1"
                >₦{{ item.fee }}</v-list-item-title
              >
              <v-list-item-subtitle
                >{{ item.maxMembers }} members</v-list-item-subtitle
              >
            </v-list-item-content>

            <v-list-item-avatar
              tile
              size="80"
              color="grey"
            ></v-list-item-avatar>
          </v-list-item>

          <v-card-actions>
            <v-btn
              text
              nuxt
              @click="loadThis(item.id)"
              class="primary"
              :disabled="item.maxMembers === item.members"
              >{{
                item.maxMembers === item.members ? 'Full' : 'Spin Draw'
              }}</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-spacer></v-spacer>
      <v-btn nuxt to="/adashiCategory/new" class="primary">new category</v-btn>
      <v-spacer></v-spacer>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'Index',
  computed: {
    categories() {
      return this.$store.state.adashi.categories
    }
  },
  methods: {
    loadThis(id) {
      this.$router.push(`/coperateSavings/${id}`)
    }
  }
}
</script>

<style scoped></style>
