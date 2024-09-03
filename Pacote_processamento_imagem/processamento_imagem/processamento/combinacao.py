import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def diferencas(image1, image2):
    assert image1.shape == image2.shape, 'Especificar duas imagens com mesma forma.'
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score,imagem_de_diferenca) = structural_similarity(gray_image1,gray_image2,full=True)
    print('Similaridade de imagens',score)
    diferenca_imagem_normalizada = (imagem_de_diferenca-np.min(imagem_de_diferenca))/(np.max(imagem_de_diferenca)-np.min(imagem_de_diferenca))
    return diferenca_imagem_normalizada 

def transferir_histogramas(image1,image2):
    imagem_combinada = match_histograms(image1,image2,multichannel = True)
    return imagem_combinada  



