<template>
    <div>                                   
        <!--                                当传的是数字时,使用v-bind -->
        <Hello></Hello>
        <hr>
        <Student></Student>
    </div>
</template>

<script>
//引入Hello组件
import Hello from './components/Hello.vue'
import Student from './components/Student.vue'
export default {
    name:'App',
    components:{Hello,Student}
}
</script>
<style>

</style>