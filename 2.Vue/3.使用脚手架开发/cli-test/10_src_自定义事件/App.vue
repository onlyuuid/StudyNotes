<template>
    <div>
        <!-- 子组件给父组件传递数据 -->
        <!-- 1.通过props的方式向子组件传递函数   
                                    组件上写原生的DOM事件名依然会被认为是自定义事件,
                                    需要加上native修饰符-->
        <Student :aleData="aleData" @click.native="test" ></Student>
        <hr/>
        <!-- 2.通过绑定自定义事件 v-on或@ -->
        <School v-on:atguigu="aleData" @hint="aleAddress"></School>    
        <hr/>
        <!-- 3.通过ref给组件绑定自定义事件,更加灵活-->
        <!-- <School ref="school"></School>  -->
    </div>
</template>

<script>
//引入Hello组件
import School from './components/School.vue'
import Student from './components/Student.vue'
export default {
    name:'App',
    components:{Student,School},
    methods:{
        aleData(value){
           alert("@@App收到了:"+value)
        },
        aleAddress(address){
           console.log('##收到了:'+address) 
        }
    },
    mounted() {
        setTimeout(() => {
            //通过ref拿到子组件实例绑定事件  //写成普通函数this指向触发事件组件的实例对象
            this.$refs.school.$on('hint',function(){
            console.log('hint事件被触发了...')
        })}, 3000);  //可以设置延迟多少秒再绑定,这种方式更加灵活
    },
    
}
</script>
<style >
    .sty{
        background-color: red;
    }
</style>