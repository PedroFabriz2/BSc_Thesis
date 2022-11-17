import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from scipy import signal  

class FirstProcedure:

    def __init__(self) -> None:
        self.extension_full_range_0 = pd.read_csv("/Users/fabriz/Pedro/LabGuará/Joelho/PG/Experimentos/Exp1/Dados/1Teste/EMG00.csv",sep=",")
        self.extension_full_range_1 = pd.read_csv("/Users/fabriz/Pedro/LabGuará/Joelho/PG/Experimentos/Exp1/Dados/1Teste/EMG01.csv",sep=",")
        self.flexion_full_range_2 = pd.read_csv("/Users/fabriz/Pedro/LabGuará/Joelho/PG/Experimentos/Exp1/Dados/1Teste/EMG02.csv",sep=",")
        self.flexion_full_range_3 = pd.read_csv("/Users/fabriz/Pedro/LabGuará/Joelho/PG/Experimentos/Exp1/Dados/1Teste/EMG03.csv",sep=",")

    def get_extension_data(self):
        self.time0 = self.extension_full_range_0.n / 1000
        self.emg0_quad = self.extension_full_range_0.quadriceps * (3.3/4095)
        self.emg0_bic = self.extension_full_range_0.biceps * (3.3/4095)

        self.time1 = self.extension_full_range_1.n / 1000
        self.emg1_quad = self.extension_full_range_1.quadriceps * (3.3/4095)
        self.emg1_bic = self.extension_full_range_1.biceps * (3.3/4095)

    def get_flexion_data(self):
        self.time0 = self.flexion_full_range_2.n / 1000
        self.emg0_quad = self.flexion_full_range_2.quadriceps * (3.3/4095)
        self.emg0_bic = self.flexion_full_range_2.biceps * (3.3/4095)

        self.time1 = self.flexion_full_range_3.n / 1000
        self.emg1_quad = self.flexion_full_range_3.quadriceps * (3.3/4095)
        self.emg1_bic = self.flexion_full_range_3.biceps * (3.3/4095)

      
    def plot_signals(self, lim):
        '''
            Primeira parte é para mostrar o sinal raw retirado da myoware

        '''
        #extension
        '''first trial'''
        fig, ax = plt.subplots(2,2)
        ax[0,0].plot(self.time0, self.emg0_quad, linewidth=0.1)
        ax[1,0].plot(self.time0, self.emg0_bic, linewidth=0.1)
        ax[0,0].set_ylim(lim)
        ax[0,0].set_ylabel('Volts')
        ax[0,0].set_title('Quadríceps')
        ax[1,0].set_ylim(lim)
        ax[1,0].set_ylabel('Volts')
        ax[1,0].set_title('Bíceps')

        '''second trial'''
        ax[0,1].plot(self.time1, self.emg1_quad, 'r', linewidth=0.1)
        ax[1,1].plot(self.time1, self.emg1_bic, 'r', linewidth=0.1)
        ax[0,1].set_ylim(lim)
        ax[0,1].set_ylabel('Volts')
        ax[0,1].set_title('Quadríceps')
        ax[1,1].set_ylim(lim)
        ax[1,1].set_ylabel('Volts')
        ax[1,1].set_title('Bíceps')

        plt.show()

    def filter_signal(self):

        bp = signal.butter(4, 10, 'hp', fs=1000, output='sos')
        self.emg0_quad = signal.sosfilt(bp, self.emg0_quad)
        self.emg0_bic = signal.sosfilt(bp, self.emg0_bic)
        self.emg1_quad = signal.sosfilt(bp, self.emg1_quad)
        self.emg1_bic = signal.sosfilt(bp, self.emg1_bic)

        bs = signal.butter(2, [59.5,60.5], 'bandstop', fs=1000, output='sos')
        self.emg0_quad = signal.sosfilt(bs, self.emg0_quad)
        self.emg0_bic = signal.sosfilt(bs, self.emg0_bic)
        self.emg1_quad = signal.sosfilt(bs, self.emg1_quad)
        self.emg1_bic = signal.sosfilt(bs, self.emg1_bic)

def run_first_procedure():

    # 0 is for flexion data, 1 is for extension
    side = 1

    # 0 is raw_signal, 1 is with bwh
    filter_opt = 1

    Step1 = FirstProcedure()

    if filter_opt:
        if side:
            Step1.get_extension_data()
            Step1.filter_signal()
            Step1.plot_signals(lim=[-0.80,0.80])
        else:
            Step1.get_flexion_data()
            Step1.filter_signal()
            Step1.plot_signals(lim=[-0.8,0.8])
    else:
        if side:
            Step1.get_extension_data()
            Step1.plot_signals(lim=[1.25,1.85])
        else:
            Step1.get_flexion_data()
            Step1.plot_signals(lim=[1.25,1.85])

