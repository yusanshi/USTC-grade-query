$(function () {
    $('#loginForm').on('submit', function(e) {
        e.preventDefault();

        $.ajax({
            url: "get_grade.php",
            type: "POST",
            data: $('#loginForm').serialize(),
            dataType: "json",
            success: function (data) {
                if (data == "{}") {
                    alert("Username or password is wrong!");
                } else {
                    var data = JSON.parse(data);
                    fill_form(data);
                }
            },
            error: function () {
                alert('Failed. "get_grade.php" has no response!');
            }
        });
    });
});

function fill_form(data) {
    document.getElementById("all_gpa").innerHTML = data['overview']['all_gpa'];
    document.getElementById("all_credits").innerHTML = data['overview']['all_credits'];
    document.getElementById("latest_gpa").innerHTML = data['overview']['latest_gpa'];
    document.getElementById("latest_credits").innerHTML = data['overview']['latest_credits'];

    var table = document.getElementById("table");
    var tbody = document.getElementById("tbody");
    table.removeChild(tbody);
    tbody = document.createElement("tbody");
    tbody.id = "tbody";


    for (var key in data['record']) {
        var tr = document.createElement("tr");
        var td1 = document.createElement("td");
        var td2 = document.createElement("td");
        var td3 = document.createElement("td");
        var td4 = document.createElement("td");

        td1.innerHTML = key;
        td2.innerHTML = data['record'][key]['credits'];
        td3.innerHTML = data['record'][key]['gp'];
        td4.innerHTML = data['record'][key]['score'];

        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
        tr.appendChild(td4);
        tbody.appendChild(tr);
    }
    table.appendChild(tbody);
}