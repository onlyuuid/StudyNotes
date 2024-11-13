<template>
  <div class="person">
    <h4 style="color:red">computed组件的求和为:{{ number }}</h4>
    <h1>人员列表</h1>
    <input type="text" v-model="person">
    <button @click="addPerson">添加</button>
    <button @click="addWang">添加姓王的人员信息</button>
    <button @click="addPersonServer">从服务器添加人员信息</button>
    <ol>
        <li v-for="p in personList">
            {{ p.name }}
        </li>
    </ol>
    <h2>获取所有人员的姓:{{ connation }}</h2>
  </div>
</template>

<script>
import {nanoid} from 'nanoid'  //需要使用分别引入
export default {
    name:'Person',
    data() {
        return {
            person:''
        }
    },
    // vuex模块配置中, 通过人工编写方法操作或获取store中的数据
    computed:{
        personList(){
            return this.$store.state.personAboot.personList
        },
        number(){
            return this.$store.state.computedAboot.number
        },
        //加工后的名字
        connation(){
            return this.$store.getters["personAboot/connation"]
        },
        
    },
    methods: {
        addPerson(){
            let personObj = {id:nanoid(),name:this.person}
            this.$store.commit('personAboot/ADD_PERSON',personObj)
            this.person = ''
        },
        addWang(){
            let personWang = {id:nanoid(),name:this.person}
            this.$store.dispatch('personAboot/addWang',personWang)
            this.person = ''
        },
        addPersonServer(){
            this.$store.dispatch('personAboot/addPersonServer')
            this.person = ''
        }
    },
   

}
</script>

<style>

</style>