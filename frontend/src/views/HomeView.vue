<template>
  <div class="home">
    <WelcomeSite msg="Welcome to ForTesting Site"/>
  </div>
</template>

<script>
// @ is an alias to /src
import WelcomeSite from '@/components/WelcomeSite.vue'

export default {
  name: 'HomeView',
  components: {
    WelcomeSite
  }
}
</script>
