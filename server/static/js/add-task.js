$('.add-task').click(function (){
    let btn = $(this);
    $('#saveTask').data('url', btn.data('url'));
});

$('#saveTask').click(function (){
    let btn = $(this);
   $.ajax(btn.data('url'), {
       'type': 'POST',
       'async': true,
       'dataType': 'json',
       'data': {
           'name': $('#taskName').val(),
           'deadline': $('#taskDeadline').val(),
           'priority': $('#taskPriority').val(),
       },
       'success': function (response){
            document.getElementById(`projectTasks${response.id}`).innerHTML += `<h4></h4>`;
       }
   })
});
