<template>
    <div class="header">
        <input id="addTodo" type="text" v-model="value"  @keyup.enter="addValue" placeholder="请添加你的待办事项">
        <button @click="addValue" id="but">添加</button>
    </div>
</template>

<script>
import { nanoid  } from 'nanoid';
//切记不要修改porps中的数据, 这样是违背原则的
export default {
    name:"Header",
    props:['addTodo','addTodo'],
    data() {
        return {
           value:'',
           name:''
        }
    },
    methods:{
        // addValue(event){
        //     this.name = event.target.value
        //     if(this.name=='' | this.name == null){
        //         alert("请注意,您的待办事项不能为空哦!")
        //         return false
        //     }
        //     //完善数据
        //     let obj = {id:nanoid(),name:this.name,done:false}
        //     //将数据传给父辈
        //     this.addTodo(obj)
        //     //传完之后清空输入框
        //     event.target.value = ''
        // },
        addValue(){
            if(this.value=='' | this.value == null){
                alert("请注意,您的待办事项不能为空哦!")
                return false
            }
            //完善数据
            let obj = {id:nanoid(),name:this.value,done:false}
            //将数据传给父辈
            this.addTodo(obj)
            //传完之后清空输入框
            this.value = ''
        },
        // addValue2(){
            
        // }
    }

}
</script>

<style>
     .header{
            width: 360px;
            height: 40px;
            background-color: rgb(198, 198, 250);
            /* border: 1px solid red; */
        }
        #addTodo{
            width: 280px;
            height: 30px;
            border-radius: 5px 5px 5px 5px;
            border-color: aliceblue;
            /* border: 1px solid red; */
        }
        #addTodo :focus{
            border-color: gainsboro;
        }
        #but{
            transform: translateY(2px);
            width: 70px;
            height: 30px;
            font-family: Verdana, Geneva, Tahoma, sans-serif;
            font-size: 0.8rem;
            border-color: aliceblue;
            border-radius: 5px 5px 5px 5px;
            border-color: white;
            float: right;
            transform: translateY(5px);
            
        
        }
        #but:hover{
            background-color: gainsboro;
            cursor: pointer;
        }
    /* 媒体查询 */
    @media screen and(max-width: 500px) {
        .but{
            background-color: blue;
        }
    }
</style>