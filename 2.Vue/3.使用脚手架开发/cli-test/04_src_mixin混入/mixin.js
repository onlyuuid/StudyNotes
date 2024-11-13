//配置共用混入
export  let mixin = {
    methods: {
        update() {
            alert(this.name);
        }
    },
    data() {
        return {
            a:89,
            b:60
        }
    },
    mounted() {
        console.log('mixin执行了...')
    },
}