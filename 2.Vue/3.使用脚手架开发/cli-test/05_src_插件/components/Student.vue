<template>
    <div>
        <h2>{{ name | trim }}</h2>
        <h2>{{ age }}</h2>
        <button @click="test">点我提示hello</button>
    </div>
</template>

<script>
export default {
    name:'Student',
    data() {
        return {
            name:'王五wangwu',
            age:18,
        }
    },
    methods:{
        test(){
          this.hello();
        }
    }
}
</script>

<style>

</style>