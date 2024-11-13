<template>
    <div class="foot" :style="styObj">
        <input id="check" @click="update" type="checkbox" :checked="bool"/>
        &nbsp;
        已完成{{checked}}项/共{{ todosLength }}项
        <button @click="bathDel" class="checkSel">删除完成事项</button>
    </div>
</template>

<script>

export default {
    name:"Foot",
    props:['todos','modifyTodoDone','bathDelTodo'],
    data() {
        return {
            bool:false
        }
    },
    //监听checked属性
    watch:{
        checked(){
            // console.log('checked修改了')
            if(this.checked === this.todosLength){
                this.bool = true
            }else{
                this.bool = false
            }
        }
    },
    methods:{
        //修改this.bool
        update() {
            this.bool = !this.bool
            this.todos.forEach(todo => {
                // console.log(this.bool)
            this.modifyTodoDone(this.bool,todo.id)
            });
        },
        //删除todo
        bathDel(){
            if(!confirm("你确定要删除吗?")) return false;
            return this.bathDelTodo(this.todos)
        }
    },
    computed:{
        todosLength(){
            return this.todos.length
        },
        checked(){              //pre将上一次返回的结果作为下一次输出的条件
            return this.todos.reduce((pre,current)=>{
                let i = pre+= current.done?1:0
                // console.log(i)
                return i
            },0)
        },
        styObj(){
            if(this.todosLength == 0){
                return {display:'none'}
            }else{
                return {display:''}
            }
        },
        
       


    }

}
</script>

<style>
    .foot{
            width:  360px;
            height: 40px;
            background-color: rgb(224, 234, 251);
            line-height: 40px;
            font-size: 0.7rem;
        }
        .checkSel{
            float: right;
            transform: translate(-10px,8px);
            border: none;
            border-radius: 4px 4px 4px 4px;
            width: 100px;
            height: 25px;
            background-color: rgb(252, 59, 59);
        }
        .checkSel:hover{
            background-color: rgb(246, 7, 7);
            cursor: pointer;
        }
</style>