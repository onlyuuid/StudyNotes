<template>
  <div class="classify">
      <Classify title="美食" >
          <img src="https://www.sanyue.com/jiameng/public/pinpai/pic/1668B9F31E6.jpg" alt="">
      </Classify>

      <Classify title="游戏" :games="games">
        <ol>
          <li v-for="(item,index) in games" :key="index">
            {{ item }}
          </li>
        </ol>
      </Classify>

      <Classify title="电影" :listData="films">
        <video controls src="https://vd3.bdstatic.com/mda-keb3adb0p4pg2cc7/sc/mda-keb3adb0p4pg2cc7.mp4?v_from_s=hkapp-haokan-hna&auth_key=1678953616-0-0-14b2c99fd85759309486fb86e8914e5d&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=1816382449&vid=10716133163556787497&abtest=107354_1-107353_1&klogid=1816382449"></video>
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
      foot:['火锅','烧烤','小龙虾','牛排'],
      games:['红色警戒','穿越火线','劲舞团','超级玛丽'],
      films:['《教父》','《拆弹专家》','《你好,李焕英》','《尚硅谷》'],
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
    .classify{
      display: flex;
      justify-content: space-around;
    }
    img{
      width: 100%;
    }
    video{
      width: 100%;
    }
</style>