class SecondProcedure:

    def __init__(self) -> None:
        self.extension_only_0 = pd.read_csv("/Users/fabriz/Pedro/LabGuará/Joelho/PG/Experimentos/Exp1/Dados/1Teste_parte2/EMG00.csv",sep=",")
        self.extension_only_1 = pd.read_csv("/Users/fabriz/Pedro/LabGuará/Joelho/PG/Experimentos/Exp1/Dados/1Teste_parte2/EMG01.csv",sep=",")
        self.flexion_only_0 = pd.read_csv("/Users/fabriz/Pedro/LabGuará/Joelho/PG/Experimentos/Exp1/Dados/1Teste_parte2/EMG02.csv",sep=",")

    def get_extension_data(self):
        self.time0 = self.extension_only_0.n / 1000
        self.emg0_quad = self.extension_only_0.quadriceps * (3.3/4095)
        self.emg0_bic = self.extension_only_0.biceps * (3.3/4095)

        self.time1 = self.extension_only_1.n / 1000
        self.emg1_quad = self.extension_only_1.quadriceps * (3.3/4095)
        self.emg1_bic = self.extension_only_1.biceps * (3.3/4095)

    def get_flexion_data(self):
        self.time0 = self.flexion_only_0.n / 1000
        self.emg0_quad = self.flexion_only_0.quadriceps * (3.3/4095)
        self.emg0_bic = self.flexion_only_0.biceps * (3.3/4095)

        self.time1 = np.ones(100)
        self.emg1_quad = np.ones(100)
        self.emg1_bic = np.ones(100)

    def plot_signals(self, lim):
        '''
            Segunda parte é ...

        '''
        #extension
        '''first trial'''
        fig, ax = plt.subplots(2,2)
        ax[0,0].plot(self.time0, self.emg0_quad, linewidth=0.1)
        ax[1,0].plot(self.time0, self.emg0_bic, linewidth=0.1)
        ax[0,0].set_ylim(lim)
        ax[0,0].set_ylabel('Volts')
        ax[0,0].set_title('Quadríceps')
        ax[1,0].set_ylim(lim)
        ax[1,0].set_ylabel('Volts')
        ax[1,0].set_title('Bíceps')

        '''second trial'''
        ax[0,1].plot(self.time1, self.emg1_quad, 'r', linewidth=0.1)
        ax[1,1].plot(self.time1, self.emg1_bic, 'r', linewidth=0.1)
        ax[0,1].set_ylim(lim)
        ax[0,1].set_ylabel('Volts')
        ax[0,1].set_title('Quadríceps')
        ax[1,1].set_ylim(lim)
        ax[1,1].set_ylabel('Volts')
        ax[1,1].set_title('Bíceps')
        plt.plot()

        plt.show()

    def filter_signal(self):

        bp = signal.butter(4, [10,450], 'bandpass', fs=1000, output='sos')
        self.emg0_quad = signal.sosfilt(bp, self.emg0_quad)
        self.emg0_bic = signal.sosfilt(bp, self.emg0_bic)
        self.emg1_quad = signal.sosfilt(bp, self.emg1_quad)
        self.emg1_bic = signal.sosfilt(bp, self.emg1_bic)

        bs = signal.butter(8, [59.5,60.5], 'bandstop', fs=1000, output='sos')
        self.emg0_quad = signal.sosfilt(bs, self.emg0_quad)
        self.emg0_bic = signal.sosfilt(bs, self.emg0_bic)
        self.emg1_quad = signal.sosfilt(bs, self.emg1_quad)
        self.emg1_bic = signal.sosfilt(bs, self.emg1_bic)

def run_second_procedure():

    # 0 is for flexion data, 1 is for extension
    side = 0

    # 0 is raw_signal, 1 is with bwh
    filter_opt = 1
    
    Step2 = SecondProcedure()

    if filter_opt:
        if side:
            Step2.get_extension_data()
            Step2.filter_signal()
            Step2.plot_signals(lim=[-0.80,0.80])
        else:
            Step2.get_flexion_data()
            Step2.filter_signal()
            Step2.plot_signals(lim=[-0.8,0.8])
    else:
        if side:
            Step2.get_extension_data()
            Step2.plot_signals(lim=[1.25,1.85])
        else:
            Step2.get_flexion_data()
            Step2.plot_signals(lim=[1.25,1.85])

