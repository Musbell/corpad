<template>
  <div class="container fluid">
    <span>Prize number: {{ prizeListOrigin.length }}</span>
    <!-- <button type="button" @click="!rolling && prizeNumber < 8 && (prizeNumber++)" :disabled="rolling || prizeNumber === 8">Add</button>
  <button type="button" @click="!rolling && prizeNumber > 2 && (prizeNumber--)" :disabled="rolling || prizeNumber === 2">Remove</button> -->
   <div class="wheel-wrapper">
    <div
      class="wheel-pointer"
      @click="rotate"
    >
      Start
    </div>
    <div
      class="wheel-bg"
      :class="{freeze: freeze}"
      :style="`transform: rotate(${wheelDeg}deg)`"
    >
      <div class="prize-list">
        <div
          class="prize-item-wrapper"
          v-for="(item,index) in prizeList"
          :key="index"
        >
          <div
            class="prize-item"
            :style="`transform: rotate(${(360/ prizeList.length) * index}deg)`"
          >
            <div class="prize-name">
              {{ item.name }}
            </div>
            
            <!-- <div class="prize-icon">
              <img :src="item.icon">
            </div> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
export default {
  props: ['category'],
  data() {
    return {
      freeze: false,
      rolling: false,
      wheelDeg: 0,
      // category: {
      //   members: 25,
      //   takenPositions : [0, 1, 3, 7, 11],
      // },
    };
  },
  computed: {
    prizeList() {
      return this.prizeListOrigin.slice(0, this.category.members);
    },
    prizeListOrigin(){
      let arr = [];
      for (let i = 0; i <= this.category.members; i++){
          if(this.category.takenPositions.includes(i)){
            continue; 
          }else{
            arr.push({name: i})
          }
        }
        return arr;
      }
    },
  
  methods: {
    rotate() {
      if (this.rolling) {
        return;
      }
      const result = Math.floor(Math.random() * this.category.members.length);
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
        alert("Result：" + prizeList[result].name);
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
}
</script>
<style lang="scss" scoped>
  html {
  background: #dd7c7d;
}

.wheel-wrapper {
  width: 500px;
  height: 500px;
  position: absolute;
  top: 53%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.wheel-pointer {
  width: 60px;
  height: 60px;
  border-radius: 1000px;
  background: rgb(248, 99, 0);
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  line-height: 60px;
  z-index: 10;
  cursor: pointer;

  &::after {
    content: "";
    position: absolute;
    top: -32px;
    left: 50%;
    border-width: 0 8px 40px;
    border-style: solid;
    border-color: transparent transparent rgb(248, 99, 0);
    transform: translateX(-50%);
  }
}
.wheel-bg {
  width: 100%;
  height: 100%;
  border-radius: 1000px;
  overflow: hidden;
  transition: transform 4s ease-in-out;
  background: orange;

  &.freeze {
    transition: none;
    background: red;
  }
}

.prize-list {
  width: 100%;
  height: 100%;
  position: relative;
  text-align: center;
}

.prize-item-wrapper {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 250px;
  height: 250px;
}

.prize-item {
  width: 100%;
  height: 100%;
  transform-origin: bottom;
}
  .prize-name {
    padding: 16px 0;
  }

  // .prize-icon {
  // }

</style>


