<template>
  <div id="app">
      <div class="navi_1">
        <button @click="retreat">后退</button>
        <button @click="forward">前进</button>
       
        <!-- 将浏览器历史记录的模式改为替换模式(replace), 
          默认是追加模式, 追加模式能够记录浏览历史, replace模式不记录浏览历史 -->
        <!-- <router-link replace active-class="active" :to="{
          name:'guanyu'
        }"> -->
          <span @click="toGuanyu">Aboot</span>
        <!-- </router-link>yd -->
        <!-- <router-link replace active-class="active" :to="{
          name:'zhuye'
        }"> -->
          <span @click="toHome">Home</span>
        <!-- </router-link>   -->
      </div>
      <div class="show_1">
        <!--    缓存路由组件, 让被替换的路由组件保持挂载, 而不是销毁, include的值为组件名
                单个组件用字符串, 多个组件用数组
        -->
        <keep-alive :include="['Aboot1','Home']">
          <router-view></router-view>
        </keep-alive>
          
      </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  methods: {
    toGuanyu(){
      // 编程式路由导航, 可以不借助router-link实现跳转
      this.$router.push({
        name:'guanyu',
      })
    },
    toHome(){
      this.$router.push({
        name:'zhuye'
      })
    },
    forward(){  //操作浏览器的历史步骤
      this.$router.forward()
    },
    retreat(){
      this.$router.back()
    },

    go(){
      this.$router.go(-1)  //可前进,也可后退, 正数表示前进, 负数表示后退, -3表示退三步
    }
    
  },
 
 
}
</script>

<style scoped>
  #app{
    display: flex;
    width: 100vw;
    height: 100vh;
  }
  .navi_1{
    width: 130px;
    height: 100px;
    border-right: 1px solid rgb(122, 122, 122);
  }
  .navi_1 span{
    display: inline-block;
    border-radius: 5px;
    text-align: center;
    line-height: 40px;
    width: 120px;
    height: 40px;
    /* background-color: rgb(225, 240, 254); */
    /* margin: 2px; */
  }

  .active{
    display: inline-block;
    height: 40px;
    background-color: rgb(76, 162, 255);
    color: white;
  }
  .show_1{
    position: relative;
    left: 50px;

  }
</style>