class ThirdProcedure:

    def __init__(self) -> None:
        self.walking = pd.read_csv("/Users/fabriz/Pedro/LabGuará/Joelho/PG/Experimentos/Exp1/Dados/Teste2e3/EMG08.csv",sep=",")
        self.flexion_data = pd.read_csv("/Users/fabriz/Pedro/LabGuará/Joelho/PG/Experimentos/Exp1/Dados/1Teste/EMG03.csv",sep=",")
        self.extension_data = pd.read_csv("/Users/fabriz/Pedro/LabGuará/Joelho/PG/Experimentos/Exp1/Dados/1Teste/EMG00.csv",sep=",")
        

    def get_data(self):
        self.time0 = self.walking.n / 1000
        self.emg0_quad = self.walking.quadriceps * (3.3/4095)
        self.emg0_bic = self.walking.biceps * (3.3/4095)
        self.emg0_phase = self.walking.phase * -30 + 30

        self.MVCe = self.extension_data * (3.3/4095)
        self.MVCf = self.flexion_data * (3.3/4095)


    def plot_signals(self, lim, wdth):
        '''
            Terceira parte é andando na esteira em 5km/h.

        '''
        interval = [15,19]
        fig, ax = plt.subplots(3,1)
        ax[0].plot(self.time0, self.emg0_quad, linewidth=wdth)
        ax[0].plot(self.time0, self.emg0_phase, 'black', linewidth=0.3)
        ax[0].set_ylim(lim)
        ax[0].set_xlim(interval)
        ax[0].set_ylabel('quadríceps (%)MVC')

        ax[1].plot(self.time0, self.emg0_bic, linewidth=wdth)
        ax[1].plot(self.time0, self.emg0_phase, 'black', linewidth=0.3)
        ax[1].set_ylim(lim)
        ax[1].set_xlim(interval)
        ax[1].set_ylabel('bíceps (%)MVC')

        ax[2].plot(self.time0, self.emg0_quad - (self.emg0_bic), linewidth=wdth)
        # ax[2].plot(self.time0, self.emg0_bic, linewidth=wdth)
        ax[2].plot(self.time0, self.emg0_phase, 'black', linewidth=0.3)
        ax[2].set_ylim(lim)
        ax[2].set_xlim(interval)
        ax[2].legend(['EMGquadríceps - EMGbíceps','gait cycle'],)
        ax[2].set_ylabel('both muscles (%)MVC')

        plt.plot()
        plt.show()

    def filter_signal(self):

        bp = signal.butter(4, [5,450], 'bandpass', fs=1000, output='sos')
        self.emg0_quad = signal.sosfilt(bp, self.emg0_quad)
        self.emg0_bic = signal.sosfilt(bp, self.emg0_bic)
        self.MVCe = signal.sosfilt(bp, self.MVCe)
        self.MVCf = signal.sosfilt(bp, self.MVCf)

        bs = signal.butter(4, [58,62], 'bandstop', fs=1000, output='sos')
        self.emg0_quad = signal.sosfilt(bs, self.emg0_quad)
        self.emg0_bic = signal.sosfilt(bs, self.emg0_bic)
        self.MVCe = np.amax(abs(signal.sosfilt(bs, self.MVCe)))
        self.MVCf = np.amax(abs(signal.sosfilt(bs, self.MVCf)))

    def average_signal(self):

        lp = signal.butter(2, 2, 'lowpass', fs=1000, output='sos')
        self.emg0_quad = signal.sosfilt(lp, abs(self.emg0_quad))
        self.emg0_bic = signal.sosfilt(lp, abs(self.emg0_bic)) 
        
        self.emg0_quad = 100*self.emg0_quad*(self.MVCe*0.6/max(self.emg0_quad))
        self.emg0_bic = 100*self.emg0_bic*(self.MVCf*0.6/max(self.emg0_bic))

def run_third_procedure():

    # 0 is raw_signal, 1 is with bwh
    filter_opt = 1

    avg = 1
    
    Step3 = ThirdProcedure()

    if filter_opt and avg==0:
        Step3.get_data()
        Step3.filter_signal()
        Step3.plot_signals(lim=[-0.10,0.10])
    elif filter_opt==0 and avg==0:
        Step3.get_data()
        Step3.plot_signals(lim=[1.25,1.85])
    else:
        Step3.get_data()
        Step3.filter_signal()
        Step3.average_signal()
        Step3.plot_signals(lim=[-50,50], wdth = 0.7)


def main():

    run_third_procedure()
    
    

if __name__ == '__main__':
    main()