# interview-tree
Input a value and create a tree of that depth with certain specific features

Higher level explanation:

Simply put, a default tree is first created. Then, breath first search is used to traverse the tree and number the nodes in such a way that a connection can exist between the nodes. Parent nodes determine the child node values, and the child node can also hint at what the parent value is. The position of the Nth node will be the value of ((n+1)/2) + ((n-1)/2). To provide an example, node #5 = ((5+1)/2) + ((5-1)/2) which is true, as 3 + 2 = 5. This is the property that was used to form the crux of the logic for this tree. Now that the parent nodes are determined, the value of the child node = left parent value + right parent value. If the node is an end node (left-most node or right-most node), then the value defaults to 1. 

Commit Sample:

I didn't create this git repository until this morning because I forgot to do the git part of the assignment from the beginning. (I've actually only ever used git one other time and that was a few years ago for one class). 

So, unfortunately, the code had been written and completed so it wouldn't make sense for me to backtrack and recreate the process on git. 

I can provide an example of when I might commit though, based on my knowledge of how often I save code when I'm working on it:

Usually, the code will be saved at least once a day, providing I work on it then. Just out of general practice. Each time a new element gets added, whether or not that element stays in the final code, I'd push it to git. Each time an element works, the code would be pushed. So, I'd push when the tree was first created, when BFT was used, when the logic behind populatetree was set in place. I'm not the type who would commit after every single line of code. I look at code as a compilation of elements, so again, each time a new element (section) was completed, I would push. Also, if I was doing one major process and changed it radically, I would push and comment something like: "Code process changed from x to y" for others to know. For example, earlier, I was considered using Depth first search, and tried that out but changed my mind, so I would indicate that. 
