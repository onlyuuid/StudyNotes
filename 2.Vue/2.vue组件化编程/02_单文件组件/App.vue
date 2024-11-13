<template>
    <!-- App组件用来汇总其他组件 -->
    <div>
        <!-- 使用组件 -->
        <School></School>
        <Student></Student>
    </div>
</template>
<script>
        // 用于编写网页的交互
        //1.引入其他子组件组件
import School from "./School.vue"  //后缀.vue可写可不写
import Student from "./Student.vue"

        //定义App组件
export default {
    name:'App', //组件名
    //注册组件
    compoments:{
        School,
        Student
    }
}               
</script>
<!-- 如果确定不写样式 style标签可以省略 -->