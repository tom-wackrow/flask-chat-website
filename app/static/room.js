// var socket = io({transports: ['websocket'], upgrade: false}).connect('http://' + document.domain + ':' + location.port + '/room');
var socket = io.connect('http://' + document.domain + ':' + location.port + '/room');

const msgRegExp = "/^(?:([A-Za-z]+):)?(\/{0,3})([0-9.\-A-Za-z]+)(?::(\d+))?(?:\/([^?#]*))?(?:\?([^#]*))?(?:#(.*))?$/"

socket.on('connect', function () {
    socket.emit("join", {
        user_name: "{{ current_user.username }}",
        message: 'connected'
    })
    var form = $('form').on('submit', function (e) {
        e.preventDefault()
        let user_name = "{{ current_user.username}}"
        let user_input = $('input.message').val()
        user_input = linkify(user_input)

        socket.emit('message', {
            user_name: user_name,
            message: user_input
        })
        $('input.message').val('').focus()
    })
})
socket.on('message', function (msg) {
    if (typeof msg.user_name !== 'undefined') {
        $('h3').remove()
        $('div.message_holder').append('<div><b>\<' + msg.user_name + '\></b> ' + msg.message + '</div>')
    }
})


function linkify(inputText) {
    var replacedText, replacePattern1, replacePattern2, replacePattern3;

    //URLs starting with http://, https://, or ftp://
    replacePattern1 = /(\b(https?|ftp):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/gim;
    replacedText = inputText.replace(replacePattern1, '<a href="$1" target="_blank">$1</a>');

    //URLs starting with "www." (without // before it, or it'd re-link the ones done above).
    replacePattern2 = /(^|[^\/])(www\.[\S]+(\b|$))/gim;
    replacedText = replacedText.replace(replacePattern2, '$1<a href="http://$2" target="_blank">$2</a>');

    //Change email addresses to mailto:: links.
    replacePattern3 = /(([a-zA-Z0-9\-\_\.])+@[a-zA-Z\_]+?(\.[a-zA-Z]{2,6})+)/gim;
    replacedText = replacedText.replace(replacePattern3, '<a href="mailto:$1">$1</a>');

    return replacedText;
}