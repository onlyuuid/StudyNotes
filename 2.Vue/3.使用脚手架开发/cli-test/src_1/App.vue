<template>
   <div class="main">
        <!-- 向子组件传递数据 -->
        <Header @addTodo="addTodo"></Header>
        <List :todos="todos"></List>
        <Foot :todos="todos" @bathDelTodo="bathDelTodo" @modifyTodoDone="modifyTodoDone"></Foot>
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
// 导入pubsub-js
import PubSub from 'pubsub-js'
//引入Hello组件
import Header from './components/Header.vue'
import List from './components/List.vue'
import Foot from './components/Foot.vue'

export default {
    name:'App',
    components:{Header,List,Foot},
    data() {
        return {
            todos: JSON.parse(localStorage.getItem('todos'))==null?[]:JSON.parse(localStorage.getItem('todos'))
        }
    },
    methods:{
        //添加todo
        addTodo(value){
          this.todos.unshift(value)
          localStorage.setItem('todos',JSON.stringify(this.todos))
        },
        //删除todo
        delTodos(_,value){
            // console.log(value)
            console.log("App收到了消息")
            this.todos = this.todos.filter((todo)=>{
            return todo.id !== value
           })
           localStorage.setItem('todos',JSON.stringify(this.todos))
        },
        //批量删除todo
        bathDelTodo(value){
            this.todos = value.filter((todo)=>{
                return todo.done == false
            })
            localStorage.setItem('todos',JSON.stringify(this.todos))
        },
        //修改todo
        editTodo(id,title){
            this.todos = this.todos.filter(todo =>{
                return todo.id === id?todo.name = title:todo.name=todo.name
            })
            localStorage.setItem('todos',JSON.stringify(this.todos))
        },
        //修改todo.done
        modifyTodoDone(bool,id){
            // console.log('@@',bool,id)
            this.todos.forEach(todo => {
                if(todo.id === id){
                    todo.done = bool
                }
                localStorage.setItem('todos',JSON.stringify(this.todos))
            });
        }
    },
    mounted() {
        // this.$bus.$on('delTodos',this.delTodos)
        // 订阅消息
        PubSub.subscribe("delTodos",this.delTodos)
        this.$bus.$on('modifyTodoDone',this.modifyTodoDone)
        this.$bus.$on('editTodo',this.editTodo)
    },
    beforeDestroy(){
        // 取消订阅
        PubSub.unsubscribe('delTodos')
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