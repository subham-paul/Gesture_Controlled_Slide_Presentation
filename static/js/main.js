/* ============================================================
   GestureSlides AI — main.js
   Handles:
   - Camera start / stop
   - Live video feed control
   - Gesture status polling
   - Safe execution (dashboard-only)
============================================================ */

document.addEventListener("DOMContentLoaded", () => {

  /* ------------------------------
     ELEMENT REFERENCES
  ------------------------------ */
  const startBtn = document.getElementById("startCam");
  const stopBtn  = document.getElementById("stopCam");
  const videoEl  = document.getElementById("cameraFeed");
  const statusEl = document.getElementById("gestureStatus");

  // If not on dashboard, safely exit
  if (!startBtn || !stopBtn || !videoEl || !statusEl) {
    return;
  }

  let statusInterval = null;

  /* ------------------------------
     START CAMERA
  ------------------------------ */
  startBtn.addEventListener("click", async () => {
    try {
      await fetch("/start_camera", { cache: "no-store" });

      // Attach live stream
      videoEl.src = "/video_feed";
      videoEl.alt = "Live Camera Feed";

      startBtn.disabled = true;
      stopBtn.disabled = false;

      statusEl.innerText = "Camera started. Waiting for gesture…";

      startGesturePolling();
    } catch (err) {
      console.error("Camera start failed:", err);
      statusEl.innerText = "Error starting camera";
    }
  });

  /* ------------------------------
     STOP CAMERA
  ------------------------------ */
  stopBtn.addEventListener("click", async () => {
    try {
      await fetch("/stop_camera", { cache: "no-store" });

      videoEl.src =
        "https://images.unsplash.com/photo-1518779578993-ec3579fee39f";
      videoEl.alt = "Camera stopped";

      startBtn.disabled = false;
      stopBtn.disabled = true;

      statusEl.innerText = "Camera stopped";

      stopGesturePolling();
    } catch (err) {
      console.error("Camera stop failed:", err);
      statusEl.innerText = "Error stopping camera";
    }
  });

  /* ------------------------------
     GESTURE STATUS POLLING
  ------------------------------ */
  function startGesturePolling() {
    stopGesturePolling(); // safety

    statusInterval = setInterval(async () => {
      try {
        const res = await fetch("/gesture_status", { cache: "no-store" });
        const data = await res.json();

        if (data.gesture) {
          statusEl.innerText = data.gesture;
        }
      } catch (err) {
        console.error("Gesture status error:", err);
      }
    }, 1000);
  }

  function stopGesturePolling() {
    if (statusInterval) {
      clearInterval(statusInterval);
      statusInterval = null;
    }
  }

  /* ------------------------------
     CLEANUP ON PAGE UNLOAD
  ------------------------------ */
  window.addEventListener("beforeunload", () => {
    stopGesturePolling();
  });

});
