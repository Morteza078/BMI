$('#bmi_form').on('submit', function (e) {
    var form = $(this);
    var url = form.attr('action');
    let weight = $('#id_weight').val()
    let height = $('#id_height').val()
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: url ,
        data: JSON.stringify({
            weight: weight,
            height: height,
        }),
        success: function (data) {
            alert(data['bmi'])
        },
        error: function (xhr, errmsg, err) {

        },
        contentType: "application/json",
        dataType: 'json',
    });
});