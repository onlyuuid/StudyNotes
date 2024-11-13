//与计算相关的配置
export default {
    //开启命名空间
    namespaced:true,
    actions:{
        jiaOdd(context,value){
            console.log('处理了一些事情...jiaOdd')
            context.dispatch('demo1',value)
        },
        demo1(context,value){
            console.log('处理了一些事情...demo1')
            context.dispatch('demo2',value)
        },
        demo2(context,value){
            console.log('处理了一些事情...demo2')
            // 为奇数再加
            if(context.state.number % 2){
                context.commit('JIA',value)
            }
        },
        jiaWait(context,value){
            // 等一等再加
            setTimeout(() => {
                context.commit('JIA',value)
            }, 1000);
        }
    },
    mutations:{
        JIA(state,value){
            console.log("mutations中的JIA被调用了")
            state.number += value
        },
        JIAN(state,value){
            state.number -= value
        },
    },
    state:{
        number:0,  //当前的和
        school:'尚硅谷',
        subject:'前端',
    },
    getters:{
        bigNumber(state){
            return state.number * 10 
        }
    }
}