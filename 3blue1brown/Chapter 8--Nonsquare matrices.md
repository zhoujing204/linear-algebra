# Chapter 8: Nonsquare matrices as transformations between dimensions

> On this quiz, I asked you to find the determinant of 2*3 matrix. Some of you, to my great amusement, actually tried to do this. --(Via mathprofessorquotes.com, no name listed)

(1) Nonsquare matrices as transformations between dimensions | Chapter 8, Essence of linear algebra - YouTube

[https://www.youtube.com/watch?v=v8VSDg_WQlA](https://www.youtube.com/watch?v=v8VSDg_WQlA)

Transcript:
(00:00) Hey, everyone! I've got another quick footnote for you between chapters today. When I talked about linear transformation so far, I've only really talked about transformations from 2-D vectors to other 2-D vectors, represented with 2-by-2 matrices; or from 3-D vectors to other 3-D vectors, represented with 3-by-3 matrices.

(00:29) But several commenters have asked about non-square matrices, so I thought I'd take a moment to just show with those means geometrically. By now in the series, you actually have most of the background you need to start pondering a question like this on your own. But I'll start talking through it, just to give a little mental momentum.

(00:44) It's perfectly reasonable to talk about transformations between dimensions, such as one that takes 2-D vectors to 3-D vectors. Again, what makes one of these linear is that grid lines remain parallel and evenly spaced, and that the origin maps to the origin. What I have pictured here is the input space on the left, which is just 2-D space, and the output of the transformation shown on the right.

(01:07) The reason I'm not showing the inputs move over to the outputs, like I usually do, is not just animation laziness. It's worth emphasizing the 2-D vector inputs are very different animals from these 3-D vector outputs, living in a completely separate unconnected space. Encoding one of these transformations with a matrix is really just the same thing as what we've done before.

(01:27) You look at where each basis vector lands and write the coordinates of the landing spots as the columns of a matrix. For example, what you're looking at here is an output of a transformation that takes i-hat to the coordinates (2, -1, -2) and j-hat to the coordinates (0, 1, 1). Notice, this means the matrix encoding our transformation has 3 rows and 2 columns, which, to use standard terminology, makes it a 3-by-2 matrix.

(01:58) In the language of last video, the column space of this matrix, the place where all the vectors land is a 2-D plane slicing through the origin of 3-D space. But the matrix is still full rank, since the number of dimensions in this column space is the same as the number of dimensions of the input space. So, if you see a 3-by-2 matrix out in the wild, you can know that it has the geometric interpretation of mapping two dimensions to three dimensions, Since the two columns indicate that the input space has two basis vectors, and the three rows indicate that the landing spots for each of those basis vectors

(02:35) is described with three separate coordinates. Likewise, if you see a 2-by-3 matrix with two rows and three columns, what do you think that means? Well, the three columns indicate that you're starting in a space that has three basis vectors, so we're starting in three dimensions; and the two rows indicate that the landing spot for each of those three basis vectors is described with only two coordinates, so they must be landing in two dimensions.

(03:01) So it's a transformation from 3-D space onto the 2-D plane. A transformation that should feel very uncomfortable if you imagine going through it. You could also have a transformation from two dimensions to one dimension. One-dimensional space is really just the number line, so transformation like this takes in 2-D vectors and spits out numbers.

(03:26) Thinking about gridlines remaining parallel and evenly spaced is a little bit messy to all of the squishification happening here. So in this case, the visual understanding for what linearity means is that if you have a line of evenly spaced dots, it would remain evenly spaced once they're mapped onto the number line.

(03:44) One of these transformations is encoded with a 1-by-2 matrix, each of whose two columns as just a single entry. The two columns represent where the basis vectors land and each one of those columns requires just one number, the number that that basis vector landed on. This is actually a surprisingly meaningful type of transformation with close ties to the dot product, and I'll be talking about that next video.

(04:06) Until then, I encourage you to play around with this idea on your own, contemplating the meanings of things like matrix multiplication and linear systems of equations in the context of transformations between different dimensions. Have fun!

Generate with Glarity.
