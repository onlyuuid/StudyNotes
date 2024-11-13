<template>
  <div>
        <ul>
            <li v-for="item in messageList" :key="item.id">
                {{ item.title }}
            </li>
        </ul>
        <div class="navi_3">
            <!-- 跳转并携带参数, to的字符串写法 params参数-->
            <!-- <router-link replace :to="`/home/message/detail/你好`"> -->
                <span @click="wenhou">发送问候语</span>
            <!-- </router-link> -->
            <!-- <router-link replace :to="`/home/message/detail/生日快乐`"> -->
                <span @click="zhufu">发送祝福语</span>
            <!-- </router-link>  -->
            
             <!-- 跳转并携带参数, to的对象写法 -->
            <!-- <router-link replace :to="{
                name:'xiangqing',       
                params:{                //params参数只能配合name跳转, 不能配合path跳转 
                    title:'非常感谢!'
                }
            }"> -->
                <span @click="ganxie">发送感谢语</span>
            <!-- </router-link>   -->
        </div>
        <span>
            
                <router-view></router-view>
            
            
        </span>
  </div>
</template>

<script>
export default {
    name:'Message',
    data() {
        return {
            messageList:[
                {
                    id:'001',
                    title:'怨犹不会让困难减少, 但是乐观会让人变得强大'
                },
                {
                    id:'002',
                    title:'弱小和无知不是生存的障碍, 傲慢才是'
                },
                {
                    id:'003',
                    title:'人生没有意义, 但找寻人生意义这件事有意义'
                }

            ]
        }
    },
    methods:{
        // 编程式路由导航
        wenhou(){
            this.$router.push({
               name:'xiangqing',
               params:{
                    title:'你好'
               }
            })   
        },
        zhufu(){
            this.$router.push({
               name:'xiangqing',
               params:{
                    title:'生日快乐'
               }
            })  
        },
        ganxie(){
            this.$router.push({
               name:'xiangqing',
               params:{
                    title:'非常感谢'
               }
            })  

        },
    },
    beforeDestroy(){
      console.log("@@",'Message组件被销毁了...')
    }
}
</script>

<style scpoed>
    .navi_3{
        display: inline-block;
        border-bottom: 2px solid rgb(171, 171, 171);
    }
    .navi_3 span{
        margin:20px
    }

    .active{
        color: rgb(63, 143, 247);
    }
</style>