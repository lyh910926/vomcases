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
  input_10:
    default: VP
    streamable: false
    type: string
  input_11:
    default: Pres
    streamable: false
    type: string
  input_12:
    default: d
    streamable: false
    type: string
  input_2:
    default:
      class: File
      path: ../../data/VOM_input/HowardSprings/0_benchmark/dailyweather.prn
    streamable: false
    type: File
  input_3:
    default: linear
    streamable: false
    type: string
  input_4:
    default: data/VOM_input/HowardSprings/9_weather/dailyweather.prn
    streamable: false
    type: string
  input_5:
    default:
      class: File
      path: ../../data/Silo/howard.txt
    streamable: false
    type: File
  input_6:
    default: T.Max
    streamable: false
    type: string
  input_7:
    default: T.Min
    streamable: false
    type: string
  input_8:
    default: Rain
    streamable: false
    type: string
  input_9:
    default: Radn
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
      input_10: input_2
      input_11: input_3
      input_12: input_4
      input_2: input_5
      input_3: input_6
      input_4: input_7
      input_5: input_8
      input_6: input_9
      input_7: input_10
      input_8: input_11
      input_9: input_12
    out:
    - output_0
    run: 8199bf4fd3444f04b6f20fd237f285de_python3.cwl
