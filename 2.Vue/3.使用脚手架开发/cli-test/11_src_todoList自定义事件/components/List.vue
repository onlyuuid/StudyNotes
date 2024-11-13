<template>
    <div class="list">
        <ol>
            <Item v-for="todo in todos" :modifyTodoDone="modifyTodoDone" :key="todo.id" :todo="todo" :delTodos="delTodos"></Item>
        </ol>
    </div>
</template>

<script>
import Item from './Item.vue'

export default {
    name:"List",
    components:{Item},
    data() {
        return {
            
        }
    },
    props:['todos','delTodos','modifyTodoDone']

}
</script>

<style>
     .list{
            /* width: 360px; */
            height: auto;
            padding: 0px;
        }
        ol{
            margin: 0px;
            list-style: none;
            width: auto;
            padding: 0px;
        }
       
</style>