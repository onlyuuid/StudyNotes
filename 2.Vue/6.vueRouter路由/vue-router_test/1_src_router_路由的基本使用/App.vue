<template>
  <div id="app">
      <div class="navi_1">
        <router-link active-class="active" to="/aboot">
          <span>Aboot</span>
        </router-link>
        <router-link active-class="active" to="/home">
          <span>Home</span>
        </router-link>  
      </div>
      <div class="show_1">
          <router-view></router-view>
      </div>
  </div>
</template>

<script>

export default {
  name: 'App',
 
}
</script>

<style scoped>
  #app{
    display: flex;
    justify-content: center;
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
