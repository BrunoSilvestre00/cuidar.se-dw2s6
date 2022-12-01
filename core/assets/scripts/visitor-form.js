const form = $('#visitor-form');
const root = $(':root').get(0);
const submit = $('#submit-visitor-form')
const checkValid = () => {
    if(form.get(0).checkValidity()){
        root.style.setProperty('--theme-color', '#198344');
        submit.prop('disabled', false);
    } else {
        root.style.setProperty('--theme-color', '#CA3545');
        submit.prop('disabled', true);
    }
};


$(document).ready(() => {
    $('#input-phone').mask('(00) 00000-0000');
    $('#input-cpf').mask('000.000.000-00');
    checkValid();
});

form.change(checkValid);