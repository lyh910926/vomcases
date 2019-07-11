class: Workflow
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_sh/gis_analysis.sh
    streamable: false
    type: File
  input_10:
    default: 7.5d0
    streamable: false
    type: string
  input_11:
    default: '0.2'
    streamable: false
    type: string
  input_12:
    default: work/HowardSprings/freedrainage_cpcff1.0/vom_namelist
    streamable: false
    type: string
  input_13:
    default: s
    streamable: false
    type: string
  input_14:
    default: 1.0d-6
    streamable: false
    type: string
  input_15:
    default: '2.49'
    streamable: false
    type: string
  input_16:
    default: '2.0'
    streamable: false
    type: string
  input_17:
    default: '6.6'
    streamable: false
    type: string
  input_18:
    default: 2.5d-6
    streamable: false
    type: string
  input_2:
    default:
      class: File
      path: ../../data/ELVIS/howardsprings.tif
    streamable: false
    type: File
  input_3:
    default: '131.150007276'
    streamable: false
    type: string
  input_4:
    default: '2.4882868434'
    streamable: false
    type: string
  input_5:
    default: data/ELVIS/howard_stats.txt
    streamable: false
    type: string
  input_6:
    default:
      class: File
      path: ../../src_py/write_namelist.py
    streamable: false
    type: File
  input_7:
    default: 0.065d0
    streamable: false
    type: string
  input_8:
    default: 0.41d0
    streamable: false
    type: string
  input_9:
    default: 1.89d0
    streamable: false
    type: string
outputs:
  output_0:
    outputSource: step_1/output_0
    streamable: false
    type: File
  output_1:
    outputSource: step_2/output_0
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
    run: ca98ae208d934c658b22d0fdb58d31f4_bash.cwl
  step_2:
    in:
      input_1: input_6
      input_10: input_7
      input_11: input_8
      input_12: input_9
      input_13: input_10
      input_14: input_11
      input_15: input_12
      input_2: input_13
      input_3: step_1/output_0
      input_4: input_14
      input_6: input_15
      input_7: input_16
      input_8: input_17
      input_9: input_18
    out:
    - output_0
    run: d356bf00611a437dbbce93dda49d6ece_python3.cwl
