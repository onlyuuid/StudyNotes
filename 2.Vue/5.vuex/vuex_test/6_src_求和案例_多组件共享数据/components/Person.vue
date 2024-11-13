<template>
  <div class="person">
    <h4 style="color:red">computed组件的求和为:{{ number }}</h4>
    <h1>人员列表</h1>
    <input type="text" v-model="person">
    <button @click="addPerson">添加</button>
    <ol>
        <li v-for="p in personList">
            {{ p.name }}
        </li>
    </ol>
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
    methods: {
        addPerson(){
            let personObj = {id:nanoid(),name:this.person}
            this.$store.commit('ADD_PERSON',personObj)
            this.person = ''
        }
    },
    computed:{
        personList(){
            return this.$store.state.personList
        },
        number(){
            return this.$store.state.number
        }
    }

}
</script>

<style>

</style>