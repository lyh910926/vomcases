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
      path: ../../data/ELVIS/litchfield.tif
    inputBinding:
      position: 2
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: '130.795565681'
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default: '3.179210211'
    inputBinding:
      position: 4
      prefix: '-1'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: data/ELVIS/litchfield_demstats.txt
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default: data/ELVIS/litchfield_slopestats.txt
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default: data/ELVIS/litchfield_area.txt
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_7)
    streamable: false
    type: File
  output_1:
    outputBinding:
      glob: $(inputs.input_6)
    streamable: false
    type: File
  output_2:
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
