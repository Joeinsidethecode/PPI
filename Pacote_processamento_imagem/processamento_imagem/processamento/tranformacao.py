from skimage.transform import resize

def redimensionar_imagem(imagem,proporcao):
    assert 0 <= proporcao <= 1, 'Especificar uma proporção válida entre 0  e 1' 
    altura = round(imagem.shape[0] * proporcao)
    largura = round(imagem.shape[1] * proporcao)
    imagem_redimensionada = resize(imagem(altura,largura),anti_aliasing=True)
    return imagem_redimensionada