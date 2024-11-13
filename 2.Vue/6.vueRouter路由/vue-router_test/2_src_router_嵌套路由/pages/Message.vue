<template>
  <div>
        <ul>
            <li v-for="item in messageList" :key="item.id">
                {{ item.title }}
            </li>
        </ul>
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

<style>

</style>