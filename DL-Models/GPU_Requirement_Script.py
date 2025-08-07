import tensorflow as tf

# Check for available GPUs
gpus = tf.config.list_physical_devices('GPU')

if gpus:
    try:
        # Restrict TensorFlow to only allocate memory as needed
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        
        logical_gpus = tf.config.list_logical_devices('GPU')
        print(f"Found {len(gpus)} Physical GPU(s), Configured {len(logical_gpus)} Logical GPU(s)")

        # Optional: Run a test operation to see which device is used
        print("\n--- GPU Test ---")
        with tf.device('/GPU:0'):
            a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
            b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
            c = tf.matmul(a, b)
        print("Test matrix multiplication on GPU:")
        print(c.numpy())
        print("----------------\n")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized.
        # This error is common if you try to configure GPUs after a TF operation has already run.
        print(e)
else:
    print("No GPU found. The model will run on the CPU.")

# ... (rest of your code for data loading, model building, etc.)