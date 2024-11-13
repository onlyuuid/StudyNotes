## 一.目录及文件介绍
    (1).node_modules:  存放了Vue所使用的核心资源(不要动)
    (2).public:        存放了网页的index(首页)页面, 所有的组件最终都是挂载到这个页面的容器中.以及网站的图标

    (3).src: 这个文件是Vue的核心文件,里面包含了两个文件夹assets和components,以及两个文件App.vue以及main.js
    -   components: 该文件夹用于存放子组件 
    -   assets: 该文件夹用于存放一些静态资源,如图片或视频等
    -   App.vue: 该文件是所有组件的父组件, 即App.vue组件用于管理其他子组件, 该组件由vm管理
    -   main.js: 该文件是整个应用的入口文件, 用于引入vue实例和App.vue组件, 该组件不和其他子组件直接交互
    (4).gitgnore: git的忽略文件,哪些文件不用git管理可以在里面配置
    (5).balel.config.js: 将ES6转为ES5的配置文件
    (6).package-lock.json: 包管理器
    (7).package.json: 显示系统信息, 以及所用的的库
    (8).README.md: 描述应用信息, 使用方式等
    (9).vue.config.js: 应用的配置文件, 可以在此文件中修改首页名称, 主组件名
#
## 二.关于不同版本的Vue
### 1.Vue.js与Vue.runtime.xxx.js的区别:
-      (1)Vue.js是完整版的Vue, 包含: Vue的核心功能 和 模板解析器
-      (2).Vue.runtime.xxx.js只有核心功能, 没有模板解析器

### 2.因为Vue.runtime.xxx.js没有模板解析器, 所有不能使用template配置项, 需要使用render函数接收到reateElement函数去指定具体内容

#
## 三.ref的使用:
### 1.获取dom元素或子组件的信息(id的替代)
    2.使用方式:
    <Hello ref='hel'/>或<Hello ref='hel'></Hello>
#
## 四.props配置项
    功能:让组件接收外部传来的数据:
        (1).传递数据:
            <Dome name='xxx'/>或<Dome name='xxx'></Dome>
        (2).接收数据:
            <!-- 1.简单传入 -->
            props:['name'],

            <!-- 2.接收数据的同时限制数据类型 -->
            props:{ 
                name:String,
            },

            <!-- 3.接收数据的同时限制数据类型+必要限制+默认值 -->
            props:{
                name:{
                    type:String, //类型
                    required:true， //必要性
                    default：'老王' //默认值
                },
            }
        备注：props中的数据是只读的, Vue会检测你的修改,如果你修改了数据, Vue会发出警告,
             如果业务需要修改数据, 那么请将props中的数据复制一份到data中,然后修改data中的数据
#
## 五.mixin混入(合)
    功能: 可以把多个组件共用的配置提取成一个混入对象
    使用方式:
        第一步定义混入: 例:
            {
                data(){
                    return {...}
                },
                methods:{...}    
            }
        第二步使用混入: 例:
            (1).局部使用: mixins:[xxx]
            (2).全局使用: Vue.mixin(xxx)
#
## 六.插件
    功能: 用于增强Vue
    本质: 包含一个install方法的对象,install的第一个参数是Vue, 第二个以后是插件使
          用者传递的数据
    定义插件:
        对象: {
            install(){
                // 全局过滤器(可以在多个vue实例或组件上使用)
                Vue.filter("过滤器名",{...})
                
                //全局指令
                Vue.directive('指令名',function(element,binding){...})
                
                //定义全局混入
                Vue.mixin({...})
                
                //给Vue的原型上配置函数
                Vue.prototype.hello = ()=>{...}
                    }
        }
    使用插件:
        (1).在main.js中引入插件: import plugins from './plugins'
        (2).使用插件: Vue.use(plugins)
#
## 七.scoped
    功能: 解决多个组件使用相同样式名所带来的的问题, 避免冲突
    使用: <style scoped>
#
## 八.todoList案例总结
    1.组件化编码流程:
        (1).拆分静态组件: 组件要按照功能点拆分, 命名不要与html元素冲突
        (2).实现动态组件: 考虑好数据的存放位置, 数据是一个组件在用,还是一堆组件在用
            1).一个组件在用: 放在组件自身即可
            2).一堆组件在用: 放在它们共同的父组件上(状态提升)
        (3).实现交互: 从绑定事件开始
    2.props适用于:
        (1).父组件 ==> 子组件 通信
        (2).子组件 ==> 父组件 通信(要求父组件先传递一个函数给子组件)
    3.使用v-model时要切记: v-model绑定的值不能是props传递过来的值, 因为props是不可
      以修改的
    4.props传递过来的若是对象类型的值, 修改对象中的属性时Vue不会报错, 但不推荐这样
      做    
