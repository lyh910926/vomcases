arguments: []
baseCommand:
- bash
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_sh/gis_analysis.sh
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default:
      class: File
      path: ../../data/ELVIS/sturtplains.tif
    inputBinding:
      position: 2
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: '133.346086362'
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default: '7.1438801023'
    inputBinding:
      position: 4
      prefix: '-1'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: data/ELVIS/sturtplains.tif
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_5)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/ELVIS
    writable: true
successCodes: []
temporaryFailCodes: []
