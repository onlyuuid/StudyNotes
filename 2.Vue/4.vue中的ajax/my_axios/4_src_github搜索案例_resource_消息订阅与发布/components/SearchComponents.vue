<template>
    <div class="search">
        <div>
            <h1>github搜索案例</h1>
        </div>
        <input type="text" v-model="searchMsg">
        <button @click="getSearchMsg">搜索</button>
    </div>
</template>

<script>
import pubsub from 'pubsub-js';

// import axios from 'axios';
export default {
    name:'SearchComponents',
    data() {
        return {
            searchMsg: '',
        };
    },
    methods:{
        getSearchMsg(){
            // 发送请求前
            // this.$bus.$emit('updateListData',{isFirst:false,isLoading:true,Users:[],load_error:''})
            //发布消息
            pubsub.publish('updateListData',{isFirst:false,isLoading:true,Users:[],load_error:''})

            this.$http.get(`https://autumnfish.cn/api/cq?query=${this.searchMsg}`).then(
                res => {
                    //请求成功后
                    // this.$bus.$emit('updateListData',{isLoading:false,Users:res.data.list,load_error:''})
                    //发布消息
                    pubsub.publish('updateListData',{isLoading:false,Users:res.data.list,load_error:''})

                },
                error => {
                    // 请求成功后
                    // this.$bus.$emit('updateListData',{isLoading:false,Users:[],load_error:error.message})
                    //发布消息
                    pubsub.publish('updateListData',{isLoading:false,Users:[],load_error:error.message})

                }
            );
        }
    }
}
</script>

<style>
   
    .search{
        display: flex;
        justify-content: center;
        align-items:center;
        width: auto;
        height: 10vh;
        background-color: aliceblue;
        box-sizing: border-box;
    }
    .search div:nth-child(1){
        position: absolute;
        top: 10px;
        left: 20px;
    }
    input{
        width: 230px;
        height: 40px;
        box-sizing: border-box;
    }
    button{
        width: 80px;
        height: 40px;
    }
</style>