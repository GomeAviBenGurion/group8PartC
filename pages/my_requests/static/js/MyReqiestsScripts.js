async function cancelRequest(requestId) {
    if (!confirm("Are you sure you want to cancel this adoption request?")) {
        return;
    }

    try {
        let response = await fetch('/cancel_request', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ request_id: requestId })
        });

        let result = await response.json();
        console.log(result);

        if (response.ok) {
            alert("Request has been cancelled.");
            location.reload();  // Reload to reflect status change
        } else {
            alert("Error canceling request. Please try again.");
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred.");
    }
}
