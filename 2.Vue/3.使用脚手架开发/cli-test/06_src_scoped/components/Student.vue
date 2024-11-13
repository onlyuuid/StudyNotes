<template>
    <div class="demo ">
        <h2>{{ name }}</h2>
        <h2 class=atguigu>{{ age }}</h2>
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
}
</script>

<style lang="less"> //less支持嵌套编写
    .demo{
        background-color: pink;
        .atguigu{
        font-size:10rem;
        }
    }
    
    
</style>