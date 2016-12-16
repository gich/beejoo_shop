/**
 * Created by psyh on 16.12.2016.
 */
'use strict';

function sendRequest(url, userData) {
    var request = $.ajax({
        method: "POST",
        url: url,
        dataType: 'json',
        data: userData
    });
    request.done(function (data, textStatus, jqXHR) {
        console.log('yes', data);
        $('.basketText').text(data['items_in_basket'])
    });
}

$('button').click(function (e) {
    var button = $(this);
    var formData = {
        'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
        'product': button.data('id')
    };

    sendRequest('/addtocart/', formData);

});