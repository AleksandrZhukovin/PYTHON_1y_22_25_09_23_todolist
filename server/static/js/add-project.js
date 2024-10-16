$('#saveProject').click(function (){
    $.ajax('/add-project', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
            'name': $('#projectName').val(),
        },
        'success': function (response){
            let projectsDiv = document.getElementById('projects');
            projectsDiv.innerHTML = `<h3>${$('#projectName').val()}</h3>` + projectsDiv.innerHTML;
            $('#projectName').val('');
            const projectModal = new bootstrap.Modal('#projectModal');
            projectModal.hide();
        },
    })
})
