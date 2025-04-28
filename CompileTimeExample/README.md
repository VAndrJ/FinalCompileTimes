xcodebuild -project FinalCompileTimeExample.xcodeproj -scheme FinalCompileTimeExample -configuration Debug clean build -showBuildTimingSummary

SwiftCompile

Umbrella + Single class files + Multiple classes file

1 + 1024 + 1024

[
35.868,
35.596,
33.366,
33.895,
33.401,
34.813,
34.364,
33.517,
34.038,
33.202,
32.875,
33.112,
]

1 + 2048 + 2048

[
80.358,
79.688,
79.182,
80.143,
79.424,
80.775,
80.167,
80.860,
79.532,
80.697,
79.958,
79.760,
]


xcodebuild -project FinalCompileTimeExample.xcodeproj -scheme FinalCompileTimeExample -configuration Release clean build -showBuildTimingSummary

1 + 1024 + 1024

[
42.125,
41.261,
42.051,
41.385,
41.923,
41.306,
42.689,
42.221,
41.323,
41.399,
42.098,
41.434,
]

1 + 2048 + 2048

[
264.218,
260.252,
263.032,
264.144,
261.331,
262.691,
260.793,
264.906,
262.615,
261.909,
262.387,
262.437,
]
