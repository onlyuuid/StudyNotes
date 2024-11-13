//定义插件
export default {
    install(Vue){
        // 全局过滤器(可以在多个vue实例或组件上使用)
        Vue.filter("trim",function(value){
            return value.slice(0,4);
        })
        //全局指令
        Vue.directive('fbind',function(element,binding){
            element.innerText = binding.value * 10
            console.log(binding)
        })
        //定义全局混入
        Vue.mixin({
            data() {
                return {
                    a:1,
                    b:2
                }
            },
        })
        //给Vue的原型上配置函数
        Vue.prototype.hello = ()=>{alert('李四')}
    }
}