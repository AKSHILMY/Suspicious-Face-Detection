# Lip Movement Tracking
The face and eye movement tracking would not be sufficient for a student to be monitored in a lab as a student could silently speak to the adjacent person surpassing the other detections.
This tracking procedure is to ensure that the person monitored by the system does not speak with another person.

## Proposed Method
A simple RNN based detector watches lip movements in a sequence of video frames , thus  determines whether someone is speaking. The detector can be run in real time on a video file, or on the output of a webcam.

### The RNN's detection algorithm :

1. Accept a sequence of frames with configurable sequence length
2. For each video frame in this sequence:

   - Convert it to a gray frame.

   - Detect the face in the frame using a [face detector](https://github.com/AKSHILMY/Suspicious-Face-Detection/tree/main/Implementation/Face%20Detection%20Feature).
   
   - Feed the detector's bounding box to a facial landmarks predictor. 

   - From the landmark predictor, fetch the points that mark the inner edges of the top and bottom lip. In case of the dlib predictor, these are part numbers 61, 62, 63 for the top lip, and 67, 66, 65 on the bottom lip. 
   See figure below.

   - Calculate the average pixel separation between part pairs.
    $$ avg = {dist(61, 67) + dist(62, 66) + dist(63, 65) \over 3} $$

   - Store away this distance value into the lip separation sequence.

3. Perform `min-max scaling` over the sequence.

4. Feed this normalized lip separation sequence into the RNN.

5. The RNN outputs a 2-element tuple (speech, silence) containing the respective probability of whether the speaker was speaking or was silent during the preceding 25 video frames.

6. Slide forward the 25-frame window by one frame through the input video, and repeat steps 2 through 5.

### Some datasets to look at are:
   1. [GRID](http://spandh.dcs.shef.ac.uk/gridcorpus/),
   2. [AMFED](https://www.affectiva.com/facial-expression-dataset/),
   3. [DISFA](http://www.engr.du.edu/mmahoor/DISFA.htm),
   4. [HMDB](http://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/),
   5. [Cohn-Kanade](http://www.pitt.edu/~emotion/ck-spread.htm),
