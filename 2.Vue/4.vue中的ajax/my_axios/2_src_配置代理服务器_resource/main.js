import Vue from 'vue'
import App from './App.vue'
// 引入vue-resource
import vueResource from 'vue-resource'
Vue.use(vueResource);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
