from backend.networks import Model
import matplotlib.pyplot as plt
import numpy as np


# visualize network output on a trial, compared to desired output
def visualize_2_input_one_output_trial(model, sess, data):
    preds = model.test(sess, data[0])[0]
    length = data[0].shape[1]
    plt.plot(range(length), data[0][0, :, 0], 'b', data[1][0, :, 0], 'r', range(length), preds[0, :, 0], 'g')
    plt.show()

def show_W_rec(model, sess):
    if model.dale:
        plt.pcolor(np.matmul(abs(model.W_rec.eval(session=sess)), model.dale_rec))
    else:
        plt.pcolor(model.W_rec.eval(session=sess))
    plt.colorbar()
    plt.show()

def show_W_out(model, sess):
    if model.dale:
        plt.pcolor(np.matmul(abs(model.W_out.eval(session=sess)), model.dale_out))
    else:
        plt.pcolor(model.W_out.eval(session=sess))
    plt.colorbar()
    plt.show()
