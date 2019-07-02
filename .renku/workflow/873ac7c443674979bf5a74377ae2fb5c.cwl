class: Workflow
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/write_dailyweather.py
    streamable: false
    type: File
  input_2:
    default: m
    streamable: false
    type: string
  input_3:
    default:
      class: File
      path: ../../data/Silo/dry.txt
    streamable: false
    type: File
  input_4:
    default: c
    streamable: false
    type: string
  input_5:
    default:
      class: File
      path: ../../data/MaunaLoa/weekly_in_situ_co2_mlo.csv
    streamable: false
    type: File
  input_6:
    default: linear
    streamable: false
    type: string
  input_7:
    default: data/VOM_input/DryRiver/dailyweather.prn
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
      input_6: input_6
      input_7: input_7
    out:
    - output_0
    run: 303eb1ad0a004e10965a55a4d464d1dd_python3.cwl
