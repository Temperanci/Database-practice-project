<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-setting"></i> 查询</el-breadcrumb-item>
                <el-breadcrumb-item>按素材</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <el-row :gutter="12">

            <el-col :span="14">
                <div>
                    <el-card  shadow="hover">
                        <div slot="header" class="clearfix">
                            <span>推荐地图</span>
                        </div>
                    <el-table :data="data"  stripe  style="width:100%" >
                        <el-table-column label="地图名称" prop="map_name" width="250px" ></el-table-column>
                        <el-table-column label="掉落率" prop="prob_item" width="150px" ></el-table-column>
                        <el-table-column label="记录次数" prop="Count" width="230px" ></el-table-column>

                    </el-table>
                    </el-card>
                    <br />
                    <el-button type="primary" @click="QueryByItem()" align="center">查询指定素材</el-button>
                </div>
            </el-col>
            <el-col :span="8" >
                <el-row :gutter="12">
                <el-card  shadow="hover">
                    <div slot="header" class="clearfix">
                        <span>快速上手</span>
                    </div>
                    点击下方按钮，选择你需要的素材查询<br/><br/>
                    企鹅物流将会为您推荐合适的地图
                </el-card>
                </el-row>

            </el-col>
        </el-row>





        <el-dialog
            width="30%"
            title="查询指定物品"
            :visible.sync="dialogFormVisibleed1">
            <div class="form-box">
                <el-form :model="form" :rules="rules" ref="form" label-width="150px">

                    <el-form-item label="选择物品" prop="type">
                        <el-select v-model="form.type" placeholder="请选择物品">
                            <el-option
                                v-for="item in options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item style="text-align: center" >
                        <el-button @click="dialogFormVisibleed1 = false" >取消</el-button>
                        <el-button type="primary" @click="queryitem(form)">查询</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import main from "../../main";
export default {
    data: function(){
        return {
            data:[],
            options:[{value: 1, label: "源岩"},{value: 2, label: "固源岩"},{value: 3, label: "双酮"},
                {value: 4, label: "酯原料"},{value: 5, label: "代糖"},{value: 6, label: "异铁碎片"},
                {value: 7, label: "破损装置"},{value: 8, label: "赤金"},{value: 9, label: "初级作战记录"},
                {value: 10, label: "聚酸酯"},{value: 11, label: "碳"},{value: 12, label: "技巧概要·卷1"},
                {value: 13, label: "装置"}],
            dialogFormVisibleed:false,
            dialogFormVisibleed1:false,
            form:{

                type:''
            },
            rules:{

                type:[
                    {required:true,message:'请设置权限',trigger:'blur'}
                ]
            },


        }
    },
    created(){
        if(localStorage.getItem('username')===""){
            this.$router.replace('/login')
        }else{this.init();}
    },
    methods:{
        init(){
            this.$http.post(main.url+"/Total_map/listmaps",
                {'item_num': localStorage.getItem('item_num')},
                {
                    headers: {'Content-Type':'application/x-www-form-urlencoded'},
                    emulateJSON: true
                }).then(
                success=>{
                    this.data=success.data;

                }
            );
        },



        QueryByItem(){this.dialogFormVisibleed1=true},
        queryitem(form){ //查询指定物品掉率
           if(this.form.type==="")
                this.$message({type: 'error', message: '请选择物品！'});
            else{
               localStorage.setItem('item_num',this.form.type);
                this.$http.post(main.url+"/Total_map/listmaps",
                    {
                        /*'uid': localStorage.getItem('id'),*/

                        'item_num': this.form.type
                    },
                    {
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                        emulateJSON: true
                    }).then(
                    success => {
                        this.$message({type: 'success', message: '查询成功'});
                        this.form = {

                            type:''
                        };

                        this.init();
                    }
                );
                this.dialogFormVisibleed1 = false;
            }
        }

    }
}
</script>
<style>

</style>
