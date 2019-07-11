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
    default: 0.078d0
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
    default: 1.56d0
    inputBinding:
      position: 12
      prefix: --i_nvg
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_13:
    default: 3.6d0
    inputBinding:
      position: 13
      prefix: --i_avg
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_14:
    default: '0.2'
    inputBinding:
      position: 14
      prefix: --i_delz
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_15:
    default: work/DalyUncleared/freedrainage_cpcff1.6/vom_namelist
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
      path: ../../data/ELVIS/daly_stats.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default: 1.6d-6
    inputBinding:
      position: 4
      prefix: --i_cpccf
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default: '4.1592'
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
    default: '67.8'
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
    entryname: work/DalyUncleared/freedrainage_cpcff1.6
    writable: true
successCodes: []
temporaryFailCodes: []
