import {modelName, myData} from "../../data/index.js";
import {formConstructor, formTypes} from "../form/index.js";

const editBtn   = `<i class="btn-outline-primary edit bi bi-pencil-square" data-bs-toggle="modal" data-bs-target="#exampleModal"></i>`
const removeBtn = `<i class="btn-outline-danger remove bi bi-eraser"></i>`

const toastLive = document.getElementById('liveToast')
const toast     = new bootstrap.Toast(toastLive)

const setToastBody = (text,type) => {
    document.querySelector('.toast-body').innerHTML = text

    toastLive.className =  type === 'success'
        ?
    toastLive.className.replace(/bg-.+/,'bg-success')
        :
    toastLive.className.replace(/bg-.+/,'bg-danger')

}

// Add Button + Events
export const addController = (formType) => {

    const myModalEl = document.getElementById('exampleModal');
    const modal = new bootstrap.Modal(myModalEl , {})

    const addContainer = document.createElement('div')

    const addBtn = document.createElement('button')
    addBtn.className = 'btn btn-primary mx-1'
    addBtn.textContent = '+'
    addBtn.id = 'add'

    addContainer.appendChild(addBtn)

    document.querySelector('.dropdown').insertBefore(addContainer ,
        document.querySelector('#dropdownMenuButton1')
    )

    addBtn.addEventListener('click' , (e) => {
        formType = formTypes.ADD
        formConstructor(formTypes.ADD)
        modal.show()
    })
}

function search_action() {

    const searchValue = document.querySelector('#search').value

    const searchParams = new URLSearchParams(window.location.search)
    searchParams.set("search", searchValue);
    searchParams.set("page", '1');
    const newRelativePathQuery = window.location.pathname + '?' + searchParams.toString();
    window.history.pushState({},'',newRelativePathQuery)
    location.reload()
}

// Search Box + Events
export const search = () => {

    const searchContainer     = document.createElement('div')
    searchContainer.className = 'd-flex'
    searchContainer.id        = 'search-container'
    
    const searchInput         = document.createElement('input')
    searchInput.className     = 'form-control mx-1'
    searchInput.setAttribute('placeholder', 'search...')
    searchInput.setAttribute('id','search')
    searchInput.setAttribute('type','text')

    const searchBtn           = document.createElement('button')
    searchBtn.className       = 'btn btn-primary'
    searchBtn.setAttribute('id','search-btn')
    searchBtn.innerHTML       = '<i class="bi bi-search"></i>'

    searchContainer.appendChild(searchInput)
    searchContainer.appendChild(searchBtn)

    document.querySelector('.dataTable-top').appendChild(searchContainer)

    // Trigger Search on ENTER
    document.querySelector('#search').addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            search_action();
        }    
    })

    // Trigger Search on Button Click
    document.querySelector('#search-btn').addEventListener('click',() => {
        search_action();
    })
}

// Unused 
export const middleContainer = (dataTable) => {

    const middleContainer     = document.createElement('div')
    middleContainer.className = 'd-flex'
    middleContainer.id        = 'middle-container'

    const span       = document.createElement('span')
    span.className   = 'mx-1'
    span.id          = 'span1'
    span.textContent = 'Dummy'

    middleContainer.appendChild(span)

    document.querySelector('.dataTable-top').insertBefore(middleContainer, document.querySelector('#search-container'));
}

// Filter Combo (layout + Events)
export const columnsManage = (dataTable) => {

    const dropDown     = document.createElement('div')
    dropDown.className = 'dropdown d-flex'
    dropDown.id        = 'filter-container'

    const button       = document.createElement('button')
    button.className   = 'btn dropdown-toggle'
    button.id          = 'dropdownMenuButton1'
    button.setAttribute( 'data-bs-toggle' , 'dropdown')
    button.textContent = 'Filter'

    dropDown.appendChild(button)

    const ul           = document.createElement( 'ul')
    ul.className       = 'dropdown-menu'

    myData.headings.forEach((d,i) => {

        const li          = document.createElement('li')
        li.className      = 'dropdown-item'

        const check       = document.createElement('input')
        check.className   = 'form-check-input'
        check.id          = d
        check.setAttribute('type','checkbox')

        const label       = document.createElement('label')
        label.className   = 'form-check-label mx-1'
        label.textContent = d

        li.appendChild(check)
        li.appendChild(label)

        ul.appendChild(li)
    })

    dropDown.appendChild(ul)
    document.querySelector('.dataTable-top').insertBefore(dropDown, document.querySelector('#search-container'));

    dropDown.addEventListener('change' , (e) => {
        if (e.target.nodeName === 'INPUT') {

            const id = myData.headings.indexOf(e.target.closest('input').id)
            if (e.target.closest('input').checked) {
                dataTable.columns().hide([parseInt(id)])
                const hideColumns = JSON.parse(localStorage.getItem('hideColumns')) || []
                localStorage.setItem('hideColumns' , JSON.stringify([...hideColumns , e.target.closest('input').id]))
            } else {
                dataTable.columns().show([parseInt(id)])
                const hideColumns = JSON.parse(localStorage.getItem('hideColumns')) || []
                localStorage.setItem('hideColumns' , JSON.stringify(hideColumns.filter(d => d !== e.target.closest('input').id)))
            }

        }
    })
}

