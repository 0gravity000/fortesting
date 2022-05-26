<template>
  <div class="welcome-site">
    <h1>{{ msg }}</h1>
    <p>
      テストに役立つものをピックアップしています。
    </p>
  </div>
</template>

<script>
export default {
  name: 'WelcomeSite',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
