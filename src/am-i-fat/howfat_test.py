import pytest
import random
from howfat import *


def howfat_test_valid():
    #metric arguments valid
    actual = howfat(25, 180, 67, "m")
    assert actual==20.68, "howfat() did not return expected BMI"