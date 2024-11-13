<template>
    <div>
        <h2>{{ name }}</h2>
        <h2>{{ age }}</h2>
        <button @click="update">点我提示信息</button>
    </div>
</template>

<script>
//引入混入
import {mixin} from '../mixin.js'
export default {
    name:'Student2',
    data() {
        return {
            name:'王五',
            age:18,
            a:100
        }
    },
    //配置混入(局部)
    // mixins:[mixin],
    // mounted(){
    //     console.log('student2执行了...')
    // }
}
</script>

<style>

</style>