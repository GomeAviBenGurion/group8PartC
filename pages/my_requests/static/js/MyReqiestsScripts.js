async function cancelRequest(requestId) {
    console.log("🚀 Request ID being sent:", requestId);  // Debugging line

    if (!requestId) {
        alert("Error: Missing request ID.");
        return;
    }

    if (!confirm("Are you sure you want to cancel this adoption request?")) {
        return;
    }

    try {
        let response = await fetch('/cancel_request', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ request_id: requestId })  // Ensure `request_id` is being passed
        });

        let result = await response.json();
        console.log("🎯 Server Response:", result);  // Debugging line

        if (response.ok) {
            alert("✅ Request has been cancelled.");
            location.reload();
        } else {
            alert("❌ Error canceling request: " + result.error);
        }
    } catch (error) {
        console.error("❌ Error:", error);
        alert("An error occurred.");
    }
}

async function deleteRequest(requestId) {
    if (!requestId) {
        alert("Error: Missing request ID.");
        return;
    }

    if (!confirm("Are you sure? 🐶 Once deleted, this request can't be retrieved!")) {
        return;
    }

    try {
        let response = await fetch('/delete_request', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ request_id: requestId })
        });

        let result = await response.json();

        if (response.ok) {
            alert("✅ Request has been deleted.");
            location.reload();
        } else {
            alert("❌ Error deleting request: " + result.error);
        }
    } catch (error) {
        console.error("❌ Error:", error);
        alert("An error occurred.");
    }
}
