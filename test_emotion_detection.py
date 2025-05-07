"""
Emotion Detection Unit Tests
"""

from emotion_detection import emotion_detector

def test_joy():
    """
    Tests detection of Joy
    """
    assert emotion_detector("I am glad this happened")["dominant_emotion"] == "joy"

def test_anger():
    """
    Tests detection of Anger
    """
    assert emotion_detector("I am really mad about this")["dominant_emotion"] == "anger"

def test_disgust():
    """
    Tests detection of disgust
    """
    assert emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"] == "disgust"

def test_sadness():
    """
    Tests detection of Sadness
    """
    assert emotion_detector("I am so sad about this")["dominant_emotion"] == "sadness"

def test_fear():
    """
    Tests detection of Fear
    """
    assert emotion_detector("I am really afraid that this will happen")["dominant_emotion"] == "fear"
