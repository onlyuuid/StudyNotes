<template>
    <li>
        <input id="check" @click="modify" type="checkbox"  :checked="this.todo.done">
         {{ todo.name }}
        <button class="delBut" @click="delTodo()" :style="styObj">删除</button>
    </li>
</template>

<script>
export default {
    name:"Item",
    props:['todo','delTodos','modifyTodoDone'],

    methods: {
        //修改this.todo.done
        modify(){
            this.todo.done = !this.todo.done
            this.modifyTodoDone(this.todo.done,this.todo.id)
        },
        //删除todo
        delTodo(){
            if(!confirm("你确定要删除吗?")) return false;
            if(this.todo.done){
                this.delTodos(this.todo.id)
            } 
        }
    },
    computed:{
        styObj(){
            if(!this.todo.done){
                return {display:'none'}
            }else{
                return {display:''}
            }
        },
        
       
       
    }

}
</script>

<style>
     li{
            line-height: 40px;
            height: 40px;
            width: 360px;
            background-color: rgb(210, 244, 251);
            margin-bottom: 1px;
            
        }
        #check{
            vertical-align: middle;  /*垂直居中 以文本的中间为准*/
        }
        .delBut{
            float: right;
            transform: translate(-10px,8px);
            border: none;
            border-radius: 4px 4px 4px 4px;
            width: 50px;
            height: 25px;
            background-color: rgb(250, 55, 55);
        }
        .delBut:hover{
            cursor: pointer;
            background-color: rgb(246, 18, 18);
        }
</style>