// Export layout
export const exportController = (dataTable) => {

    const exportContainer     = document.createElement('div')
    exportContainer.id        = 'export-container'
    exportContainer.className = 'mx-1'

    const pdfImg = document.createElement('img')
    pdfImg.setAttribute('src',"/static/src/images/pdf.svg")
    pdfImg.id = 'pdf'

    const csvImg = document.createElement('img')
    csvImg.setAttribute('src',"/static/src/images/csv.svg")
    csvImg.id = 'csv'

    /*
    const excelImg = document.createElement('img')
    excelImg.setAttribute('src',"/static/src/images/excel.svg")
    excelImg.id = 'excel'
    */

    exportContainer.addEventListener('click' , (e) => {
        if (e.target.nodeName === 'IMG' ) {
            exportData(dataTable , e.target.id )
        }
    })

    exportContainer.appendChild(pdfImg)
    exportContainer.appendChild(csvImg)

    //exportContainer.appendChild(excelImg)

    document.querySelector('.dropdown').insertBefore(exportContainer ,
        document.querySelector('#dropdownMenuButton1')
    )

    //document.querySelector('.dropdown').appendChild(exportContainer);
}

// Action: Export
export const exportData = (dataTable, type) => {

    const searchParam = new URLSearchParams(window.location.search).get('search') || ''
    
    const hiddenColumns = myData.headings.filter((d,i) => !dataTable.columns().visible(i))

    fetch (`/datatb/${modelName}/export/`,
        {method: 'POST',body: JSON.stringify({
                search: searchParam,
                hidden_cols: hiddenColumns,
                type: type === 'excel' ? 'xlsx' : type
            })})
        .then((response) => {
            if(!response.ok) {
                return response.text().then(text => { throw new Error(text) })
            } else {
                return response.json()
            }
        })
        .then((result) => {
             let a      = document.createElement("a");
             a.href     = `data:application/${result.file_format};base64,${result.content}`
             a.download = `data-table.${result.file_format === 'excel' ? 'xlsx' : result.file_format}`
             a.click();
        })
        .catch((err) => {
            console.log(err.toString())
        })
}

export const addRow = async (dataTable, item) => {

    const myModalEl = document.getElementById('exampleModal');
    const modal = bootstrap.Modal.getInstance(myModalEl)

    delete item.id

    // server
    fetch (`/datatb/${modelName}/add/`, {
        method: "POST",
        body: JSON.stringify(item),
    })
        .then((response) => {
            if(!response.ok) {
                return response.text().then(text => { throw new Error(text) })
            } else {
                return response.json()
            }
        })
        .then((result) => {
            dataTable.rows().add(
                [...Object.values({id: result.id.toString(),...item}),editBtn + " " + removeBtn]
            )

            const alert = document.querySelector('.alert')
            alert.className = alert.className.replace('d-block','d-none')
            location.reload();

            modal.hide();
        })
        .catch((err) => {
            const alert = document.querySelector('.alert')
            alert.textContent = JSON.parse(err.toString().replace('Error: ','')).detail
            alert.className = alert.className.replace('d-none','d-block')
        })
}

export const editRow = (dataTable , item) => {

    const id = item.id
    delete item.id

    // server
    fetch (`/datatb/${modelName}/edit/${id}/`, {
        method: "POST",
        body: JSON.stringify(item),
    })
        .then((response) => {
            if(!response.ok) {
                return response.text().then(text => { throw new Error(text) })
            } else {
                return response.json()
            }
        })
        .then((result) => {

            dataTable.data.forEach((d,i) => {
                if ( dataTable.data[i].cells[0].data === item.id ) {
                    dataTable.rows().remove(i)
                }
            })
            dataTable.rows().add(
                [...Object.values(item),editBtn + " " + removeBtn]
            )

            const alert = document.querySelector('.alert')
            alert.className = alert.className.replace('d-block','d-none')
            location.reload();
        })
        .catch((err) => {
            const alert = document.querySelector('.alert')
            alert.textContent = JSON.parse(err.toString().replace('Error: ','')).detail
            alert.className = alert.className.replace('d-none','d-block')
        })
}

export const removeRow = (dataTable , item) => {

    const id = dataTable.data[item].cells[0].data

    // server
    fetch (`/datatb/${modelName}/delete/${id}/`, {
        method: "POST",
    })
        .then((response) => {
            if(!response.ok) {
                return response.text().then(text => { throw new Error(text) })
            } else {
                return response.json()
            }
        })
        .then((result) => {
            dataTable.rows().remove(item)

            setToastBody(result.message,'success')
            toast.show()
            location.reload()
     })
        .catch((err) => {
            setToastBody(JSON.parse(err.toString().replace('Error: ','')).detail,'fail')
            toast.show()
        })

}
