# Sign Language Processing

Sign Language Processing (SLP) is a field of [artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence) 
concerned with automatic processing and analysis of [sign language](https://en.wikipedia.org/wiki/Sign_language) content.
It is a subfield of both [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing) and 
[Computer Vision](https://en.wikipedia.org/wiki/Computer_vision).

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
There are various notations systems but no writing system has been adopted widely enough, 
by the international Deaf community, that it could be considered the "written form" of a given sign language.

Additionally, sign language corpora may include human [poses](https://en.wikipedia.org/wiki/Pose_(computer_vision)), either recorded with [motion capture](https://en.wikipedia.org/wiki/Motion_capture) technologies,
or estimated from videos using [pose estimation](https://en.wikipedia.org/wiki/Pose_(computer_vision)#Pose_estimation) techniques.
Full body human poses include all the relevant information for sign language processing (manual or non-manual), except for visual cues such as props.

The following table exemplifies the various data formats.
For this example we use "SignWriting" as the writing system.
Note that the same sign might have two unrelated glosses and the same gloss might have multiple valid texts.

{{formats.html}}

### Available Datasets

The following table contains a curated list of datasets including various sign languages and data formats:

{{../dst/datasets.html}}


## Tasks


### Sign Language Detection

Sign language detection <ref names="borg2019sign,moryossef2020real" /> is defined as the binary-classification for any
given frame of a video weather a person is using sign-language or not.

<ref name="borg2019sign" /> introduced the classification of frames taken from YouTube videos as either signing or not. 
They take a spatial and temporal approach based on <ref name="simonyan2014very">VGG-16</ref> CNN to encode each frame 
and use a [GRU](https://en.wikipedia.org/wiki/Gated_recurrent_unit)<pref name="cho2014learning" /> 
to encode the sequence of frames, in a window of 20 frames at 5fps.
In addition to the raw frame, they also either encode optical flow history, aggregated motion history, or frame difference.

<ref name="moryossef2020real" /> improved upon their method by performing the sign language detection in real-time.
They identified that sign language use involves movement of the body, and such designed a model that works on top of 
human poses rather than directly on the video signal.
They calculate the optical flow norm of every joint detected on the body, and apply a small yet effective contextualized model
to predict for every frame weather the person is signing or not.

### Sign Language Identification

Sign language identification <ref names="gebre2013automatic,monteiro2016detecting" /> is defined as the classification between two or more sign languages.

<ref name="gebre2013automatic" /> found that a simple random-forest classifier can distinguish between 
British Sign Language (BSL) and Greek Sign Language (ENN) with a 95\% F1 score.
This finding is further supported by <ref name="monteiro2016detecting" /> which manages to differentiate between 
British Sign Language and French Sign Language (Langue des Signes Française, LSF) with 98\% F1 score in videos with static backgrounds,
and between American Sign Language and British Sign Language with 70\% F1 score for videos mined from popular video sharing sites. 
The authors attribute their success mainly to the different fingerspelling systems, which is two-handed in the case of BSL and one-handed in the case of ASL and LSF.

### Sign Language Recognition, Translation and Production
While seemingly straightforward, sign language 


<object type="image/svg+xml" data="assets/tasks.svg" class="logo"></object>


