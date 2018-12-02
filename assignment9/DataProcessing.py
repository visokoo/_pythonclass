#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 9-1
1) Create a DataProcessing Class.

2) Create a test harness and test that it works

3) Add code to make sure other developers do not run the DataProcessing
class as a stand-alone script.
NOTE: Python will automatically create a subfolder called __pycache__ when
you first use your module.
'''
if __name__ == "__main__":
  raise Exception("This file is not meant to ran by itself")

class DataProcessing(object):
  # --Constructor--
  def __init__(self, FileName="SavedData.txt", TextData=""):
    # Attributes
    self.FileName = FileName
    self.TextData = TextData

  # --Properties--
  # FileName
  @property
  def FileName(self):
    return self.__FileName

  @FileName.setter
  def FileName(self, Value):
    self.__FileName = Value

  # TextData
  @property
  def TextData(self):
    return self.__TextData

  @TextData.setter
  def TextData(self, Value):
    self.__TextData = Value

  # --Methods--
  def SaveData(self):
    """Writes data"""
    try:
      objFile = open(self.FileName, "a")
      objFile.write(self.TextData)
      objFile.close()
    except Exception as e:
      print("Python reported the following error: " + str(e))
    return "Data Saved"

  def GetData(self):
    """Reads data"""
    try:
      objFile = open(self.FileName, "r")
      self.TextData = objFile.read()
      objFile.close()
    except Exception as e:
      print("Python reported the following error: " + str(e))
    return self.TextData

  def ToString(self):
    """Explictly returns field data"""
    return self.FileName + "," + self.TextData

  def __str__(self):
    """Implictly returns field data"""
    return self.ToString()