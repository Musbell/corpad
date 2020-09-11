var Main = {
  data() {
    return {
      freeze: false,
      rolling: false,
      wheelDeg: 0,
      prizeNumber: 15,
      prizeListOrigin: [
        {
          icon: "https://picsum.photos/40?random=1",
          name: "1"
        },
        {
          icon: "https://picsum.photos/40?random=6",
          name: "2"
        },
        {
          icon: "https://picsum.photos/40?random=2",
          name: "3"
        },
        {
          icon: "https://picsum.photos/40?random=3",
          name: "4"
        },
        {
          icon: "https://picsum.photos/40?random=6",
          name: "5"
        },
        {
          icon: "https://picsum.photos/40?random=4",
          name: "6"
        },
        {
          icon: "https://picsum.photos/40?random=5",
          name: "7"
        },
        {
          icon: "https://picsum.photos/40?random=6",
          name: "8"
        },
        {
          icon: "https://picsum.photos/40?random=6",
          name: "9"
        },
        {
          icon: "https://picsum.photos/40?random=6",
          name: "10"
        },
        {
          icon: "https://picsum.photos/40?random=6",
          name: "11"
        },
        {
          icon: "https://picsum.photos/40?random=6",
          name: "12"
        },
        {
          icon: "https://picsum.photos/40?random=6",
          name: "13"
        },
        {
          icon: "https://picsum.photos/40?random=6",
          name: "14"
        },
        {
          icon: "https://picsum.photos/40?random=6",
          name: "15"
        }
      ]
    };
  },
  computed: {
    prizeList() {
      return this.prizeListOrigin.slice(0, this.prizeNumber);
    }
  },
  methods: {
    onClickRotate() {
      if (this.rolling) {
        return;
      }
      const result = Math.floor(Math.random() * this.prizeList.length);
      this.roll(result);
    },
    roll(result) {
      this.rolling = true;
      const { wheelDeg, prizeList } = this;
      this.wheelDeg =
        wheelDeg -
        wheelDeg % 360 +
        6 * 360 +
        (360 - 360 / prizeList.length * result);
      setTimeout(() => {
        this.rolling = false;
        alert("Your Position：" + prizeList[result].name);
      }, 4500);
    }
  },
  watch: {
    prizeNumber() {
      this.freeze = true;
      this.wheelDeg = 0;

      setTimeout(() => {
        this.freeze = false;
      }, 0);
    }
  }
};
var App = Vue.extend(Main);
new App().$mount("#app");
