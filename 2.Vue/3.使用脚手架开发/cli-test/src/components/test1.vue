<template>
    <div >
        <button @click="editStatus">点我显示或隐藏</button>
        <!-- name: 给动画的class属性起名字, 默认是v 
             appear: 让动画一上来就出现 -->
        <transition name="pbb" appear> 
            <h2 v-show="status">{{ name }}</h2>
        </transition>
    </div>
</template>

<script>
export default {  
    name:'test1',
    data() {
        return {
            name:'某某大学(动画)',
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
    /* 进入时激活 */
    .pbb-enter-active{
        animation: atguigu 0.5s linear;
    }
    /* 离开时激活 */
    .pbb-leave-active{
        animation: atguigu 0.5s linear reverse;
    }

    @keyframes atguigu{
        from{
            transform: translateX(-100%);
        }
        to{
            transform: translateX(0);
        }
    }
</style>