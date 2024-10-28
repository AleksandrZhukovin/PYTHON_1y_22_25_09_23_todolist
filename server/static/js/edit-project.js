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
            document.getElementById(`projectHeader${response.id}`).innerHTML = $(`#${btn.data('input')}`).val();
            document.getElementById(`projectEditBlock${response.id}`).classList.add('d-none');
            document.getElementById(`projectDisplayBlock${response.id}`).classList.remove('d-none');
       },
   });
});
