import matplotlib.pyplot as plt

def plotar_imagem(imagem):
    plt.figure(figsize=(12,4))
    plt.imshow(imagem, cmap='cinza')
    plt.axis('off')
    plt.show()

def plotar_resultado(*args):
    quantidade_imagens = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=quantidade_imagens, figsize=(12,4))
    lista_nomes = [f'imagem {i}' for i in range(1,quantidade_imagens)]
    lista_nomes.append('resultado')
    for ax, nome, imagem in zip(axis,lista_nomes,args):
        ax.set_title(nome)
        ax.imshow(imagem,cmap='cinza')
        ax.axis('off')
    fig.tight_layout()
    plt.show()

def plotar_histograma(imagem):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12,4),sharex=True,sharey=True)
    lista_cores = ['vermelho','verde','azul']
    for index, (ax,color) in enumerate(zip(axis, lista_cores)):
        ax.set.title(f'{color.title()} histograma')
        ax.hist(imagem[:,:,index].ravel(), bins=256, color=color, alpha=0.8)
    fig.tight_layout()
    plt.show()