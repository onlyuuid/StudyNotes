<template>
    <div >
        <button @click="editStatus">点我显示或隐藏</button>
        <!-- name: 给动画的class属性起名字, 默认是v 
             appear: 让动画一上来就出现
            多个元素实现过渡/动画不能使用transition,必须使用transition-group
        -->
        <transition-group 
            name="pbb"  
            appear> 
            <h2 v-show="!status"  :key="0">{{ name }}</h2>
            <h2 v-show="status"  :key="1">{{ name }}</h2>
            <!-- 如果要使两个元素互斥显示, 只需要将其中一个的条件渲染取反即可 -->
        </transition-group>
    </div>
</template>

<script>
export default {  
    name:'test3',
    data() {
        return {
            name:'某某大学(过渡)(多个元素同时实现动画效果 transition-group)',
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
    /* 进入前  离开的终点*/
    .pbb-enter,.pbb-leave-to{
        transform: translateX(-100%);
    }
    /* 进入的过程中 离开的过程中*/
    .pbb-enter-active,.pbb-leave-active{
        transition: 0.5s linear;
    }
    /* 进入的终点 离开前*/
    .pbb-enter-to,.pbb-leave{
        transform: translateX(0);
    }


</style>