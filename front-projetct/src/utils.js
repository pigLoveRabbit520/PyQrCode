// utils to delay promise
function wait(ms) {
    return (x) => {
        return new Promise(resolve => setTimeout(() => resolve(x), ms));
    };
}

function getLocalImage(file) {
    return new Promise((resolve, reject) => {
        const fReader = new FileReader()

        fReader.onload = () => {
            resolve(fReader.result);
        }

        fReader.readAsDataURL(file);
    })
}

export { wait, getLocalImage }