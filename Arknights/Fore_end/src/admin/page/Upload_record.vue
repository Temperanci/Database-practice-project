<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-setting"></i> 作战汇报</el-breadcrumb-item>

            </el-breadcrumb>
        </div>

        <div class="form-box">

            <el-row><el-col>
            <el-form :model="form" :rules="rules" ref="form" label-width="80px">
                <el-form-item label="选择地图" prop="type">
                    <el-select v-model="form.type" placeholder="请选择地图">
                         <el-option
                             v-for="item in maps"
                             :key="item.value"
                             :label="item.label"
                                :value="item.value">
                         </el-option>
                    </el-select>
                </el-form-item>

            </el-form></el-col>

        </el-row>
        </div>







        <div>

            <el-checkbox-group v-model="checkboxGroup1">
                <el-checkbox-button v-for="item in items" :label="item" :key="item" >{{item}}</el-checkbox-button>
            </el-checkbox-group>

        </div>



        <div style="margin-top: 20px">
           <el-button type="primary" @click="addnew()" align="center">添加新记录</el-button>
        </div>



    </div>
</template>

<script>
    import main from "../../main";
    const itemOptions = [ '源岩', '固源岩', '双酮', '酯原料','代糖','异铁碎片',
        '破损装置', '赤金','初级作战记录','聚酸酯', '碳', '技巧概要·卷1','装置'];
    export default {
    data: function(){
        return {
            data:[],
            maps:[{value: 1, label: "1-1 孤岛"},{value: 2, label: "1-2 蔓延"},{value: 3, label: "1-3 狂奔"},
                {value: 4, label: "1-4 先兆"},{value: 5, label: "1-5 麻痹"},{value: 6, label: "1-6 灾难"},
                {value: 7, label: "1-7 暴君"},{value: 8, label: "1-8 意志"},{value: 9, label: "1-9 溃散"}
            ],
            items: itemOptions,

            checkboxGroup1: [],
                form:{

                    type:''
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

            },

            updatetotalmap(){//把对应地图的totalmap数据更新
                this.$http.post(main.url+"/Total_map/update",
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

            addnew(form,checkboxGroup1){ //添加新纪录

                var isChecked=new Array(13)//定义数组存储checkbox是否选中
                for(var a=0;a<13;a++)
                    isChecked[a]=0;

                for(var a=0;a<this.checkboxGroup1.length;a++)//如果选中，即checkbox里能找到，把数组值设为1
                {
                    isChecked[itemOptions.indexOf(this.checkboxGroup1[a])]=1;

                }

                if(this.form.type==="")
                    this.$message({type: 'error', message: '请选择地图！'});


                else{
                    localStorage.setItem('map_num',this.form.type);
                    this.$http.post(main.url+"/user_map/add",
                        {
                            'user_id': localStorage.getItem('id'),
                            'map_num': this.form.type,
                            'item1': isChecked[0],
                            'item2': isChecked[1],
                            'item3': isChecked[2],
                            'item4': isChecked[3],
                            'item5': isChecked[4],
                            'item6': isChecked[5],
                            'item7': isChecked[6],
                            'item8': isChecked[7],
                            'item9': isChecked[8],
                            'item10': isChecked[9],
                            'item11': isChecked[10],
                            'item12': isChecked[11],
                            'item13': isChecked[12]
                        },
                        {
                            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                            emulateJSON: true
                        }).then(
                        success => {
                            this.$message({type: 'success', message: '上传作战记录成功，情报已更新'});
                            this.form = {

                                type:''
                            };
                            this.init();
                            this.updatetotalmap();

                        }
                    );

                }
            },


        }
    }
</script>
<style>
.a{
    margin-bottom: 20px;

}
</style>
