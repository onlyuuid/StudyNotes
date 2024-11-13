<template>
    <div>
          <h3>显示关于Aboot的内容</h3>
    </div>
  </template>
  
  <script>
  export default {
      name:'Aboot1',
      beforeDestroy(){
        console.log("##",'Aboot组件被销毁了...')
    }
  
  }
  </script>
  
  <style>
  
  </style>