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
    default: 0.065d0
    inputBinding:
      position: 10
      prefix: --i_thetar
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_11:
    default: 0.41d0
    inputBinding:
      position: 11
      prefix: --i_thetas
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_12:
    default: 1.89d0
    inputBinding:
      position: 12
      prefix: --i_nvg
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_13:
    default: 7.5d0
    inputBinding:
      position: 13
      prefix: --i_avg
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_14:
    default: '0.30'
    inputBinding:
      position: 14
      prefix: --i_delz
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_15:
    default: work/additional_analyses/sens_delz/HS_0.30/vom_namelist
    inputBinding:
      position: 15
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
    default: 1.0d-6
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
    default: '2.0'
    inputBinding:
      position: 7
      prefix: --i_cgs
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_8:
    default: '6.4'
    inputBinding:
      position: 8
      prefix: --i_zr
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_9:
    default: 2.5d-6
    inputBinding:
      position: 9
      prefix: --i_ksat
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_15)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: work/additional_analyses/sens_delz/HS_0.30
    writable: true
successCodes: []
temporaryFailCodes: []
