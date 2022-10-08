const searchField = document.querySelector('#id_search')
const tableOutput = document.querySelector('.table-output')
const appTable = document.querySelector('.app-table')
const pagination = document.querySelector('.pagination-container')
const tableBody = document.querySelector('.table-body')



tableOutput.style.display = "none";

searchField.addEventListener('keyup',(e)=>{
    const searchValue = e.target.value;
    if(searchValue.trim().length>0){
        console.log(searchValue)
        pagination.style.display = "none";
        tableBody.innerHTML="";

     fetch("search-expenses", {
         body:JSON.stringify( {searchText: searchValue }),
         method: "POST",
        })
         .then(
            res => res.json())
         .then(data => {
         appTable.style.display = "none"
         tableOutput.style.display = "block";
         if(data.length===0){

         tableOutput.style.display = "none";
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


        </tr>
                `
             })

         }
        });
    }
    else{
        appTable.style.display = "block";
        pagination.style.display = "block";
        tableOutput.style.display ="none";

    }
})