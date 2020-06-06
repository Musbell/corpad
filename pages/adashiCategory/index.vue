<template>
  <v-container>
    <v-row>
      <v-col v-for="(item, i) in 6" :key="i" cols="12" sm="4">
        <v-card class="mx-auto" max-width="344" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">Category {{ i + 1 }}</div>
              <v-list-item-title class="headline mb-1"
                >₦10,000</v-list-item-title
              >
              <v-list-item-subtitle>20 members</v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-avatar
              tile
              size="80"
              color="grey"
            ></v-list-item-avatar>
          </v-list-item>

          <v-card-actions>
            <v-btn text nuxt to="/coperateSavings">Spin draw</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'Index'
}
</script>

<style scoped></style>
