<template>
    <div >
        <h2>{{ name }}</h2>
        <h2 class=atguigu>{{ age }}</h2>
        <button @click="aleName()">点我提示学生名</button>
    </div>
</template>

<script>
export default {
    name:'Student',
    data() {
        return {
            name:'王五',
            age:18,
        }
    },
    props:['aleData'],
    methods:{
        aleName(){
            this.aleData(this.name)
        }
    }
}
</script>

<style lang="less"> //预编译css,less支持嵌套编写  
   
    
</style>