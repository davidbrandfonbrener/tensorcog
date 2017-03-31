import tensorflow as tf
import backend as B
import task as task

params = task.set_params(epochs=200, sample_size= 64, input_wait=5, stim_dur=5, quiet_gap=10, nturns=5, N_rec=50, rec_noise=0.05,
                        stim_noise=0.1, dale_ratio=.8, tau=100)
generator = task.generate_train_trials(params)
model = B.Model(2, 50, 1, 80, .9, .1, .8, .1, 64)
sess = tf.Session()
B.train(sess, model, generator, .001, 50000, 64, 10, .8)

data = generator.next()
B.visualize_2_input_one_output_trial(sess, model, data)
