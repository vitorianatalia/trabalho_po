console.log("Hello World");

function getFileName() {
    var fullPath = document.getElementById('formFile').value;
    if (fullPath) {
        var startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
        var filename = fullPath.substring(startIndex);
        if (filename.indexOf('\\') === 0 || filename.indexOf('/') === 0) {
            filename = filename.substring(1);
        }
    return filename;    
    }
}

function populateFileName() {
    document.getElementById('fileName').innerText = getFileName();
}

function getFile() {
    var file = document.getElementById('formFile').files[0];
    return file;
}

function getFileSize() {
    var file = getFile();
    return file.size;
}

function populateFileSize() {
    document.getElementById('fileSize').innerText = getFileSize() + " bytes";
}

function getUploadDate() {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();
    if(dd<10) {
        dd='0'+dd
    } 
    if(mm<10) {
        mm='0'+mm
    } 
    today = dd+'/'+mm+'/'+yyyy;
    return today;
}

function populateUpdate() {
    document.getElementById('lastUpdated').innerText = getUploadDate();
}

function populateFileTable() {
    populateFileName();
    populateFileSize();
    populateUpdate();
}

function sendFile() {
    const formData = new FormData();

    // HTML file input, chosen by user
    formData.append("userfile", fileInputElement.files[0]);

    // JavaScript file-like object
    const content = '<q id="a"><span id="b">hey!</span></q>'; // the body of the new file…
    const blob = new Blob([content], { type: "text/xml"});

    formData.append("webmasterfile", blob);

    const request = new XMLHttpRequest();
    request.open("POST", "http://foo.com/submitform.php");
    request.send(formData);
}