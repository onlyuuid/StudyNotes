<template>
  <div>
      <Computed></Computed>
      <hr>
      <Person></Person>
  </div>
</template>

<script>
// import axios from 'axios'
import Person from './components/Person.vue';

import Computed from './components/Computed.vue';

export default {
  name: 'App',
  data() {
    return {
      res:[]
    };
  },
  components:{Computed,Person},
  
}
</script>

<style>
    body{
      /* border: 1px solid red; */
      margin: 0px;
    }
</style>
