<template>
    <div class="list">
        <ol>
            <transition-group>
                <Item v-for="todo in todos" :key="todo.id" :todo="todo"></Item>
            </transition-group>
        </ol>
    </div>
</template>

<script>
// 导入扩展包
import 'animate.css'
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
       .v-enter,.v-leave-to{
        transform: translateX(-100%);
       }

       .v-enter-active,.v-leave-active{
        transition: all linear 0.3s;
       }

       .v-enter-to,.v-leave{
        transform: translateX(0);
       }
</style>