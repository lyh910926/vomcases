arguments:
- position: 4
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
    default: 2
    inputBinding:
      position: 10
      prefix: --vom_command
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_11:
    default: work/SturtPlains/freedrainage_cpcff1.6/best/vom_namelist
    inputBinding:
      position: 11
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default: '29.0'
    inputBinding:
      position: 2
      prefix: --i_cz
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default: 1.6d-6
    inputBinding:
      position: 3
      prefix: --i_cpccf
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: '7.1507'
    inputBinding:
      position: 5
      prefix: '-1'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default: '2.0'
    inputBinding:
      position: 6
      prefix: --i_cgs
      separate: true
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
    default: '0.2'
    inputBinding:
      position: 9
      prefix: --i_delz
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
    entryname: work/SturtPlains/freedrainage_cpcff1.6/best
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/write_namelist.py
    writable: false
successCodes: []
temporaryFailCodes: []
