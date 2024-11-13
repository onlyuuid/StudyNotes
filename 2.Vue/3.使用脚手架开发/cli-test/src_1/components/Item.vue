<template>
    <li @mouseenter="enter" @mouseleave="leave" >
        <input id="check" @click="modify" type="checkbox"  :checked="this.todo.done">
         <span v-show="!isEdit">{{ todo.name }}</span>
         <input v-show="isEdit" type="text" :value="todo.name" ref="title" @blur="blur(todo,$event)">
        <button 
            class="delBut" 
            :class="isShow?'':'hiddeBut'" 
            @click='delTodo'>删除
        </button>
        <button v-show="!isEdit"
            class="editBut" 
            :class="isShow?'':'hiddeBut'" 
            @click='editTodo'>修改
        </button>
    </li>
</template>

<script>
import PubSub from 'pubsub-js';
export default {
    name:"Item",
    props:['todo'],
    data() {
        return {
            isShow: false,
            isEdit: false
        }
    },
    methods: {
        //修改this.todo.done
        modify(){
            this.todo.done = !this.todo.done
            this.$bus.$emit('modifyTodoDone',this.todo.done,this.todo.id)
        },
        blur(todo,e){
            this.isEdit = false
            if(!e.target.value) return alert('待办不能为空');
            this.$bus.$emit("editTodo",todo.id,e.target.value)
        },
        //删除todo
        delTodo(){
            if(!confirm("你确定要删除吗?")) return false;
            if(this.todo){
                //发布消息
                console.log("Item发布了消息")
                PubSub.publish("delTodos",this.todo.id)
            } 
        },
        editTodo(){
            this.isEdit = !this.isEdit 
            // 配置编辑的input框一上来就获取到焦点
            
            // setTimeout(()=>{  //这种方法能解决问题,但还有更好的 方式一
            //     this.$refs.title.focus()
            // },)
            // 方式二
            this.$nextTick(()=>{  //告诉vue,等页面渲染完毕后再调用这个方法
                // console.log(this)
                this.$refs.title.focus()
                
            })
            
        },
        enter(){
            return this.isShow = true
        },  
        leave(){
            return this.isShow = false
        },
    },
    computed:{
        
    },
    beforeDestroy(){
        this.$bus.$off(['delTodos','modifyTodoDone'])
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
    .editBut{
        float: right;
        transform: translate(-10px,8px);
        border: none;
        border-radius: 4px 4px 4px 4px;
        width: 50px;
        height: 25px;
        margin-right: 5px;
        background-color: rgb(99, 183, 211);
    }
    .delBut:hover{
        cursor: pointer;
        background-color: rgb(246, 18, 18);
    }
    .hiddeBut{
        display: none;
    }
</style>