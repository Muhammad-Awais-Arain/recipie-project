function showLoadingScreen() {
    document.getElementById("loadingScreen").style.display = "block";
}

function hideLoadingScreen() {
    document.getElementById("loadingScreen").style.display = "none";
}

document.getElementById("modalSubmit").addEventListener("click", function(event) { // Added 'event' parameter
    event.preventDefault();

    const testType = document.getElementById("testType").value;

    if (testType === "") {
        showAlert('Select Script', 'Please Select a script to run', 'warning');
    } else {
        const url_enter = document.getElementById("url_enter").value;

        $("#myModal").modal("hide");
        showLoadingScreen();
        fetch("/run-test/" + testType, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: url_enter })
        })
        .then(response => response.text())
        .then(data => {
            hideLoadingScreen();
            showAlert('Test Result', data, 'success');
        })
        .catch(error => {
            hideLoadingScreen();
            showAlert('Test Result', error, 'error');
        });
    }
});


document.getElementById("runV4").addEventListener("click", function() {
    showLoadingScreen();

    fetch("/v4", { method: "POST" })
    .then(response => response.text())
    .then(data => {
        hideLoadingScreen();
        showAlert('Test Result', data, 'success');
    })
    .catch(error => {
        hideLoadingScreen();
        showAlert('Test Result', error, 'error');
    });
});


function showAlert(title, message, icon) {
    Swal.fire({
        title: title,
        text: message,
        icon: icon,
        confirmButtonText: 'Okay'
    });
}