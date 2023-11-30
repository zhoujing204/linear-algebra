# Chapter 11: Cross products in the light of linear transformations

(1) Cross products in the light of linear transformations | Chapter 11, Essence of linear algebra - YouTube

[Chapter 11: Cross products in the light of linear transformations](https://www.youtube.com/watch?v=BaM7OCEm3G0)

Transcript:
(00:09) Hey folks! Where we left off, I was talking about how to compute a three-dimensional cross product between two vectors, v x w. It's this funny thing where you write a matrix, whose second column has the coordinates of v, whose third column has the coordinates of w, but the entries of that first column, weirdly, are the symbols i-hat, j-hat and k-hat where you just pretend like those guys are numbers for the sake of computations.

(00:43) Then with that funky matrix in hand, you compute its determinant. If you just chug along with those computations, ignoring the weirdness, you get some constant times i-hat + some constant times j-hat + some constant times k-hat. How specifically you think about computing that determinant is kind of beside the point.

(01:05) All that really matters here is that you'll end up with three different numbers that are interpreted as the coordinates of some resulting vector. From here, students are typically told to just believe that the resulting vector has the following geometric properties. Its length equals the area of the parallelogram defined by v and w.

(01:26) It points in a direction perpendicular to both of v and w. And this direction obeys the right hand rule in the sense that if you point your forefinger along v and your middle finger along w then when you stick up your thumb it'll point in the direction of the new vector. There are some brute force computations that you could do to confirm these facts.

(01:48) But I want to share with you a really elegant line of reasoning. It leverages a bit of background, though. So for this video I'm assuming that everybody has watched chapter 5 on the determinant and chapter 7 where I introduce the idea of duality. As a quick reminder, the idea of duality is that anytime you have a linear transformation from some space to the number line, it’s associated with a unique vector in that space in the sense that performing the linear transformation is the same as taking a dot product with that vector.

(02:22) Numerically, this is because one of those transformations is described by a matrix with just one row where each column tells you the number that each basis vector lands on. And multiplying this matrix by some vector v is computationally identical to taking the dot product between v and the vector you get by turning that matrix on its side.

(02:47) The takeaway is that whenever you're out in the mathematical wild and you find a linear transformation to the number line you will be able to match it to some vector which is called the “dual vector” of that transformation so that performing the linear transformation is the same as taking a dot product with that vector.

(03:06) The cross product gives us a really slick example of this process in action. It takes some effort, but it's definitely worth it. What I'm going to do is to define a certain linear transformation from three dimensions to the number line. And it will be defined in terms of the two vectors v and w. Then, when we associate that transformation with its “dual vector” in 3D space that “dual vector” is going to be the cross product of v and w.

(03:33) The reason for doing this will be that understanding that transformation is going to make clear the connection between the computation and the geometry of the cross product. So to back up a bit, remember in two dimensions what it meant to compute the 2D version of the cross product? When you have two vectors v and w, you put the coordinates of v as the first column of the matrix and the coordinates of w is the second column of matrix then you just compute the determinant.

(04:02) There's no nonsense with basis vectors stuck in a matrix or anything like that. Just an ordinary determinant returning a number. Geometrically, this gives us the area of a parallelogram spanned out by those two vectors with the possibility of being negative, depending on the orientation of the vectors.

(04:19) Now, if you didn't already know the 3D cross product and you're trying to extrapolate you might imagine that it involves taking three separate 3D vectors u, v and w. And making their coordinates the columns of a 3x3 matrix then computing the determinant of that matrix. And, as you know from chapter 5 geometrically, this would give you the volume of a parallelepiped spanned out by those three vectors with the plus or minus sign depending on the right-hand rule orientation of those three vectors.

(04:52) Of course, you all know that this is not the 3D cross product. The actual 3D cross product takes in two vectors and spits out a vector. It doesn't take in three vectors and spit out a number. But this idea actually gets us really close to what the real cross product is. Consider that first vector u to be a variable say, with variable entries x, y and z while v and w remain fixed.

(05:23) What we have then is a function from three dimensions to the number line. You input some vector x, y, z and you get out a number by taking the determinant of a matrix whose first column is x, y, z and whose other two columns are the coordinates of the constant vectors v and w. Geometrically, the meaning of this function is that for any input vector x, y, z, you consider the parallelepiped defined by this vector v and w then you return its volume with the plus or minus sign depending on orientations.

(05:56) Now, this might feel like kind of a random thing to do. I mean, where does this function come from? Why are we defining it this way? And I'll admit at this stage of my kind of feel like it's coming out of the blue. But if you're willing to go along with it and play around with the properties that this guy has it's the key to understanding the cross product.

(06:16) One really important fact about this function is that it's linear. I'll actually leave it to you to work through the details of why this is true based on properties of the determinant. But once you know that it's linear we can start bringing in the idea of “duality”. Once you know that it's linear you know that there's some way to describe this function as matrix multiplication.

(06:41) Specifically, since it's a function that goes from three dimensions to one dimension there will be a 1x3 matrix that encodes this transformation. And the whole idea of duality is that the special thing about transformations from several dimensions to one dimension is that you can turn that matrix on its side and, instead, interpret the entire transformation as the dot product with a certain vector.

(07:09) What we're looking for is the special 3D vector that I'll call p such that taking the dot product between p and any other vector [x, y, z] gives the same result as plugging in [x, y, z] as the first column of a 3x3 matrix whose other two columns have the coordinates of v and w then computing the determinant.

(07:28) I'll get to the geometry of this in just a moment. But right now, let's dig in and think about what this means computationally. Taking the dot product between p and [x, y, z] will give us something times x + something times y + something times z where those somethings are the coordinates of p. But on the right side here, when you compute the determinant you can organize it to look like some constant times x + some constant times y + some constant times z where those constants involve certain combinations of the components of v and w.

(08:04) So, those constants, those particular combinations of the coordinates of v and w are going to be the coordinates of the vector p that we're looking for. But what's going on the right here should feel very familiar to anyone who's actually worked through a cross-product computation. Collecting the constant terms that are multiplied by x, y and z like this is no different from plugging in the symbols i-hat, j-hat and k-hat to that first column and seeing which coefficients aggregate on each one of those terms.

(08:41) It's just that plugging in i-hat, j-hat and k-hat is a way of signaling that we should interpret those coefficients as the coordinates of a vector. So, what all of this is saying is that this funky computation can be thought of as a way to answer the following question: What vector p has the special property that when you take a dot product between p and some vector [x, y, z] it gives the same result as plugging in [x, y, z] to the first column of the matrix whose other two columns have the coordinates of v and w then computing the determinant? That's a bit of a mouthful.

(09:18) But it's an important question to digest for this video. Now for the cool part which ties all this together with the geometric understanding of the cross product that I introduced last video. I'm going to ask the same question again. But this time, we're going to try to answer it geometrically instead of computationally.

(09:37) What 3D vector p has the special property that when you take a dot product between p and some other vector [x, y, z] it gives the same result as if you took the signed volume of a parallelepiped defined by this vector [x, y, z] along with v and w? Remember, the geometric interpretation of a dot product between a vector p and some other vector is to project that other vector onto p then to multiply the length of that projection by the length of p.

(10:14) With that in mind, let me show a certain way to think about the volume of the parallelepiped that we care about. Start by taking the area of the parallelogram defined by v and w then multiply it, not by the length of [x, y, z] but by the component of [x, y, z] that's perpendicular to that parallelogram.

(10:35) In other words, the way our linear function works on a given vector is to project that vector onto a line that's perpendicular to both v and w then, to multiply the length of that projection by the area of the parallelogram spanned by v and w. But this is the same thing as taking a dot product between [x, y, z] and a vector that's perpendicular to v and w with a length equal to the area of that parallelogram.

(11:03) What's more, if you choose the appropriate direction for that vector the cases where the dot product is negative will line up with the cases where the right hand rule for the orientation of [x, y, z], v and w is negative. This means that we just found a vector p so that taking a dot product between p and some vector [x, y, z] is the same thing as computing that determinant of a 3x3 matrix whose columns are [x, y, z], the coordinates of v and w.

(11:35) So, the answer that we found earlier, computationally using that special notational trick must correspond geometrically to this vector. This is the fundamental reason why the computation and the geometric interpretation of the cross product are related. Just to sum up what happened here I started by defining a linear transformation from 3D space to the number line and it was defined in terms of the vectors v and w then I went through two separate ways to think about the “dual vector” of this transformation the vector such that applying the transformation is the same thing as taking a dot product with that vector.

(12:15) On the one hand, a computational approach will lead you to the trick of plugging in the symbols i-hat, j-hat and k-hat to the first column of the matrix and computing the determinant. But, thinking geometrically we can deduce that this duel vector must be perpendicular to v and w with a length equal to the area of the parallelogram spanned out by those two vectors.

(12:40) Since both of these approaches give us a dual vector to the same transformation they must be the same vector. So that wraps up dot products and cross products. And the next video will be a really important concept for linear algebra “change of basis”

Generate with Glarity.
