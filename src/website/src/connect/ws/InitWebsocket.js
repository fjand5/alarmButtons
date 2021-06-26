var connection
var onOpen = []
var onClose = []

var onMessages = []
function init() {
    
    // let url = "ws://"+window.location.hostname+(window.location.port ? ':'+window.location.port: '')+"/ws/maintain/"
    if(connection != null){
        connection.close();
    }
    let url = "ws://"+window.location.hostname+":8000/ws/maintain/"
    connection = new WebSocket(url)
    connection.onmessage = function(event) {
        let data = JSON.parse(event.data).data
        onMessages.forEach(element => {
            if (element instanceof Function){
                element(data);
            }
        });
    }
    
    connection.onopen = function(event) {

        onOpen.forEach(element => {
            if (element instanceof Function){
                element(event);
            }
        });
    }
    connection.onclose = function (event) {

        setTimeout(() => {
            init()
          }, 3000);
        onClose.forEach(element => {
            if (element instanceof Function){
                element(event);
            }
        });
    }
}
function addOnOpen(func) {
    onOpen.push(func)
}
function addOnClose(func) {
    onClose.push(func)
}
function addOnMessages(func) {
    onMessages.push(func)
}
module.exports = {
    init,
    addOnOpen,
    addOnClose,
    addOnMessages
  };