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
        <button @click="addition(value)">+</button>
        <button @click="subtraction(value)">-</button>
        <button @click="jiaOdd(value)">为奇数再加</button>
        <button @click="jiaWait(value)">等一等再加</button>
    </div>
</template>

<script>
// 引入mapState映射函数
import {mapState,mapGetters,mapMutations,mapActions} from 'vuex'

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
        // 自己写的调用mutations的方法
        // addition(){
        //     this.$store.commit('JIA',this.value)
        // },
        // subtraction(){
        //     this.$store.commit('JIAN',this.value)
        // },

        // 使用mapMutations自动生成使用mutations的方法(对象写法)
        ...mapMutations({addition:'JIA',subtraction:'JIAN'}),

        // 使用mapMutations自动生成使用mutations的方法(数组写法)
        // ...mapMutations(['JIA','JIAN']),

        // 自己写的调用actions的方法
        // additionOdd(){
        //     this.$store.dispatch('jiaOdd',this.value)
        // },
        // additionWait(){
        //     this.$store.dispatch('jiaWait',this.value)
        // }

        // 使用mapActions自动生成使用actions的(对象写法)
        // ...mapActions({additionOdd:'jiaOdd',additionWait:'jiaWait'}),

        // 使用mapActions自动生成使用actions的(数组写法)
        ...mapActions(['jiaOdd','jiaWait'])
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