<template>
  <div class="container-fluid">
    <NavbarMain />
    <div class="row">
      <div class="col-3">
        <SidebarHome />
      </div>
      <div class="col-9">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import NavbarMain from '@/components/NavbarMain.vue'
import SidebarHome from '@/components/SidebarHome.vue'

//const axios = require('axios').default

export default {
  components: {
    NavbarMain,
    SidebarHome,
  },
  data () {
    return {
    }
  },
  created() {
  },
  methods: {
  }
}
</script>

<style>

</style>
