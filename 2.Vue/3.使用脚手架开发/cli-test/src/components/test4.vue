<template>
    <div >
        <button @click="editStatus">点我显示或隐藏</button>
        <!-- name: 给动画的class属性起名字, 默认是v 
             appear: 让动画一上来就出现
            多个元素实现过渡/动画不能使用transition,必须使用transition-group
        -->
        <!-- 集成第三方库 -->
        <transition 
            appear
            name="animate__animated animate__bounce"
            enter-active-class="animate__headShake" 
            leave-active-class="animate__backOutUp"> 
            <h2 v-show="status">{{ name }}</h2>
        </transition>
    </div>
</template>

<script>
// 导入第三方库
import 'animate.css'
export default {  
    name:'test4',
    data() {
        return {
            name:'某某大学(集成第三方动画库)',
            status: true
        }
    },
    methods: {
        editStatus(){
            console.log("@@")
            this.status = !this.status
        }
    },
}
</script>

<style> 
    h2{
        width: 500px;
        height: 100px;
        background-color: orange;
    }
   


</style>