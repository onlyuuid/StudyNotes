import Vue from 'vue'
import App from './App.vue'
//引入VueRouter
import VueRouter from 'vue-router'
//引入路由配置文件
import router from './router'

Vue.config.productionTip = false
// 使用VueRouter
Vue.use(VueRouter)

new Vue({
  render: h => h(App),
  //配置路由项
  router,
}).$mount('#app')
