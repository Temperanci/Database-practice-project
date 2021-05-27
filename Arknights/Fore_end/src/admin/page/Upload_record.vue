<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-setting"></i> 作战汇报</el-breadcrumb-item>

            </el-breadcrumb>
        </div>

        <div>  <el-checkbox-group
            v-model="checkedCities"
            :min="1"
            :max="8">
            <el-checkbox v-for="city in cities" :label="city" :key="city">{{city}}</el-checkbox>
             </el-checkbox-group>
        </div>

        <div>
           <el-button type="primary" @click="addfavorite()" align="center">添加新记录</el-button>
        </div>


        <el-dialog
            width="30%"
            title="添加收藏"
            :visible.sync="dialogFormVisibleed1">
            <div class="form-box">
                <el-form :model="form" :rules="rules" ref="form" label-width="150px">
                    <el-form-item label="网站名称" prop="wname">
                        <el-input v-model="form.wname" placeholder="请输入网站名称"></el-input>
                    </el-form-item>
                    <el-form-item label="网站地址" prop="wurl">
                        <el-input v-model="form.wurl" placeholder="请输入网站地址"></el-input>
                    </el-form-item>
                    <el-form-item label="权限" prop="type">
                        <el-select v-model="form.type" placeholder="请设置权限">
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
                        <el-button type="primary" @click="addnew(form)">添加</el-button>
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
                options:[{value: 0, label: "公开"},{value: 1, label: "私有"}],
                dialogFormVisibleed:false,
                dialogFormVisibleed1:false,
                form:{
                    id: '',
                    wname:'',
                    wurl:'',
                    type:''
                },
                rules:{
                    wname:[
                        {required:true,message:'请输入网站名称',trigger:'blur'}
                    ],
                    wurl:[
                        {required:true,message:'请输入网站地址',trigger:'blur'}
                    ],
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
                this.$http.post(main.url+"/favorite/list",
                    {'uid': localStorage.getItem('id')},
                    {
                        headers: {'Content-Type':'application/x-www-form-urlencoded'},
                        emulateJSON: true
                    }).then(
                    success=>{
                        this.data=success.data;
                        for(let i=0;i<this.data.length;i++){
                            if(this.data[i].type===0)
                                this.data[i].type = "公开";
                            else
                                this.data[i].type = "私有";
                        }
                    }
                );
            },


            addfavorite(){this.dialogFormVisibleed1=true},
            addnew(form){ //添加新收藏
                if(this.form.wname==="")
                    this.$message({type: 'error', message: '网站名称！'});
                else if(this.form.wurl==="")
                    this.$message({type: 'error', message: '网站地址不能为空！'});
                else if(this.form.type==="")
                    this.$message({type: 'error', message: '请设置权限！'});
                else{
                    this.$http.post(main.url+"/favorite/add",
                        {
                            'uid': localStorage.getItem('id'),
                            'wname': this.form.wname,
                            'wurl': this.form.wurl,
                            'type': this.form.type
                        },
                        {
                            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                            emulateJSON: true
                        }).then(
                        success => {
                            this.$message({type: 'success', message: '添加成功'});
                            this.form = {
                                id: '',
                                wname:'',
                                wurl:'',
                                type:''
                            };
                            this.init();
                        }
                    );
                    this.dialogFormVisibleed1 = false;
                }
            },

        }
    }
</script>
