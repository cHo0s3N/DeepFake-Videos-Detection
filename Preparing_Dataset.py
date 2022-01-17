import glob
import os 

#------------------------- REAL -------------------------

path_REAL = 'Path to the directory of REAL samples videos'

# Changes the current working directory to the given path . 
os.chdir(path_REAL)

# Loading the given videos 
txtfiles = []
for file in glob.glob("*.mp4"):
   txtfiles.append(file)

# Rename the videos starting from 000-999  
for i in range(len(txtfiles)):
   ss = "{0:03}.mp4".format(i)
   os.rename(txtfiles[i],ss)


# Loading the renamed videos
meta = []
for file in glob.glob("*.mp4"):
   meta.append(file)

# Build REAL meta data for the renamed videos  
x = '{'
for i in range(len(meta)):
   x +='"'+meta[i]+'":{"label":"REAL"}'+',\n'
x = x[:-1:]


print("Done Creating REAL metadata! ")
print("-"*50)

#------------------------- FAKE -------------------------

path_fake = 'Path to the directory of FAKE samples videos'

# Changes the current working directory to the given path . 
os.chdir(path_fake)

# Loading the given videos  
txtfiles = []
for file in glob.glob("*.mp4"):
   txtfiles.append(file)

# Continunig the renaming from last renamed real video
i +=1
for j in range(len(txtfiles)):
   ss = "{0:03}.mp4".format(j+i)
   os.rename(txtfiles[j],ss)

# Loading the renamed videos
meta = []
for file in glob.glob("*.mp4"):
   meta.append(file)


# Build FAKE metadata for the renamed videos  
y='\n'
for i in range(len(meta)):
   y +='"'+meta[i]+'":{"label":"FAKE"}'+',\n'
y = y[:-1:]
y +="}"


all_meta = x+y
print("Done FAKE metadata !!!! ")


# save the output of metadata as json file
file = open('metadata.json', 'w')
file.write(all_meta)
file.close()
os.system("mv metadata.json ../")
