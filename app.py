import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt

"""
The speedup from using Numpy is ridiculous...
Image Histograms match Gimp, not compared with Photoshop... 
"""

def main():
    img = cv2.imread("/Users/lukemccartney/Documents/Programming Languages/Python/python-frequency/img/_DSC9483.jpg")
    img_array = np.array(img)
    print(img_array)
    print("Shape of Image: \t", img_array.shape)
    plot_frequencies(img_array)

def plot_frequencies(img_array: np.array(int)) -> None:
    channel_r = img_array[:,:,0]
    channel_g = img_array[:,:,1]
    channel_b = img_array[:,:,2]
    channel_r_frequency = frequency(channel_r)
    print("Shape of Red Channel:\t", channel_r.shape)
    channel_g_frequency = frequency(channel_g)
    print("Shape of Green Channel:\t", channel_g.shape)
    channel_b_frequency = frequency(channel_b)
    print("Shape of Blue Channel:\t", channel_b.shape)
    fig, axs = plt.subplots(3, sharex=True)
    fig.suptitle("Colour Channel Frequencies")
    axs[0].plot(channel_r_frequency,'tab:red')
    axs[1].plot(channel_g_frequency, 'tab:green')
    axs[2].plot(channel_b_frequency, 'tab:blue')
    plt.show()

def frequency(channel: np.array(int)) -> np.array(int):
    flat_channel = channel.flatten()
    """
    frequency_array = np.zeros(shape=(256,1))
    for i, pixel in enumerate(flat_channel):
        frequency_array[pixel] += 1
    """
    np_unique = np.unique(flat_channel, return_counts=True)[1]
    return np_unique

if __name__ == '__main__':
    main()
