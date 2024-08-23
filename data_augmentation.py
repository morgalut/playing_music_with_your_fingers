"""
data_augmentation.py

This module provides functions for data augmentation using TensorFlow's Keras API.
"""

import tensorflow as tf
from tensorflow.keras import layers

def create_data_augmentation():
    """
    Creates a data augmentation pipeline using TensorFlow's Keras layers.

    Returns:
        tf.keras.Sequential: A Keras Sequential model with data augmentation layers.
    """
    return tf.keras.Sequential([
        layers.RandomFlip('horizontal'),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1),
    ])
