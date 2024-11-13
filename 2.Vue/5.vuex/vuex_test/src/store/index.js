
// 该文件用于创建vuex中最为核心的store

//引入vue
import Vue from 'vue'
// 引入vuex
import Vuex from 'vuex'
//使用vuex
Vue.use(Vuex)
import computedAboot from './count'
import personAboot from './person'


//创建store并暴露store
export default new Vuex.Store({
    // 将配置注册进store
    modules:{
        computedAboot:computedAboot,  
        personAboot:personAboot
    }
})
 