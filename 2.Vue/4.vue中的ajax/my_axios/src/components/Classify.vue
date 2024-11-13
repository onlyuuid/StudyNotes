<template>
    <div class="slot">
        <h3>{{title}}分类</h3>
        <!-- 插槽, 挖个坑, 等待组件的使用者来填 -->
        <!-- 将games传递给插槽的使用者 -->
        <slot :games="games"></slot>

    </div>
</template>

<script>

export default {
    props:['title'],
    name:'Classify',
    data() {
        return {
            games:['红色警戒','穿越火线','劲舞团','超级玛丽'],

        };
    }
}
</script>

<style scoped>
    .slot{
        background-color:skyblue;
        width: 200px;
        height: 300px;
        margin-left: 20px;
    }
    h3{
        text-align: center;
        background-color: rgb(241, 103, 68);
    }
</style>