<template>
  <v-app id="inspire">
    <v-container>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="4">
          <div id="app">
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
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: 'RaffleDraw',
  data() {
    return {
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
  methods: {
    handleStart() {
      console.log('Draw start')
    },
    handleEnd(index) {
      alert('Hurray! you belong to ' + this.awards[this.currIndex].name)
    }
  }
}
</script>

<style scoped></style>
