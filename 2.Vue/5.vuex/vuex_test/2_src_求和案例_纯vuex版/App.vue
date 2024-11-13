<template>
  <div>
      <Computed></Computed>
  </div>
</template>

<script>
// import axios from 'axios'
import Computed from './components/Computed.vue';

export default {
  name: 'App',
  data() {
    return {
      res:[]
    };
  },
  components:{Computed},
  
}
</script>

<style>
    body{
      /* border: 1px solid red; */
      margin: 0px;
    }
</style>
