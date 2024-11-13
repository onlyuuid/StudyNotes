<template>
  <div class="classify">
      <Classify title="游戏" :games="games">
        <!-- 作用域插槽, 必须使用template标签包裹 -->
        <template scope="{games}">
          <ul>
            <li v-for="(item,index) in games" :key="index">
              {{ item }}
            </li>
          </ul>
        </template>
      </Classify>

      <Classify title="游戏" :games="games">
        <template scope="{games}">
          <ol>
            <li v-for="(item,index) in games" :key="index">
              {{ item }}
            </li>
          </ol>
        </template>
      </Classify>

      <Classify title="游戏" :games="games">
        <template scope="{games}">
              <h4 v-for="(item,index) in games" :key="index">
                {{ item }}
              </h4>
        </template>
      </Classify>
  </div>
</template>

<script>
// import axios from 'axios'
import Classify from './components/Classify.vue';

export default {
  name: 'App',
  data() {
    return {
    };
  },
  components:{Classify},
  
}
</script>

<style>
    body{
      /* border: 1px solid red; */
      margin: 0px;
    }
    .classify,.foot{
      display: flex;
      justify-content: space-around;
    }
    img{
      width: 100%;
    }
    video{
      width: 100%;
    }
    .footer{
      border: 1px solid red;
    }
</style>
