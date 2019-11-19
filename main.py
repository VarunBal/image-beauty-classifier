import tflearn
from alexnet_small import alexnet
import fetch_data

training_data = fetch_data.main()

X, Y = training_data[0],training_data[1]
##print(X)
##print(Y)

network=alexnet()

model = tflearn.DNN(network, checkpoint_path='model_alexnet',
                    max_checkpoints=1, tensorboard_verbose=2,tensorboard_dir='log')
model.fit(X, Y, n_epoch=10, validation_set=0.1, shuffle=True,
          show_metric=True, batch_size=64, snapshot_step=200,
          snapshot_epoch=False, run_id='alexnet_tdgcanvas')
model.save('model-1.tfl')
