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
//定义组件
export default {
    name: "Hello",
    data() {
        return {
            name: "李四",
            age: 19
        };
    },
    //配置混入(局部)
    // mixins:[mixin]
   
}
</script>