<template>
  <div class="title">
    <h3 class="text-center headline my-3">{{ title }}</h3>
  </div>
</template>
<script>
export default {
  props: {
    title: String
  }
}
</script>
<style>
.title {
  color: darkorange;
}
</style>
