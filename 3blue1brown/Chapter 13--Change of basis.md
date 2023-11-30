# Chapter 13: Change of basis

(1) Change of basis | Chapter 13, Essence of linear algebra - YouTube
<https://www.youtube.com/watch?v=P2LTAUO1TdA>

Transcript:
(00:00) If I have a vector sitting here in 2D space we have a standard way to describe it with coordinates. In this case, the vector has coordinates [3, 2], which means going from its tail to its tip involves moving 3 units to the right and 2 units up. Now, the more linear-algebra-oriented way to describe coordinates is to think of each of these numbers as a scalar a thing that stretches or squishes vectors.

(00:37) You think of that first coordinate as scaling i-hat the vector with length 1, pointing to the right while the second coordinate scales j-hat the vector with length 1, pointing straight up. The tip to tail sum of those two scaled vectors is what the coordinates are meant to describe. You can think of these two special vectors as encapsulating all of the implicit assumptions of our coordinate system.

(01:03) The fact that the first number indicates rightward motion that the second one indicates upward motion exactly how far unit of distances. All of that is tied up in the choice of i-hat and j-hat as the vectors which our scalar coordinates are meant to actually scale. Anyway to translate between vectors and sets of numbers is called a coordinate system and the two special vectors, i-hat and j-hat, are called the basis vectors of our standard coordinate system.

(01:30) What I'd like to talk about here is the idea of using a different set of basis vectors. For example, let's say you have a friend, Jennifer who uses a different set of basis vectors which I'll call b1 and b2 Her first basis vector b1 points up into the right a little bit and her second vector b2 points left and up Now, take another look at that vector that I showed earlier The one that you and I would describe using the coordinates [3, 2] using our basis vectors i-hat and j-hat.

(02:02) Jennifer would actually describe this vector with the coordinates [5/3, 1/3] What this means is that the particular way to get to that vector using her two basis vectors is to scale b1 by 5/3, scale b2 by 1/3 then add them both together. In a little bit, I'll show you how you could have figured out those two numbers 5/3 and 1/3.

(02:26) In general, whenever Jennifer uses coordinates to describe a vector she thinks of her first coordinate as scaling b1 the second coordinate is scaling b2 and she adds the results. What she gets will typically be completely different from the vector that you and I would think of as having those coordinates.

(02:45) To be a little more precise about the setup here her first basis vector b1 is something that we would describe with the coordinates [2, 1] and her second basis vector b2 is something that we would describe as [-1, 1]. But it's important to realize from her perspective in her system those vectors have coordinates [1, 0] and [0, 1] They are what define the meaning of the coordinates [1, 0] and [0, 1] in her world.

(03:12) So, in effect, we're speaking different languages We're all looking at the same vectors in space but Jennifer uses different words and numbers to describe them. Let me say a quick word about how I'm representing things here when I animate 2D space I typically use this square grid But that grid is just a construct a way to visualize our coordinate system and so it depends on our choice of basis.

(03:37) Space itself has no intrinsic grid. Jennifer might draw her own grid which would be an equally made-up construct meant is nothing more than a visual tool to help follow the meaning of her coordinates. Her origin, though, would actually line up with ours since everybody agrees on what the coordinates [0, 0] should mean.

(04:00) It's the thing that you get when you scale any vector by 0. But the direction of her axes and the spacing of her grid lines will be different, depending on her choice of basis vectors. So, after all this is set up a pretty natural question to ask is How we translate between coordinate systems? If, for example, Jennifer describes a vector with coordinates [-1, 2] what would that be in our coordinate system? How do you translate from her language to ours? Well, what our coordinates are saying is that this vector is -1 b1 + 2 b2.

(04:40) And from our perspective b1 has coordinates [2, 1] and b2 has coordinates [-1, 1] So we can actually compute -1 b1 + 2 b2 as they're represented in our coordinate system And working this out you get a vector with coordinates [-4, 1] So, that's how we would describe the vector that she thinks of as [-1, 2] This process here of scaling each of her basis vectors by the corresponding coordinates of some vector then adding them together might feel somewhat familiar It’s matrix-vector multiplication with a matrix whose columns represent Jennifer's basis vectors in our language In fact, once you understand matrix-vector multiplication

(05:29) as applying a certain linear transformation say, by watching what I've you to be the most important video in this series, chapter 3. There's a pretty intuitive way to think about what's going on here. A matrix whose columns represent Jennifer's basis vectors can be thought of as a transformation that moves our basis vectors, i-hat and j-hat the things we think of when we say [1,0] and [0, 1] to Jennifer's basis vectors the things she thinks of when she says [1, 0] and [0, 1] To show how this works let's walk through what it would mean to take the vector that we think of as having coordinates [-1, 2]

