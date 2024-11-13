<template>
    <div>
        <!-- 接收params参数 -->
        {{ title }}   
    </div>
</template>

<script>
export default {
    name:'Detail',
    props:['title'],
    mounted() {
        // console.log('@@',this.$route)
        // console.log('@@',this.title)
        // console.log("##",this.route)
      },
}
</script>

<style>

</style>