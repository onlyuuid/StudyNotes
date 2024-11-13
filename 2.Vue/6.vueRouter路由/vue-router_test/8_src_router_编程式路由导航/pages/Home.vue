<template>
  <div>
        <h3>显示关于Home的内容</h3>
        <div class="navi_2">
                                        <!-- 点击的时候指定样式 -->
          <!-- <router-link replace to="/home/news" active-class="active"> -->
            <span @click="toNews">news</span>
          <!-- </router-link>         -->
          <!-- <router-link replace to="/home/message" active-class="active"> -->
            <span @click="toMessage">messge</span>
          <!-- </router-link> -->
        </div>
        <div class="show_2">
          <router-view></router-view>
        </div>
  </div>
</template>

<script>
export default {
    name:'Home',
    methods: {
      toNews(){
        //编程式路由导航
        this.$router.replace({
          path:'/home/news'
        })
      },
      toMessage(){
        this.$router.replace({
          path:'/home/message'
        })
      }
    },

}
</script>

<style scpoed>
  .navi_2{
    border-bottom: 2px solid rgb(126, 126, 126);
  }

  .navi_2 span{
    display: inline-block;
    width: 120px;
    height: 20px;
  }

  .active{
    color: blue;
  }
</style>