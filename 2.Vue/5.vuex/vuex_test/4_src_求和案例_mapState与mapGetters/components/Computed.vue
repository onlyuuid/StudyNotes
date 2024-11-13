<template>
    <div>
        <h2>
            当前求和为: {{ number }}
        </h2>
        <h4>当前求和放大10倍后为:{{ bigNumber }}</h4>
        <h4>我在{{ school }},学习{{ subject }}</h4>
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
// 引入mapState映射函数
import {mapState,mapGetters} from 'vuex'

export default {
    name:'Computed',
    data() {
        return {
            property: 'value',
            value:1   //用户选择的数字
        };
    },
    computed:{
        // 自己写的计算属性
        // number(){
        //     return this.$store.state.number
        // },
        // school(){
        //     return this.$store.state.school
        // },
        // subject(){
        //     return this.$store.state.subject
        // },


        // 利用mapState从state中寻找数据生成对应的计算属性(对象写法)
        // ...mapState({number:'number',school:'school',subject:'subject'}),

        // 利用mapState从state中寻找数据生成对应的计算属性(数组写法)
        ...mapState(['number','school','subject']),


        //---------------------------------
        // 自己写的计算属性
        // bigNumber(){
        //     return this.$store.getters.bigNumber
        // },

        // 利用mapGetters从getters中寻找数据生成对应的计算属性(对象写法)
        // ...mapGetters({bigNumber:'bigNumber'}),

        // 利用mapGetters从getters中寻找数据生成对应的计算属性(数组写法)
        ...mapGetters(['bigNumber'])

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