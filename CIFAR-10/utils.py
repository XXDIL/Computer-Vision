'''
	These are the code snippits of some of the data preprocessing I had done.
'''


''' ------------------------------- To get the optimal k value for the KNN Classifier ------------------------------- '''

features = FE_model.predict(trainX, verbose=1)
test_features = FE_model.predict(testX, verbose=1)
hist = []

for k in tqdm(range(1, 100)):
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(features, KNN_trainy)

    pred = classifier.predict(test_features)
    pred = pred.reshape(10000, 1)

    acc = np.sum(1*(pred==testy))/testy.shape[0]
    hist.append(acc)
    
plt.figure(figsize=(12,7))
plt.plot(range(1, 100), hist, marker='o')
plt.plot(range(1, 100), np.ones(99)*max(hist), color='lime', linestyle='--')
plt.plot(np.ones(2)*(hist.index(max(hist))+1), range(0,2), color='lime', linestyle='--')
plt.plot(9, 0.8892, color='r', marker='x', markersize=15)
plt.legend(['Trend', 'Y Intercept', 'X Intercept', 'Max Acc'])
plt.ylim(0.883, .89)
plt.xlabel('K value')
plt.ylabel('Accuracy')
plt.title('Trend of Accuracy on Varying K values')
plt.show()


''' ----------------------------------------  Plot Loss and Classification  ---------------------------------------- '''

plt.figure(figsize=(15,9))
plt.subplot(2, 1, 1)
plt.title('Cross Entropy Loss')
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['Train', 'Test'])
plt.subplot(2, 1, 2)
plt.title('Classification Accuracy')
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.show()


''' ------------------------------------------------ CNN model used ------------------------------------------------ '''

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', kernel_regularizer=l2(0.001), input_shape=(32, 32, 3)))
model.add(BatchNormalization())
model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', kernel_regularizer=l2(0.001)))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.2))

model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', kernel_regularizer=l2(0.001)))
model.add(BatchNormalization())
model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', kernel_regularizer=l2(0.001)))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.3))

model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', kernel_regularizer=l2(0.001)))
model.add(BatchNormalization())
model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', kernel_regularizer=l2(0.001)))
model.add(BatchNormalization())
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.4))

model.add(Flatten())
model.add(Dense(128, activation='relu', kernel_initializer='he_uniform', kernel_regularizer=l2(0.001)))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
