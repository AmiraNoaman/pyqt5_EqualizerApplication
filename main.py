from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.Qt import *
import os, sys
import numpy as np
import csv
import matplotlib.pyplot as plt
import pyaudio
import wave
import scipy
import operator
import contextlib
import scipy.fftpack
from scipy import signal
from scipy.fftpack import fft, fftshift
from numpy.fft import fft,fftfreq,ifft
from scipy.io import wavfile
import scipy as sci
# from scipy.signal import boxcar
import sounddevice as sd
import winsound
from NewWindowUI import Ui_Form
# from NewWindowPY import Ui_Form
import pandas as pd
from pathlib import Path
from scipy.interpolate import UnivariateSpline
from GUI2 import Ui_MainWindow

class ApplicationWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setGeometry(600, 300, 400, 200)
        self.setWindowTitle('Equalizer')

        self.ui.upload.clicked.connect(self.UploadSignal)
        self.ui.hammingbutton.clicked.connect(lambda : self.ChangeHamming_Hanning(1))
        self.ui.hanningbutton.clicked.connect(lambda: self.ChangeHamming_Hanning(2))
        self.ui.Rect.clicked.connect(self.Rectangular)
        self.ui.playInput.clicked.connect(self.playSound)
        self.ui.inverse.clicked.connect(self.openWindow)
        self.ui.stopInput.clicked.connect(self.stopWav)
        # self.ui.refresh.clicked.connect(self.Refresh)
        # self.ui.fourier.clicked.connect(self.OriginalFFT)
        self.ui.exit.clicked.connect(self.Exit)



        self.signal=[]
        self.spf=[]
        self.FFT=[]
        self.FFT_flip=[]
        self.FFT_side=[]
        self.fft_freqs_side=[]

        self.fourierinverse_0 = []
        self.fourierinverse_1 = []
        self.FourierInverse = [ self.fourierinverse_0 , self.fourierinverse_1 ]

        self.Output1 = []
        self.Output2 = []
        self.FourierInversemin = [0,0]
        self.FourierInversemax = [0,0]

        self.RecArray=[]   
        self.xfourier=[]
        self.yfourier=[]
        self.xwav=[]
        self.ywav=[]
        self.signal=[]
        self.spf=[]

        self.FFT=[]
        self.FFT_sideArr=[]
        self.FFT_sideArr1=[]
        # self.fft_freqs_side=[]

        self.bands=[]
        self.fromBeg=[]
        self.fromEnd=[]
        self.RectangleArray=[]
        self.HammingArr=[]
        self.Temp=[]
        self.Edit=True

        
       
    def UploadSignal(self):

        self.ui.GVOriginal.clear()
        filePaths = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open File',"~/Desktop/sigViews",'*.wav')
        
        for filePath in filePaths:
            for self.f in filePath:
                if self.f == '*':
                     break
                p = pyaudio.PyAudio()
                self.waveFile=wave.open(self.f,'rb')


                        # wav1 = wave.open(f,'rb')
                        # self.ywav1=wav1.readframes(-1)
                        # self.ywav1 =np.fromstring(self.ywav1,'Int16')
                        # fs=wav1.getframerate()                                                  
                        # self.xwav1=np.linspace(0,len(self.ywav1)/fs,num=len(self.ywav1))
                        # print("length of signal")
                        # print(len(self.xwav1))
                     

                        # self.ui.GVOriginal.plot(self.xwav1,self.ywav1, pen='b')

                self.format = p.get_format_from_width(self.waveFile.getsampwidth())

                channel = self.waveFile.getnchannels()
                self.rate = self.waveFile.getframerate()
                self.frame = self.waveFile.getnframes()
                self.stream = p.open(format=self.format,  # DATA needed for streaming
                                    channels=channel,
                                    rate=self.rate,
                                    output=True)

                #durationF = self.frame / float(self.rate)
                self.data_int = self.waveFile.readframes(self.frame)
                self.data_plot = np.fromstring(self.data_int, 'Int16')
                self.data_plot.shape = -1, 2
                
                self.data_plot = self.data_plot.T  # Y-axis
                self.ywav1 = self.data_plot
                print('original data',self.ywav1)
            
                self.time = np.arange(0, self.frame) * (1.0 / self.rate)    #X-axis
                self.xwav1 = self.time
                #fft_frame = np.fft.rfft(current_frame)


                self.ywav1min = np.nanmin(self.ywav1[1])
                self.ywav1max = np.nanmax(self.ywav1[1])
                self.ui.GVOriginal.setXRange(self.xwav1[0],self.xwav1[-1])
                self.ui.GVOriginal.plotItem.getViewBox().setLimits(xMin=self.xwav1[0], xMax=self.xwav1[-1], yMin=self.ywav1min- self.ywav1min * 0.1, yMax=self.ywav1max + self.ywav1max* 0.1)
        
                self.ui.GVOriginal.plot(self.xwav1,self.ywav1[1], pen='b')

                        
      #===============================================Fourier Transform===============================================#
    

                self.fs_rate,self.spf = wavfile.read(self.f)
            

                # print("araay",self.spf.shape)
                print ("Frequency sampling", self.fs_rate)
                
                l_audio=len(self.spf.shape)
                print("Channels",l_audio)
                if l_audio ==2:
                    self.spf=self.spf.mean(axis=1)     # To make it a mono signal, 1 channel only

                N=self.spf.shape[0]                 # Give number of rows
                print("complete Sampling N",N)
                secs= N/float( self.fs_rate)
                print("secs",secs)
                Ts=1.0/self.fs_rate    # sampling interval in time
                print("Timestep between Ts",Ts)
                t= scipy.arange(0, secs, Ts)


                self.FFT = abs(scipy.fft(self.spf))
        
                self.freqs = scipy.fftpack.fftfreq(self.spf.size, t[1]-t[0])   # Return the Discrete Fourier Transform sample frequencies. t[1]-t[0] is the sample spacing
                

                FFT_side = self.FFT[range(N//2)] # one side FFT range, remove the negative part (starts from zero)
                self.FFT_sideArr= np.array(FFT_side)

            
                self.bands=np.array_split(self.FFT_sideArr,10)
                # self.bands=np.array_split(self.FFT,20)
                print('lehgth of band', int(len(self.bands[1])))
            
                self.BandSize = int(len(self.FFT_sideArr)/10)


                self.phase= np.angle(scipy.fft(self.spf)) #phase, we will use it later

                freqs_side = self.freqs[range(N//2)]
                self.fft_freqs_side = np.array(freqs_side)


                self.ui.GVFourier.plot(self.freqs,self.FFT, pen='g')
                QtCore.QCoreApplication.processEvents()
#=========================================Hamming, Hanning, Rectangular windows======================================================#

    
    def ChangeHamming_Hanning(self , n):
        if(len(self.xwav1) != 0):
            self.ui.GVwindow.clear()

            band_length = int(len(self.FFT) / 20)
            self.sliderList=[int(self.ui.l1.text()),int(self.ui.l2.text()),int(self.ui.l3.text()),int(self.ui.l4.text()),int(self.ui.l5.text()),int(self.ui.l6.text()),int(self.ui.l7.text()),int(self.ui.l8.text()),int(self.ui.l9.text()),int(self.ui.l10.text())]
            
            Hamming = []
            self.HammingArr=[]
            self.Output1 = []
            self.Output2 =[]

            Hamming = np.zeros(len(self.FFT_sideArr))  

            Hamming_Window = np.hamming(band_length)
            #Hamming_Window_Length = self.optimumLengthOfArray(Hamming_Window)



            Optimium_Width_X = []

            temp_window = []
            temp_x = []
            if (n == 1):
                temp_window = np.hamming(band_length)
            else:
                temp_window = np.hanning(band_length)

            temp_x = np.arange(band_length)

            #temp_window = temp_window - np.ones(band_length) * 0.5
            
           # Freq_Side_Arr_Length = int(len(self.FFT_sideArr)/10)
            Freq_Side_Arr_Length = int(np.nanmax(self.freqs)/10)
            Freq_Length = len(self.freqs)


            for x in range(len(temp_window)):
                if temp_window[x] >= 0.5:
                    Optimium_Width_X.append(temp_x[x])
            print(len(Optimium_Width_X))


            percent = float(Optimium_Width_X[-1] - Optimium_Width_X[0]) / Freq_Side_Arr_Length * 100
            Hamming_Window_Length = float(100/percent) * Freq_Length
            Hamming_Window_Length = int(Hamming_Window_Length)

            if (n==1) :
                Hamming_Window = np.hamming(Hamming_Window_Length)
            else:
                Hamming_Window = np.hanning(Hamming_Window_Length)



            centre_window = int(Hamming_Window_Length/2)

            beginning = int(centre_window - band_length/2)
            end = int(centre_window + band_length/2)
            

            index = 0
            tail_left = len(Hamming_Window[0:beginning])
            tail_right = len(Hamming_Window[end:len(Hamming_Window)])

            Band_Index = 0 # Index where band is
            for i in range(10):
                if (self.sliderList[i] > 0):

                    Hamming[index: index+tail_right]= Hamming[index:index+tail_right] +self.FFT[index: index+tail_right] * (Hamming_Window[beginning:beginning+tail_right]* self.sliderList[i])
                    Hamming[index+tail_right: index +band_length]= self.FFT[index+tail_right:index+ band_length] * (Hamming_Window[beginning+tail_right:end]* self.sliderList[i])

             
                    if (Band_Index <= 9 and Band_Index != 0) : # no left tail at band = 0
                        Hamming[index - tail_left : index] = Hamming[index - tail_left : index] + self.FFT[index-tail_left: index] * ( (Hamming_Window[0:beginning]) * self.sliderList[i] )

                    if (Band_Index==0 or Band_Index < 9): # no right tail at band = 9
                        Hamming[index + band_length : index + band_length + tail_right] = self.FFT[index + band_length : index + band_length + tail_right] * Hamming_Window[end:end+tail_right] * self.sliderList[i]

                elif (self.sliderList[i] < 0):

                    Hamming[index: index+tail_right]= Hamming[index:index+tail_right] +self.FFT[index: index+tail_right] * (Hamming_Window[beginning:beginning+tail_right]/ abs(self.sliderList[i]))
                    Hamming[index+tail_right: index +band_length]= self.FFT[index+tail_right:index+ band_length] * (Hamming_Window[beginning+tail_right:end]/ abs(self.sliderList[i]) )

                    if (Band_Index <= 9 and Band_Index != 0): # no left tail at band = 0
                        Hamming[index - tail_left : index] = Hamming[index-tail_left:index] + self.FFT[index - tail_left : index] *( (Hamming_Window[0:beginning]) / abs(self.sliderList[i]) )
                    if (Band_Index == 0 or Band_Index <9): # no right tail at band = 9
                        Hamming[index + band_length : index + band_length + tail_right] = self.FFT[index + band_length : index + band_length + tail_right] * Hamming_Window[end:end+tail_right] / abs(self.sliderList[i])

                Band_Index = Band_Index + 1
                index = index + band_length

            self.HammingArr = np.append( self.HammingArr,Hamming)
            self.HammingArr= np.append( self.HammingArr, np.flip(Hamming,axis=0))

            print(len(self.FFT)-len( self.HammingArr))
            Hammingtemp = []
            
            for x in range(len(self.FFT)-len( self.HammingArr)):
                Hammingtemp = np.append(Hammingtemp, self.HammingArr[-x])
            self.HammingArr = np.append( self.HammingArr,Hammingtemp)


            if(self.Edit== True):
                self.Output1= np.append(self.Output1,self.HammingArr)  
               
                self.ui.GVwindow.plot(self.freqs,self.Output1,pen='r')
                self.Edit=False
            
            elif(self.Edit==False):
                self.ui.GVwindow.clear()
                self.Output2= np.append(self.Output2,self.HammingArr)  
                self.ui.GVwindow.plot(self.freqs,self.Output2,pen='r')
                self.Edit=True


    def Rectangular(self):

        self.sliderList=[int(self.ui.l1.text()),int(self.ui.l2.text()),int(self.ui.l3.text()),int(self.ui.l4.text()),int(self.ui.l5.text()),int(self.ui.l6.text()),int(self.ui.l7.text()),int(self.ui.l8.text()),int(self.ui.l9.text()),int(self.ui.l10.text())]
        print('whatever',self.sliderList)

    
        self.Rectanglepositive = []
        self.Rectanglenegative= []
        self.Rectangle=[]
        self.RectangleArray=[]
        self.AddArr = []

        self.Output1 = []
        self.Output2 =[]


        for i in range(10):

            if(self.sliderList[i]<0):
                self.RecArray=self.bands[i]/abs(self.sliderList[i])
                self.RectangleArray=np.append(self.RectangleArray,self.RecArray)

            if(self.sliderList[i]>0):
                self.RecArray=self.bands[i]* self.sliderList[i]
                self.RectangleArray=np.append(self.RectangleArray,self.RecArray)

                     
        self.Rectanglepositive=np.append(self.Rectanglepositive, self.RectangleArray)  
        print('Positive',self.Rectanglepositive)
        self.Rectanglenegative=np.flip(self.RectangleArray, axis=0)  
        print('Negative',self.Rectanglenegative)
        self.Rectangle=np.append(self.Rectanglepositive,self.Rectanglenegative)   
        print('Rec array',self.Rectangle)


        for x in range(len(self.freqs)-len(self.Rectangle)):
            self.AddArr = np.append(self.AddArr,self.Rectangle[-x])          
            self.AddArr = np.flip(self.AddArr, axis=0)                             # Appended value to Rectangle because the array is not the same size as the freqs, it should be but flipping causes this!
            self.Rectangle = np.append(self.AddArr,self.Rectangle)


        if(self.Edit== True):
            self.Output1= np.append(self.Output1,self.Rectangle)  
            self.ui.GVwindow.plot(self.freqs,self.Output1,pen='r')
            self.Edit=False
            
        elif(self.Edit==False):
            self.ui.GVwindow.clear()
            self.Output2= np.append(self.Output2,self.Rectangle)  
            self.ui.GVwindow.plot(self.freqs,self.Output2,pen='r')
            self.Edit=True


        QtCore.QCoreApplication.processEvents()


# ========================================= PLAY BUTTON ===========================================
    def playSound(self):
        sd.play(self.ywav1[1],self.fs_rate)

# ========================================= SAVE BUTTON ===========================================

    def saveSound(self):
        scipy.io.wavfile.write('Listen to me!.wav', self.fs_rate, self.FFTinverse) 
        print('file is saved!')   
 
# ========================================= STOP BUTTON ===========================================
    def stopWav(self):
        sd.stop()

  
    def Exit(self):
        sys.exit()
    
    def Inverse(self, FFTMag, Phase):


        fft = np.multiply(FFTMag , np.exp(1j*Phase))

        self.FFTinverse = np.real(np.fft.ifft(fft))
        print('Inverse', self.FFTinverse)

        # FFTinverse= np.round(FFTinverse)

        for i in range(len(self.FFTinverse)):

            self.FFTinverse[i] = int(round(self.FFTinverse[i]))

        self.FFTinverse = self.FFTinverse.astype(np.int16)

        

        return self.FFTinverse


    def Refresh(self):
        self.ui.GVwindow.clear()
        self.ui.GVwindow.clear()
  

# ========================================= NEW WINDOW BUTTON ===========================================
    def openWindow(self):

        
        if(len(self.Output1) != 0):
            self.FourierInverse[0] = self.Inverse(self.Output1,self.phase)
        if (len(self.Output2) != 0):
            self.FourierInverse[1] = self.Inverse(self.Output2,self.phase)


        for i in range(len(self.FourierInverse)):
            if(len(self.FourierInverse[i]) != 0):
                self.FourierInversemin[i] = np.nanmin(self.FourierInverse[i])
                self.FourierInversemax[i] = np.nanmax(self.FourierInverse[i])
            else:
                pass

        self.SECOND= Dialog(self.xwav1, self.FourierInverse, self.fs_rate,self.FourierInversemin,self.FourierInversemax,self.Edit)
        self.SECOND.show() 

class Dialog(QtWidgets.QMainWindow):
    def __init__(self, xwavSignal, inverseSignal, samplingRate, fftmin, fftmax, EditArray):
        super(Dialog, self).__init__()
 
        self.x_output=xwavSignal
        self.inverse = inverseSignal
        self.rate=samplingRate
        self.fourierMin=fftmin
        self.fourierMax=fftmax
        self.Edited= EditArray


        self.SECOND = Ui_Form()
        self.SECOND.setupUi(self)

        self.plotInverse()
        self.SECOND.playOutput.clicked.connect(lambda: self.playSound2(0))
        self.SECOND.playOutput2.clicked.connect(lambda: self.playSound2(1))
        self.SECOND.stopOutput.clicked.connect(lambda: self.stopSound2(0))
        self.SECOND.saveOutput.clicked.connect(lambda: self.saveSound2(0))
        self.SECOND.saveOutput2.clicked.connect(lambda: self.saveSound2(1))

    def plotInverse(self):
 
        if (len(self.inverse[0]) != 0):
           self.SECOND.graphicsViewOP1.setXRange(self.x_output[0],self.x_output[-1])
           self.SECOND.graphicsViewOP1.plotItem.getViewBox().setLimits(xMin=self.x_output[0], xMax=self.x_output[-1], yMin=self.fourierMin[0] - self.fourierMin[0]* 0.1, yMax=self.fourierMax[0] + self.fourierMax[0]*0.1)
           self.SECOND.graphicsViewOP1.plot(self.x_output,self.inverse[0],pen='b') 
        if (len(self.inverse[1]) != 0):
            self.SECOND.graphicsViewOP2.setXRange(self.x_output[0],self.x_output[-1])
            self.SECOND.graphicsViewOP2.plotItem.getViewBox().setLimits(xMin=self.x_output[0], xMax=self.x_output[-1], yMin=self.fourierMin[1] - self.fourierMin[1]* 0.1, yMax=self.fourierMax[1] + self.fourierMax[1]*0.1)
            self.SECOND.graphicsViewOP2.plot(self.x_output,self.inverse[1],pen='b')   


        pass


    def playSound2(self,n):
        sd.play(self.inverse[n], self.rate)

    def stopSound2(self,n):
        sd.stop()

    def saveSound2(self,n):
        scipy.io.wavfile.write('This is it!.wav', self.rate, self.inverse[n]) 
        print('file is saved!')   

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == '__main__':
    main()
