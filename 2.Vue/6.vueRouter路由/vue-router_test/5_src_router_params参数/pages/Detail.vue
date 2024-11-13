<template>
    <div>
        <!-- 接收params参数 -->
        {{ $route.params.title }}   
    </div>
</template>

<script>
export default {
    name:'Detail',
    mounted() {
        console.log('@@',this.$route)
      },
}
</script>

<style>

</style>