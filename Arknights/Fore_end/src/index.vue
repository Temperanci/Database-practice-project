<template>
    <div>
        <div id="app" align="center" class="p">
            <el-carousel :interval="5000" arrow="always" type="card" height="350px">
                <el-carousel-item v-for="(img,index) in imgList" :key="index">
                    <img v-bind:src="img.url">
                </el-carousel-item>
            </el-carousel>
        </div>
        <div align="center" >
            <el-row >
            <el-col >
                <el-card shadow="always">
                    欢迎来到企鹅物流数据统计！
                    <div> 当前本站总记录数目：
                    {{msg}}</div>
                </el-card>
            </el-col>

            </el-row>
        </div>

        <div align="center">
            <el-button type="primary" @click="submit()" >请登录</el-button>
        </div>

    </div>
</template>

<script>
    import main from './main';
    export default {
        data: function(){
            return {
                msg:localStorage.getItem('count'),
                dialogVisible:false,
                data:[],
                imgList:[
                    {url:require('./assets/qiewuliu.jpg')},
                    {url:require('./assets/chen.jpg')},
                    {url:require('./assets/yinhui.jpg')}
                ]
            }
        },
        created(){
            this.init();
        },
        methods: {
            init(){
                this.$http.post(main.url+"/Total_map/count",
                    {},
                    {
                        headers: {'Content-Type':'application/x-www-form-urlencoded'},
                        emulateJSON: true
                    }).then(
                    success=>{
                        this.data=success.data;
                       localStorage.setItem('count',this.data)
                    }
                );
            },

            submit(){
                this.$router.push({ path: '/login' });
            }
        }
    }
</script>

<style scoped>

    body{
    /* 设置背景渐变 */
    background-image: linear-gradient(to left,
    #FAACA8,#3cadeb);
    display: flex;
    justify-content: center;
    }


    .login-btn button{
        position: absolute;
        width: 50%;
        height: 50px;
        right: 10%;
        top: 20%;

    }
    .p{
        margin-top: 50px;
        margin-bottom: 50px;
    }
    .el-carousel__item h3 {
        width: 60%;
        color: #475669;
        font-size: 18px;
        opacity: 0.75;
        line-height: 300px;
        margin: 0;
    }

    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
        width: 60%;
    }

    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
        width: 60%;

    }

    .el-card{
        border-radius: 10px;
        position: absolute;
        left:50%;
        top:50%;
        transform: translate(-50%,-50%);

    }
    .el-button{
        background-image: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%);
        margin-top: 60px;
        width: 200px;
        border:none
    }
</style>
