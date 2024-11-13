<template>
  <div>
        <ul>
            <li v-for="item in messageList" :key="item.id">
                {{ item.title }}
            </li>
        </ul>
        <div class="navi_3">
            <!-- 跳转并携带参数, to的字符串写法 -->
            <router-link :to="`/home/message/detail?title=你好`">
                <span>发送问候语</span>
            </router-link>
            <router-link :to="`/home/message/detail?title=生日快乐`">
                <span>发送祝福语</span>
            </router-link> 
            
             <!-- 跳转并携带参数, to的对象写法 -->
            <router-link :to="{
                name:'xiangqing',       //命名路由:即,给路由规则取名字,可以直接通过路由名使用跳转
                query:{                 //这种方式要求to必须配置成对象的形式
                    title:'非常感谢!'
                }
            }">
                <span>发送感谢语</span>
            </router-link>  
        </div>
        <span>
            <router-view></router-view>
        </span>
  </div>
</template>

<script>
export default {
    name:'Message',
    data() {
        return {
            messageList:[
                {
                    id:'001',
                    title:'怨犹不会让困难减少, 但是乐观会让人变得强大'
                },
                {
                    id:'002',
                    title:'弱小和无知不是生存的障碍, 傲慢才是'
                },
                {
                    id:'003',
                    title:'人生没有意义, 但找寻人生意义这件事有意义'
                }

            ]
        }
    },
}
</script>

<style scpoed>
    .navi_3{
        display: inline-block;
        border-bottom: 2px solid rgb(171, 171, 171);
    }
    .navi_3 span{
        margin:20px
    }

    .active{
        color: rgb(63, 143, 247);
    }
</style>