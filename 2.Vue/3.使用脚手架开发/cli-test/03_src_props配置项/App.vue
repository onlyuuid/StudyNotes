<template>
    <div>                                   
        <!--                                当传的是数字时,使用v-bind -->
        <Hello name="张三" address="金华大道" ></Hello>
    </div>
</template>

<script>
//引入Hello组件
import Hello from './components/Hello.vue'
export default {
    name:'App',
    components:{Hello}
}
</script>

<style>

</style>