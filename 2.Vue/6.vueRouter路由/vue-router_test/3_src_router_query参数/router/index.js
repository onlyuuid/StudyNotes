// 该文件专门用于配置路由所有规则

//引入VueRouter
import VueRouter from "vue-router"
//引入路由组件
import Aboot1 from '../pages/Aboot1.vue'
import Home from '../pages/Home.vue'
import News from "../pages/News.vue"
import Message from '../pages/Message.vue'
import Detail from '../pages/Detail.vue'

//创建路由实例, 并配置规则
export default new VueRouter({
    routes:[
        {
            path:'/aboot',
            component: Aboot1
        },
        {
            path:'/home',
            component: Home,
            children:[
                {
                    path:'news',   //嵌套路由不要再写 /
                    component: News 
                },
                {
                    path:'message',
                    component: Message,
                    children:[
                        {
                            path:'detail',
                            component: Detail
                        }
                    ]
                }

            ]
        }
    ]
})