// 此js只和App组件打交道
//导入App组件
import App from "./App.vue";

new Vue({
    el:'#app',
    data() { 
        return {
        }
    },
    //注册组件(局部)
    components:{
        App
    }
})

