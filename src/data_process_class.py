import os
import math
import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2 
from tqdm import tqdm
from mpl_toolkits.mplot3d import Axes3D
from .MatrixTB_2D_class import MatrixTB_2D

class DataProcess:
    def __init__(self, folder_path, suffix, savefig_flag_loop):
        self.cfg_path = folder_path
        self.suffix = suffix
        self.Matrix_2D = None
        self.flag = savefig_flag_loop

    def draw_2D_heatmap(self):
        plt.matshow(self.Matrix_2D, cmap='hot')
        plt.colorbar()
        # save figure
        fig = plt.gcf() # get figure
        plt.margins(0,0)
        fig_savename = "HeatMap_" + str(self.flag) + ".png"
        fig.savefig(fig_savename, dpi=500)
        plt.show()

    def draw_3D_figure(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        matrix_size = self.Matrix_2D.shape
        X = np.arange(0, matrix_size[1], 1)
        Y = np.arange(0, matrix_size[0], 1)
        X,Y = np.meshgrid(X,Y)
        ax.plot_surface(X,Y,self.Matrix_2D, rstride=1, cstride=1, cmap="rainbow")
        plt.show()

    def SizeDistribution_jpg(self):
        size_delta = [10, 10]
        size_Matrix_TB_2D = MatrixTB_2D()
        SD_Matrix_output = np.zeros((10, 10))
        SD_Matrix_output = size_Matrix_TB_2D.matrix_make(SD_Matrix_output, size_delta)
        for root, dirs, files in os.walk(self.cfg_path):
            for file_path in tqdm(files):
                if os.path.splitext(file_path)[1] == self.suffix:
                    file_path = os.path.join(self.cfg_path, file_path)
                    img = cv2.imread(file_path)
                    size = img.shape
                    size_delta[0] = round(size[0]/10) + 1
                    size_delta[1] = round(size[1]/10) + 1
                    SD_Matrix_output = size_Matrix_TB_2D.matrix_make(SD_Matrix_output, size_delta)
                    ds_row = round(size[0]/10)
                    ds_columns = round(size[1]/10)
                    SD_Matrix_output[ds_row][ds_columns] = SD_Matrix_output[ds_row][ds_columns] + 1
        
        # don't delete the code
        self.Matrix_2D = SD_Matrix_output
        # self.draw_3D_figure()
        self.draw_2D_heatmap()

        return SD_Matrix_output


