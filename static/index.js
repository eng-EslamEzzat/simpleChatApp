document.addEventListener('DOMContentLoaded', () => {

        var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

        socket.on('connect', () => {
            document.querySelector('#send').onclick = () => {
                const message = document.querySelector('#message').value
                socket.emit('submit message', {'message':message,});
            }
        });

        socket.on('announce vote', data => {
            const li = document.createElement('li');
            li.innerHTML = `Vote recorded: ${data.message}`;
            document.querySelector('#chat').append(li);
            document.querySelector('#message').value = '';
        });
});