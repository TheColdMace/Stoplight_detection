from jetcam.csi_camera import USBCamera

camera = USBCamera(capture_device=1)

camera.running = True
image = camera.value