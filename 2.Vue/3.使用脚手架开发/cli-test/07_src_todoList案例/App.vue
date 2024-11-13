<template>
   <div class="main">
        <Header :addTodo="addTodo"></Header>
        <List :todos="todos" :delTodos="delTodos"></List>
        <Foot :todos="todos" :bathDelTodo="bathDelTodo"></Foot>
   </div>
</template>

<script>
/*
        组件化编写流程:
            1.创建静态组件
            2.绑定数据
            3.完成交互
*/
//用的是分别暴露,需要将{},不然不能使用
import {nanoid} from 'nanoid'
//引入Hello组件
import Header from './components/Header.vue'
import List from './components/List.vue'
import Foot from './components/Foot.vue'

export default {
    name:'App',
    components:{Header,List,Foot},
    data() {
        return {
            todos:[
                {id:nanoid(),name:'完成vue的学习',done:false},
                {id:nanoid(),name:'完成ES6的学习',done:true},
                {id:nanoid(),name:'完成thymeleaf的学习',done:false},
                {id:nanoid(),name:'完成spring cloud(Alibaba)的学习',done:true},
                {id:nanoid(),name:'完成博客网站的建设',done:true},
                {id:nanoid(),name:'完成docker的学习',done:false},
                {id:nanoid(),name:'完成k8s的学习',done:true},
            ]
        }
    },
    methods:{
        addTodo(value){
          this.todos.unshift(value)
        },
        delTodos(value){
            this.todos = this.todos.filter((todo)=>{
            return todo.id !== value
           })
        },
        bathDelTodo(value){
        this.todos = value.filter((todo)=>{
            return todo.done == false
          })
           
        }
    }
}
</script>
<style >
    body{
        padding: 0px;
        margin: 0px;
        }
    .main{
        display:inline-block;
        background-color: aliceblue;
        width: 375px;
        /* width: auto; */
        color: rgba(17, 15, 15, 0.807);
        padding-left: 17px;
    }
</style>