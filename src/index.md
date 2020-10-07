<link rel="stylesheet" href="style.css" />

---
title: "Sign Language Processing"
link-citations: true
...

Sign Language Processing (SLP) is a field of [artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence) 
concerned with automatic processing and analysis of [sign language](https://en.wikipedia.org/wiki/Sign_language) content.
It is a subfield of both [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing) and 
[computer vision](https://en.wikipedia.org/wiki/Computer_vision).

Challenges in sign language processing frequently involve 
[machine translation of sign languages](https://en.wikipedia.org/wiki/Machine_translation_of_sign_languages)
to written languages (sign language translation) or from written languages (sign language production),
or sign language recognition for sign language understanding.


## Corpora

### Data Formats

The only widely accepted format for sign language data is including videos of the signing, 
and either a [gloss](https://en.wikipedia.org/wiki/Gloss_(annotation)) or a written language translation.
Sign language videos may include a "depth" channel produced by a [time-of-flight camera](https://en.wikipedia.org/wiki/Time-of-flight_camera).

Sign languages have no formal written format. 
There are various language specific notations systems ([si5s](https://en.wikipedia.org/wiki/Si5s), [Stokoe notation](https://en.wikipedia.org/wiki/Stokoe_notation) [@writing:stokoe2005sign])
and various universal notations systems ([SignWriting](https://en.wikipedia.org/wiki/SignWriting), [HamNoSys](https://en.wikipedia.org/wiki/Hamburg_Notation_System) [@writing:prillwitz1990hamburg]) but no writing system has been adopted widely enough, 
by the international Deaf community, that it could be considered the "written form" of a given sign language.

Additionally, sign language corpora may include human [poses](https://en.wikipedia.org/wiki/Pose_(computer_vision)), either recorded with [motion capture](https://en.wikipedia.org/wiki/Motion_capture) technologies,
or estimated from videos using [pose estimation](https://en.wikipedia.org/wiki/Pose_(computer_vision)#Pose_estimation) techniques.
Full body human poses include all the relevant information for sign language processing (manual or non-manual), except for visual cues such as props.

The following table exemplifies the various data formats.
For this example we use [SignWriting](https://en.wikipedia.org/wiki/SignWriting) as the writing system.
Note that the same sign might have two unrelated glosses and the same gloss might have multiple valid texts.

formats.html

### Existing Datasets

The following table contains a curated list of datasets including various sign languages and data formats:

datasets.html

Currently, there is no easy way or agreed upon format to download all datasets, and as such, evaluation on these datasets is scarce.

## Tasks


### Sign Language Detection

Sign language detection [@detection:borg2019sign;@detection:moryossef2020real] is defined as the binary-classification for any
given frame of a video whether a person is using sign-language or not.

@detection:borg2019sign introduced the classification of frames taken from YouTube videos as either signing or not. 
They take a spatial and temporal approach based on VGG-16 [@simonyan2014very] CNN to encode each frame 
and use a [GRU](https://en.wikipedia.org/wiki/Gated_recurrent_unit) [@cho2014learning] 
to encode the sequence of frames, in a window of 20 frames at 5fps.
In addition to the raw frame, they also either encode optical flow history, aggregated motion history, or frame difference.

@detection:moryossef2020real improved upon their method by performing the sign language detection in real-time.
They identified that sign language use involves movement of the body, and such designed a model that works on top of 
human poses rather than directly on the video signal.
They calculate the optical flow norm of every joint detected on the body, and apply a small yet effective contextualized model
to predict for every frame whether the person is signing or not.

### Sign Language Identification

Sign language identification [@identification:gebre2013automatic;@identification:monteiro2016detecting] is defined as the classification between two or more sign languages.
 
@identification:gebre2013automatic found that a simple random-forest classifier can distinguish between 
British Sign Language (BSL) and Greek Sign Language (ENN) with a 95\% F1 score.
This finding is further supported by @identification:monteiro2016detecting which manages to differentiate between 
British Sign Language and French Sign Language (Langue des Signes Française, LSF) with 98\% F1 score in videos with static backgrounds,
and between American Sign Language and British Sign Language with 70\% F1 score for videos mined from popular video sharing sites. 
The authors attribute their success mainly to the different fingerspelling systems, which is two-handed in the case of BSL and one-handed in the case of ASL and LSF.

### Sign Language Recognition, Translation and Production

Sign language translation is generally considered the task of translating between a video in sign language to text in a written language.
Sign language production is the reverse process, of producing a sign language video from text in a written language.
Sign language recognition is the task of recognizing the signs themselves in the sign language, but not necessarily the written language text.


In the following graph we can see a fully connected pentagon where each node is a single data representation, 
and each directed edge represents the task of converting between one data representation to another.

We split the graph in 2: 

- Every edge to the left, on the orange background represents a task in computer vision. These tasks are inherently multilingual, thus generalize over all sign languages.
- Every edge to the right, on the blue background represents a task in natural language processing. These tasks are sign language specific, requiring a specific sign language lexicon or written language tokens.
- Every edge on both backgrounds represents a task requiring a combination of computer vision and natural language processing.

<p>
<span style="font-weight: bold;">Computer Vision</span>
<span style="font-weight: bold;float:right">Natural Language Processing</span>
<object type="image/svg+xml" data="assets/tasks.svg" class="logo"></object>
</p>

In total, there are 20 tasks defined by this graph, with varying amount of previous research.
Every path between two nodes might or might not be valid, depending on how lossy the tasks in the path are.

---

##### Video-to-Pose

Video-to-Pose---commonly known as pose estimation---is the task to detect human figures in images and videos, 
so that one could determine, for example, where someone’s elbow shows up in an image.

This area has been thoroughly researched [@pose:pishchulin2012articulated;@pose:chen2017adversarial;@pose:cao2018openpose;@pose:alp2018densepose]
with objectives varying from predicting 2D / 3D poses, to a selection of a small specific set of landmarks, or a dense mesh of a person.

OpenPose [@pose:cao2018openpose;@pose:simon2017hand;@pose:cao2017realtime;@pose:wei2016cpm] is the first real-time multi-person system to 
jointly detect human body, hand, facial, and foot keypoints (in total 135 keypoints) in 2D on single images.
While their model can estimate the full pose directly from an image in a single inference,
they also suggest a pipeline approach where first they estimate the body pose, and then independently estimate 
the hands and face poses by acquiring higher resolution crops around those areas.
With multiple angles of recording, OpenPose also offers keypoint triangulation in order to reconstruct the pose in 3D.

@pose:alp2018densepose takes a different approach with DensePose. 
Instead of classifying for every keypoint which pixel is most likely, they suggest similarly to semantic segmentation ,
for each pixel to classify which body part it belongs to.
Then, for each pixel, knowing the bodypart, they predict where that pixel is on the body part, relative to a 2D projection of a representative body model.
This approach results in reconstruction of the full body mesh, and allows sampling to find specific keypoints similar to OpenPose.

However, 2D human poses might not be sufficient to fully understand the position and orientation of landmarks in space,
and applying pose estimation per-frame does not take the video temporal movement information into account, 
especially in cases of rapid movement which contain motion blur.

@pose:pavllo20193d developed two methods to convert between 2D poses to 3D poses. 
The first, a supervised method, was trained to use the temporal information between frames to predict the missing Z axis.
The second, an unsupervised method, leveraged the fact that the 2D poses are meerly a projection of an unknown 3D pose, 
and train a model to estimate the 3D pose and back-project to the input 2D poses. This back-projection is a deterministic process, 
and as such it applies constraints on the 3D pose encoder. 

@pose:panteleris2018using suggests converting the 2D poses to 3D using inverse kinematics (IK), 
a process taken from computer animation and robotics to calculate the variable joint parameters needed to place the end of a kinematic chain, 
such as a robot manipulator or animation character's skeleton, in a given position and orientation relative to the start of the chain.
Demonstrating their approach on hand pose estimation, they manually explicitly encode the constraints and limits of each joint, resulting in 26 degrees of freedom.
Then, non-linear least-squares minimization fits a 3D model of the hand to the estimated 2D joint positions, recovering the 3D hand pose.
This is similar to the back-projection used by @pose:pavllo20193d, except here no temporal information is being used.

##### Pose-to-Video

Pose-to-Video, also known as motion-transfer or skeletal animation in the field of robotics and animation is the
conversion of a sequence of poses to a realistic looking video.
For sign language production, this is the final "rendering" to make the produced sign language looks human.

@pose:chan2019everybody demonstrates a semi-supervised approach where they take a set of videos, 
run pose-estimation with OpenPose [@pose:cao2018openpose], and learn an image-to-image translation [@isola2017image]
between the rendered skeleton and the original video.
They demonstrate their approach on human dancing, where they can extract poses from a choreography, 
and render any person as if they were dancing that dance.
They predict two consecutive frames for temporally coherent video results and 
introduce a separate pipeline for a more realistic face synthesis, although still flawed.

@pose:wang2018vid2vid suggest a similar method using DensePose [@pose:alp2018densepose] representations 
in addition to the OpenPose [@pose:cao2018openpose] ones. 
They formalize a different model, with various objectives to optimize for such as background-foreground separation and
temporal coherence by using the previous two timestamps in the input.

Using the same method by @pose:chan2019everybody on "Everybody Dance Now", @pose:girocan2020slrtp asks "Can Everybody Sign Now"?
They evaluate the generated videos by asking signers various tasks after watching them, and comparing the signers ability to
perform these tasks on the original videos, rendered pose videos, and reconstructed videos.
They show that subjects prefer synthesized realistic videos over skeleton visualizations, 
and that out-of-the-box synthesis methods are not really effective enough, 
as subjects struggled to understand the reconstructed videos.

[Deepfakes](https://en.wikipedia.org/wiki/Deepfake) is a technique to replace a person in an 
existing image or video with someone else's likeness [@nguyen2019deep]. 
This technique can be used to improve the unrealistic face synthesis, resulting from not face-specialized models,
or even replace cartoon faces from animated 3D models. 

---

##### Pose-to-Writing
TODO

##### Writing-to-Pose
TODO

---

##### Gloss-to-Text
TODO

##### Text-to-Gloss
TODO

---

##### Video-to-Text
Trivially, this is the task of translating between videos directly to text.
However, doing so is computationally expensive in memory, and so videos are capped at being very short.
Moreover, this direct pipeline does not take advantage of the universalities between sign languages,
and requires large amounts of data to cover the various signing styles and diverse population.

TODO


##### Text-to-Video
TODO

---

##### Video-to-Gloss
TODO

##### Gloss-to-Video
TODO

---

##### Video-to-Writing
TODO

##### Writing-to-Video
TODO

---

##### Pose-to-Gloss
TODO

##### Gloss-to-Pose

To produce a sign language video, @stoll2018sign constructs a lookup-table between glosses and sequences of 2D poses.
They align all pose sequences at the neck joint of a reference skeleton, and group all sequences belonging to the same gloss.
Then, for each group they apply dynamic time warping and average out all sequences in the group to construct the mean pose sequence.
This approach suffers from not having an accurate set of poses aligned to the gloss, and from unnatural motion transitions between glosses.

To alleviate the downsides of the previous work, @stoll2020text2sign constructs a lookup-table of gloss to group of sequences of poses rather than creating a mean pose sequence.
They build a Motion Graph [@min2012motion] - which is a Markov process that can be used to generate new motion sequences that are representative of real motion,
and select the motion primitives (sequence of poses) per gloss with the highest transition probability.
To smooth that sequence and reduce unnatural motion, they use Savitzky–Golay motion transition smoothing filter [@savitzky1964smoothing].

---

##### Pose-to-Text
TODO

##### Text-to-Pose
TODO

---

##### Writing-to-Text
TODO

##### Text-to-Writing
TODO

---

##### Writing-to-Gloss
TODO

##### Gloss-to-Writing
TODO


## References
