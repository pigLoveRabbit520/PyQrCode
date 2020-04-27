<template>
    <div id="app">
        <div class="container">
            <!--UPLOAD-->
            <form enctype="multipart/form-data" novalidate v-if="isInitial || isSaving">
                <h1>上传图片</h1>
                <div class="dropbox">
                    <input type="file" :name="uploadFieldName" :disabled="isSaving"
                           @change="filesChange($event.target.name, $event.target.files); fileCount = $event.target.files.length"
                           accept="image/*" class="input-file">
                    <p v-if="isInitial">
                        拖入图片<br> 或者点击这里上传图片
                    </p>
                    <p v-if="isSaving">
                        处理 {{ fileCount }} 图片...
                    </p>
                </div>
            </form>
            <!--SUCCESS-->
            <div v-if="isSuccess">
                <h1>二维码识别成功✓</h1>
                <p>
                    <a href="javascript:void(0)" @click="reset()">重新上传</a>
                </p>
            </div>
            <!--FAILED-->
            <div v-if="isFailed">
                <h2>网络错误</h2>
                <p>
                    <a href="javascript:void(0)" @click="reset()">重试</a>
                </p>
                <pre>{{ uploadError }}</pre>
            </div>

            <div style="margin-top: 20px">
                <table class="table table-bordered table-hover">
                    <thead>
                    <tr class="table-info">
                        <th scope="col">#</th>
                        <th width="30%" scope="col">图片</th>
                        <th scope="col">识别结果</th>
                        <th scope="col">操作</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(item, index) in recognizationResult">
                        <td class="align-middle">{{ index + 1 }}</td>
                        <td><img :src="item.img" alt="图片" width="320px"></td>
                        <td class="align-middle">
                            <span v-for="text in item.data" style="font-weight: bold; display: inline-block; margin-top: 8px;">
                                {{ text }} <br/>
                            </span>
                        </td>
                        <td class="align-middle">
                            <button type="button" class="btn btn-danger" @click="recognizationResult.splice(index, 1)">删除</button>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    // swap as you need
    //   import { upload } from './file-upload.fake.service'; // fake service
    import { upload } from './file-upload.service';   // real service
    import { wait, getLocalImage } from './utils';

    const STATUS_INITIAL = 0, STATUS_SAVING = 1, STATUS_SUCCESS = 2, STATUS_FAILED = 3;

    export default {
        name: 'app',
        data() {
            return {
                uploadedFiles: [],
                uploadError: null,
                currentStatus: null,
                uploadFieldName: 'file',
                recognizationResult: [],
            }
        },
        computed: {
            isInitial() {
                return this.currentStatus === STATUS_INITIAL;
            },
            isSaving() {
                return this.currentStatus === STATUS_SAVING;
            },
            isSuccess() {
                return this.currentStatus === STATUS_SUCCESS;
            },
            isFailed() {
                return this.currentStatus === STATUS_FAILED;
            }
        },
        methods: {
            reset() {
                // reset form to initial state
                this.currentStatus = STATUS_INITIAL;
                this.uploadedFiles = [];
                this.uploadError = null;
            },
            save(formData) {
                const files = formData.getAll('file')
                // upload data to the server
                this.currentStatus = STATUS_SAVING;

                upload(formData)
                    .then(wait(1500)) // DEV ONLY: wait for 1.5s
                    .then(body => {
                        getLocalImage(files[0]).then(img => {
                            this.recognizationResult.push({
                                img: img,
                                data: body.data,
                            })
                            this.currentStatus = STATUS_SUCCESS;
                        })
                    })
                    .catch(err => {
                        this.uploadError = err.response;
                        this.currentStatus = STATUS_FAILED;
                    });
            },
            filesChange(fieldName, fileList) {
                // handle file changes
                const formData = new FormData();

                if (!fileList.length) return;

                // append the files to FormData
                Array
                    .from(Array(fileList.length).keys())
                    .map(x => {
                        formData.append(fieldName, fileList[x], fileList[x].name);
                    });

                // save it
                this.save(formData);
            }
        },
        mounted() {
            this.reset();
        },
    }

</script>

<style lang="scss">
    .dropbox {
        outline: 2px dashed grey; /* the dash box */
        outline-offset: -10px;
        background: lightcyan;
        color: dimgray;
        padding: 10px 10px;
        min-height: 200px; /* minimum height */
        position: relative;
        cursor: pointer;
    }

    .input-file {
        opacity: 0; /* invisible but it's there! */
        width: 100%;
        height: 200px;
        position: absolute;
        cursor: pointer;
    }

    .dropbox:hover {
        background: lightblue; /* when mouse over to the drop zone, change color */
    }

    .dropbox p {
        font-size: 1.2em;
        text-align: center;
        padding: 50px 0;
    }

</style>