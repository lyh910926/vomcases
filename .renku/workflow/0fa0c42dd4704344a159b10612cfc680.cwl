class: Workflow
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/adj_dailyweather.py
    streamable: false
    type: File
  input_2:
    default: d
    streamable: false
    type: string
  input_3:
    default:
      class: File
      path: ../../data/VOM_input/HowardSprings/0_benchmark/dailyweather.prn
    streamable: false
    type: File
  input_4:
    default: linear
    streamable: false
    type: string
  input_5:
    default: data/VOM_input/HowardSprings/7_rgdepth/dailyweather.prn
    streamable: false
    type: string
outputs:
  output_0:
    outputSource: step_1/output_0
    streamable: false
    type: File
requirements: []
steps:
  step_1:
    in:
      input_1: input_1
      input_2: input_2
      input_3: input_3
      input_4: input_4
      input_5: input_5
    out:
    - output_0
    run: bdf30955718c4ffe82161075db8ab8ed_python3.cwl
