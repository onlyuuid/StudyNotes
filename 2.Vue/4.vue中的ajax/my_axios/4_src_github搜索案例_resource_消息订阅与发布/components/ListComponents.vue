<template>
    <div class="list">
        <span v-show="info.Users.length" v-for="item in info.Users" :key="item.login">
            <span style="position: absolute;">
                {{ item.name}}
            </span>
            <img :src="item.icon" alt="">
        </span>
        <h3 v-show="info.isFirst">
            欢迎使用
        </h3>
        <h3 v-show="info.isLoading">
            加载中....
        </h3>
        <!-- 展示异常信息 -->
        <h3 v-show="info.load_error">
            {{ info.load_error }}
        </h3>
    </div>
</template>

<script>
import pubsub from 'pubsub-js'
export default {
    name:'ListComponents',
    data() {
        return {
            info:{
                Users:[],
                isFirst: true,      //是否是第一次访问
                isLoading: false,   //是否处于加载状态
                load_error:''       //加载失败的信息
            }
        }
    },
    methods:{
        // 第一个参数是消息名,不是传递过来的数据,可以用 _ 占个位
        getUsers(_,objdata){
            // console.log('收到消息...',objdata)
            // ES6语法
            //将将info对象和objdata对象里的属性名进行比对, 
            //属性名相同的以objdata为准将其赋值给info,
            //info中有,而objdata中没有的属性,维持info中该属性的原状态
            this.info = {...this.info,...objdata}
            console.log("@",this.info)
        }
    },

    mounted() {
        // this.$bus.$on('updateListData',this.getUsers)
        //订阅消息
        this.pubid = pubsub.subscribe('updateListData',this.getUsers)

    },
    beforeDestroy() {
        pubsub.unsubscribe(this.pubid)
    },

}
</script>

<style>
    .list{
        margin-top: 30px;
        width: auto;
        height: auto;
        /* overflow: hidden; */
        box-sizing: border-box;
        background-color: azure;
        /* border: 1px solid red; */
    }
    .list span{
        display:inline-block;
        width: 150px;
        height: 150px;
        overflow: hidden;
        /* border: 1px solid blue; */
        margin: 4px;
    }
    img{
        width: 100%;
        height: 100%;
    }
    h3{
        position: absolute;
        left: 10px;
    }
</style>