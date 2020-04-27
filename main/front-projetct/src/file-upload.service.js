import * as axios from 'axios';

function upload(formData) {
    const url = `/decode`
    return axios.post(url, formData)
        // get data
        .then(x => x.data)
}

export { upload }