<template>
  <div id="app">
      <button @click="getPerson">点我发送请求(获取person信息)</button>
      <div v-for="(item,index) in res" :key="index">
        {{item.name}}
      </div>
  </div>
</template>

<script>

// import axios from 'axios'
export default {
  name: 'App',
  data() {
    return {
      res:[]
    };
  },
  methods: {
    getPerson(){ 
      
    },
    // getSchool(){
    //   axios.get('http://localhost:8080/demo/school').then(
    //     response => {
    //       console.log("访问servlet02成功...",response.data)
    //     },
    //     error => {
    //       console.log('访问失败',error.message)
    //     }
    //   )
    // }
  },
  mounted() {
    console.log(this)
    this.$http.get('http://localhost:8080/atguigu/person').then(
        response => {
          console.log("访问servlet01成功...",response.data)
          this.res = response.data  
          // 获取到的数据对象属性不能有空的, 否则页面无法渲染 
        },
        error => {
          console.log('访问失败',error.message)
        }
      )
  },
 
}
</script>

<style>

</style>
