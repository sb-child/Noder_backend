_mode_rgb = {
    "channels": [
        "R", "G", "B"
    ],
    "min_value": [
        0, 0, 0
    ],
    "max_value": [
        255, 255, 255
    ],
}
_mode_lab = {
    "channels": [
        "L", "a", "b"
    ],
    "min_value": [
        0, -120, -120
    ],
    "max_value": [
        100, 120, 120
    ],
}
_mode_cmyk = {
    "channels": [
        "C", "M", "Y", "K"
    ],
    "min_value": [
        0, 0, 0, 0
    ],
    "max_value": [
        100, 100, 100, 100
    ],
}
_mode_hsb = {
    "channels": [
        "H", "S", "B"
    ],
    "min_value": [
        0, 0, 0
    ],
    "max_value": [
        360, 100, 100
    ],
}
_mode_gray = {
    "channels": [
        "G"
    ],
    "min_value": [
        0
    ],
    "max_value": [
        255
    ],
}
_mode_bitmap = {
    "channels": [
        "B"
    ],
    "min_value": [
        0
    ],
    "max_value": [
        1
    ],
}


def getMode(m: str):
    m = m.lower()
    if m == "rgb":
        return _mode_rgb
    if m == "cmyk":
        return _mode_cmyk
    if m == "lab":
        return _mode_lab
    if m == "bitmap":
        return _mode_bitmap
    if m == "gray":
        return _mode_gray
