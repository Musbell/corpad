<template>
  <v-app id="inspire">
    <v-container>
      <v-row align="center" justify="center" class="elevation-5">
        <v-col cols="12" sm="8" md="4">
          <LuckDraw
            v-model="currIndex"
            :awards="awards"
            :rate="rate"
            :radius="radius"
            :textFontSize="textFontSize"
            :lineHeight="lineHeight"
            :textColor="textColor"
            :textMargin="textMargin"
            :textPadding="textPadding"
            :btnFontSize="btnFontSize"
            :btnColor="btnColor"
            :btnBorderColor1="btnBorderColor1"
            :btnBorderColor2="btnBorderColor2"
            :btnBorderColor3="btnBorderColor3"
            :btnBgColor="btnBgColor"
            :btnText="btnText"
            :btnRadius="btnRadius"
            :borderColor="borderColor"
            @start="handleStart"
            @end="handleEnd"
          />
        </v-col>
      </v-row>
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
        </v-col>

        <v-divider vertical></v-divider>

        <v-col class="d-flex text-center">
          <v-scroll-y-transition mode="out-in">
            <div
              v-if="!selected"
              class="title grey--text text--lighten-1 font-weight-light"
              style="align-self: center;"
            >
              Select a User
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
const avatars = [
  '?accessoriesType=Blank&avatarStyle=Circle&clotheColor=PastelGreen&clotheType=ShirtScoopNeck&eyeType=Wink&eyebrowType=UnibrowNatural&facialHairColor=Black&facialHairType=MoustacheMagnum&hairColor=Platinum&mouthType=Concerned&skinColor=Tanned&topType=Turban',
  '?accessoriesType=Sunglasses&avatarStyle=Circle&clotheColor=Gray02&clotheType=ShirtScoopNeck&eyeType=EyeRoll&eyebrowType=RaisedExcited&facialHairColor=Red&facialHairType=BeardMagestic&hairColor=Red&hatColor=White&mouthType=Twinkle&skinColor=DarkBrown&topType=LongHairBun',
  '?accessoriesType=Prescription02&avatarStyle=Circle&clotheColor=Black&clotheType=ShirtVNeck&eyeType=Surprised&eyebrowType=Angry&facialHairColor=Blonde&facialHairType=Blank&hairColor=Blonde&hatColor=PastelOrange&mouthType=Smile&skinColor=Black&topType=LongHairNotTooLong',
  '?accessoriesType=Round&avatarStyle=Circle&clotheColor=PastelOrange&clotheType=Overall&eyeType=Close&eyebrowType=AngryNatural&facialHairColor=Blonde&facialHairType=Blank&graphicType=Pizza&hairColor=Black&hatColor=PastelBlue&mouthType=Serious&skinColor=Light&topType=LongHairBigHair',
  '?accessoriesType=Kurt&avatarStyle=Circle&clotheColor=Gray01&clotheType=BlazerShirt&eyeType=Surprised&eyebrowType=Default&facialHairColor=Red&facialHairType=Blank&graphicType=Selena&hairColor=Red&hatColor=Blue02&mouthType=Twinkle&skinColor=Pale&topType=LongHairCurly'
]
const pause = (ms) => new Promise((resolve) => setTimeout(resolve, ms))

export default {
  name: 'Index',
  data() {
    return {
      active: [],
      avatar: null,
      open: [],
      users: [],
      currIndex: 0,
      rate: 80,
      radius: 200,
      textFontSize: '13px',
      lineHeight: 20, // 文字行高
      textColor: '#d64737',
      textMargin: 30,
      textPadding: 0,
      btnFontSize: '26px',
      btnColor: '#d64737',
      btnBorderColor1: '#d64737',
      btnBorderColor2: '#ffffff',
      btnBorderColor3: '#f6c66f',
      btnBgColor: '#ffdea0',
      btnText: 'Play',
      btnRadius: 60,
      borderColor: '#d64737',
      awards: [
        { name: 'Category 1', color: '#f9e3bb' },
        { name: 'Category 2', color: '#f8d384' },
        { name: 'Category 3', color: '#f9e3bb' },
        { name: 'Category 4', color: '#f8d384' },
        { name: 'Category 5', color: '#f9e3bb' },
        { name: 'Category 6', color: '#f8d384' },
        { name: 'Category 7', color: '#f9e3bb' },
        { name: 'Category 8', color: '#f8d384' }
      ]
    }
  },
  computed: {
    items() {
      return [
        {
          name: 'Users',
          children: this.users
        }
      ]
    },
    selected() {
      if (!this.active.length) return undefined

      const id = this.active[0]

      return this.users.find((user) => user.id === id)
    }
  },

  watch: {
    selected: 'randomAvatar'
  },

  methods: {
    handleStart() {
      console.log('Draw start')
    },
    handleEnd(index) {
      alert('Hurray! you belong to ' + this.awards[this.currIndex].name)
    },
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
    }
  }
}
</script>

<style scoped></style>
