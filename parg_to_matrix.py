import numpy as np
import matplotlib.pyplot as plt

paragraph = ("Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length:"
             " a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality,"
             " though, the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph"
             " is defined as “a group of sentences or a single sentence that forms a unit."
             " Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some "
             "styles of writing, particularly journalistic styles, a paragraph can be just one sentence long. Ultimately"
             "a paragraph is a sentence or group of sentences that support one main idea. In this handout, we will refer"
             " to this as the “controlling idea,” because it controls what happens in the rest of the paragraph.Example paragraph is hard what to do right now")

text = paragraph.split()
arr = np.asarray(text)
arr2 = np.array([])
for i in range(len(arr)):
    uzunluk = len(arr[i])
    arr2 = np.append(arr2, uzunluk)


arr2 = np.reshape(arr2, (12,12))

first_y = arr2[:,0]
first_x = arr2[0,:]

j = 1
for i in range(12):
    column = arr2[:,i]
    plt.scatter(np.repeat(j,12),column)
    column = np.array([])
    j+=1


temp_y = np.array([8.5,4,6,6,2.5,2.7,2.5,2,1,1,1,6])
temp_x = np.arange(1,13,1)
print(temp_x)
plt.plot(temp_x,temp_y)



plt.xlim(0,14)
plt.show()

