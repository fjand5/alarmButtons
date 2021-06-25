var connection
var onOpen = null;
var onClose = null;

var onMessages = []
function init() {
    
    // let url = "ws://"+window.location.hostname+(window.location.port ? ':'+window.location.port: '')+"/ws/maintain/"
    if(connection != null){
        connection.close();
    }
    let url = "ws://"+window.location.hostname+":8000/ws/maintain/"
    connection = new WebSocket(url)
    connection.onmessage = function(event) {

        onMessages.forEach(element => {
            if (element instanceof Function){
                element(event);
            }
        });
    }
    
    connection.onopen = function(event) {
        if (onOpen instanceof Function){
            onOpen(event);
        }
    }
    connection.onclose = function (event) {
        if (onClose instanceof Function){
            onClose(event);
        }
    }
}
function setOnOpen(func) {
    onOpen = func
}
function setOnClose(func) {
    onClose = func
}
function addOnMessages(func) {
    onMessages.push(func)
}
module.exports = {
    init,
    setOnOpen,
    setOnClose,
    addOnMessages
  };