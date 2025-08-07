import tensorflow as tf

# Check for available GPUs
gpus = tf.config.list_physical_devices('GPU')

if gpus:
    try:
        # Currently, don't grow memory, just a demonstration of using the GPU
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print(f"GPU(s) found and configured: {len(gpus)}")
        logical_gpus = tf.config.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        print(e)
else:
    print("No GPU found. The model will run on the CPU.")

# ... (rest of your code for data loading, model building, etc.)