arguments:
- position: 5
  separate: true
  shellQuote: true
  valueFrom: --i_lat
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/write_namelist.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default: '0.45'
    inputBinding:
      position: 10
      prefix: --i_delz
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_11:
    default: work/additional_analyses/sens_delz/HS_0.45/vom_namelist
    inputBinding:
      position: 11
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default: s
    inputBinding:
      position: 2
      prefix: -i
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default:
      class: File
      path: ../../data/ELVIS/howard_stats.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default: 1.2d-6
    inputBinding:
      position: 4
      prefix: --i_cpccf
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default: '2.49'
    inputBinding:
      position: 6
      prefix: '-1'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default: '0.20'
    inputBinding:
      position: 7
      prefix: --i_zr
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_8:
    default: '0.02'
    inputBinding:
      position: 8
      prefix: --i_go
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_9:
    default: '2.0'
    inputBinding:
      position: 9
      prefix: --i_cgs
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_11)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: work/additional_analyses/sens_delz/HS_0.45
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/write_namelist.py
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/ELVIS/howard_stats.txt
    writable: false
successCodes: []
temporaryFailCodes: []
