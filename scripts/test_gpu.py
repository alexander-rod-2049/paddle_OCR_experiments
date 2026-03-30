import paddle

# Verificar si Paddle detecta la GPU
gpu_available = paddle.device.is_compiled_with_cuda()
device_count = paddle.device.cuda.device_count()
current_device = paddle.get_device()

print(f"--- Verificación de Hardware ---")
print(f"¿Paddle compilado con CUDA?: {gpu_available}")
print(f"GPUs detectadas: {device_count}")
print(f"Dispositivo en uso: {current_device}")

if gpu_available:
    print("¡Listo para procesar imágenes con la RTX 3050!")
else:
    print("Ojo: Paddle está usando CPU. Revisa la instalación de drivers en WSL.")