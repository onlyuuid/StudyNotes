<template>
  <div>
    <h2>{{ name }}</h2>
    <h2>{{ age }}</h2>
    <button @click="endStudentName">点我向school组件发送数据</button>
  </div>
</template>

<script>
export default {
    name:'Student',
    data() {
        return {
            name: '张三',
            age: 19
        }
    },
    methods:{
        endStudentName(){
            //触发事件
            this.$bus.$emit('getStudentName',this.name)
        }
    }
}
</script>

<style>

</style>