<template>
    <div>
        <h2>{{ name }}</h2>
        <h2 v-fbind="3"></h2>
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
    //配置混入(局部)
    // mixins:[mixin]
   
}
</script>