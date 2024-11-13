//与人员列表相关的配置
import axiso from 'axios'
import {nanoid} from 'nanoid'

export default {
    //开启命名空间
    namespaced:true,
    actions:{
        addWang(context,value){
            if(value.name.indexOf('王') === 0){
                context.commit('ADD_WANG',value)
            }
        },
        addPersonServer(context){
            axiso.get('https://api.uixsj.cn/hitokoto/get?type=social').then(
                res => {
                    context.commit('ADD_PERSON_SERVER',{id:nanoid(),name:res.data})
                    console.log("服务器数据添加成功")
                },
                error => {
                    console.log('失败',error.message)
                }
            )
            
        }
    },
    mutations:{
        ADD_PERSON(state,value){
            if(value.name === ''){
                alert("姓名不能为空!")
                return false
            }
            // 添加人员信息
            console.log("ADD_PERSON被执行了...",value)
            state.personList.unshift(value)
        },
        ADD_WANG(state,value){
            // 添加姓王的人员信息
            state.personList.unshift(value)
        },
        ADD_PERSON_SERVER(state,value){
            state.personList.unshift(value)
        }
    },
    state:{
         //人员列表
        personList:[
            // 初始人员信息
            {id:'001',name:'张三'}
    ]
    },
    getters:{
        //获取所有人员的姓
        connation(state){
           const arr = []
           state.personList.forEach(element => {
            arr.unshift(element.name.substring(0,1)) 
            
           });
           return arr
        }
    }
}