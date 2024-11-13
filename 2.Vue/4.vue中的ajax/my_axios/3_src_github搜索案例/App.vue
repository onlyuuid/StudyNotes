<template>
  <div>
      <SearchComponents></SearchComponents>
      <ListComponents></ListComponents>
  </div>
</template>

<script>
// import axios from 'axios'
import SearchComponents from './components/SearchComponents.vue';
import ListComponents from './components/ListComponents.vue';
export default {
  name: 'App',
  data() {
    return {
      res:[]
    };
  },
  components:{SearchComponents,ListComponents},
  
}
</script>

<style>
    body{
      /* border: 1px solid red; */
      margin: 0px;
    }
</style>
