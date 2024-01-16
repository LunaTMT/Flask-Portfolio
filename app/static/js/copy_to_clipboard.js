
function copyToClipboard(textToCopy) {
    
    navigator.clipboard.writeText(textToCopy).then(function() {
        alert("Copied to clipboard: " + textToCopy);
    }).catch(function(err) {
        console.error('Unable to copy text to clipboard', err);
    });
}