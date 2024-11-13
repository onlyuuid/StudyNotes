<template>
    <div class="demo">
        <h2>{{ name }}</h2>
        <h2>{{ age }}</h2>
    </div>
</template>

<script>
//定义组件
export default {
    name: "Hello",
    data() {
        return {
            name: "李四",
            age: 19
        };
    },
   
}
</script>
<style scoped>
    .demo{
        background-color: skyblue;
    }
</style>