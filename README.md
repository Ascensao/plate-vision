# Plate Vision

**Plate Vision is a sophisticated Python script designed to detect and identify vehicle license plates.**

It provides an optimal solution for scenarios requiring automated vehicle identification, such as gas stations, road toll systems, car park payment systems, and more. Leveraging advanced image processing and recognition algorithms, Plate Vision delivers a high level of accuracy, speed, and reliability. Its versatility also caters to other applications like traffic control, surveillance, logistics, and fleet management, making it an all-inclusive solution for seamless vehicular identification and tracking.

## Example

https://github.com/Ascensao/plate-vision/assets/8701603/236a2e8e-5385-4b72-ad72-ba25ee669f32

## Usage

**Setup**

- Run `pip install -r requirements.txt`

**Models**

- yolov8n.pt (model used to detect all vehicles)
- [license_plates_ascensao.pt](https://app.roboflow.com/ascensao/license_plates_ascensao/1) (model used to detect all license plates)


**Run**

1. Add your video with cars to the root directory and name it 'sample.mp4'.

2. Execute `main.py` --> frames.csv

3. Execute `add_missing_frames.py` --> frames_interpolated.csv

4. Execute `visualize.py` --> out.mp4

5. To run the script again, delete: `frames.csv, 'frames_interpolated.csv', and out.mp4` and add a new `sample.mp4`

**Results**

- View the output video `out.mp4` containing the detected plates.
- `frames.csv` contains all detected vehicles, plates and corresponding coordinates.
- `frames_interpolated.csv` contains all the data of frames.csv but with more frames for a smooth video.

## Features

- The current script is designed to read Portuguese license plates. Support for more regions' license formats will be added in the near future.

- This is a demo version of the code. The complete code is not public for now. If you are interested in the full code that achieves an accuracy of 100%, please contact me at b.ascensao@gmail.com.

- The results currently showcased in this repository are generated using the full version, not the demo version. Therefore, if you run the script with the `sample.mp4` provided in this repo, the outcome will not be exactly the same.

## Buy me a coffee
Whether you use this project, have learned something from it, or just like it, please consider supporting it by buying me a coffee, so I can dedicate more time on open-source projects like this :)

<a href="https://www.buymeacoffee.com/ascensao1" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-yellow.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Contributing

If you are interested in contributing to this project, I would be delighted to have you on board! Please reach me via email at b.ascensao@gmail.com.
