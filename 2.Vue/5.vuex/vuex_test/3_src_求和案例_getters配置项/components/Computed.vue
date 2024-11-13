<template>
    <div>
        <h2>
            当前求和为: {{ $store.state.number }}
        </h2>
        <h4>当前求和放大10倍后为:{{ $store.getters.bigNumber }}</h4>
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
            value:1   //用户选择的数字
        };
    },
    methods: {
        addition(){
            this.$store.commit('JIA',this.value)
        },
        subtraction(){
            this.$store.commit('JIAN',this.value)
        },
        additionOdd(){
            this.$store.dispatch('jiaOdd',this.value)
        },
        additionWait(){
            this.$store.dispatch('jiaWait',this.value)
        }
    },
    mounted() {
        this.$store.getters.bigNumber
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