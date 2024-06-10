
import {myData} from '../../data/index.js'

export const formTypes = {
    ADD: 'add',
    EDIT: 'edit'
}

export const formConstructor = (formType,item) => {

    // create form
    const form = document.getElementById('form')
    form.className = 'd-flex flex-column gap-1 p-3'
    form.innerHTML = ''
    
    myData.headings.forEach((d,i) => {
        
        const label = document.createElement('label')
        label.setAttribute('htmlFor',i)
        label.innerHTML = d;
        label.className = "form-label m-0";

        const input = document.createElement('input');

        if (myData.isDate[i] === 'True')
            input.setAttribute('type','date');
        else
            input.setAttribute('type','text');

        input.className = 'form-control m-0'
        input.placeholder = d

        if (d === 'id')
            input.setAttribute('disabled','true')

        if (formType === formTypes.EDIT)
            input.setAttribute('value', item[i])

        form.innerHTML += label.outerHTML
        form.innerHTML += input.outerHTML
    })

    if (formType === formTypes.ADD) {
        document.querySelector('.modal-title').innerHTML = 'add Item'
        document.querySelector('.modal-btn').value = 'add'
    
    } else if (formType === formTypes.EDIT) {
        document.querySelector('.modal-title').innerHTML = 'edit Item'
        document.querySelector('.modal-btn').value = 'edit'
    }

    return form;
}