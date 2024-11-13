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
        <button @click="additionOdd(value)">为奇数再加</button>
        <button @click="additionWait(value)">等一等再加</button>
        <h4 style="color:red">person组件中的人员个数为:{{personList.length }}</h4>
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
    //vuex模块配置中, 通过映射函数map操作或获取store中的数据
    computed:{
        // 利用mapState从state中寻找数据生成对应的计算属性(数组写法)
        ...mapState('computedAboot',['number','school','subject']),
        ...mapState('personAboot',['personList']),
        // 利用mapGetters从getters中寻找数据生成对应的计算属性(对象写法)
        ...mapGetters("computedAboot",{bigNumber:'bigNumber'}),
    },
    methods: {
        // 使用mapMutations自动生成使用mutations的方法(对象写法)
        ...mapMutations("computedAboot",{addition:'JIA',subtraction:'JIAN'}),

        // 使用mapActions自动生成使用actions的(对象写法)
        ...mapActions("computedAboot",{additionOdd:'jiaOdd',additionWait:'jiaWait'}),
    },
    mounted() {
        console.log("@@",this.$store)
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