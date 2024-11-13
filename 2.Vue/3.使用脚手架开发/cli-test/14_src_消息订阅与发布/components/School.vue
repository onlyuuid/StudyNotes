<template>
  <div>
        <h2>学校名: {{ name }}</h2>
        <h2>学校地址:  {{ address }}</h2>
        <h2>学生名:{{ studentName }}</h2>
  </div>
</template>

<script>   
    /*
            消息订阅与发布
                1.消息订阅与发布是一种理念, 实现这种理念的方式有很多, 下面只是其中一种
                    (这种方式在任意的框架中都可以使用)
                2.使用步骤:
                    (1).安装pubsub-js
                    (2).在需要使用的地方导入pubsub-js:
                        1>.在使用数据的地方订阅消息
                        2>.在提供数据的地方发布消息
    */
// 导入pubsub-js
import pubsub from 'pubsub-js' 
export default {
    name:'School',
    data(){
        return {
            name: '未来中学',
            address:'正华大道',
            studentName:''
        }
    },
    methods: {
        getStudentName(msgName,studentName){
            console.log('收到了学生组件传递过来的数据:'+studentName,'消息名:'+msgName)
            this.studentName = studentName
        }
    },
    mounted() {
        //挂载完时绑定事件     this.$bus = vm       
        // this.$bus.$on('getStudentName',this.getStudentName)
        // console.log(this.$bus)

        // 挂载完时订阅消息       
        // pubsub.subscribe("demo",(msgName,data)=>{
        //     console.log("School收到了Student传递过来的信息:"+msgName,data)
        // })
        this.pubid = pubsub.subscribe("demo",this.getStudentName)
    },
    beforeDestroy() {
        // 取消订阅
        pubsub.unsubscribe(this.pubid)
    },
}
</script>

<style>

</style>