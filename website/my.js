$(function () {
    $('#loginForm').on('submit', function (e) {
        e.preventDefault();

        $.ajax({
            url: "https://yusanshi.com/api/get_grade/",
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
                alert('Unknown error!');
            }
        });
    });
});

function fill_form(data) {
    document.getElementById("all_gpa").innerHTML = data['overview']['all_gpa'];
    document.getElementById("all_credits").innerHTML = data['overview']['all_credits'];
    document.getElementById("latest_gpa").innerHTML = data['overview']['latest_gpa'];
    document.getElementById("latest_credits").innerHTML = data['overview']['latest_credits'];

    var table_data = [];

    for (var key in data['record']) {
        table_data.push({
            name: key,
            credits: data['record'][key]['credits'],
            gp: data['record'][key]['gp'],
            score: data['record'][key]['score']
        })
    }

    $('#table').bootstrapTable('load', table_data);

}