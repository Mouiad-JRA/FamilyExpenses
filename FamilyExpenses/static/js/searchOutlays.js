const searchField = document.querySelector('#id_search')
const tableOutput = document.querySelector('.table-output')
const appTable = document.querySelector('.app-table')
const pagination = document.querySelector('.pagination-container')
const tableBody = document.querySelector('.table-boday')

tableOutput.style.display = "none";

searchField.addEventListener('keyup',(e)=>{
    const searchValue = e.target.value;
    if(searchValue.trim().length>0){
        pagination.style.display = "none";
        tableBody.innerHTML="";
     fetch("search-expenses", {
         body:JSON.stringify( {searchText: searchValue }),
         method: "POST",
        }).then(
            res => res.json(),
        ).then(data => {
           console.log('data',data)
         appTable.style.display = "none"
         tableOutput.style.display = "block";
         if(data.length==0){
         tableOutput.innerHTML = "No results Found";
         }else{
             data.forEach(outlay=>{
                 console.log(outlay)
             tableBody.innerHTML+=`
          <tr>
            <td>
                ${outlay.price}
            </td>
            <td>
                ${outlay.outlay_type_id}
            </td>
            <td>
                ${outlay.material_id}
            </td>
            <td>
               ${outlay.description}
            </td>
            <td>
                ${outlay.date}
            </td>
                     <th><a href="{% url "expenses-dash:delete" outlay.id %}" class="btn btn-danger btn-sm">
             {% trans "Delete" %}</a> </th>
         <th><a href="{% url "expenses-dash:edit" outlay.id %}" class="btn btn-secondary btn-sm">
             {% trans "Edit" %}</a> </th>

        </tr>
                `
             })

         }
        });
    }
    else{
        tableOutput.style.display ="none";
        appTable.style.display = "block";
        pagination.style.display = "block";



    }
})