const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false  //关闭检查
  // 配置代理服务器 方式一
  // devServer:{
  //   proxy: 'http://localhost:5000' //服务器地址
  // },
  // 方式二
  // devServer:{
  //   proxy:{
  //     // 请求前缀信息, 匹配前缀信息的路径走代理, 不匹配的不走代理
  //     "/atguigu" : {
  //       target: 'http://localhost:5000',
  //       pathRewrite:{
  //         "^/atguigu":''  //重写路径发送到服务器
  //       }, 
  //       wb:true,          //用于支持webSocket
  //       changeOrigin:true //控制请求host信息 默认开启
  //     },
  //     "/demo" : {
  //       target: 'http://localhost:5001',
  //       pathRewrite:{
  //         "^/demo":''  //重写路径发送到服务器
  //       }, 
  //       wb:true,          //用于支持webSocket
  //       changeOrigin:true //控制请求host信息 默认开启
  //     }
  //   }
  // }
})
