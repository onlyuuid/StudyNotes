import Vue from 'vue'
import App from './App.vue'

// 引入store
import store from './store'
Vue.config.productionTip = false

const vm = new Vue({
  render: h => h(App),
  //配置store
  store,
  beforeCreate(){
    Vue.prototype.$bus = this
  }
}).$mount('#app')
console.log(vm)
