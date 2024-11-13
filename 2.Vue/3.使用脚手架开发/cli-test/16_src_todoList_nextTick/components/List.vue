<template>
    <div class="list">
        <ol>
            <Item v-for="todo in todos" :key="todo.id" :todo="todo"></Item>
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
    props:['todos']

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