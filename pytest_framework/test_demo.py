import pytest

def test_demo2_methodA(oneTimeSetUp, setUp):
    print("Running demo2 method A")

def test_demo2_methodB(setUp, oneTimeSetUp):
    print("Running demo2 method B")
