<template>
    <div class="sty">
        <div>{{ msg }}</div>
        <div>{{ name }}</div>
        <div>{{ address }}</div>
        <div>{{ myAge }}</div>
        <button @click="updateData">点我修改接收的数据</button>
    </div>
</template>

<script>
//定义组件
export default {
    name:'Hello',
    data() {
        return {
            msg:'你好啊!',
            myAge:this.age
        }
    },
    methods:{
        updateData(){
            this.myAge++
        }
    },
    // 1.简单传入
    props:['name','address','age'],
    // 2.接收数据的同时限制数据类型
    props:{ 
        name:String,
        address:String,
        age:Number
    },
    //  3.接收数据的同时限制数据类型+必要限制+默认值
     props:{
        name:{
            type:String,
            required:true
        },
        address:{
            type:String,
            required:true,
        },
        age:{
            type:Number,
            default:19
        }
     }

}
</script>

<style>
    .sty{
        width: auto;
        height: 20vh;
        background-color: aqua;
    }
</style>