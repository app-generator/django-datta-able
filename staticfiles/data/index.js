export let myData = {}
export let modelName = ''

export const setData = (headings , data,isDate) => {
    myData = {
        headings: headings,
        data: data,
        isDate: isDate,
    }
}

export const setModelName = (data) => {
    modelName = data
}