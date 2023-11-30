# Chapter 10: Cross products

(1) Cross products | Chapter 10, Essence of linear algebra - YouTube
<https://www.youtube.com/watch?v=eu6i7WJeinw>

Transcript:
(00:09) Last video, I've talked about the dot product. Showing both the standard introduction to the topic, as well as a deeper view of how it relates to linear transformations. I'd like to do the same thing for cross products, which also have a standard introduction along with a deeper understanding in the light of linear transformations.

(00:27) But this time I am dividing it into two separate videos. Here i'll try to hit the main points that students are usually shown about the cross product. And in the next video, I'll be showing a view which is less commonly taught, but really satisfying when you learn it. We'll start in two dimensions.

(00:42) If you have two vectors v̅ and w̅, think about the parallelogram that they span out What i mean by that is, that if you take a copy of v̅ and move its tail to the tip of w̅, and you take a copy of w̅ And move its tail to the tip of v̅, the four vectors now on the screen enclose a certain parallelogram. The cross product of v̅ and w̅, written with the X-shaped multiplication symbol, is the area of this parallelogram.

(01:09) Well, almost. We also need to consider orientation. Basically, if v̅ is on the right of w̅, then v̅×w̅ is positive and equal to the area of the parallelogram. But if v̅ is on the left of w̅, then the cross product is negative, namely the negative area of that parallelogram. Notice this means that order matters.

(01:33)  If you swapped v̅ and w̅ instead taking w̅×v̅, the cross product would become the negative of whatever it was before. The way I always remember the ordering here is that when you take the cross product of the two basis vectors in order, î×ĵ, the results should be positive. In fact, the order of your basis vectors is what defines orientation so since î is on the right of ĵ, I remember that v̅×w̅ has to be positive whenever v̅ is on the right of w̅.

(02:01) So, for example with the vector shown here, I'll just tell you that the area of that parallelogram is 7. And since v̅ is on the left of w̅, the cross product should be negative so v̅×w̅ is -7. But of course you want to be able to compute this without someone telling you the area. This is where the determinant comes in.

(02:23) So, if you didn't see Chapter 5 of this series, where I talk about the determinant now would be a really good time to go take a look. Even if you did see it, but it was a while ago. I'd recommend taking another look just to make sure those ideas are fresh in your mind. For the 2-D cross-product v̅×w̅, what you do is you write the coordinates of v̅ as the first column of the matrix and you take the coordinates of w̅ and make them the second column then you just compute the determinant.
(02:52) This is because a matrix whose columns represent v̅ and w̅ corresponds with a linear transformation that moves the basis vectors î and ĵ to v̅ and w̅. The determinant is all about measuring how areas change due to a transformation. And the prototypical area that we look at is the unit square resting on î and ĵ.

(03:17) After the transformation, that square gets turned into the parallelogram that we care about. So the determinant which generally measures the factor by which areas are changed, gives the area of this parallelogram; since it evolved from a square that started with area 1. What's more if v̅ is on the left of w̅, it means that orientation was flipped during that transformation, which is what it means for the determinant to be negative.

(03:44) As an example let's say v̅ has coordinates negative (-3,1) and w̅ has coordinates (2,1). The determinant of the matrix with those coordinates as columns is (-3·1) - (2·1), which is -5. So evidently the area of the parallelogram we define is 5 and since v̅ is on the left of w̅, it should make sense that this value is negative.

(04:13)  As with any new operation you learn I'd recommend playing around with this notion of it in your head just to get kind of an intuitive feel for what the cross product is all about. For example you might notice that when two vectors are perpendicular or at least close to being perpendicular their cross product is larger than it would be if they were pointing in very similar directions.

(04:31)  Because the area of that parallelogram is larger when the sides are closer to being perpendicular. Something else you might notice is that if you were to scale up one of those vectors, perhaps multiplying v̅ by three then the area of that parallelogram is also scaled up by a factor of three. So what this means for the operation is that 3v̅×w̅ will be exactly three times the value of v̅×w̅ .

(04:57) Now, even though all of this is a perfectly fine mathematical operation what i just described is technically not the cross-product. The true cross product is something that combines two different 3D vectors to get a new 3D vector. Just as before, we're still going to consider the parallelogram defined by the two vectors that were crossing together.

(05:19)  And the area of this parallelogram is still going to play a big role. To be concrete let's say that the area is 2.5 for the vectors shown here but as I said the cross product is not a number it's a vector. This new vector's length will be the area of that parallelogram which in this case is 2.5.

(05:38)  And the direction of that new vector is going to be perpendicular to the parallelogram. But which way!, right? I mean there are two possible vectors with length 2.5 that are perpendicular to a given plane. This is where the right hand rule comes in. Put the fore finger of your right hand in the direction of v̅ then stick out your middle finger in the direction of w̅.

(06:00) Then when you point up your thumb, that's the direction of the cross product. For example let's say that v̅ was a vector with length 2 pointing straight up in the Z direction and w̅ is a vector with length 2 pointing in the pure Y direction. The parallelogram that they define in this simple example is actually a square, since they're perpendicular and have the same length.

(06:24) And the area of that square is 4. So their cross product should be a vector with length 4. Using the right hand rule, their cross product should point in the negative X direction. So the cross product of these two vectors is -4·î. For more general computations, there is a formula that you could memorize if you wanted but it's common and easier to instead remember a certain process involving the 3D determinant.

(06:55) Now, this process looks truly strange at first. You write down a 3D matrix where the second and third columns contain the coordinates of v̅ and w̅. But for that first column you write the basis vectors î, ĵ and k̂. Then you compute the determinant of this matrix. The silliness is probably clear here. What on earth does it mean to put in a vector as the entry of a matrix? Students are often told that this is just a notational trick.

(07:26)  When you carry out the computations as if î, ĵ and k̂ were numbers, then you get some linear combination of those basis vectors. And the vector defined by that linear combination, students are told to just believe, is the unique vector perpendicular to v̅ and w̅ whose magnitude is the area of the appropriate parallelogram and whose direction obeys the right hand rule.

(07:50) And, sure!. In some sense this is just a notational trick. But there is a reason for doing in. It's not just a coincidence that the determinant is once again important. And putting the basis vectors in those slots is not just a random thing to do. To understand where all of this comes from it helps to use the idea of duality that I introduced in the last video.

(08:13) This concept is a little bit heavy though, so I'm putting it in a separate follow-on video for any of you who are curious to learn more. Arguably it falls outside the essence of linear algebra. The important part here is to know what that cross product vector geometrically represents. So if you want to skip that next video, feel free.

(08:31)  But for those of you who are willing to go a bit deeper and who are curious about the connection between this computation and the underlying geometry, the ideas that I will talk about in the next video or just a really elegant piece of math.

Generate with Glarity.
