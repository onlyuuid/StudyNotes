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
            name:'guanyu',      //命名路由: 给路由起名字
            path:'/aboot',
            component: Aboot1
        },
        {
            name:'zhuye',
            path:'/home',
            component: Home,
            children:[
                {
                    name:'xinwen',
                    path:'news',   //嵌套路由不要再写 /
                    component: News 
                },
                {
                    name:'xiaoxi',
                    path:'message',
                    component: Message,
                    children:[
                        {
                            name:'xiangqing',
                            path:'detail/:title',  //params参数需要在路由文件中设置匹配规则
                            component: Detail,
                            // props参数, 让组件更好的接收到参数
                            //方式一: props的值为对象  一般不用, 不能动态传递数据
                            // props:{title:'你好'},

                            //方式二: props的值为布尔值, true为开启,能动态传递数据, 将参数以props的方式传递
                            // props:true

                             //方式三: props的值为函数, 能动态传递数据, 将参数以props的方式传递
                             props(route){ //参数是$route
                                return {title:route.params.title}   //该函数依赖返回值, 返回的是一个对象
                             }
                        }
                    ]
                }

            ]
        }
    ]
})