
// 该文件用于创建vuex中最为核心的store

//引入vue
import Vue from 'vue'
// 引入vuex
import Vuex from 'vuex'
//使用vuex
Vue.use(Vuex)

// 准备actions---用于响应组件中的动作
const actions = {

    jiaOdd(context,value){
        console.log('处理了一些事情...jiaOdd')
        context.dispatch('demo1',value)
    },
    demo1(context,value){
        console.log('处理了一些事情...demo1')
        context.dispatch('demo2',value)
    },
    demo2(context,value){
        console.log('处理了一些事情...demo2')
        // 为奇数再加
        if(context.state.number % 2){
            context.commit('JIA',value)
        }
    },
    jiaWait(context,value){
        // 等一等再加
        setTimeout(() => {
            context.commit('JIA',value)
        }, 1000);
    }
}
// 准备mutations---用于操作数据(status)
const mutations = {
    JIA(state,value){
        console.log("mutations中的JIA被调用了")
        state.number += value
    },
    JIAN(state,value){
        state.number -= value
    },
}

// 准备status---用于存储数据
const state = {
    number:0,  //当前的和
}

//创建store并暴露store
export default new Vuex.Store({
    actions,
    mutations,
    state
})
 