#
## 九.浏览器的本地存储
    localStorage与sessionStorage的区别:
        (1).相同点: localStorage和sessionStorage都有那四个API,即:
                (1).xxxStorage.setItem('key',value)  //添加数据(如果value是对象的话,可以使用JSON,stringify(value)来解析).
                (2).xxxStorage.getItem('key')   //获取数据(如果得到的值是一个json字符串,可以使用JSON.parse()将其解析成对象).
                (3).xxxStorage.removeItem('key') //删除数据
                (4).xxxStorage.clear()          //清空数据
        
        (2).不同点: localStorage需要调用removeItem或clear方法或用户 手动清除浏览器数据时才可以清除localStorage中存储的数据,而
                    sessionStorage中的数据在用户关闭浏览器时就会清除
#
## 十.优化todoList案例 略
#
## 十一.自定义事件
---
1. 一种组件间通讯的方式, 适用于: **子组件==>父组件**
2. 使用场景: A是父组件, B是子组件, B想给A传数据, 那么就要在A中给B绑定自定义事件(事件的回调在A中)
3. 绑定自定义事件:

    1.第一种方式: 在父组件中绑定自定义事件`<Dome @eventName='test'/>` 或 `<Dome v-on:eventName='test'/>`  
    2.在父组件中给子组件加上`ref`属性:  

        <Dome  ref='test'/>
        ....
        methods:{
            demo(){
                ...
            }
        },
        mounted(){
            this.$refs.test.$on('atguigu',this.dome)
        }

    3.若想让事件只触发一次, 可以使用`once`修饰符,或`$once`
4. 触发自定义事件: `this.$emit('atguigu',数据)`  
5. 解绑自定义事件: `this.$off('atguigu')`  
6. 组件也可以绑定原生DOM事件, 只是需要native修饰符  
7. 注意: 使用```this.$refs.test.$on```('事件名',回调)绑定自定义事件时, 回调要么写在methods中, 要么使用箭头函数, 不然this的指向会出问题
#
## 十二.全局事件总线
---
1. 一种组件间的通信方式, 适用于任意组件间的通信
2. 安装全局事件总线:

        new Vue({
            ...,
            beforeCreate(){
                this.prototype.$bus = this
            },
            ...
        })

3. 使用事件总线:
    
    1. 接收数据: A组件想要接收数据, 则在A组件中给$bus绑定自定义事件, 事件的回调在A组件自身
            
            methods:{
                demo(){
                    ...
                }
            },
            mounted(){
                this.$bus.$on('xxx',this.demo)
            }
    2. 提供数据: `this.$bus.$emit('xxx',数据)`  
4. 最好在beforeDestroy钩子中, 解绑当前组件用到的事件`this.$bus.$off('xxx')`
#
## 十三.消息订阅与发布
---

1. 消息订阅与发布是一种理念, 实现这种理念的方式有很多, 下面只 是其中一种
>(这种方式在任意的框架中都可以用)           
2. 使用步骤:

        (1).安装pubsub-js
        (2).在需要使用的地方导入pubsub-js:
            1>.在使用数据的地方订阅消息
            2>.在提供数据的地方发布消息
#
## 十四.nextTick
---
1. nextTick 用于解决函数未执行完就需要先解析页面的情况
2. 使用方式:
    ```
    this.$nextTick(()={
        页面解析后要执行的回调内容
    })
    ```

#
## 十五.vue封装的过渡与动画
---
1. 作用: 在插入, 更新或移除DOM元素时, 在合适的时候给元素添加样式类名.
2. 图示: ![图示](./src/assets/Z1X%5B4Y(912XF%7BH%60TL)U6L62.png)
3. 写法:

    1. 准备好样式:
        -    元素进入的样式

                1.v-enter:          进入的起点

                2.v-enter-active    进入的过程
                
                3.v-enter-to        进入的终点
        -    元素离开的样式

                1.v-leave           离开的起点

                2.v-leave-active    离开的过程

                3.v-leave-to        离开的终点

    2. 使用`<transition>`包裹要过渡的元素, 并配置name属性
    ```
        <transition name="pbb" appear> 
            <h2 v-show="status">{{ name }}</h2>
        </transition>
    ```
    3. 备注: 若有多个元素需要过渡, 则需要使用`<transition-group>`, 并且每个元素都需要指定key值
#
## 十六.axios的使用
---
1. 安装axios

        vue i axios 或 vue install axios
2. 在mian.js中使用axios(全局使用)

        //全局使用
        import axios from 'axios'
        Vue.use(axios)

        //局部使用 在需要发送ajax请求组件的script位置引入axios
        import axios from 'axios'
