<template>
  <div>
        <h2>学校名: {{ name }}</h2>
        <h2>学校地址:  {{ address }}</h2>
        <h2>学生名:{{ studentName }}</h2>
  </div>
</template>

<script>
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
        getStudentName(studentName){
            console.log('收到了学生组件传递过来的数据:'+studentName)
            this.studentName = studentName
        }
    },
    mounted() {
        //挂载完时绑定事件              //this一开始是vm, 后来是School的vc
        this.$bus.$on('getStudentName',this.getStudentName)
    },
}
</script>

<style>

</style>