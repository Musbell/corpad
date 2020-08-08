<!--<template>-->
<!--  <div class="chart"></div>-->
<!--</template>-->

<!--<script>-->
<!--import Anychart from 'anychart'-->

<!--export default {-->
<!--  name: 'VueAnychart',-->
<!--  // eslint-disable-next-line vue/require-prop-types-->
<!--  props: ['options', 'Anychart'],-->
<!--  data() {-->
<!--    return {-->
<!--      chart: null,-->
<!--    }-->
<!--  },-->
<!--  watch: {-->
<!--    options(options) {-->
<!--      if (!this.chart && options) {-->
<!--        this.init()-->
<!--      } else {-->
<!--        this.chart.dispose()-->
<!--        this.chart = null-->
<!--        this.init()-->
<!--      }-->
<!--    },-->
<!--  },-->
<!--  mounted() {-->
<!--    if (!this.chart && this.options) {-->
<!--      this.init()-->
<!--    }-->
<!--  },-->
<!--  beforeDestroy() {-->
<!--    if (this.chart) {-->
<!--      this.chart.dispose()-->
<!--      this.chart = null-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    removeSeries() {-->
<!--      if (this.chart.getSeriesCount()) {-->
<!--        this.chart.removeSeriesAt(0)-->
<!--      }-->
<!--    },-->
<!--    removeAllSeries() {-->
<!--      if (this.chart.getSeriesCount()) {-->
<!--        this.chart.removeAllSeries()-->
<!--      }-->
<!--    },-->
<!--    addSeries(data) {-->
<!--      this.delegateMethod('addSeries', data)-->
<!--    },-->
<!--    delegateMethod(name, data) {-->
<!--      if (!this.chart) {-->
<!--        warn(-->
<!--          `Cannot call [$name] before the chart is initialized. Set prop [options] first.`,-->
<!--          this-->
<!--        )-->
<!--        return-->
<!--      }-->

<!--      return this.chart[name](data)-->
<!--    },-->
<!--    init() {-->
<!--      if (!this.chart && this.options) {-->
<!--        const _Anychart = this.Anychart || Anychart-->
<!--        this.chart = new _Anychart.fromJson(this.options)-->
<!--        this.chart.container(this.$el).draw()-->
<!--      }-->
<!--    },-->
<!--  },-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->
<!--.chart {-->
<!--}-->
<!--</style>-->
