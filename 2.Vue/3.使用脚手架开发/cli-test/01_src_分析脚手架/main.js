//引入vue 残缺版
// import Vue from 'vue'
// 引入完整版vue
import Vue from 'vue/dist/vue'
//引入App组件
import App from './App.vue'
//关闭生产提示
Vue.config.productionTip = false
/*
    不同版本的Vue:
      1.Vue.js与Vue.runtime.xxx.js的区别:
          (1)Vue.js是完整版的Vue, 包含: Vue的核心功能 和 模板解析器
          (2).Vue.runtime.xxx.js只有核心功能, 没有模板解析器
      
      2.因为Vue.runtime.xxx.js没有模板解析器, 所有不能使用template配置项, 需要使用
        render函数接收到reateElement函数去指定具体内容
  
*/
//创建vue实例
new Vue({
  // template:`<h1>你好啊!</h1>`
  //将组件渲染到指定容器上
  // render: h => h(App),
  // components:{App}
  //render函数需要有返回值
  render:h=>h(App),
  
}).$mount('#app')
