
import matplotlib.pyplot as plt


def plot_hist_pickle(hist, title='Loss'):
    epochs = np.arange(len(hist['loss']))
    plt.figure(figsize=(17,5)) 
    plt.subplot(1, 2, 1)
    plt.grid()
    plt.plot(hist['loss'], '.-')
    plt.ylabel('loss')
    plt.xlabel('epochs');
    plt.title(title)
    plt.subplot(1, 2, 2)
    plt.grid()
    nb_epochs = len(hist['loss']) // 2
    plt.plot(epochs[-nb_epochs:], hist['loss'][-nb_epochs:], '.-')
    plt.ylabel('loss')
    plt.xlabel('epochs');
    plt.show()

def plot_hist_pickle_by_key(hist, title='Loss', keys=['loss']):
    epochs = np.arange(len(hist[keys[0]]))
    plt.figure(figsize=(17,5)) 
    plt.grid()
    for i in keys:
        plt.plot(hist[i], '.-', label=i)
    plt.ylabel('loss')
    plt.xlabel('epochs');
    plt.legend()
    plt.title(title)
    plt.show()
