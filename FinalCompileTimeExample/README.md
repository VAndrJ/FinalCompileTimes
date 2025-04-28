xcodebuild -project FinalCompileTimeExample.xcodeproj -scheme FinalCompileTimeExample -configuration Debug clean build -showBuildTimingSummary

SwiftCompile

Umbrella + Single class files + Multiple classes file

1 + 1024 + 1024

[
33.071,
35.199,
35.193,
34.361,
35.019,
33.778,
33.477,
33.509,
35.273,
32.577,
33.072,
33.756,
]

1 + 2048 + 2048

[
79.255,
81.518,
79.623,
82.873,
80.684,
81.896,
79.675,
78.452,
79.816,
78.365,
82.007,
79.163,
]


xcodebuild -project FinalCompileTimeExample.xcodeproj -scheme FinalCompileTimeExample -configuration Release clean build -showBuildTimingSummary

1 + 1024 + 1024

[
42.892,
42.513,
41.474,
42.646,
41.939,
42.182,
42.151,
42.281,
41.901,
41.777,
42.366,
41.752,
]

1 + 2048 + 2048

[
256.459,
261.880,
258.736,
261.599,
261.612,
259.290,
260.813,
261.785,
258.021,
258.725,
259.219,
259.773,
]
