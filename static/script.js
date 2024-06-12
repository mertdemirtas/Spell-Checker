function search() {
    let searchBar = document.getElementById("searchBar");
    let tableList = document.getElementById('output')

    let searchText = searchBar.value;

    if (searchText.length < 3) {
        clearTableView(tableList)
        return
    }

    $.ajax({
        url: '/search/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(searchText),

        success: function (response) {
            tableList.innerHTML = "";
            tableList.style.border = "1px solid #ddd"

            response.data.forEach(function(item) {
                let li = document.createElement('li');

                li.textContent = item;

                tableList.appendChild(li);
            });

        },
        error: function (error) {
            console.log(error)
        }
    });
}

function clearTableView(tableList) {
        tableList.innerHTML = "";
        tableList.style.border = null
}