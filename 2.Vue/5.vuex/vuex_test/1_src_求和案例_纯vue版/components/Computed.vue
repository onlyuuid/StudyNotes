<template>
    <div>
        <h2>
            当前求和为: {{ number }}
        </h2>
        <span>
            <select v-model.number="value">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
            </select>
        </span>
        <button @click="addition">+</button>
        <button @click="subtraction">-</button>
        <button @click="additionOdd">为奇数再加</button>
        <button @click="additionWait">等一等再加</button>
    </div>
</template>

<script>
export default {
    name:'Computed',
    data() {
        return {
            property: 'value',
            number:0,  //当前的和
            value:1   //用户选择的数字
        };
    },
    methods: {
        addition(){
            this.number += this.value
        },
        subtraction(){
            this.number -= this.value
        },
        additionOdd(){
            if(this.number % 2){
                this.number += this.value
            }
        },
        additionWait(){
            setTimeout(()=>{
                this.number += this.value
            },1000)
        }
    },
}
</script>

<style>
    button{
        margin-left: 10px;
    }
    select{
        margin-left: 10px;
    }
</style>