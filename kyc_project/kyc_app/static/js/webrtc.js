let localVideo = document.getElementById("localVideo");
let remoteVideo = document.getElementById("remoteVideo");
let localStream = null;

// Start webcam
async function startCall() {
    localStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });

    if (localVideo) localVideo.srcObject = localStream;
    if (remoteVideo) remoteVideo.srcObject = localStream; // For admin demo
}

// Stop webcam
function stopCall() {
    if (localStream) {
        localStream.getTracks().forEach(track => track.stop());
        if (localVideo) localVideo.srcObject = null;
        if (remoteVideo) remoteVideo.srcObject = null;
        alert("Call stopped.");
    }
}
