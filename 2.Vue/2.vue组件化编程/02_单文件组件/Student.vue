<template>
    <div class="back">
        <!-- 用于编写网页的结构 -->
        姓名:{{ name }}
    </div>
</template>
<script>
        // 用于编写网页的交互
        // 1.创建school组件 (组件名应和文件名保持一致)
        export default { //简写
            name:'Student',
            data() {
                return {
                    msg:'张三!'
                }
            },
        }
        //将组件导出给其他组件使用
        //方式一: 批量导出
        // export {Stuent}
        //默认导出
        // export default Student
        
</script>
<style>
        /* 用于编写网页的样式 */
        .back{
            background-color: rgb(48, 148, 73);
        }
</style>