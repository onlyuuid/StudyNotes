<template>
    <!-- 需要有一个根容器 -->
    <div class="style01">
        {{msg}}
    </div>
</template>

<script>
//定义组件
export default {
    name:'Hello',
    data() {
        return {
            msg:'欢迎来到Vue!!!'
        }
    },

}
</script>

<style>
    .style01{
        width: 30vw;
        height: 20vh;
        background-color: aqua;
    }
</style>