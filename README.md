remix-tree
==========

constructs a binary tree out of audio segments then traverse it generating a new audio file

A echonest's remix (http://code.google.com/p/echo-nest-remix/) hack.

 * uploads "../zambi.mp3" to echonest  (http://developer.echonest.com/docs/v4/track.html#upload)
 * analyses it (http://developer.echonest.com/docs/v4/track.html#analyze)
 * get a list of segments (a set of sound entities (typically under a second) each relatively uniform in timbre and harmony.  
Segments are characterized by their perceptual onsets and duration in seconds, loudness (dB), pitch and timbral 
content.)
 * using one of the segment's properties (start, duration, timbre, loudness_begin, loudness_max, time_loudness_max or loudness_end) as a key insert into a binary tree. 
 * traverse the binary tree generating a new sound file ("../inorder.mp3"). Traversal methods are pre-order, in-order and post-order (http://en.wikipedia.org/wiki/Tree_traversal#Depth-first_traversal)


Conclusion: 
all results are pretty random. 
