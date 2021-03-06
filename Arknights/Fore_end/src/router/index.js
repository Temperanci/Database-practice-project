import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            component: resolve => require(['../index.vue'], resolve)
        },
        {
            path: '/login',
            component: resolve => require(['../login.vue'], resolve)
        },
        {
            path: '/admin',
            component: resolve => require(['../admin/common/Home.vue'], resolve),
            children:[
                {
                    path: '/account_admin',//用户管理页面
                    component: resolve => require(['../admin/page/account_admin.vue'], resolve)
                },
                {
                    path: '/map_admin1',//按素材查询物品掉落的页面
                    component: resolve => require(['../admin/page/map_admin1.vue'], resolve)
                },
                {
                    path: '/map_admin2',//按作战查询物品掉落的页面
                    component: resolve => require(['../admin/page/map_admin2.vue'], resolve)
                },
                {
                    path: '/Upload_record',
                    component: resolve => require(['../admin/page/Upload_record'], resolve)
                }
            ]
        }
    ]
})
