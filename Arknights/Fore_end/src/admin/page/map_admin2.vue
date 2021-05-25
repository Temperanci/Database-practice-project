<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-setting"></i> 查询</el-breadcrumb-item>
                <el-breadcrumb-item>按作战</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div>
            <el-table :data="data" border style="width: 100%" ref="multipleTable" >
                <el-table-column label="地图名称" prop="map_name" width="100px" ></el-table-column>
                <el-table-column label="源岩" prop="prob_item1" width="100px" ></el-table-column>
                <el-table-column label="固源岩" prop="prob_item2" width="100px" ></el-table-column>
                <el-table-column label="双酮" prop="prob_item3" width="100px" ></el-table-column>
                <el-table-column label="酯原料" prop="prob_item4" width="100px" ></el-table-column>
                <el-table-column label="代糖" prop="prob_item5" width="100px" ></el-table-column>
                <el-table-column label="异铁碎片" prop="prob_item6" width="100px" ></el-table-column>
                <el-table-column label="破损装置" prop="prob_item7" width="100px" ></el-table-column>
                <el-table-column label="赤金" prop="prob_item8" width="100px" ></el-table-column>
                <el-table-column label="初级作战记录" prop="prob_item9" width="200px" ></el-table-column>
                <el-table-column label="聚酸酯" prop="prob_item10" width="100px" ></el-table-column>
                <el-table-column label="碳" prop="prob_item11" width="70px" ></el-table-column>
                <el-table-column label="技巧概要·卷1" prop="prob_item12" width="200px" ></el-table-column>
                <el-table-column label="记录次数" prop="Count" width="200px" ></el-table-column>

            </el-table>
            <br />
            <el-button type="primary" @click="QueryByMap()" align="center">查询指定地图</el-button>
        </div>

        <el-dialog
            width="30%"
            title="查询指定地图"
            :visible.sync="dialogFormVisibleed1">
            <div class="form-box">
                <el-form :model="form" :rules="rules" ref="form" label-width="150px">

                    <el-form-item label="选择地图" prop="type">
                        <el-select v-model="form.type" placeholder="请选择地图">
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
                        <el-button type="primary" @click="querymap(form)">查询</el-button>
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
            options:[{value: 1, label: "1-1 孤岛"},{value: 2, label: "1-2 蔓延"},{value: 3, label: "1-3 狂奔"},
                {value: 4, label: "1-4 先兆"},{value: 5, label: "1-5 麻痹"},{value: 6, label: "1-6 灾难"},
                {value: 7, label: "1-7 暴君"},{value: 8, label: "1-8 意志"},{value: 9, label: "1-9 溃散"}
               ],
            dialogFormVisibleed:false,
            dialogFormVisibleed1:false,
            form:{

                type:''
            },
            rules:{

                type:[
                    {required:true,message:'请设置权限',trigger:'blur'}
                ]
            }
        }
    },
    created(){
        if(localStorage.getItem('username')===""){
            this.$router.replace('/login')
        }else{this.init();}
    },
    methods:{
        init(){
            this.$http.post(main.url+"/Total_map/listItems",
                {'map_num': localStorage.getItem('map_num')},
                {
                    headers: {'Content-Type':'application/x-www-form-urlencoded'},
                    emulateJSON: true
                }).then(
                success=>{
                    this.data=success.data;

                }
            );
        },



        QueryByMap(){this.dialogFormVisibleed1=true},
        querymap(form){ //查询指定地图素材掉率
            if(this.form.type==="")
                this.$message({type: 'error', message: '请选择地图！'});
            else{
                localStorage.setItem('map_num',this.form.type);
                this.$http.post(main.url+"/Total_map/listItems",
                    {
                        /*'uid': localStorage.getItem('id'),*/

                        'map_num': this.form.type
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
