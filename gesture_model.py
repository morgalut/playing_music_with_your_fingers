import tensorflow as tf
from tensorflow.keras import models, layers
from data_augmentation import create_data_augmentation
from gesture import Gesture

def create_gesture_model(input_shape):
    data_augmentation = create_data_augmentation()

    base_model = tf.keras.applications.MobileNetV2(input_shape=input_shape,
                                                   include_top=False,
                                                   weights='imagenet')
    base_model.trainable = False  # Freeze the base model

    model = models.Sequential([
        layers.Input(shape=input_shape),  # Explicitly define the input shape
        data_augmentation,
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(len(Gesture), activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model
