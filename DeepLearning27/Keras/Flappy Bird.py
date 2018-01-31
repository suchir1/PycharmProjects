import wrapped_flappy_bird as game
x_t1_colored, r_t, terminal = game_state.frame_step(a_t)
x_t1 = skimage.color.rgb2gray(x_t1_colored)
x_t1 = skimage.transform.resize(x_t1,(80,80))
x_t1 = skimage.exposure.rescale_intensity(x_t1, out_range=(0, 255))

x_t1 = x_t1.reshape(1, 1, x_t1.shape[0], x_t1.shape[1])
s_t1 = np.append(x_t1, s_t[:, :3, :, :], axis=1)


def buildmodel():
    print("Now we build the model")
    model = Sequential()
    model.add(Convolution2D(32, 8, 8, subsample=(4, 4), init=lambda shape, name: normal(shape, scale=0.01, name=name),
                            border_mode='same', input_shape=(img_channels, img_rows, img_cols)))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 4, 4, subsample=(2, 2), init=lambda shape, name: normal(shape, scale=0.01, name=name),
                            border_mode='same'))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 3, 3, subsample=(1, 1), init=lambda shape, name: normal(shape, scale=0.01, name=name),
                            border_mode='same'))
    model.add(Activation('relu'))
    model.add(Flatten())
    model.add(Dense(512, init=lambda shape, name: normal(shape, scale=0.01, name=name)))
    model.add(Activation('relu'))
    model.add(Dense(2, init=lambda shape, name: normal(shape, scale=0.01, name=name)))

    adam = Adam(lr=1e-6)
    model.compile(loss='mse', optimizer=adam)
    print("We finish building the model")
    return model

init=lambda shape, name: normal(shape, scale=0.01, name=name)
if t > OBSERVE:
    #sample a minibatch to train on
    minibatch = random.sample(D, BATCH)

    inputs = np.zeros((BATCH, s_t.shape[1], s_t.shape[2], s_t.shape[3]))   #32, 80, 80, 4
    targets = np.zeros((inputs.shape[0], ACTIONS))                         #32, 2

    #Now we do the experience replay
    for i in range(0, len(minibatch)):
        state_t = minibatch[i][0]
        action_t = minibatch[i][1]   #This is action index
        reward_t = minibatch[i][2]
        state_t1 = minibatch[i][3]
        terminal = minibatch[i][4]
        # if terminated, only equals reward

        inputs[i:i + 1] = state_t    #I saved down s_t

        targets[i] = model.predict(state_t)  # Hitting each buttom probability
        Q_sa = model.predict(state_t1)

        if terminal:
            targets[i, action_t] = reward_t
        else:
            targets[i, action_t] = reward_t + GAMMA * np.max(Q_sa)

        loss += model.train_on_batch(inputs, targets)

    s_t = s_t1
    t = t + 1

if random.random() <= epsilon:
    print("----------Random Action----------")
    action_index = random.randrange(ACTIONS)
    a_t[action_index] = 1
else:
    q = model.predict(s_t)       #input a stack of 4 images, get the prediction
    max_Q = np.argmax(q)
    action_index = max_Q
    a_t[max_Q] = 1
