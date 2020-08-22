<template>
  <v-app id="inspire">
    <pageTitle :title="singleCategory(id).name" />
    <v-container>
      <v-alert text color="warning">
        <h4 class="title">Category Name: {{singleCategory(id).name}} </h4>
        <div>
          Description: {{singleCategory(id).description}}
        </div>

        <v-divider class="my-4 warning" style="opacity: 0.22;"></v-divider>

        <!-- <v-row align="center" no-gutters> -->
          <!-- <v-col class="grow"
            > -->
            <p>Start Date: {{new Date(singleCategory(id).start).toUTCString()}}</p>
            <p>Ammount to pay: NGN {{singleCategory(id).ammount}} </p>
            <p>Payment Interval : {{singleCategory(id).interval}} days</p>
            <p>Ammount to recieve: NGN {{singleCategory(id).payment}}</p>
            <p>Maximum Users: {{singleCategory(id).maxUsers}}</p>
            <p>Current Members: {{singleCategory(id).members}}</p>
            <!-- </v-col
          > -->
          <!-- <v-spacer></v-spacer> -->
          <!-- <v-col class="shrink"> -->
            <v-row justify="center">
              <v-dialog v-model="dialog" persistent max-width="500" scrollable>
                <template v-slot:activator="{ on }">
                  <v-btn color="#FFAB40" outlined class="ma-5" v-on="on" :disabled="singleCategory(id).members == singleCategory(id).maxUsers">
                    Spin Now!
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title class="headline"
                    >Spin to be a member</v-card-title
                  >
                  <v-card-text>
                    <spinner :category="{members: singleCategory.members}"/>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="orange darken-1" text @click="dialog = false"
                      >Close</v-btn
                    >
                    <!--                    <v-btn @click="dialog = false" color="green darken-1" text-->
                    <!--                      >Agree</v-btn-->
                    <!--                    >-->
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-row>
          <!-- </v-col> -->
        <!-- </v-row> -->
      </v-alert>
      <v-subheader>Joined members</v-subheader>
      <v-row class="pa-4" justify="space-between">
        <v-col cols="12" sm="5">
          <v-treeview
            :active.sync="active"
            :items="items"
            :load-children="fetchUsers"
            :open.sync="open"
            activatable
            color="warning"
            open-on-click
            transition
          >
            <template v-slot:prepend="{ item }">
              <v-icon v-if="!item.children">mdi-account</v-icon>
            </template>
          </v-treeview>
          <v-btn block color="error" dark>Opt out</v-btn>
        </v-col>

        <v-divider vertical></v-divider>

        <v-col class="d-flex text-center">
          <v-scroll-y-transition mode="out-in">
            <div
              v-if="!selected"
              class="title grey--text text--lighten-1 font-weight-light"
              style="align-self: center;"
            >
              Select a Member
            </div>
            <v-card
              v-else
              :key="selected.id"
              class="pt-6 mx-auto"
              flat
              max-width="400"
            >
              <v-card-text>
                <v-avatar v-if="avatar" size="88">
                  <v-img
                    :src="`https://avataaars.io/${avatar}`"
                    class="mb-6"
                  ></v-img>
                </v-avatar>
                <h3 class="headline mb-2">
                  {{ selected.name }}
                </h3>
                <div>
                  <v-badge color="orange" content="6">
                    Position {{ selected.id }}
                  </v-badge>
                </div>
                <div class="blue--text mb-2">{{ selected.email }}</div>
                <div class="blue--text subheading font-weight-bold">
                  {{ selected.username }}
                </div>
              </v-card-text>
              <v-divider></v-divider>
              <v-row class="text-left" tag="v-card-text">
                <v-col class="text-right mr-4 mb-2" tag="strong" cols="5"
                  >Company:</v-col
                >
                <v-col>{{ selected.company.name }}</v-col>
                <v-col class="text-right mr-4 mb-2" tag="strong" cols="5"
                  >Website:</v-col
                >
                <v-col>
                  <a :href="`//${selected.website}`" target="_blank">{{
                    selected.website
                  }}</a>
                </v-col>
                <v-col class="text-right mr-4 mb-2" tag="strong" cols="5"
                  >Phone:</v-col
                >
                <v-col>{{ selected.phone }}</v-col>
              </v-row>
            </v-card>
          </v-scroll-y-transition>
        </v-col>
      </v-row>
    </v-container>

    
  </v-app>
</template>

<script>
import {mapGetters} from 'vuex'
import spinner from '~/components/Spinner'
const avatars = [
  '?accessoriesType=Blank&avatarStyle=Circle&clotheColor=PastelGreen&clotheType=ShirtScoopNeck&eyeType=Wink&eyebrowType=UnibrowNatural&facialHairColor=Black&facialHairType=MoustacheMagnum&hairColor=Platinum&mouthType=Concerned&skinColor=Tanned&topType=Turban',
  '?accessoriesType=Sunglasses&avatarStyle=Circle&clotheColor=Gray02&clotheType=ShirtScoopNeck&eyeType=EyeRoll&eyebrowType=RaisedExcited&facialHairColor=Red&facialHairType=BeardMagestic&hairColor=Red&hatColor=White&mouthType=Twinkle&skinColor=DarkBrown&topType=LongHairBun',
  '?accessoriesType=Prescription02&avatarStyle=Circle&clotheColor=Black&clotheType=ShirtVNeck&eyeType=Surprised&eyebrowType=Angry&facialHairColor=Blonde&facialHairType=Blank&hairColor=Blonde&hatColor=PastelOrange&mouthType=Smile&skinColor=Black&topType=LongHairNotTooLong',
  '?accessoriesType=Round&avatarStyle=Circle&clotheColor=PastelOrange&clotheType=Overall&eyeType=Close&eyebrowType=AngryNatural&facialHairColor=Blonde&facialHairType=Blank&graphicType=Pizza&hairColor=Black&hatColor=PastelBlue&mouthType=Serious&skinColor=Light&topType=LongHairBigHair',
  '?accessoriesType=Kurt&avatarStyle=Circle&clotheColor=Gray01&clotheType=BlazerShirt&eyeType=Surprised&eyebrowType=Default&facialHairColor=Red&facialHairType=Blank&graphicType=Selena&hairColor=Red&hatColor=Blue02&mouthType=Twinkle&skinColor=Pale&topType=LongHairCurly',
]
const pause = (ms) => new Promise((resolve) => setTimeout(resolve, ms))

export default {
  components: { spinner },
  name: 'Index',
  data() {
    return {
      active: [],
      avatar: null,
      open: [],
      users: [],
      alert: true,
      dialog: false,
    }
  },
  computed: {
    ...mapGetters('categoriesModule', ['singleCategory']),
    items() {
      return [
        {
          name: 'Members',
          children: this.users,
        },
      ]
    },
    id(){
      return this.$route.params.id;
    },
    selected() {
      if (!this.active.length) return undefined

      const id = this.active[0]

      return this.users.find((user) => user.id === id)
    },
  },

  watch: {
    selected: 'randomAvatar',
  },

  methods: {
    async fetchUsers(item) {
      // Remove in 6 months and say
      // you've made optimizations! :)
      await pause(1500)

      return fetch('https://jsonplaceholder.typicode.com/users')
        .then((res) => res.json())
        .then((json) => item.children.push(...json))
        .catch((err) => console.warn(err))
    },
    randomAvatar() {
      this.avatar = avatars[Math.floor(Math.random() * avatars.length)]
    },
  },
}
</script>
