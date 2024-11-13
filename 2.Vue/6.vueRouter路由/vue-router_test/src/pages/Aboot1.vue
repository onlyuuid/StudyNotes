<template>
    <div>
          <h3>显示关于Aboot的内容</h3>
    </div>
  </template>
  
  <script>
  export default {
        name:'Aboot1',
        // beforeDestroy(){
        //     console.log("##",'Aboot组件被销毁了...')
        // },
        // 两个新的生命周期钩子
        activated(){  //组件被激活的时候调用
            console.log("Aboot组件被激活了...")
        },
        deactivated(){  //组件失活的时候调用
            console.log("Aboot组件失活了...")
        }
  
  }
  </script>
  
  <style>
  
  </style>