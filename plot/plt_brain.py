import numpy as np
import neurite as ne



def ne_plot_slices(array, titles=None, seg=False):

    if titles is None:
        titles = ["" for i in range(len(array))]

    if seg:
        img = [np.rot90(np.argmax(i, axis=-1), -1) for i in array]
        ne.plot.slices(img, titles = titles)

    else:
        img = [np.rot90(i, -1) for i in array]
        ne.plot.slices(img, titles = titles, cmaps=['gray'], do_colorbars=True)

