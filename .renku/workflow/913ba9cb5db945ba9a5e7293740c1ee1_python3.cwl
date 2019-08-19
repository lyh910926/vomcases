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
      path: ../../src_py/calc_vp.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default:
      class: File
      path: ../../data/DINGO2/VPD_howard.txt
    inputBinding:
      position: 2
      prefix: --vpdfile
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default:
      class: File
      path: ../../data/DINGO2/Tmean_howard.txt
    inputBinding:
      position: 3
      prefix: --tempfile
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default: data/DINGO2/VP_howard.txt
    inputBinding:
      position: 4
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_4)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/DINGO2
    writable: true
successCodes: []
temporaryFailCodes: []
