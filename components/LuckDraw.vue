<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="12">
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
  </v-container>
</template>

<script>
export default {
  name: 'RaffleDraw',
  // props: ['maxUsers'],
  data() {
    return {
      maxUsers: 20,
      currIndex: null,
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
      btnText: 'Spin',
      btnRadius: 60,
      borderColor: '#d64737'
      // awards: [
      //   { name: 'Position 1', color: '#f9e3bb' },
      //   { name: 'Position 2', color: '#f8d384' },
      //   { name: 'Position 3', color: '#f9e3bb' },
      //   { name: 'Position 4', color: '#f8d384' },
      //   { name: 'Position 5', color: '#f9e3bb' },
      //   { name: 'Position 6', color: '#f8d384' },
      //   { name: 'Position 7', color: '#f9e3bb' },
      //   { name: 'Position 8', color: '#f8d384' }
      // ]
    }
  },
  mounted() {
    this.currIndex = Math.floor(Math.random() * this.awards.length)
  },
  computed: {
    awards() {
      const arr = []
      for (let i = 1; i <= this.maxUsers; i++) {
        arr.push({
          name: `pos ${i}`,
          color: i % 2 === 0 ? '#f9e3bb' : '#f8d384'
        })
      }
      return arr
    }
  },
  methods: {
    handleStart() {
      console.log('Draw start')
    },
    handleEnd(index) {
      alert('Hurray! you belong to ' + this.awards[this.currIndex].name)
      this.$emit('closeDialog')
      this.awards = [
        ...this.awards.filter((i) => i !== this.awards[this.currIndex])
      ]
      console.log('new awards', this.awards)
      this.currIndex = Math.floor(Math.random() * this.awards.length)
    }
  }
}
</script>