3. 使用

        1.发送get请求
            (1).不带参数的情况
            axiso.get(代理服务器路径).then(
                response => {
                    请求成功执行该模块代码..
                },
                error => {
                    请求失败执行该模块代码..
                }
            )
            (2).带参数的情况
            axiso.get(`代理服务器路径/${参数}`).then(
                response => {
                    请求成功执行该模块代码..
                },
                error => {
                    请求失败执行该模块代码..
                }
            )
        2.发送post请求
        axios({
            ...
            url: 代理服务器路径
            data:{参数}
            ...
        }).then(
            response => {
                请求成功执行该模块代码..
            },
            error => {
                请求失败执行该模块代码..
            }
        )
#
## 十七.vue脚手架配置代理
---
### 方法一
>在```vue.config.js```中添加如下配置
    
    devServer:{
        proxy:'http://localhost:5000'
    }
说明: 
    
1. 优点: 配置简单, 请求资源时直接转发给前端(8080)即可.

2. 缺点: 不能配置多个代理, 不能灵活控制走不走代理

3. 工作方式: 若按照上述配置代理, 当请求的前端资源不存在时, 那么该请求会转发给后端服务器(优先匹配前端资源)

### 方法二
>编写```vue.config.js```配置具体代理规则
    
    devServer:{
    proxy:{
      // 请求前缀信息, 匹配前缀信息的路径走代理, 不匹配的不走代理
      "/atguigu" : {
        target: 'http://localhost:5000',
        pathRewrite:{
          "^/atguigu":''  //重写路径发送到服务器
        }, 
        wb:true,          //用于支持webSocket
        changeOrigin:true //控制请求host信息 默认开启
      },
      "/demo" : {
        target: 'http://localhost:5001',
        pathRewrite:{
          "^/demo":''  //重写路径发送到服务器
        }, 
        wb:true,          //用于支持webSocket
        changeOrigin:true //控制请求host信息 默认开启
      }
    }
  }
说明:

1. 优点: 可以配置多个代理, 且可以灵活地控制是否走代理.

2. 配置略微繁琐, 请求资源时必须加前缀.
#
## 十八.使用resource发请求
---
1. 下载resource

        npm i vue-resource
2. 引用resource

        //在main.js中引入并使用resource
        import vueResource from 'vue-resource'
        Vue.use(vueResource)

        // 这样,vm和所有的vc身上都有了$http
3. 使用resource

        直接将axios替换为this.$http
        如:
        axios.get(url).then(res=>{
            ...
        })
        //替换为
        this.$http.get(url).then(res=>{
            ...
        })

        //平常用的多的还是axios
#
## 十九.插槽
1. 作用: 让父组件可以向子组件指定位置插入html结构, 也是一种组件间的通信方式, 适用于: 父组件==>子组件
2. 分类: 默认插槽, 具名插槽, 作用域插槽
3. 使用方式:
    
    1.默认插槽:

        父组件中:
                <Classify title="美食">
                html结构
                </Classify>
        子组件中:
                <div class="slot">
                    <h3>{{title}}分类</h3>
                    <!-- 定义插槽 -->
                    <slot></slot>
                </div>
    2.具名插槽:

        父组件中:
                <Classify title="美食">
                            <!-- 指定使用哪个个插槽 -->
                    <template slot="center">
                        html结构
                    </template>
                </Classify>
                <Classify title="美食">
                            <!-- 指定使用哪个个插槽 新的指定方式 -->
                    <template v-slot:center>
                        html结构
                    </template>
                </Classify>
        子组件中:
                <div class="slot">
                    <h3>{{title}}分类</h3>
                    <!-- 定义插槽, 并给插槽命名 -->
                    <slot name="centre"></slot>
                    <slot name="footer"></slot>
                </div>
    3.作用域插槽:
        
    1. 理解: 数据在组件的自身, 但根据数据生成的结构需要组件的使用者来决定. (games数据在Classify组件中, 但使用数据所遍历出来的结构由App组件决定)
    2. 具体编码:

            父组件中:
                    <Classify title="游戏" :games="games">
                        <!-- 作用域插槽, 必须使用template标签包裹. 支持结构赋值-->
                        <template scope="{games}">
                        <!-- 生成ul标签 -->
                            <ul>
                                <li v-for="(item,index) in games" :key="index">
                                {{ item }}
                                </li>
                            </ul>
                        </template>
                    </Classify>
                    <Classify title="游戏" :games="games">
                        <template scope="{games}">
                        <!-- 生成h4标签 -->
                            <h4 v-for="(item,index) in games" :key="index">
                                {{ item }}
                            </h4>
                        </template>
                    </Classify>

            子组件中:
                    <div class="slot">
                        <h3>{{title}}分类</h3>
                        <!-- 将games传递给插槽的使用者 -->
                        <slot :games="games"></slot>
                    </div>

                    <script>
                    export default {
                        props:['title'],
                        name:'Classify',
                        data() {
                            return {
                                games:['红色警戒','穿越火线','劲舞团','超级玛丽'],

                            };
                        }
                    }
                    </script>



    


                


