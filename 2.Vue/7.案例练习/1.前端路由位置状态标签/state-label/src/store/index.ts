import { defineStore } from 'pinia'


const store = defineStore("label",{
        state: () => {
            return {
                manuList:[
                    {title:'首页',path:'/home',show:0}
                ]
            }
        },
        actions: {
            
        }
        
    }
)

export default store