(06:06) and applying that transformation. Before the linear transformation we’re thinking of this vector as a certain linear combination of our basis vectors -1 x i-hat + 2 x j-hat. And the key feature of a linear transformation is that the resulting vector will be that same linear combination but of the new basis vectors -1 times the place where i-hat lands + 2 times the place where j-hat lands.

(06:34) So what this matrix does is transformed our misconception of what Jennifer means into the actual vector that she's referring to. I remember that when I was first learning this it always felt kind of backwards to me. Geometrically, this matrix transforms our grid into Jennifer's grid. But numerically, it's translating a vector described in her language to our language.

(07:01) What made it finally clicked for me was thinking about how it takes our misconception of what Jennifer means the vector we get using the same coordinates but in our system then it transforms it into the vector that she really meant. What about going the other way around? In the example I used earlier this video when I have the vector with coordinates [3, 2] in our system How did I compute that it would have coordinates [5/3, 1/3] in Jennifer system? You start with that change of basis matrix that translates Jennifer's language into ours then you take its inverse.

(07:41) Remember, the inverse of a transformation is a new transformation that corresponds to playing that first one backwards. In practice, especially when you're working in more than two dimensions you'd use a computer to compute the matrix that actually represents this inverse. In this case, the inverse of the change of basis matrix that has Jennifer's basis as its columns ends up working out to have columns [1/3, -1/3] and [1/3, 2/3] So, for example to see what the vector [3, 2] looks like in Jennifer's system we multiply this inverse change of basis matrix by the vector [3, 2] which works out to be [5/3, 1/3]

(08:28) So that, in a nutshell is how to translate the description of individual vectors back and forth between coordinate systems. The matrix whose columns represent Jennifer's basis vectors but written in our coordinates translates vectors from her language into our language. And the inverse matrix does the opposite.

(08:51) But vectors aren't the only thing that we describe using coordinates. For this next part it's important that you're all comfortable representing transformations with matrices and that you know how matrix multiplication corresponds to composing successive transformations. Definitely pause and take a look at chapters 3 and 4 if any of that feels uneasy.

(09:13) Consider some linear transformation like a 90°counterclockwise rotation. When you and I represent this with the matrix we follow where the basis vectors i-hat and j-hat each go. i-hat ends up at the spot with coordinates [0, 1] and j-hat end up at the spot with coordinates [-1, 0] So those coordinates become the columns of our matrix but this representation is heavily tied up in our choice of basis vectors from the fact that we're following i-hat and j-hat in the first place to the fact that we're recording their landing spots in our own coordinate system.

(09:50) How would Jennifer describe this same 90°rotation of space? You might be tempted to just translate the columns of our rotation matrix into Jennifer's language. But that's not quite right. Those columns represent where our basis vectors i-hat and j-hat go. But the matrix that Jennifer wants should represent where her basis vectors land and it needs to describe those landing spots in her language.

(10:21) Here's a common way to think of how this is done. Start with any vector written in Jennifer's language. Rather than trying to follow what happens to it in terms of her language first, we're going to translate it into our language using the change of basis matrix the one whose columns represent her basis vectors in our language.

(10:40) This gives us the same vector but now written in our language. Then, apply the transformation matrix to what you get by multiplying it on the left. This tells us where that vector lands but still in our language. So as a last step apply the inverse change of basis matrix multiplied on the left as usual to get the transformed vector but now in Jennifer's language.

(11:04) Since we could do this with any vector written in her language first, applying the change of basis then, the transformation then, the inverse change of basis That composition of three matrices gives us the transformation matrix in Jennifer's language. it takes in a vector of her language and spits out the transformed version of that vector in her language For this specific example when Jennifer's basis vectors look like [2, 1] and [-1, 1] in our language and when the transformation is a 90°rotation the product of these three matrices if you work through it has columns [1/3, 5/3] and [-2/3, -1/3] So if Jennifer multiplies that matrix

(11:47) by the coordinates of a vector in her system it will return the 90°rotated version of that vector expressed in her coordinate system. In general, whenever you see an expression like A^(-1) M A it suggests a mathematical sort of empathy. That middle matrix represents a transformation of some kind, as you see it and the outer two matrices represent the empathy, the shift in perspective and the full matrix product represents that same transformation but as someone else sees it.

(12:23) For those of you wondering why we care about alternate coordinate systems the next video on eigen vectors and eigen values will give a really important example of this. See you then!

Generate with Glarity.
