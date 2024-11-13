<template>
    <div>
        <test1></test1>  
        <test2></test2> 
        <test3></test3> 
        <test4></test4>  
    </div>
</template>

<script>
//引入Hello组件
import test1 from './components/test1.vue'
import test2 from './components/test2.vue'
import test3 from './components/test3.vue'
import test4 from './components/test4.vue'


export default {
    name:'App',
    components:{test1,test2,test3,test4}
}
</script>
<style >
</style>