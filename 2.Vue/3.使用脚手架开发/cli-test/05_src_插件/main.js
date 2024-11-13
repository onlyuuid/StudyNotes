//引入Vue
import Vue from 'vue'
//引入 App 组件
import App from './App.vue'
//关闭生产提示
Vue.config.productionTip=false
//引入插件
import plugins from './plugins'
//引用(使用)插件
Vue.use(plugins)
//创建vue实例
new Vue({
    render: h=>h(App)
}).$mount("#app")