//引入Vue
import Vue from 'vue'
//引入 App 组件
import App from './App.vue'
//关闭生产提示
Vue.config.productionTip=false
//创建vue实例
new Vue({
    render: h=>h(App),
    beforeCreate() {
        //安转全局事件总线
        Vue.prototype.$bus = this
    },
}).$mount("#app")