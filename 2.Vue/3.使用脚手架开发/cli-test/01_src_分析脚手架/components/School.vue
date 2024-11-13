<template>
    <div class="back">
        <!-- 用于编写网页的结构 -->
        欢迎语:{{ msg }}
    </div>
</template>
<script>
        // 用于编写网页的交互
        // 1.创建school组件 (组件名应和文件名保持一致)
        export default { //简写
            name:'School',
            data() {
                return {
                    msg:'hello!'
                }
            },
        }
        //将组件导出给其他组件使用
        //方式一: 批量导出
        // export {School}
        //默认导出
        // export default School
        
</script>
<style>
        /* 用于编写网页的样式 */
        .back{
            background-color: lightblue;
        }
</style>