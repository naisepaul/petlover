
// Remove alert messages after 5 seconds
document.addEventListener('DOMContentLoaded', function () {
    var alertElements = document.querySelectorAll('.alert');
    alertElements.forEach(function (alert) {
        setTimeout(function () {
            alert.remove();
        }, 5000); // 5000 milliseconds = 5 seconds
    });

    document.getElementById('listings-link').addEventListener('click', function (event) {
        event.preventDefault();
        document.getElementById('profile-section').classList.add('d-none');
        document.getElementById('listings-section').classList.remove('d-none');
        document.getElementById('profile-link').classList.remove('active');
        document.getElementById('listings-link').classList.add('active');
    });

    document.getElementById('profile-link').addEventListener('click', function (event) {
        event.preventDefault();
        document.getElementById('listings-section').classList.add('d-none');
        document.getElementById('profile-section').classList.remove('d-none');
        document.getElementById('listings-link').classList.remove('active');
        document.getElementById('profile-link').classList.add('active');
    });
});