// 该文件专门用于配置路由所有规则

//引入VueRouter
import VueRouter from "vue-router"
//引入路由组件
import Aboot from '../pages/Aboot.vue'
import Home from '../pages/Home.vue'

//创建路由实例, 并配置规则
export default new VueRouter({
    routes:[
        {
            path:'/aboot',
            component: Aboot
        },
        {
            path:'/home',
            component: Home
        }
    ]
})