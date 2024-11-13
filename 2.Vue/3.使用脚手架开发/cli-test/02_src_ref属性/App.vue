<template>
    <div class="core">
        <h2 ref="title">{{name}}</h2>
        <!-- 使用组件 -->
        <button ref="but" @click="getRef">点我获取ref</button>
        <Hello ref="hel"></Hello>
    </div>
</template>

<script>
//引入其他组件
import Hello from "./components/Hello.vue"
//定义App组件
export default {
    name:'App',
    data() {
       return{
        name:'你好'
       }
    },
    methods:{
        getRef(){
            console.log(this.$refs.title) //真实dom元素
            console.log(this.$refs.but)//真实dom元素
            console.log(this.$refs.hel)//Hello的实例对象
        }
    },
    //注册组件
    components:{Hello}
}
</script>

<style>
    .core{
        background-color: lightblue;
    }
</style>