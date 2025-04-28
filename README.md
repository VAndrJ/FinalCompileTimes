# Non-final vs Final Classes Compile Times


## To run this test:


- Navigate to the corresponding folder.
- Unzip the archive.
- Open the unzipped folder.
- Open `file_generator.py` and change `num_classes` to half the number of classes you want (`num_classes` classes in one file + `num_classes` classes each in their own file + "umbrella" class).
- Generate the files.
- Run the following command:
```
xcodebuild -project FinalCompileTimeExample.xcodeproj -scheme FinalCompileTimeExample -configuration Release clean build -showBuildTimingSummary
```
- Check the reported `SwiftCompile` compile time.
- Compare it to the results from the other folder.


# My Results on MacBook Air M1

Total of 12 runs. Dropped 1 minimum and 1 maximum value. Averaged the remaining 10 runs.

## num_classes = 1024 (2049 total classes):
---
- Debug without keyword:
### 33.93 s.
- Debug with `final` keyword:
### 34.04 s. (~ +0.32%)
---
- Release without keyword:
### 41.73 s.
- Release with `final` keyword:
### 42.15 s. (~ +1%)
---
## num_classes = 2048 (4097 total classes):
---
- Debug without keyword:
### 80.05 s. 
- Debug with `final` keyword:
### 80.21 s. (~ +0.2%)
---
- Release without keyword:
### 262.56 s.
- Release with `final` keyword:
### 259.96 s. (~ -0.99%)
---
