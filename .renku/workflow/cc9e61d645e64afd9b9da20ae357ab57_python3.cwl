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
      path: ../../src_py/sce_stats_best.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/DryRiver/nofreedrainage_cpcff1.0/bestruns/resultsdaily_best.txt
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: data/VOM_output/DryRiver/nofreedrainage_cpcff1.0/beststats2
    inputBinding:
      position: 3
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default: o
    inputBinding:
      position: 4
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default:
      class: File
      path: ../../data/DINGO/Ea_dry.txt
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default: o
    inputBinding:
      position: 6
      prefix: -a
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_dry.txt
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default: 5
    inputBinding:
      position: 8
      prefix: -s
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_9:
    default: 9
    inputBinding:
      position: 9
      prefix: -e
      separate: true
      shellQuote: true
    streamable: false
    type: int
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_3)
    streamable: false
    type: Directory
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/VOM_output/DryRiver/nofreedrainage_cpcff1.0/beststats2
    writable: true
successCodes: []
temporaryFailCodes: []
