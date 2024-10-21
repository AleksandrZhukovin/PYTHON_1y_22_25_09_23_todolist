$('#saveProject').click(function (){
    $.ajax('/add-project', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
            'name': $('#projectName').val(),
        },
        'success': function (response){
            let newProjectHTML = `<div class="card">
                                           <h5 class="card-header">${$('#projectName').val()}</h5>
                                           <div class="card-body">
                                           </div>
                                         </div>`
            let projectsDiv = document.getElementById('projects');
            projectsDiv.innerHTML = newProjectHTML + projectsDiv.innerHTML;
            $('#projectName').val('');
            const projectModal = new bootstrap.Modal('#projectModal');
            projectModal.hide();
        },
    })
})
