<template>
    <ol>
        <li v-for="item in newList" :key="item.id">
            {{ item.title }}
            <input type="text">
        </li>
    </ol>
</template>

<script>
export default {
    name:'News',
    data() {
        return {
            newList:[
                {
                    id:'001',
                    title:'即时更新'
                },
                {
                    id:'002',
                    title:'极速快报'
                },
                {
                    id:'003',
                    title:'今日头条'
                }
            ]
        }
    },
    beforeDestroy(){
        console.log("##",'News组件被销毁了...')
    }
}
</script>

<style>

</style>