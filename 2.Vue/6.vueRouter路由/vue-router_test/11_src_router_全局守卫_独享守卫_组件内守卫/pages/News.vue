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
    },

    // 组件内守卫
    beforeRouteEnter(to,from,next){  //进入该组件时调用
        if(localStorage.getItem('school') === 'atguigu'){
            next()
        }else{
            alert("身份信息不匹配,school不是atguigu")
        }
    },
    beforeRouteLeave(to,from,next){ //离开该组件时调用
        next()
    }
}
</script>

<style>

</style>