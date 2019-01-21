
# No grain no gain!

For Hack Zurich 2017 we worked on an image recognition project that detects unwanted material in a box of grain. This project was proposed by Buhler to ease the processing of grain on a big scale. During harvest a lot of unwanted material is collected between the grain, the aim of this project was to detect how much of these materials were present in a box of grain. We limited the amount of materials to the materials that have been provided by Buhler:
- Pumpkin seeds 
- Red kidney beans 
- Stones
- Straws
- Black lentils 
 
 
 ## Method 
 Buhler provided us with a box containing grain and all other materials, next to this we were handed a Raspberry pi with a normal and infrared camera.  Eventually we decided to take pictures of the grain with our phone and analyze these results, so we could get a head start with the actual task instead of focusing on hardware. 
 
We implemented a simple classification model that classifies every part of the picture into one of the provided categories. We trained the model on pictures of these materials, both taken our-self and found online. After classifying all parts of the picture, the predicted materials are combined and we use that to calculate the presence of every individual material in the picture. 

## Results 
