<template>
    <div >
        <h2>{{ name }}</h2>
        <h2 >{{ address }}</h2>
        <h2>当前求和为:{{ msg }}</h2><br>
        <button @click="increment">点我msg++</button>

        <button @click="aleName">点我提示学校名</button>
        <button @click="aleAdress">点我提示学校地址</button>
        <button @click="unbind">点我解绑事件(1个)</button>
        <button @click="unbinds">点我解绑事件(多个个)</button>

        <button @click="destruction">点我销毁school组件</button>
    </div>
</template>

<script>
export default {  
    name:'Student',
    data() {
        return {
            name:'xxx大学',
            address:'正华大道',
            msg:0
        }
    },
    methods: {
        increment(){
            this.msg++
            console.log('increment执行了...')
        },
        aleName(){
            // console.log(this)
            this.$emit('atguigu',this.name)
        },
        aleAdress(){
            this.$emit('hint',this.address)
        },
        unbind(){
            this.$off('hint') //解绑一个自定义事件
        },
        unbinds(){
            this.$off(['atguigu','hint']) //解绑多个自定义事件
        },
        unbindAll(){
            this.$off()  //解绑所有自定义事件
        },
        //在vue以前的版本中调用$dostory方法销毁实例后,实例所绑定的自定义事件就不奏效了,但js的原生事件还能工作
        //在Vue 2.6.14及以上的版本中, 调用$dostory方法销毁实例后,自定义事件和原生的事件都不奏效了
        destruction(){
            this.$destroy() //销毁school实例
        }
    },
}
</script>

<style lang="less"> //预编译css,less支持嵌套编写  
   
    
</style>