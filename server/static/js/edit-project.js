$('.project-edit').click(function (){
    let btn = $(this);
    document.getElementById(btn.data('edit-block')).classList.remove('d-none');
    document.getElementById(btn.data('display-block')).classList.add('d-none');
});

$('.projectEditSave').click(function (){
   let btn = $(this);
   $.ajax(btn.data('url'), {
       'type': 'POST',
       'async': true,
       'dataType': 'json',
       'data': {
           'name': $(`#${btn.data('input')}`).val(),
       },
       'success': function (response){

       },
   });
});
