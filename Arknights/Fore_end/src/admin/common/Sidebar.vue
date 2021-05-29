<template>
    <div class="sidebar" >
        <el-menu :default-active="onRoutes" class="el-menu-vertical-demo"  unique-opened router>


            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index" >

                        <template slot="title"><i :class="item.icon"></i>
                            {{ item.title }}</template>
                        <el-menu-item v-for="(subItem,i) in item.subs" :key="i" :index="subItem.index">{{ subItem.title }}
                        </el-menu-item>

                    </el-submenu>
                </template>
                <template v-else >
                    <el-menu-item :index="item.index">
                        <i :class="item.icon"></i>{{ item.title }}
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script>
export default {
    data() {
        return {
            items:
                [
                    {
                        icon: 'el-icon-setting',
                        index: 'account_admin',
                        title: '用户管理',
                    },
                    {
                        icon: 'el-icon-setting',
                        index: 'map_admin1',
                        title: '按素材查询物品掉率',
                    },
                    {
                        icon: 'el-icon-setting',
                        index: 'map_admin2',
                        title: '按作战查询物品掉率',
                    },
                    {
                        icon: 'el-icon-setting',
                        index: 'Upload_record',
                        title: '单次作战记录汇报',
                    }
                ]
        }
    },
    created(){
        if(localStorage.getItem('username')===""){
            this.$router.replace('/login');
        }
    },
    computed:{
        onRoutes(){
            return this.$route.path.replace('/','');
        }
    }
}
</script>

<style scoped>
.sidebar{
    display: block;
    position: absolute;
    width: 250px;
    left: 0;
    top: 70px;
    bottom:0;
    background-color:#a6c0fe;
}
.sidebar > ul {
    height:100%;
}
</style>
