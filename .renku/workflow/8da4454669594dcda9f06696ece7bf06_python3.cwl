arguments: []
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/sce_best.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default: 1
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_11:
    default: 1
    inputBinding:
      position: 11
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_12:
    default: 1
    inputBinding:
      position: 12
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_13:
    default: 0
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_14:
    default: 1
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_15:
    default: src/VOM/VOM_fortran/VOM-code/*
    inputBinding:
      position: 15
      prefix: -c
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/nofreedrainage_cpcff2.0/sce_out.txt
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: data/VOM_output/HowardSprings/nofreedrainage_cpcff2.0/bestruns/resultsdaily_best.txt
    inputBinding:
      position: 3
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default:
      class: Directory
      listing: []
      path: ../../work/HowardSprings/nofreedrainage_cpcff2.0/best
    inputBinding:
      position: 4
      prefix: -w
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_5:
    default:
      class: File
      path: ../../data/VOM_input/HowardSprings/dailyweather.prn
    inputBinding:
      position: 5
      prefix: -d
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default: p
    inputBinding:
      position: 6
      prefix: -o
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default: 1
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_8:
    default: 1
    inputBinding:
      position: 8
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_9:
    default: 1
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: int
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_3)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/VOM_output/HowardSprings/nofreedrainage_cpcff2.0/bestruns
    writable: true
successCodes: []
temporaryFailCodes: []
