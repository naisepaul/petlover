
// Remove alert messages after 5 seconds
document.addEventListener('DOMContentLoaded', function () {
    var alertElements = document.querySelectorAll('.alert');
    alertElements.forEach(function (alert) {
        setTimeout(function () {
            alert.remove();
        }, 5000); // 5000 milliseconds = 5 seconds
    });
});