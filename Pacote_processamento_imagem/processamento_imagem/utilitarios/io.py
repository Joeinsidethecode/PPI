from skimage.io import imread, imsave

def ler_imagem(caminho, is_gray=False):
    imagem = imread(caminho,is_gray=is_gray)
    return imagem

def salvar_imagem(imagem, caminho):
    imsave(caminho, imagem)